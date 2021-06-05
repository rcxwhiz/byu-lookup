import byu_lookup.model
import byu_lookup.api_access.to_models


load = False
data_path = 'data.byu'
year = 2020
term = 3


def print_term(term: byu_lookup.model.Term) -> None:
	print(term)
	print()
	print('Courses:')
	for course in term.courses:
		print(course)
		for section in course.sections:
			print(f'\t{section}')
	print()


def run() -> None:
	data = byu_lookup.model.get_data_set(data_path, load=load)
	if not load:
		t = data.make_term(year, term)
		byu_lookup.api_access.to_models.populate_term(t)
	else:
		t = data.get_term(year, term)
	data.save()
	print_term(t)


if __name__ == '__main__':
	run()
