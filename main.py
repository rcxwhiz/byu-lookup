from sortedcontainers import SortedSet
import byu_lookup.model
import byu_lookup.api_access.to_models


def run():
    data = byu_lookup.model.DataSet(SortedSet(),
                                    SortedSet(),
                                    SortedSet(),
                                    SortedSet(),
                                    SortedSet(),
                                    SortedSet(),
                                    SortedSet(),
                                    SortedSet())
    term = data.make_term(2020, 3)
    byu_lookup.api_access.to_models.populate_term(term)


if __name__ == '__main__':
    run()
