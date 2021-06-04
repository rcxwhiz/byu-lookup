import byu_lookup.model
import byu_lookup.api_access.to_models


def run():
    term = byu_lookup.api_access.to_models.get_term_model(2020, 3)
    byu_lookup.api_access.to_models.populate_term(term)


if __name__ == '__main__':
    run()
