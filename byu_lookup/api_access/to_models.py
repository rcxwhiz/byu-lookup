import asyncio
import tqdm
import tqdm.asyncio

from byu_lookup.api_access import apis
from byu_lookup.model import DataSet, Term


def add_departments(department_map: dict, data_set: DataSet) -> None:
	for name, abbr in tqdm.tqdm(department_map.items(), desc='Parsing department map'):
		data_set.get_department(name, abbr)
	print(f'Deparments: {data_set.departments}')


def add_instructors(instructor_list: list, data_set: DataSet) -> None:
	for instructor in tqdm.tqdm(instructor_list, desc='Parsing instructors'):
		data_set.make_instructor(instructor['sort_name'],
		                         instructor['last_name'],
		                         instructor['first_name'],
		                         instructor['id'],
		                         None,
		                         None,
		                         None,
		                         None,
		                         None,
		                         None)


def add_buildings(building_list: list, data_set: DataSet) -> None:
	for building in tqdm.tqdm(building_list, desc='Parsing buildings'):
		data_set.get_building(building['building'])


async def add_classes(classes_response: dict, term: Term, session_id: str) -> None:
	with tqdm.asyncio.tqdm(classes_response.items(), desc='Parsing courses') as course_queue:
		async for course_id, course in course_queue:
			curriculum_id = int(course['curriculum_id'])
			title_code = int(course['title_code'])

			course_response = apis.get_course(curriculum_id, title_code, session_id, term.yearterm())

			course = term.make_course(curriculum_id,
			                          title_code,
			                          course['dept_name'],
			                          course['catalog_number'],
			                          course['catalog_suffix'],
			                          course['title'],
			                          course['full_title'],
			                          course_response['catalog']['effective_date'].split()[0],
			                          course_response['catalog']['expired_date'].split()[0],
			                          course_response['catalog']['effective_year_term'],
			                          course_response['catalog']['expired_year_term'],
			                          course_response['catalog']['description'],
			                          course_response['catalog']['note'],
			                          course_response['catalog']['offered'],
			                          course_response['catalog']['prerequisite'],
			                          course_response['catalog']['recommended'],
			                          course_response['catalog']['credit_hours'],
			                          course_response['catalog']['lecture_hours'],
			                          course_response['catalog']['lab_hours'],
			                          course_response['catalog']['honors_approved'] == 'Y',
			                          course_response['catalog']['catalog_prereq'],
			                          course_response['catalog']['when_taught'])

			for section in course_response['sections']:
				credit_type = term.data_set_ref.get_credit_type(section['credit_type'])
				section_type = term.data_set_ref.get_section_type(section['section_type'])
				section_mode = term.data_set_ref.get_section_mode(section['mode'], section['mode_desc'])
				sec = course.make_section(section['section_number'],
				                          section['fixed_or_variable'],
				                          section['credit_hours'],
				                          section['minimum_credit_hours'],
				                          section['honors'] == 'Y',
				                          credit_type,
				                          section_type,
				                          section['start_date'],
				                          section['end_date'],
				                          section['availability']['seats_available'],
				                          section['availability']['class_size'],
				                          section['availability']['waitlist_size'],
				                          section_mode)


def populate_term(term: Term) -> None:
	print(f'Populating term {term.year_term()}')

	term_response = apis.get_year_term(term.year_term())

	add_departments(term_response['department_map'], term.data_set_ref)
	add_instructors(term_response['instructor_list'], term.data_set_ref)
	add_buildings(term_response['building_list'], term.data_set_ref)

	session_id = apis.make_session_id()

	classes_response = apis.get_classes(term_response['department_list'], term.yearterm(), session_id)

	loop = asyncio.get_event_loop()
	loop.run_until_complete(add_classes(classes_response, term, session_id))
	loop.close()
