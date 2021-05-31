import asyncio
import datetime

import tqdm
import tqdm.asyncio

from byu_lookup.api_access import apis
from byu_lookup.model import Term


def get_term_model(year: int, term: int) -> Term:
	term = Term(year, term, datetime.datetime.now())
	populate_term(term)
	return term


def add_departments(department_map: dict, term: Term) -> None:
	for name, abbr in tqdm.tqdm(department_map.items(), desc='Parsing department map'):
		term.add_dept(name, abbr)


def add_instructors(instructor_list: list, term: Term) -> None:
	for instructor in tqdm.tqdm(instructor_list, desc='Parsing instructors'):
		term.add_instructor(instructor['sort_name'],
		                    instructor['last_name'],
		                    instructor['first_name'],
		                    instructor['person_id'],
		                    None,
		                    None,
		                    None,
		                    None,
		                    None,
		                    None)


def add_buildings(building_list: list, term: Term) -> None:
	for building in tqdm.tqdm(building_list, desc='Parsing buildings'):
		term.add_building(building['building'])


async def add_classes(classes_response: dict, term: Term, session_id: str) -> None:
	with tqdm.asyncio.tqdm(classes_response.items(), desc='Parsing courses') as course_queue:
		async for course_id, course in course_queue:
			curriculum_id = course['curriculum_id']
			title_code = course['title_code']

			course_response = apis.get_course(curriculum_id, title_code, session_id, term.yearterm())

			term.add_course(curriculum_id,
			                title_code,
			                course['dept_name'],
			                course['catalog_number'],
			                course['catalog_suffix'],
			                course['title'],
			                course['full_title'],
			                course_response['catalog']['header_text'],
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
			                course_response['catalog']['lecture_hours'] if course_response['catalog']['lecture_hours'] is not None else -1,
			                course_response['catalog']['lab_hours'] if course_response['catalog']['lab_hours'] is not None else -1,
			                course_response['catalog']['honors_approved'] == 'Y',
			                course_response['catalog']['catalog_prereq'],
			                course_response['catalog']['when_taught'])

			for section in course_response['sections']:
				# TODO still need to add the instructor stuff here
				term.add_section(curriculum_id,
				                 title_code,
				                 section['section_number'],
				                 section['fixed_or_variable'],
				                 section['credit_hours'],
				                 section['minimum_credit_hours'],
				                 section['honors'] == 'Y',
				                 section['credit_type'],
				                 section['section_type'],
				                 section['start_date'],
				                 section['end_date'],
				                 section['availability']['seats_available'],
				                 section['availability']['class_size'],
				                 section['availability']['waitlist_size'],
				                 section['mode'],
				                 section['mode_desc'])


def populate_term(term: Term) -> None:
	print(f'Populating term {term.yearterm()}')

	term_response = apis.get_year_term(term.yearterm())

	add_departments(term_response['department_map'], term)
	add_instructors(term_response['instructor_list'], term)
	add_buildings(term_response['building_list'], term)

	session_id = apis.make_session_id()

	classes_response = apis.get_classes(term_response['department_list'], term.yearterm(), session_id)

	loop = asyncio.get_event_loop()
	loop.run_until_complete(add_classes(classes_response, term, session_id))
	loop.close()
