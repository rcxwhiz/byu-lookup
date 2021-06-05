import datetime
import pickle
from sortedcontainers import SortedSet

id_to_term = {1: 'winter',
              3: 'spring',
              4: 'summer',
              5: 'fall'}
term_to_id = {v: k for k, v in id_to_term.items()}


class Building:
	def __init__(self, name: str):
		self.name: str = name.capitalize()

	def __str__(self):
		return self.name

	def __hash__(self):
		return hash(self.name)

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

	def __str__(self):
		return self.name

	def __hash__(self):
		return hash(self.abbreviation)

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

	def __str__(self):
		return self.instructor_role_type

	def __hash__(self):
		return hash(self.instructor_role_type)

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

	def __str__(self):
		if self.sort_name is not None:
			return self.sort_name
		elif self.surname is not None and self.rest_of_name is not None:
			return f'{self.surname}, {self.rest_of_name}'
		else:
			return f'{self.person_id:09}'

	def __hash__(self):
		return hash(self.person_id)

	def __eq__(self, other):
		return isinstance(other, Instructor) and self.person_id == other.person_id

	def __ne__(self, other):
		return not isinstance(other, Instructor) or self.person_id != other.person_id

	def __lt__(self, other):
		if not isinstance(other, Instructor):
			raise TypeError()
		return self.sort_name < other.sort_name or (
				self.sort_name == other.sort_name and self.person_id < other.person_id)

	def __le__(self, other):
		if not isinstance(other, Instructor):
			raise TypeError()
		return self.sort_name <= other.sort_name or (
				self.sort_name == other.sort_name and self.person_id <= other.person_id)

	def __gt__(self, other):
		if not isinstance(other, Instructor):
			raise TypeError()
		return self.sort_name > other.sort_name or (
				self.sort_name == other.sort_name and self.person_id > other.person_id)

	def __ge__(self, other):
		if not isinstance(other, Instructor):
			raise TypeError()
		return self.sort_name >= other.sort_name or (
				self.sort_name == other.sort_name and self.person_id >= other.person_id)


class CreditType:
	def __init__(self, credit_type: str):
		self.credit_type = credit_type.capitalize()

	def __str__(self):
		return self.credit_type

	def __hash__(self):
		return hash(self.credit_type)

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
		self.description: str = description.capitalize() if description is not None else None

	def __str__(self):
		return self.section_mode

	def __hash__(self):
		return hash(self.section_mode)

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
		self.room: str = room.lower() if room is not None else None
		self.sequence_num: int = sequence_num
		self.sunday: bool = sunday
		self.monday: bool = monday
		self.tuesday: bool = tuesday
		self.wednesday: bool = wednesday
		self.thursday: bool = thursday
		self.friday: bool = friday
		self.saturday: bool = saturday

	def __str__(self):
		s = f'{self.section_ref} - {self.sequence_num} '
		if self.sunday:
			s += 'Su'
		if self.monday:
			s += 'M'
		if self.tuesday:
			s += 'Tu'
		if self.wednesday:
			s += 'W'
		if self.thursday:
			s += 'Th'
		if self.friday:
			s += 'F'
		if self.saturday:
			s += 'Sa'
		s += f' {self.begin_time}-{self.end_time}'
		return s

	def __hash__(self):
		return hash(self.section_ref) ^ hash(self.sequence_num)

	def __eq__(self, other):
		return isinstance(other,
		                  SectionTime) and self.section_ref == other.section_ref and self.sequence_num == other.sequence_num

	def __ne__(self, other):
		return not isinstance(other,
		                      SectionTime) or self.section_ref != other.section_ref or self.sequence_num != other.sequence_num

	def __lt__(self, other):
		if not isinstance(other, SectionTime):
			raise TypeError()
		return self.section_ref < other.section_ref or (
				self.section_ref == other.section_ref and self.sequence_num < other.sequence_num)

	def __le__(self, other):
		if not isinstance(other, SectionTime):
			raise TypeError()
		return self.section_ref < other.section_ref or (
				self.section_ref == other.section_ref and self.sequence_num <= other.sequence_num)

	def __gt__(self, other):
		if not isinstance(other, SectionTime):
			raise TypeError()
		return self.section_ref > other.section_ref or (
				self.section_ref == other.section_ref and self.sequence_num > other.sequence_num)

	def __ge__(self, other):
		if not isinstance(other, SectionTime):
			raise TypeError()
		return self.section_ref > other.section_ref or (
				self.section_ref == other.section_ref and self.sequence_num >= other.sequence_num)


class SectionType:
	def __init__(self, section_type: str):
		self.section_type: str = section_type.capitalize()

	def __str__(self):
		return self.section_type

	def __hash__(self):
		return hash(self.section_type)

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

	def __str__(self):
		return f'{self.section_ref} - {self.instructor} - {self.instructor_role_type}'

	def __hash__(self):
		return hash(self.section_ref) ^ hash(self.instructor) ^ hash(self.instructor_role_type)

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

	def __str__(self):
		return f'{self.course} - {self.section_num:03}'

	def add_role(self, instructor: Instructor, role: InstructorRoleType) -> InstructorSectionRole:
		role = InstructorSectionRole(self, instructor, role)
		self.instructor_section_roles.add(role)
		return role

	def add_time(self,
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
	             saturday: bool) -> SectionTime:
		time = SectionTime(self,
		                   begin_time,
		                   end_time,
		                   building,
		                   room,
		                   sequence_num,
		                   sunday,
		                   monday,
		                   tuesday,
		                   wednesday,
		                   thursday,
		                   friday,
		                   saturday)
		self.section_times.add(time)
		return time

	def __hash__(self):
		return hash(self.course) ^ hash(self.section_num)

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
		self.catalog_suffix: str = catalog_suffix.upper() if catalog_suffix is not None else None
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

	def __str__(self):
		return f'{self.department.abbreviation} {self.catalog_num}{self.catalog_suffix if self.catalog_suffix is not None else ""}'

	def make_section(self,
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
	                 section_mode: SectionMode) -> Section:
		section = Section(self,
		                  section_num,
		                  fixed_or_variable,
		                  credit_hours,
		                  min_credit_hours,
		                  is_honors,
		                  credit_type,
		                  section_type,
		                  start_date,
		                  end_date,
		                  seats_available,
		                  class_size,
		                  waitlist_size,
		                  section_mode,
		                  SortedSet(),
		                  SortedSet())
		self.sections.add(section)
		return section

	def __hash__(self):
		return hash(self.term_ref) ^ hash(self.curriculum_id) ^ hash(self.title_code)

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
					if (self.catalog_suffix if self.catalog_suffix is not None else '') < (
					other.catalog_suffix if other.catalog_suffix is not None else ''):
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
					if (self.catalog_suffix if self.catalog_suffix is not None else '') <= (
					other.catalog_suffix if other.catalog_suffix is not None else ''):
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
					if (self.catalog_suffix if self.catalog_suffix is not None else '') > (
					other.catalog_suffix if other.catalog_suffix is not None else ''):
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
					if (self.catalog_suffix if self.catalog_suffix is not None else '') >= (
					other.catalog_suffix if other.catalog_suffix is not None else ''):
						return True
		return False


class Term:
	def __init__(self, data_set_ref, year: int, term: int, courses: SortedSet[Course],
	             collection_time: datetime.datetime):
		self.data_set_ref: DataSet = data_set_ref
		self.year: int = year
		self.term: int = term
		self.courses: SortedSet[Course] = courses
		self.collection_time = collection_time

	def __str__(self):
		return f'{id_to_term[self.term].capitalize()} {self.year}'

	def year_term(self) -> str:
		return f'{self.year}{self.term}'

	def make_course(self,
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
	                when_taught: str) -> Course:
		course = Course(self,
		                curriculum_id,
		                title_code,
		                department,
		                catalog_num,
		                catalog_suffix,
		                title,
		                full_title,
		                effective_date,
		                expired_date,
		                effective_year_term,
		                expired_year_term,
		                description,
		                note,
		                offered,
		                prerequisite,
		                recommended,
		                credit_hours,
		                lecture_hours,
		                lab_hours,
		                honors_approved,
		                catalog_prereq,
		                when_taught,
		                SortedSet())
		self.courses.add(course)
		return course

	def __hash__(self):
		return hash(self.year) ^ hash(self.term)

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
	             save_path: str,
	             buildings: SortedSet[Building],
	             departments: SortedSet[Department],
	             credit_types: SortedSet[CreditType],
	             instructors: SortedSet[Instructor],
	             instructor_role_types: SortedSet[InstructorRoleType],
	             section_modes: SortedSet[SectionMode],
	             section_types: SortedSet[SectionType],
	             terms: SortedSet[Term]):
		self.save_path: str = save_path
		self.buildings: SortedSet[Building] = buildings
		self.departments: SortedSet[Department] = departments
		self.credit_types: SortedSet[CreditType] = credit_types
		self.instructors: SortedSet[Instructor] = instructors
		self.instructor_role_types: SortedSet[InstructorRoleType] = instructor_role_types
		self.section_modes: SortedSet[SectionMode] = section_modes
		self.section_types: SortedSet[SectionType] = section_types
		self.terms: SortedSet[Term] = terms

	def __str__(self):
		return f'Data set at {self.save_path}'

	def save(self):
		save_data_set(self.save_path, self)

	def make_term(self, year: int, term: int) -> Term:
		term = Term(self, year, term, SortedSet(), datetime.datetime.now())
		try:
			self.terms.remove(term)
		except KeyError:
			pass
		self.terms.add(term)
		return term

	def get_building(self, name: str) -> Building:
		building = Building(name)
		self.buildings.add(building)
		return building

	def put_department(self, name: str, abbreviation: str) -> Department:
		dept = Department(name, abbreviation)
		self.departments.add(dept)
		return dept

	def get_department(self, abbreviation: str) -> Department:
		for dept in self.departments:
			if dept.abbreviation == abbreviation:
				return dept
		raise ValueError(f'Dept {abbreviation} not found')

	def get_credit_type(self, credit_type: str) -> CreditType:
		ct = CreditType(credit_type)
		self.credit_types.add(ct)
		return ct

	def make_instructor(self,
	                    sort_name: str,
	                    last_name: str,
	                    first_name: str,
	                    person_id: int,
	                    byu_id: int,
	                    net_id: str,
	                    surname: str,
	                    rest_of_name: str,
	                    preferred_first_name: str,
	                    phone_number: str) -> Instructor:
		instructor = Instructor(sort_name,
		                        last_name,
		                        first_name,
		                        person_id,
		                        byu_id,
		                        net_id,
		                        surname,
		                        rest_of_name,
		                        preferred_first_name,
		                        phone_number)
		self.instructors.add(instructor)
		return instructor

	def update_instructor(self,
	                      person_id: int,
	                      sort_name: str = None,
	                      last_name: str = None,
	                      first_name: str = None,
	                      byu_id: int = None,
	                      net_id: str = None,
	                      surname: str = None,
	                      rest_of_name: str = None,
	                      preferred_first_name: str = None,
	                      phone_number: str = None) -> None:
		for instructor in self.instructors:
			if instructor.person_id == person_id:
				if sort_name:
					instructor.sort_name = sort_name
				if last_name:
					instructor.last_name = last_name
				if first_name:
					instructor.first_name = first_name
				if byu_id:
					instructor.byu_id = byu_id
				if net_id:
					instructor.net_id = net_id
				if surname:
					instructor.surname = surname
				if rest_of_name:
					instructor.rest_of_name = rest_of_name
				if preferred_first_name:
					instructor.preferred_first_name = preferred_first_name
				if phone_number:
					instructor.phone_number = phone_number
				return None
		raise ValueError(f'Person ID {person_id} not found')

	def get_instructor(self, person_id: int) -> Instructor:
		for instructor in self.instructors:
			if instructor.person_id == person_id:
				return instructor
		raise ValueError(f'Person ID {person_id} not found')

	def get_instructor_role_type(self, instructor_role_type: str) -> InstructorRoleType:
		irt = InstructorRoleType(instructor_role_type)
		self.instructor_role_types.add(irt)
		return irt

	def get_section_mode(self, mode: str, description: str) -> SectionMode:
		section_mode = SectionMode(mode, description)
		self.section_modes.add(section_mode)
		return section_mode

	def get_section_type(self, section_type: str) -> SectionType:
		st = SectionType(section_type)
		self.section_types.add(st)
		return st

	def get_term(self, year: int, term: int) -> Term:
		for t in self.terms:
			if t.year == year and t.term == term:
				return t
		raise ValueError(f'Term {year}{term} not found')


def get_data_set(file: str, load: bool = True) -> DataSet:
	if not load:
		return DataSet(file,
		               SortedSet(),
		               SortedSet(),
		               SortedSet(),
		               SortedSet(),
		               SortedSet(),
		               SortedSet(),
		               SortedSet(),
		               SortedSet())
	try:
		return load_data_set(file)
	except (FileExistsError, FileNotFoundError):
		return DataSet(file,
		               SortedSet(),
		               SortedSet(),
		               SortedSet(),
		               SortedSet(),
		               SortedSet(),
		               SortedSet(),
		               SortedSet(),
		               SortedSet())


def load_data_set(file: str) -> DataSet:
	with open(file, 'rb') as f:
		item = pickle.load(f)
		if not isinstance(item, DataSet):
			raise TypeError('Loaded dataset is wrong type')
		return item


def save_data_set(file: str, data_set: DataSet) -> None:
	with open(file, 'wb') as f:
		pickle.dump(data_set, f)
