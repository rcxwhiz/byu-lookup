import datetime

import pandas as pd

departments_schema = {'name': str,
                      'abbreviation': str}
instructors_schema = {'sort_name': str,
                      'last_name': str,
                      'first_name': str,
                      'person_id': int,
                      'byu_id': int,
                      'net_id': str,
                      'surname': str,
                      'rest_of_name': str,
                      'preferred_first_name': str,
                      'phone_number': str}
instructor_role_types_schema = {'instructor_role_type': str}
buildings_schema = {'name': str}
section_types_schema = {'section_type': str}
courses_schema = {'curriculum_id': int,
                  'title_code': int,
                  'department': int,
                  'catalog_num': int,
                  'catalog_suffix': str,
                  'title': str,
                  'full_title': str,
                  'header_text': str,
                  'effective_date': 'datetime64',
                  'expired_date': 'datetime64',
                  'effective_yearterm': str,
                  'expired_yearterm': str,
                  'description': str,
                  'note': str,
                  'offered': str,
                  'prerequisite': str,
                  'recommended': str,
                  'credit_hours': float,
                  'lecture_hours': float,
                  'lab_hours': float,
                  'honors_approved': str,
                  'catalog_prereq': str,
                  'when_taught': str}
credit_types_schema = {'credit_type': str}
section_modes_schema = {'section_mode': str,
                        'description': str}
sections_schema = {'course': int,
                   'section_number': int,
                   'fixed_or_variable': str,
                   'credit_hours': float,
                   'min_credit_hours': float,
                   'is_honors': bool,
                   'credit_type': int,
                   'section_type': int,
                   'start_date': 'datetime64',
                   'end_date': 'datetime64',
                   'seats_available': int,
                   'class_size': int,
                   'waitlist_size': int,
                   'mode': int}
instructor_roles_schema = {'instructor': int,
                           'section': int,
                           'role': int}
section_times_schema = {'section': int,
                        'begin_time': 'datetime64',
                        'end_time': 'datetime64',
                        'building': int,
                        'room': str,
                        'sequence_num': int,
                        'sunday': bool,
                        'monday': bool,
                        'tuesday': bool,
                        'wednesday': bool,
                        'thursday': bool,
                        'friday': bool,
                        'saturday': bool}


class Department:
	def __init__(self, name: str, abbreviation: str):
		self.name = name
		self.abbreviation = abbreviation

	def __eq__(self, other):
		return isinstance(other, Department) and self.abbreviation == other.abbreviation


class Instructor:
	def __init__(self,
	             sort_name: str,
	             last_name: str,
	             first_name: str,
	             person_id: int,
	             byu_id: int,
	             net_id: str,
	             surname: str,
	             rest_of_name: str,
	             preferred_first_name: str,
	             phone_number: str):
		self.sort_name = sort_name
		self.last_name = last_name
		self.first_name = first_name
		self.person_id = person_id
		self.byu_id = byu_id
		self.net_id = net_id
		self.surname = surname
		self.rest_of_name = rest_of_name
		self.preferred_first_name = preferred_first_name
		self.phone_number = phone_number

	def __eq__(self, other):
		return isinstance(other, Instructor) and self.person_id == other.person_id


class InstructorRoleType:
	def __init__(self, instructor_role_type: str):
		self.instructor_role_type = instructor_role_type

	def __eq__(self, other):
		return isinstance(other, InstructorRoleType) and self.instructor_role_type == other.instructor_role_type


class Building:
	def __init__(self, name: str):
		self.name = name

	def __eq__(self, other):
		return isinstance(other, Building) and self.name == other.name


class SectionType:
	def __init__(self, section_type: str):
		self.section_type = section_type

	def __eq__(self, other):
		return isinstance(other, SectionType) and self.section_type == other.section_type


class Course:
	def __init__(self,
	             index: int,
	             curriculum_id: int,
	             title_code: int,
	             department: Department,
	             catalog_num: int,
	             catalog_suffix: str,
	             title: str,
	             full_title: str,
	             header_text: str,
	             effective_date: datetime.datetime,
	             expired_date: datetime.datetime,
	             effective_year_term: str,
	             expired_year_term: str,
	             description: str,
	             note: str,
	             offered: str,
	             prerequisite: str,
	             recommended: str,
	             credit_hours: float,
	             lecture_hours: float,
	             lab_hours: float,
	             honors_approved: str,
	             catalog_prereq: str,
	             when_taught: str):
		self.index = index
		self.curriculum_id = curriculum_id
		self.title_code = title_code
		self.department = department
		self.catalog_num = catalog_num
		self.catalog_suffix = catalog_suffix
		self.title = title
		self.full_title = full_title
		self.header_text = header_text
		self.effective_date = effective_date
		self.expired_date = expired_date
		self.effective_year_term = effective_year_term
		self.expired_year_term = expired_year_term
		self.description = description
		self.note = note
		self.offered = offered
		self.prerequisite = prerequisite
		self.recommended = recommended
		self.credit_hours = credit_hours
		self.lecture_hours = lecture_hours
		self.lab_hours = lab_hours
		self.honors_approved = honors_approved
		self.catalog_prereq = catalog_prereq
		self.when_taught = when_taught

	def __eq__(self, other):
		return isinstance(other, Course) and self.curriculum_id == other.curriculum_id and self.title_code == other.title_code


class CreditType:
	def __init__(self, credit_type: str):
		self.credit_type = credit_type

	def __eq__(self, other):
		return isinstance(other, CreditType) and self.credit_type == other.credit_type


class SectionMode:
	def __init__(self, section_mode: str, description: str):
		self.section_mode = section_mode
		self.description = description

	def __eq__(self, other):
		return isinstance(other, SectionMode) and self.section_mode == other.section_mode


class Section:
	def __init__(self,
	             course: Course,
	             section_number: int,
	             fixed_or_variable: str,
	             credit_hours: float,
	             min_credit_hours: float,
	             is_honors: bool,
	             credit_type: CreditType,
	             section_type: SectionType,
	             start_date: datetime.datetime,
	             end_date: datetime.datetime,
	             seats_available: int,
	             class_size: int,
	             waitlist_size: int,
	             mode: SectionMode,
	             times: list):
		self.course = course
		self.section_number = section_number
		self.fixed_or_variable = fixed_or_variable
		self.credit_hours = credit_hours
		self.min_credit_hours = min_credit_hours
		self.is_honors = is_honors
		self.credit_type = credit_type
		self.section_type = section_type
		self.start_date = start_date
		self.end_date = end_date
		self.seats_available = seats_available
		self.class_size = class_size
		self.waitlist_size = waitlist_size
		self.mode = mode
		self.times = times

	def __eq__(self, other):
		return isinstance(other, Section) and self.course == other.course and self.section_number == other.section_number


class InstructorSectionRole:
	def __init__(self, instructor: Instructor, section: Section, role: InstructorRoleType):
		self.instructor = instructor
		self.section = section
		self.role = role

	def __eq__(self, other):
		return isinstance(other, InstructorSectionRole) and self.instructor == other.instructor and self.section == other.section and self.role == other.role


class SectionTime:
	def __init__(self,
	             section: Section,
	             begin_time: datetime.time,
	             end_time: datetime.time,
	             building: Building,
	             room: str,
	             sequence_num: int,
	             sunday: bool,
	             monday: bool,
	             tuesday: bool,
	             wednesday: bool,
	             thursday: bool,
	             friday: bool,
	             saturday: bool):
		self.section = section
		self.begin_time = begin_time
		self.end_time = end_time
		self.building = building
		self.room = room
		self.sequence_num = sequence_num
		self.sunday = sunday
		self.monday = monday
		self.tuesday = tuesday
		self.wednesday = wednesday
		self.thursday = thursday
		self.friday = friday
		self.saturday = saturday

	def __eq__(self, other):
		return isinstance(other, SectionTime) and self.section == other.section and self.sequence_num == other.sequence_num


# this is the only dataframe based object, all the others are plain models
class Term:
	def __init__(self, year: int,  term: int, timestamp: datetime.datetime):
		self.year: int = year
		self.term: int = term
		self.timestamp: datetime.datetime = timestamp

		self.departments: pd.DataFrame = pd.DataFrame(columns=departments_schema)
		self.departments = self.departments.astype(departments_schema, copy=False)

		self.instructors: pd.DataFrame = pd.DataFrame(columns=instructors_schema)
		self.instructors = self.instructors.astype(instructors_schema, copy=False)

		self.instructor_role_types: pd.DataFrame = pd.DataFrame(columns=instructor_role_types_schema)
		self.instructor_role_types = self.instructor_role_types.astype(instructor_role_types_schema, copy=False)

		self.buildings: pd.DataFrame = pd.DataFrame(columns=buildings_schema)
		self.buildings = self.buildings.astype(buildings_schema, copy=False)

		self.section_types: pd.DataFrame = pd.DataFrame(columns=section_types_schema)
		self.section_types = self.section_types.astype(section_types_schema, copy=False)

		self.courses: pd.DataFrame = pd.DataFrame(columns=courses_schema)
		self.courses = self.courses.astype(courses_schema, copy=False)

		self.credit_types: pd.DataFrame = pd.DataFrame(columns=credit_types_schema)
		self.credit_types = self.credit_types.astype(credit_types_schema, copy=False)

		self.section_modes: pd.DataFrame = pd.DataFrame(columns=section_modes_schema)
		self.section_modes = self.section_modes.astype(section_modes_schema, copy=False)

		self.sections: pd.DataFrame = pd.DataFrame(columns=sections_schema)
		self.sections = self.sections.astype(sections_schema, copy=False)

		self.instructor_roles: pd.DataFrame = pd.DataFrame(columns=instructor_roles_schema)
		self.instructor_roles = self.instructor_roles.astype(instructor_roles_schema, copy=False)

		self.section_times: pd.DataFrame = pd.DataFrame(columns=section_times_schema)
		self.section_times = self.section_times.astype(section_times_schema, copy=False)

	def __eq__(self, other):
		return isinstance(other, Term) \
		       and self.year == other.year \
		       and self.term == other.term \
		       and self.timestamp == other.timestamp

	def yearterm(self) -> str:
		return f'{self.year}{self.term}'

	def get_courses(self) -> list[Course]:
		courses = []
		for index, row in self.courses.iterrows():
			# TODO need to add some sort of exception catching for this load
			dept_row = self.departments.iloc[row['department']]
			department = Department(dept_row['name'], dept_row['abbreviation'])
			courses.append(Course(index,
			                      row['curriculum_id'],
			                      row['title_code'],
			                      department,
			                      row['catalog_num'],
			                      row['catalog_suffix'],
			                      row['title'],
			                      row['full_title'],
			                      row['header_text'],
			                      row['effective_date'],
			                      row['expired_date'],
			                      row['effective_yearterm'],
			                      row['expired_yearterm'],
			                      row['description'],
			                      row['note'],
			                      row['offered'],
			                      row['prerequisite'],
			                      row['recommended'],
			                      row['credit_hours'],
			                      row['lecture_hours'],
			                      row['lab_hours'],
			                      row['honors_approved'],
			                      row['catalog_prereq'],
			                      row['when_taught']))
		return courses

	def get_sections(self, course: Course) -> list[Section]:
		sections = []
		self.sections.set_index(['course'])
		self.section_times.set_index(['section'])
		sections_rows = self.sections.loc[[course.index]]
		for index, row in sections_rows.iterrows():
			section_times = []
			sections_rows = self.section_times.loc[[index]]
			for _, time_row in sections_rows.iterrows():
				building = Building(self.buildings.iloc[time_row['building']]['name'])
				section_times.append(SectionTime(index,
				                                 time_row['begin_time'],
				                                 time_row['end_time'],
				                                 building,
				                                 time_row['room'],
				                                 time_row['sequence_num'],
				                                 time_row['sunday'],
				                                 time_row['monday'],
				                                 time_row['tuesday'],
				                                 time_row['wednesday'],
				                                 time_row['thursday'],
				                                 time_row['friday'],
				                                 time_row['saturday']))
			section_mode_row = self.section_modes.iloc[row['mode']]
			section_mode = SectionMode(section_mode_row['section_mode'], section_mode_row['description'])
			sections.append(Section(course,
			                        row['section_number'],
			                        row['fixed_or_variable'],
			                        row['credit_hours'],
			                        row['min_credit_hours'],
			                        row['is_honors'],
			                        row['credit_type'],
			                        row['section_type'],
			                        row['start_date'],
			                        row['end_date'],
			                        row['seats_available'],
			                        row['class_size'],
			                        row['waitlist_size'],
			                        section_mode,
			                        section_times))
		return sections
