import datetime
import pandas as pd

import betta

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

term_to_id = {'winter': 1,
              'spring': 3,
              'summer': 4,
              'fall': 5}
id_to_term = {v: k for k, v in term_to_id.items()}


class Department:
	def __init__(self, name: str, abbreviation: str):
		self.name: str = name
		self.abbreviation: str = abbreviation

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
		self.sort_name: str = sort_name
		self.last_name: str = last_name
		self.first_name: str = first_name
		self.person_id: int = person_id
		self.byu_id: int = byu_id
		self.net_id: str = net_id
		self.surname: str = surname
		self.rest_of_name: str = rest_of_name
		self.preferred_first_name: str = preferred_first_name
		self.phone_number: str = phone_number

	def __eq__(self, other):
		return isinstance(other, Instructor) and self.person_id == other.person_id


class InstructorRoleType:
	def __init__(self, instructor_role_type: str):
		self.instructor_role_type: str = instructor_role_type

	def __eq__(self, other):
		return isinstance(other, InstructorRoleType) and self.instructor_role_type == other.instructor_role_type


class Building:
	def __init__(self, name: str):
		self.name: str = name

	def __eq__(self, other):
		return isinstance(other, Building) and self.name == other.name


class SectionType:
	def __init__(self, section_type: str):
		self.section_type: str = section_type

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
		self.index: int = index
		self.curriculum_id: int = curriculum_id
		self.title_code: int = title_code
		self.department: Department = department
		self.catalog_num: int = catalog_num
		self.catalog_suffix: str = catalog_suffix
		self.title: str = title
		self.full_title: str = full_title
		self.effective_date: datetime.datetime = effective_date
		self.expired_date: datetime.datetime = expired_date
		self.effective_year_term: str = effective_year_term
		self.expired_year_term: str = expired_year_term
		self.description: str = description
		self.note: str = note
		self.offered: str = offered
		self.prerequisite: str = prerequisite
		self.recommended: str = recommended
		self.credit_hours: float = credit_hours
		self.lecture_hours: float = lecture_hours
		self.lab_hours: float = lab_hours
		self.honors_approved: str = honors_approved
		self.catalog_prereq: str = catalog_prereq
		self.when_taught: str = when_taught

	def __eq__(self, other):
		return isinstance(other, Course) and self.curriculum_id == other.curriculum_id and self.title_code == other.title_code


class CreditType:
	def __init__(self, credit_type: str):
		self.credit_type: str = credit_type

	def __eq__(self, other):
		return isinstance(other, CreditType) and self.credit_type == other.credit_type


class SectionMode:
	def __init__(self, section_mode: str, description: str):
		self.section_mode: str = section_mode
		self.description: str = description

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
		self.course: Course = course
		self.section_number: int = section_number
		self.fixed_or_variable: str = fixed_or_variable
		self.credit_hours: float = credit_hours
		self.min_credit_hours: float = min_credit_hours
		self.is_honors: bool = is_honors
		self.credit_type: CreditType = credit_type
		self.section_type: SectionType = section_type
		self.start_date: datetime.datetime = start_date
		self.end_date: datetime.datetime = end_date
		self.seats_available: int = seats_available
		self.class_size: int = class_size
		self.waitlist_size: int = waitlist_size
		self.mode: SectionMode = mode
		self.times: list[SectionTime] = times

	def __eq__(self, other):
		return isinstance(other, Section) and self.course == other.course and self.section_number == other.section_number


class InstructorSectionRole:
	def __init__(self, instructor: Instructor, section: Section, role: InstructorRoleType):
		self.instructor: Instructor = instructor
		self.section: Section = section
		self.role: InstructorRoleType = role

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
		self.section: Section = section
		self.begin_time: datetime.time = begin_time
		self.end_time: datetime.time = end_time
		self.building: Building = building
		self.room: str = room
		self.sequence_num: int = sequence_num
		self.sunday: bool = sunday
		self.monday: bool = monday
		self.tuesday: bool = tuesday
		self.wednesday: bool = wednesday
		self.thursday: bool = thursday
		self.friday: bool = friday
		self.saturday: bool = saturday

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

	def get_departments(self) -> list[Department]:
		return [Department(row['name'], row['abbreviation']) for _, row in self.departments.iterrows()]

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

	def add_dept(self, name: str, abbreviation: str) -> None:
		try:
			self.departments.append([name, abbreviation])
			# self.departments.append({'name': name, 'abbreviation': abbreviation}, ignore_index=True, verify_integrity=True)
		except ValueError as e:
			print(f'Got an error saving a dept: {e}')

	def add_instructor(self,
	                   sort_name: str,
	                   last_name: str,
	                   first_name: str,
	                   person_id: int,
	                   byu_id: int,
	                   net_id: str,
	                   surname: str,
	                   rest_of_name: str,
	                   preferred_first_name: str,
	                   phone_number: str) -> None:
		try:
			self.instructors.append({'sort_name': sort_name,
			                         'last_name': last_name,
			                         'first_name': first_name,
			                         'person_id': person_id,
			                         'byu_id': byu_id,
			                         'net_id': net_id,
			                         'surname': surname,
			                         'rest_of_name': rest_of_name,
			                         'preferred_first_name': preferred_first_name,
			                         'phone_number': phone_number},
			                        ignore_index=True,
			                        verify_integrity=True)
		except ValueError:
			pass

	def add_building(self, name: str) -> None:
		try:
			self.buildings.append({'name': name}, ignore_index=True, verify_integrity=True)
		except ValueError:
			pass

	def add_course(self,
	               curriculum_id: int,
	               title_code: int,
	               department_name: str,
	               catalog_num: int,
	               catalog_suffix: str,
	               title: str,
	               full_title: str,
	               effective_date: datetime.datetime,
	               expired_date: datetime.datetime,
	               effective_yearterm: str,
	               expired_yearterm: str,
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
	               when_taught: str) -> None:
		print(f'Going to look for {department_name} in')
		print(self.departments)
		dept_row = betta.data.get_first_matching_row(self.departments, 'name', department_name)
		dept_index = dept_row.index
		try:
			self.courses.append({'curriculum_id': curriculum_id,
			                     'title_code': title_code,
			                     'department': dept_index,
			                     'catalog_num': catalog_num,
			                     'catalog_suffix': catalog_suffix,
			                     'title': title,
			                     'full_title': full_title,
			                     'effective_date': effective_date,
			                     'expired_date': expired_date,
			                     'effective_yearterm': effective_yearterm,
			                     'expired_yearterm': expired_yearterm,
			                     'description': description,
			                     'note': note,
			                     'offered': offered,
			                     'prerequisite': prerequisite,
			                     'recommended': recommended,
			                     'credit_hours': credit_hours,
			                     'lecture_hours': lecture_hours,
			                     'lab_hours': lab_hours,
			                     'honors_approved': honors_approved,
			                     'catalog_prereq': catalog_prereq,
			                     'when_taught': when_taught})
		except ValueError:
			pass

	def add_section(self,
	                curriculum_id: int,
	                title_code: int,
	                section_number: int,
	                fixed_or_variable: str,
	                credit_hours: float,
	                min_credit_hours: float,
	                is_honors: bool,
	                credit_type: str,
	                section_type: str,
	                start_date: datetime.datetime,
	                end_date: datetime.datetime,
	                seats_available: int,
	                class_size: int,
	                waitlist_size: int,
	                mode: str,
	                mode_desc: str) -> None:
		course_row = self.courses.iloc[(self.courses['curriculum_id'] == curriculum_id) & (self.courses['title_code'] == title_code)]
		course_index = course_row.index
		if credit_type not in self.credit_types.values:
			self.credit_types.append({'credit_type': credit_type}, ignore_index=True)
		credit_type_row = self.credit_types.iloc[self.credit_types['credit_type'] == credit_type]
		credit_type_index = credit_type_row.index
		if section_type not in self.section_types.values:
			self.section_types.append({'section_type': section_type}, ignore_index=True)
		section_type_row = self.section_types.iloc[self.section_types['section_type'] == section_type]
		section_type_index = section_type_row.index
		try:
			self.section_modes.append({'mode': mode, 'description': mode_desc}, ignore_index=True, verify_integrity=True)
		except ValueError:
			pass
		section_mode_row = self.section_modes.iloc[self.section_modes['mode'] == mode]
		section_mode_index = section_mode_row.index
		try:
			self.sections.append({'course': course_index,
			                      'section_number': section_number,
			                      'fixed_or_variable': fixed_or_variable,
			                      'credit_hours': credit_hours,
			                      'min_credit_hours': min_credit_hours,
			                      'is_honors': is_honors,
			                      'credit_type': credit_type_index,
			                      'section_type': section_type_index,
			                      'start_date': start_date,
			                      'end_date': end_date,
			                      'seats_available': seats_available,
			                      'class_size': class_size,
			                      'waitlist_size': waitlist_size,
			                      'mode': section_mode_index},
			                     ignore_index=True,
			                     verify_integrity=True)
		except ValueError:
			pass
