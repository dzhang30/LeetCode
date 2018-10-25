import unittest

from dataclasses import dataclass
from typing import Union, List, Set, Dict, Iterator, Tuple, Any

from pandas import DataFrame


@dataclass
class Entry(object):
    year: int
    lower: int
    upper: int

    const_valid_years = frozenset({2020, 2040, 2060, 2075, 2036})

    def is_valid_year(self) -> bool:
        """
        Check if the Entry object's year field is within its lower(inclusive) and upper(exclusive) bounds

        :return: True/False based on if the year is within bounds
        """
        return self.lower <= self.year < self.upper or self.year in Entry.const_valid_years

    def __str__(self) -> str:
        """
        Human readable string representation of an Entry

        :return: String form of an Entry
        """
        return 'year={0}; lower={1}; upper={2}'.format(self.year, self.lower, self.upper)


# Broke down bad.py's print_conflicts into get_conflicts and print_conflicts. We want to have this standalone function
# so end users can actually access the contents of the conflicts set
def get_conflicts(entries: Union[List[Entry], Set[Entry]], bad_years: Union[List[int], Set[int]]) -> Iterator[int]:
    """
    Generator that will yield the intersection between a set of year-validated entries and a set of conflicting years

    :param entries: list or set of Entry objects
    :param bad_years: list or set of conflicting years
    :return: Iterator of conflicting years
    """
    valid_years = {entry.year for entry in entries if entry.is_valid_year()}
    return filter(lambda bad_year: bad_year in valid_years, bad_years)


def generate_rows(cols: List[str], rows: List[List[Any]]) -> Iterator[Dict]:
    """
    Generator that will yield a table row in the form of a dictionary the dict keys are the row attributes and the
    dict values are the row values

    :param cols: The header row (attribute/type for each element in a row)
    :param rows: List of rows
    :return: Iterator of dictionary objects
    """
    return map(lambda row: dict(_zip_same_length(cols, row)), rows)


def _zip_same_length(col: List[str], row: List[List[Any]]) -> Iterator[Tuple[str, Any]]:
    """
    Helper zip function that raises a ValueError if the length of the header column and row are different

    :param col: The header row
    :param row: A table row
    :return: Iterator of (col, row) tuples
    """
    if len(col) != len(row):
        raise ValueError('the length of row: {} and the header column: {} should be the same'.format(row, col))
    return zip(col, row)


def print_conflicts(entries: Union[List[Entry], Set[Entry]], bad_years: Union[List[int], Set[int]]) -> None:
    """
    Print the intersection between a set of year-validated entries and a list/set of conflicting years

    :param entries: list or set of Entry objects
    :param bad_years: list or set of conflicting years
    :return: None
    """
    conflicts = get_conflicts(entries, bad_years)
    print('\n'.join('{0} is good and bad'.format(c) for c in conflicts))


def pprint_rows_df(cols: List[str], rows: List[List[Any]]) -> None:
    """
    Pretty Print a DataFrame table given the rows and columns.

    :param cols: The header row
    :param rows: List of rows
    :return: None
    """
    table = list(generate_rows(cols, rows))
    print(DataFrame(table))


############ Test ############
class TestInternCode(unittest.TestCase):

    def test_entry_is_valid_year(self) -> None:
        self.assertFalse(Entry(2018, 2009, 2010).is_valid_year())
        self.assertTrue(Entry(2017, 2009, 2020).is_valid_year())
        self.assertTrue(Entry(2020, 1992, 1993).is_valid_year())

    def test_get_conflicts(self) -> None:
        entries = [
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
        ]
        bad_years = [2017, 2019, 2020]

        self.assertListEqual([2017, 2020], list(get_conflicts(entries, bad_years)))
        self.assertListEqual([], list(get_conflicts([], [])))

    def test_generate_rows(self) -> None:
        expected_output = [
            {'id': 1, 'name': 'Rick', 'age': 23},
            {'id': 2, 'name': 'Victor', 'age': 18},
            {'id': 3, 'name': 'Alfred', 'age': 54}
        ]
        test_output = generate_rows(
            cols=['id', 'name', 'age'],
            rows=[[1, 'Rick', 23], [2, 'Victor', 18], [3, 'Alfred', 54]]
        )

        self.assertListEqual(expected_output, list(test_output))
        self.assertListEqual([], list(generate_rows([], [])))

        with self.assertRaises(ValueError):
            generate_rows(['id', 'name', 'age'], [[7, 'not enough args']])


if __name__ == '__main__':
    print_conflicts(
        entries=[
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
        ],
        bad_years=[2017, 2019, 2020]
    )

    pprint_rows_df(
        cols=['id', 'name', 'age'],
        rows=[[1, 'Rick', 23], [2, 'Victor', 18], [3, 'Alfred', 54]]
    )

    unittest.main()
