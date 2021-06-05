import byu_lookup.model
import byu_lookup.api_access.to_models


data_path = 'data.byu'


def print_term(term: byu_lookup.model.Term) -> None:
    print(term)
    print()
    print('Courses:')
    for course in term.courses:
        print(course)
    print()


def run() -> None:
    data = byu_lookup.model.get_data_set(data_path)
    term = data.make_term(2020, 3)
    byu_lookup.api_access.to_models.populate_term(term)
    data.save()
    print_term(term)


if __name__ == '__main__':
    run()
