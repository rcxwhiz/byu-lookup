import datetime
import random
import string
import requests

import byu_lookup.model


term_api = 'http://saasta.byu.edu/noauth/classSchedule/ajax/getYeartermData.php'
classes_api = 'http://saasta.byu.edu/noauth/classSchedule/ajax/getClasses.php'
course_api = 'http://saasta.byu.edu/noauth/classSchedule/ajax/getSections.php'


def check_year_term_valid(year_term: str) -> None:
	year = int(year_term[:4])
	term = int(year_term[4:])
	if year > datetime.date.today().year or year < 2015:
		raise ValueError('Year out of range')
	if term not in byu_lookup.model.id_to_term.keys():
		raise ValueError('Invalid term')


def make_session_id() -> str:
	chars = string.ascii_uppercase + string.digits
	return ''.join((random.choice(chars) for _ in range(20)))


def get_year_term(year_term: str, tries: int = 2) -> dict:
	check_year_term_valid(year_term)
	if tries == 0:
		raise RuntimeError(f'Unable to get term {year_term}')
	try:
		term_request = {
			'yearterm': year_term
		}
		return requests.post(url=term_api, data=term_request).json()
	except Exception:
		return get_year_term(year_term, tries - 1)


def get_classes(department_list: list[str], year_term: str, session_id: str, tries: int = 2) -> dict:
	check_year_term_valid(year_term)
	if tries == 0:
		raise RuntimeError(f'Unable to get classes for {year_term}')
	try:
		classes_request = {
			'searchObject[teaching_areas][]': department_list,
			'searchObject[yearterm]': year_term,
			'sessionId': session_id
		}
		return requests.post(url=classes_api, data=classes_request).json()
	except Exception:
		return get_classes(department_list, year_term, session_id, tries - 1)


def get_course(curriculum_id: int, title_code: int, session_id: str, year_term: str, tries: int = 2) -> dict:
	check_year_term_valid(year_term)
	if tries == 0:
		raise RuntimeError(f'Unable to get class {curriculum_id} for {year_term}')
	try:
		course_request = {
			'courseId': f'{curriculum_id:05}-{title_code:03}',
			'sessionId': session_id,
			'yearterm': year_term,
			'no_outcomes': True
		}
		return requests.post(url=course_api, data=course_request).json()
	except Exception:
		return get_course(curriculum_id, title_code, session_id, year_term, tries - 1)
