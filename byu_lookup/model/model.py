import datetime
import pickle
from sortedcontainers import SortedSet


class Building:
	def __init__(self, name: str):
		self.name: str = name.title()

	def __eq__(self, other):
		return isinstance(other, Building) and self.name == other.name

	def __ne__(self, other):
		return not isinstance(other, Building) or self.name != other.name

	def __lt__(self, other):
		if not isinstance(other, Building):
			raise TypeError()
		return self.name < other.name

	def __le__(self, other):
		if not isinstance(other, Building):
			raise TypeError()
		return self.name <= other.name

	def __gt__(self, other):
		if not isinstance(other, Building):
			raise TypeError()
		return self.name > other.name

	def __ge__(self, other):
		if not isinstance(other, Building):
			raise TypeError()
		return self.name >= other.name


class Department:
	def __init__(self, name: str, abbreviation: str):
		self.name: str = name.title()
		self.abbreviation: str = abbreviation.upper()

	def __eq__(self, other):
		return isinstance(other, Department) and self.abbreviation == other.abbreviation

	def __ne__(self, other):
		return not isinstance(other, Department) or self.abbreviation != other.abbreviation

	def __lt__(self, other):
		if not isinstance(other, Department):
			raise TypeError()
		return self.abbreviation < other.abbreviation

	def __le__(self, other):
		if not isinstance(other, Department):
			raise TypeError()
		return self.abbreviation <= other.abbreviation

	def __gt__(self, other):
		if not isinstance(other, Department):
			raise TypeError()
		return self.abbreviation > other.abbreviation

	def __ge__(self, other):
		if not isinstance(other, Department):
			raise TypeError()
		return self.abbreviation >= other.abbreviation


class InstructorRoleType:
	def __init__(self, instructor_role_type: str):
		self.instructor_role_type = instructor_role_type.capitalize()

	def __eq__(self, other):
		return isinstance(other, InstructorRoleType) and self.instructor_role_type == other.instructor_role_type

	def __ne__(self, other):
		return not isinstance(other, InstructorRoleType) or self.instructor_role_type != other.instructor_role_type

	def __lt__(self, other):
		if not isinstance(other, InstructorRoleType):
			raise TypeError()
		return self.instructor_role_type < other.instructor_role_type

	def __le__(self, other):
		if not isinstance(other, InstructorRoleType):
			raise TypeError()
		return self.instructor_role_type <= other.instructor_role_type

	def __gt__(self, other):
		if not isinstance(other, InstructorRoleType):
			raise TypeError()
		return self.instructor_role_type > other.instructor_role_type

	def __ge__(self, other):
		if not isinstance(other, InstructorRoleType):
			raise TypeError()
		return self.instructor_role_type >= other.instructor_role_type


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

	def __ne__(self, other):
		return not isinstance(other, Instructor) or self.person_id != other.person_id

	def __lt__(self, other):
		if not isinstance(other, Instructor):
			raise TypeError()
		return self.sort_name < other.sort_name or (self.sort_name == other.sort_name and self.person_id < other.person_id)

	def __le__(self, other):
		if not isinstance(other, Instructor):
			raise TypeError()
		return self.sort_name <= other.sort_name or (self.sort_name == other.sort_name and self.person_id <= other.person_id)

	def __gt__(self, other):
		if not isinstance(other, Instructor):
			raise TypeError()
		return self.sort_name > other.sort_name or (self.sort_name == other.sort_name and self.person_id > other.person_id)

	def __ge__(self, other):
		if not isinstance(other, Instructor):
			raise TypeError()
		return self.sort_name >= other.sort_name or (self.sort_name == other.sort_name and self.person_id >= other.person_id)


class CreditType:
	def __init__(self, credit_type: str):
		self.credit_type = credit_type.lower()

	def __eq__(self, other):
		return isinstance(other, CreditType) and self.credit_type == other.credit_type

	def __ne__(self, other):
		return not isinstance(other, CreditType) or self.credit_type != other.credit_type

	def __lt__(self, other):
		if not isinstance(other, CreditType):
			raise TypeError()
		return self.credit_type < other.credit_type

	def __le__(self, other):
		if not isinstance(other, CreditType):
			raise TypeError()
		return self.credit_type <= other.credit_type

	def __gt__(self, other):
		if not isinstance(other, CreditType):
			raise TypeError()
		return self.credit_type > other.credit_type

	def __ge__(self, other):
		if not isinstance(other, CreditType):
			raise TypeError()
		return self.credit_type >= other.credit_type


class SectionMode:
	def __init__(self, section_mode: str, description: str):
		self.section_mode: str = section_mode.capitalize()
		self.description: str = description.capitalize()

	def __eq__(self, other):
		return isinstance(other, SectionMode) and self.section_mode == other.section_mode

	def __ne__(self, other):
		return not isinstance(other, SectionMode) or self.section_mode != other.section_mode

	def __lt__(self, other):
		if not isinstance(other, SectionMode):
			raise TypeError()
		return self.section_mode < other.section_mode

	def __le__(self, other):
		if not isinstance(other, SectionMode):
			raise TypeError()
		return self.section_mode <= other.section_mode

	def __gt__(self, other):
		if not isinstance(other, SectionMode):
			raise TypeError()
		return self.section_mode > other.section_mode

	def __ge__(self, other):
		if not isinstance(other, SectionMode):
			raise TypeError()
		return self.section_mode >= other.section_mode


class SectionTime:
	def __init__(self,
	             section_ref,
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
		self.section_ref: Section = section_ref
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
		return isinstance(other, SectionTime) and self.sequence_num == other.sequence_num

	def __ne__(self, other):
		return not isinstance(other, SectionTime) or self.sequence_num != other.sequence_num

	def __lt__(self, other):
		if not isinstance(other, SectionTime):
			raise TypeError()
		return self.section_ref < other.section_ref or (self.section_ref == other.section_ref and self.sequence_num < other.sequence_num)

	def __le__(self, other):
		if not isinstance(other, SectionTime):
			raise TypeError()
		return self.section_ref < other.section_ref or (self.section_ref == other.section_ref and self.sequence_num <= other.sequence_num)

	def __gt__(self, other):
		if not isinstance(other, SectionTime):
			raise TypeError()
		return self.section_ref > other.section_ref or (self.section_ref == other.section_ref and self.sequence_num > other.sequence_num)

	def __ge__(self, other):
		if not isinstance(other, SectionTime):
			raise TypeError()
		return self.section_ref > other.section_ref or (self.section_ref == other.section_ref and self.sequence_num >= other.sequence_num)


class SectionType:
	def __init__(self, section_type: str):
		self.section_type: str = section_type.capitalize()

	def __eq__(self, other):
		return isinstance(other, SectionType) and self.section_type == other.section_type

	def __ne__(self, other):
		return not isinstance(other, SectionType) or self.section_type != other.section_type

	def __lt__(self, other):
		if not isinstance(other, SectionType):
			raise TypeError()
		return self.section_type < other.section_type

	def __le__(self, other):
		if not isinstance(other, SectionType):
			raise TypeError()
		return self.section_type <= other.section_type

	def __gt__(self, other):
		if not isinstance(other, SectionType):
			raise TypeError()
		return self.section_type > other.section_type

	def __ge__(self, other):
		if not isinstance(other, SectionType):
			raise TypeError()
		return self.section_type >= other.section_type


class InstructorSectionRole:
	def __init__(self,
	             section_ref,
	             instructor: Instructor,
	             instructor_role_type: InstructorRoleType):
		self.section_ref: Section = section_ref
		self.instructor: Instructor = instructor
		self.instructor_role_type: InstructorRoleType = instructor_role_type

	def __eq__(self, other):
		return isinstance(other, InstructorSectionRole) \
		       and self.section_ref == other.section_ref \
		       and self.instructor == other.instructor \
		       and self.instructor_role_type == other.instructor_role_type

	def __ne__(self, other):
		return not isinstance(other, InstructorSectionRole) \
		       or self.section_ref != other.section_ref \
		       or self.instructor != other.instructor \
		       or self.instructor_role_type != other.instructor_role_type

	def __lt__(self, other):
		if not isinstance(other, InstructorSectionRole):
			raise TypeError()
		if self.section_ref < other.section_ref:
			return True
		elif self.section_ref == other.section_ref:
			if self.instructor < other.instructor:
				return True
			elif self.instructor == other.instructor:
				if self.instructor_role_type < other.instructor_role_type:
					return True
		return False

	def __le__(self, other):
		if not isinstance(other, InstructorSectionRole):
			raise TypeError()
		if self.section_ref < other.section_ref:
			return True
		elif self.section_ref == other.section_ref:
			if self.instructor < other.instructor:
				return True
			elif self.instructor == other.instructor:
				if self.instructor_role_type <= other.instructor_role_type:
					return True
		return False

	def __gt__(self, other):
		if not isinstance(other, InstructorSectionRole):
			raise TypeError()
		if self.section_ref > other.section_ref:
			return True
		elif self.section_ref == other.section_ref:
			if self.instructor > other.instructor:
				return True
			elif self.instructor == other.instructor:
				if self.instructor_role_type > other.instructor_role_type:
					return True
		return False

	def __ge__(self, other):
		if not isinstance(other, InstructorSectionRole):
			raise TypeError()
		if self.section_ref > other.section_ref:
			return True
		elif self.section_ref == other.section_ref:
			if self.instructor > other.instructor:
				return True
			elif self.instructor == other.instructor:
				if self.instructor_role_type >= other.instructor_role_type:
					return True
		return False


class Section:
	def __init__(self,
	             course,
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
	             section_times: SortedSet[SectionTime],
	             instructor_section_roles: SortedSet[InstructorSectionRole]):
		self.course: Course = course
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
		self.section_times: SortedSet[SectionTime] = section_times
		self.instructor_section_roles: SortedSet[InstructorSectionRole] = instructor_section_roles

	def __eq__(self, other):
		return isinstance(other, Section) and self.course == other.course and self.section_num == other.section_num

	def __ne__(self, other):
		return not isinstance(other, Section) or self.course != other.course or self.section_num != other.section_num

	def __lt__(self, other):
		if not isinstance(other, Section):
			raise TypeError()
		if self.course < other.course:
			return True
		elif self.course == other.course:
			if self.section_num < other.section_num:
				return True
		return False

	def __le__(self, other):
		if not isinstance(other, Section):
			raise TypeError()
		if self.course < other.course:
			return True
		elif self.course == other.course:
			if self.section_num <= other.section_num:
				return True
		return False

	def __gt__(self, other):
		if not isinstance(other, Section):
			raise TypeError()
		if self.course > other.course:
			return True
		elif self.course == other.course:
			if self.section_num > other.section_num:
				return True
		return False

	def __ge__(self, other):
		if not isinstance(other, Section):
			raise TypeError()
		if self.course > other.course:
			return True
		elif self.course == other.course:
			if self.section_num >= other.section_num:
				return True
		return False


class Course:
	def __init__(self,
	             term_ref,
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
		self.term_ref: Term = term_ref
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
		return isinstance(other, Course) \
		       and self.term_ref == other.term_ref \
		       and self.curriculum_id == other.curriculum_id \
		       and self.title_code == other.title_code

	def __ne__(self, other):
		return not isinstance(other, Course) \
		       or self.term_ref != other.term_ref \
		       or self.curriculum_id != other.curriculum_id \
		       or self.title_code != other.title_code

	def __lt__(self, other):
		if not isinstance(other, Course):
			raise TypeError()
		if self.term_ref < other.term_ref:
			return True
		elif self.term_ref == other.term_ref:
			if self.department.abbreviation < other.department.abbreviation:
				return True
			elif self.department.abbreviation == other.department.abbreviation:
				if self.catalog_num < other.catalog_num:
					return True
				elif self.catalog_num == other.catalog_num:
					if self.catalog_suffix < other.catalog_suffix:
						return True
		return False

	def __le__(self, other):
		if not isinstance(other, Course):
			raise TypeError()
		if self.term_ref < other.term_ref:
			return True
		elif self.term_ref == other.term_ref:
			if self.department.abbreviation < other.department.abbreviation:
				return True
			elif self.department.abbreviation == other.department.abbreviation:
				if self.catalog_num < other.catalog_num:
					return True
				elif self.catalog_num == other.catalog_num:
					if self.catalog_suffix <= other.catalog_suffix:
						return True
		return False

	def __gt__(self, other):
		if not isinstance(other, Course):
			raise TypeError()
		if self.term_ref > other.term_ref:
			return True
		elif self.term_ref == other.term_ref:
			if self.department.abbreviation > other.department.abbreviation:
				return True
			elif self.department.abbreviation == other.department.abbreviation:
				if self.catalog_num > other.catalog_num:
					return True
				elif self.catalog_num == other.catalog_num:
					if self.catalog_suffix > other.catalog_suffix:
						return True
		return False

	def __ge__(self, other):
		if not isinstance(other, Course):
			raise TypeError()
		if self.term_ref > other.term_ref:
			return True
		elif self.term_ref == other.term_ref:
			if self.department.abbreviation > other.department.abbreviation:
				return True
			elif self.department.abbreviation == other.department.abbreviation:
				if self.catalog_num > other.catalog_num:
					return True
				elif self.catalog_num == other.catalog_num:
					if self.catalog_suffix >= other.catalog_suffix:
						return True
		return False


class Term:
	def __init__(self, data_set_ref, year: int, term: int, courses: SortedSet[Course], collection_time: datetime.datetime):
		self.data_set_ref: DataSet = data_set_ref
		self.year: int = year
		self.term: int = term
		self.courses: SortedSet[Course] = courses
		self.collection_time = collection_time

	def __eq__(self, other):
		return isinstance(other, Term) \
		       and self.data_set_ref == other.data_set_ref \
		       and self.year == other.year \
		       and self.term == other.term

	def __ne__(self, other):
		return not isinstance(other, Term) \
		       or self.data_set_ref != other.data_set_ref \
		       or self.year != other.year \
		       or self.term != other.term

	def __lt__(self, other):
		if not isinstance(other, Term):
			raise TypeError()
		if self.data_set_ref < other.data_set_ref:
			return True
		elif self.data_set_ref == other.data_set_ref:
			if self.year < other.year:
				return True
			elif self.year == other.year:
				if self.term < other.term:
					return True
				elif self.term == other.term:
					if self.collection_time < other.collection_time:
						return True
		return False

	def __le__(self, other):
		if not isinstance(other, Term):
			raise TypeError()
		if self.data_set_ref < other.data_set_ref:
			return True
		elif self.data_set_ref == other.data_set_ref:
			if self.year < other.year:
				return True
			elif self.year == other.year:
				if self.term < other.term:
					return True
				elif self.term == other.term:
					if self.collection_time <= other.collection_time:
						return True
		return False

	def __gt__(self, other):
		if not isinstance(other, Term):
			raise TypeError()
		if self.data_set_ref > other.data_set_ref:
			return True
		elif self.data_set_ref == other.data_set_ref:
			if self.year > other.year:
				return True
			elif self.year == other.year:
				if self.term > other.term:
					return True
				elif self.term == other.term:
					if self.collection_time > other.collection_time:
						return True
		return False

	def __ge__(self, other):
		if not isinstance(other, Term):
			raise TypeError()
		if self.data_set_ref > other.data_set_ref:
			return True
		elif self.data_set_ref == other.data_set_ref:
			if self.year > other.year:
				return True
			elif self.year == other.year:
				if self.term > other.term:
					return True
				elif self.term == other.term:
					if self.collection_time >= other.collection_time:
						return True
		return False


class DataSet:
	def __init__(self,
	             buildings: SortedSet[Building],
	             credit_types: SortedSet[CreditType],
	             instructors: SortedSet[Instructor],
	             instructor_role_types: SortedSet[InstructorRoleType],
	             section_modes: SortedSet[SectionMode],
	             section_types: SortedSet[SectionType],
	             terms: SortedSet[Term]):
		self.buildings: SortedSet[Building] = buildings
		self.credit_types: SortedSet[CreditType] = credit_types
		self.instructors: SortedSet[Instructor] = instructors
		self.instructor_role_types: SortedSet[InstructorRoleType] = instructor_role_types
		self.section_modes: SortedSet[SectionMode] = section_modes
		self.section_types: SortedSet[SectionType] = section_types
		self.terms: SortedSet[Term] = terms


def load_data_set(file: str) -> DataSet:
	with open(file, 'rb') as f:
		item = pickle.load(f)
		if not isinstance(item, DataSet):
			raise TypeError('Loaded dataset is wrong type')
		return item


def save_data_set(file: str, data_set: DataSet) -> None:
	with open(file, 'wb') as f:
		pickle.dump(data_set, f)
