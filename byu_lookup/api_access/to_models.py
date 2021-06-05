import asyncio
import datetime
import tqdm
import tqdm.asyncio

from byu_lookup.api_access import apis
from byu_lookup.model import DataSet, Term, Course, Section


def add_departments(department_map: dict, data_set: DataSet) -> None:
	for name, abbr in tqdm.tqdm(department_map.items(), desc='Parsing department map', unit='department'):
		data_set.put_department(name, abbr)


def add_instructors(instructor_list: list, data_set: DataSet) -> None:
	for instructor in tqdm.tqdm(instructor_list, desc='Parsing instructors', unit='instructor'):
		data_set.make_instructor(instructor['sort_name'],
		                         instructor['last_name'],
		                         instructor['first_name'],
		                         int(instructor['id']),
		                         None,
		                         None,
		                         None,
		                         None,
		                         None,
		                         None)


def add_buildings(building_list: list, data_set: DataSet) -> None:
	for building in tqdm.tqdm(building_list, desc='Parsing buildings', unit='building'):
		data_set.get_building(building['building'])


def add_classes(classes_response: dict, term: Term, session_id: str) -> None:
	with tqdm.tqdm(classes_response.items(), desc='Parsing courses', unit='course') as course_queue:
		for course_id, course in course_queue:
			add_class(term, session_id, course)


async def add_classes_async(classes_response: dict, term: Term, session_id: str) -> None:
	with tqdm.asyncio.tqdm(classes_response.items(), desc='Parsing courses', unit='course') as course_queue:
		async for course_id, course in course_queue:
			add_class(term, session_id, course)


def add_time(term: Term, sec: Section, time: dict) -> None:
	if time['begin_time'] is not None:
		begin_time = f'{int(time["begin_time"]):04}'
		begin_hour = int(begin_time[:2])
		begin_minute = int(begin_time[2:])
		bt = datetime.time(hour=begin_hour, minute=begin_minute)
	else:
		bt = None
	if time['end_time'] is not None:
		end_time = f'{int(time["end_time"]):04}'
		end_hour = int(end_time[:2])
		end_minute = int(end_time[2:])
		et = datetime.time(hour=end_hour, minute=end_minute)
	else:
		et = None
	building = term.data_set_ref.get_building(time['building']) if time['building'] is not None else None
	sec.add_time(bt,
	             et,
	             building,
	             time['room'],
	             int(time['sequence_number']),
	             time['sun'] is not None,
	             time['mon'] is not None,
	             time['tue'] is not None,
	             time['wed'] is not None,
	             time['thu'] is not None,
	             time['fri'] is not None,
	             time['sat'] is not None)


def add_section_instructor(term: Term, sec: Section, instructor: dict) -> None:
	try:
		term.data_set_ref.update_instructor(int(instructor['person_id']),
		                                    byu_id=int(instructor['byu_id']),
		                                    net_id=instructor['net_id'],
		                                    surname=instructor['surname'],
		                                    sort_name=instructor['sort_name'],
		                                    rest_of_name=instructor['rest_of_name'],
		                                    preferred_first_name=instructor['preferred_first_name'],
		                                    phone_number=instructor['phone_number'])
	except ValueError:
		term.data_set_ref.make_instructor(instructor['sort_name'],
		                                  None,
		                                  None,
		                                  int(instructor['person_id']),
		                                  int(instructor['byu_id']),
		                                  instructor['net_id'],
		                                  instructor['surname'],
		                                  instructor['rest_of_name'],
		                                  instructor['preferred_first_name'],
		                                  instructor['phone_number'])
	ins = term.data_set_ref.get_instructor(int(instructor['person_id']))
	role = term.data_set_ref.get_instructor_role_type(instructor['attribute_type'])
	sec.add_role(ins, role)


def add_section(term: Term, course: Course, section: dict) -> None:
	credit_type = term.data_set_ref.get_credit_type(section['credit_type'])
	section_type = term.data_set_ref.get_section_type(section['section_type'])
	section_mode = term.data_set_ref.get_section_mode(section['mode'], section['mode_desc'])
	if section['start_date'] is not None:
		start_year, start_month, start_day = section['start_date'].split('-')
		sd = datetime.date(year=int(start_year), month=int(start_month), day=int(start_day))
	else:
		sd = None
	if section['end_date'] is not None:
		end_year, end_month, end_day = section['end_date'].split('-')
		ed = datetime.date(year=int(end_year), month=int(end_month), day=int(end_day))
	else:
		ed = None
	sec = course.make_section(int(section['section_number']),
	                          section['fixed_or_variable'],
	                          float(section['credit_hours']),
	                          float(section['minimum_credit_hours']),
	                          section['honors'] == 'Y',
	                          credit_type,
	                          section_type,
	                          sd,
	                          ed,
	                          int(section['availability']['seats_available']),
	                          int(section['availability']['class_size']),
	                          int(section['availability']['waitlist_size']),
	                          section_mode)
	for time in section['times']:
		add_time(term, sec, time)

	for instructor in section['instructors']:
		add_section_instructor(term, sec, instructor)


def add_class(term: Term, session_id: str, course: dict) -> None:
	curriculum_id = int(course['curriculum_id'])
	title_code = int(course['title_code'])

	course_response = apis.get_course(curriculum_id, title_code, session_id, term.year_term())

	dept = term.data_set_ref.get_department(course['dept_name'])

	try:
		ch = float(course_response['catalog']['credit_hours'])
	except (ValueError, TypeError):
		ch = None
	try:
		lh = float(course_response['catalog']['lecture_hours'])
	except (ValueError, TypeError):
		lh = None
	try:
		lah = float(course_response['catalog']['lab_hours'])
	except (ValueError, TypeError):
		lah = None

	c = term.make_course(curriculum_id,
	                     title_code,
	                     dept,
	                     int(course['catalog_number']),
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
	                     ch,
	                     lh,
	                     lah,
	                     course_response['catalog']['honors_approved'] == 'Y',
	                     course_response['catalog']['catalog_prereq'],
	                     course_response['catalog']['when_taught'])

	for section in course_response['sections']:
		add_section(term, c, section)


def populate_term(term: Term, use_async: bool = True) -> None:
	term_response = apis.get_year_term(term.year_term())

	add_departments(term_response['department_map'], term.data_set_ref)
	add_instructors(term_response['instructor_list'], term.data_set_ref)
	add_buildings(term_response['building_list'], term.data_set_ref)

	session_id = apis.make_session_id()

	classes_response = apis.get_classes(term_response['department_list'], term.year_term(), session_id)

	if use_async:
		loop = asyncio.get_event_loop()
		loop.run_until_complete(add_classes_async(classes_response, term, session_id))
		loop.close()
	else:
		add_classes(classes_response, term, session_id)
