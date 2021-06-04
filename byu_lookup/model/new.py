import datetime

from sortedcontainers import SortedSet


class Building:
	def __init__(self, name: str):
		self.name: str = name.title()

	def __eq__(self, other):
		return isinstance(other, Building) and self.name == other.name


class Department:
	def __init__(self, name: str, abbreviation: str):
		self.name: str = name.title()
		self.abbreviation: str = abbreviation.upper()

	def __eq__(self, other):
		return isinstance(other, Department) and self.abbreviation == other.abbreviation


class InstructorRoleType:
	def __init__(self, instructor_role_type: str):
		self.instructor_role_type = instructor_role_type.capitalize()

	def __eq__(self, other):
		return isinstance(other, InstructorRoleType) and self.instructor_role_type == other.instructor_role_type


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


class CreditType:
	def __init__(self, credit_type: str):
		self.credit_type = credit_type.lower()

	def __eq__(self, other):
		return isinstance(other, CreditType) and self.credit_type == other.credit_type


class SectionMode:
	def __init__(self, section_mode: str, description: str):
		self.section_mode: str = section_mode.capitalize()
		self.description: str = description.capitalize()

	def __eq__(self, other):
		return isinstance(other, SectionMode) and self.section_mode == other.section_mode


class Sectiontime:
	def __init__(self,
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
		self.begin_time: datetime.time = begin_time
		self.end_time: datetime.time = end_time
		self.building: Building = building
		self.room: str = room.lower()
		self.sequence_num: int = sequence_num
		self.sunday: bool = sunday
		self.monday: bool = monday
		self.tuesday: bool = tuesday
		self.wednesday: bool = wednesday
		self.thursday: bool = thursday
		self.friday: bool = friday
		self.saturday: bool = saturday

	def __eq__(self, other):
		return isinstance(other, Sectiontime) and self.sequence_num == other.sequence_num


class SectionType:
	def __init__(self, section_type: str):
		self.section_type: str = section_type.capitalize()

	def __eq__(self, other):
		return isinstance(other, SectionType) and self.section_type == other.section_type


class InstructorSectionRole:
	def __init__(self,
	             instructor: Instructor,
	             instructor_role_type: InstructorRoleType):
		self.instructor: Instructor = instructor
		self.instructor_role_type: InstructorRoleType = instructor_role_type

	def __eq__(self, other):
		return isinstance(other, InstructorSectionRole) \
		       and self.instructor == other.instructor \
		       and self.instructor_role_type == other.instructor_role_type


class Section:
	def __init__(self,
	             section_num: int,
	             fixed_or_variable: str,
	             credit_hours: float,
	             min_credit_hours: float,
	             is_honors: bool,
	             credit_type: CreditType,
	             section_type: SectionType,
	             start_date: datetime.date,
	             end_date: datetime.date,
	             seats_available: int,
	             class_size: int,
	             waitlist_size: int,
	             section_mode: SectionMode,
	             section_times: SortedSet[Sectiontime],
	             instructor_section_roles: SortedSet[InstructorSectionRole]):
		self.section_num: int = section_num
		self.fixed_or_variable: str = fixed_or_variable
		self.credit_hours: float = credit_hours
		self.min_credit_hours: float = min_credit_hours
		self.is_honors: bool = is_honors
		self.credit_type: CreditType = credit_type
		self.section_type: SectionType = section_type
		self.start_date: datetime.date = start_date
		self.end_date: datetime.date = end_date
		self.seats_available: int = seats_available
		self.class_size: int = class_size
		self.waitlist_size: int = waitlist_size
		self.section_mode: SectionMode = section_mode
		self.section_times: SortedSet[Sectiontime] = section_times
		self.instructor_section_roles: SortedSet[InstructorSectionRole] = instructor_section_roles

	def __eq__(self, other):
		return isinstance(other, Section) and self.section_num == other.section_num


class Course:
	def __init__(self,
	             curriculum_id: int,
	             title_code: int,
	             department: Department,
	             catalog_num: int,
	             catalog_suffix: str,
	             title: str,
	             full_title: str,
	             effective_date: datetime.date,
	             expired_date: datetime.date,
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
	             when_taught: str,
	             sections: SortedSet[Section]):
		self.curriculum_id: int = curriculum_id
		self.title_code: int = title_code
		self.department: Department = department
		self.catalog_num: int = catalog_num
		self.catalog_suffix: str = catalog_suffix.upper()
		self.title: str = title.title()
		self.full_title: str = full_title.title()
		self.effective_date: datetime.date = effective_date
		self.expired_date: datetime.date = expired_date
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
		self.sections: SortedSet[Section] = sections

	def __eq__(self, other):
		return isinstance(other, Course) and self.curriculum_id == other.curriculum_id and self.title_code == other.title_code


class Term:
	def __init__(self, year: int, term: int, courses: SortedSet[Course], collection_time: datetime.datetime):
		self.year: int = year
		self.term: int = term
		self.courses: SortedSet[Course] = courses
		self.collection_time = collection_time

	def __eq__(self, other):
		return isinstance(other, Term) and self.year == other.year and self.term == other.term


class DataSet:
	def __init__(self):
		self.buildings = 0
		self.credit_types = 0
		self.instructors = 0
		self.instructor_role_types = 0
		self.section_modes = 0
		self.section_types = 0
		self.terms = 0
