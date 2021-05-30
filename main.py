import datetime

import byu_lookup.model


def run():
    term = byu_lookup.model.Term(0, 0, datetime.datetime.now())
    print(term.sections)
    print(term.sections.dtypes)


if __name__ == '__main__':
    run()
