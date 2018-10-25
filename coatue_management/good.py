# You got the following piece of Python code written by an intern
# Your task is to "clean up" the code below and make it more Pythonic/idiomatic
# We would be using Python 3.7 and thus you are encouraged to use any new language features available upto Python 3.7
from pprint import pprint
from dataclasses import dataclass
from typing import Union, List, Set


@dataclass
class Entry(object):
    year: int
    lower: int
    upper: int

    const_valid_years = frozenset({2020, 2040, 2060, 2075, 2036})

    def is_valid_year(self) -> bool:
        return self.lower <= self.year < self.upper or self.year in Entry.const_valid_years

    def __str__(self):
        return 'year={0}; lower={1}; upper={2}'.format(self.year, self.lower, self.upper)


def print_conflicts(entries: Union[List[Entry], Set[Entry]], bad_years: Union[List[int], Set[int]]) -> None:
    valid_years = {entry.year for entry in entries if entry.is_valid_year()}
    conflicts = filter(lambda x: x in valid_years, bad_years)

    print('\n'.join('{} is good and bad'.format(c) for c in conflicts))


def generate_rows(cols, rows):
    c = len(cols)
    r = len(rows)

    i = 0
    while i < r:
        result = {}
        row = rows[i]
        j = 0
        while j < c:
            col = cols[j]
            result[col] = row[j]
            j += 1
        yield result
        i += 1


if __name__ == '__main__':
    ####### Test ############
    print_conflicts([
        Entry(2018, 2009, 2010),
        Entry(2017, 2009, 2020),
        Entry(2017, 1982, 2020),
        Entry(2016, 1992, 1999),
        Entry(2015, 1992, 2080),
        Entry(2020, 2007, 2009),
        Entry(2018, 2020, 2040),
        Entry(2020, 1992, 1993),
        Entry(2016, 1982, 1999),
        Entry(2015, 2003, 2020),
        Entry(2017, 1993, 2001),
    ], bad_years=[2017, 2019, 2016, 2020])

    output = generate_rows(
        cols=['id', 'name', 'age'],
        rows=[
            [1, 'Rick', 23],
            [2, 'Victor', 18],
            [3, 'Alfred', 54]
        ]
    )

    pprint(list(output))

    a = Entry(2015, 1992, 2080)
    b = Entry(2020, 2007, 2009)
