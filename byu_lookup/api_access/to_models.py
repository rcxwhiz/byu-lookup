import datetime

from tqdm import tqdm
import tqdm.asyncio

from byu_lookup.api_access import apis
from byu_lookup.model import Term, Department, Instructor, Building, Course, Section


def get_term_model(year: int, term: int) -> Term:
	term = Term(year, term, datetime.datetime.now())
	populate_term(term)
	return term


def get_department_models(department_map: dict) -> dict[str, Department]:
	departments = {}
	for name, abbr in tqdm(department_map.items(), desc='Parsing department map'):
		try:
			name = name.title()
			departments[name] = Department(name, abbr)
		except Exception:
			print('Error getting department')
	return departments


def get_instructor_models(instructor_list: list) -> dict[str, Instructor]:
	instructors = {}
	for instructor in tqdm(instructor_list, desc='Parsing instructors'):
		try:
			instructors[instructor['person_id']] = Instructor(instructor['sort_name'], instructor['last_name'], instructor['first_name'], instructor['person_id'], None, None, None, None, None, None)
		except Exception:
			print('Error getting instructor')
	return instructors


def get_building_models(building_list: list) -> dict[str, Building]:
	buildings = {}
	for building in tqdm(building_list, desc='Parsing buildings'):
		try:
			buildings[building['building']] = Building(building['building'])
		except Exception:
			print('Error getting building')
	return buildings


def get_classes_models(classes_response: dict, term: Term, departements: dict[str, Department], session_id: str) -> (dict[str, Course], dict[str, Section]):
	courses = {}
	sections = {}
	with tqdm.asyncio.tqdm(classes_response.items(), desc='Parsing courses') as course_queue:
		async for course_id, course in course_queue:
			try:
				curriculum_id = course['curriculum_id']
				title_code = course['title_code']
				department = departements[course['dept_name']] if course['dept_name'] in departements else None
				catalog_num = course['catalog_number']
				catalog_suffix = course['catalog_suffix']
				title = course['title']
				full_title = course['full_title']

				course_response = apis.get_course(curriculum_id, title_code, session_id, term.yearterm())

				effective_date = course_response['catalog']['effective_date'].split()[0]
				expired_date = course_response['catalog']['expired_date'].split()[0]
				effective_yearterm = course_response['catalog']['effective_year_term']
				expired_yearterm = course_response['catalog']['expired_year_term']
				description = course_response['catalog']['description']
				note = course_response['catalog']['note']
				offered = course_response['catalog']['offered']
				prerequisite = course_response['catalog']['prerequisite']
				recommended = course_response['catalog']['recommended']
				credit_hours = course_response['catalog']['credit_hours']

				lecture_hours = course_response['catalog']['lecture_hours'] if course_response['catalog']['lecture_hours'] is not None else -1
				lab_hours = course_response['catalog']['lab_hours'] if course_response['catalog']['lab_hours'] is not None else -1

				honors_approved = (course_response['catalog']['honors_approved'] == 'Y')
				catalog_prereq = course_response['catalog']['catalog_prereq']
				when_taught = course_response['catalog']['when_taught']

				course_sections = []
				for section in course_response['sections']:
					section_num = section['section_number']
					fixed_or_variable = section['fixed_or_variable']
					credit_hours = section['credit_hours']
					minimum_credit_hours = section['minimum_credit_hours']
					is_honors = (section['honors'] == 'Y')
					# TODO section type
					# TODO credit type
					start_date = section['start_date']
					end_date = section['end_date']
					seats_available = section['availability']['seats_available']
					class_size = section['availability']['class_size']
					waitlist_size = section['availability']['waitlist_size']

			except Exception:
				print('Error getting course')
	return courses, sections


# TODO change all of this to be editing the pandas dataframe stuff in the given term
def populate_term(term: Term) -> None:
	print(f'Populating term {term.yearterm()}')
	data = {}
	term_response = apis.get_year_term(term.yearterm())

	data['department_models'] = get_department_models(term_response['department_map'])
	data['instructor_models'] = get_instructor_models(term_response['instructor_list'])
	data['building_models'] = get_building_models(term_response['building_list'])

	session_id = apis.make_session_id()

	classes_response = apis.get_classes(term_response['department_list'], term.yearterm(), session_id)
