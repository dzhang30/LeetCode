# You got the following piece of Python code written by an intern
# Your task is to "clean up" the code below and make it more Pythonic/idiomatic
# We would be using Python 3.7 and thus you are encouraged to use any new language features available upto Python 3.7
from pprint import pprint

def is_valid_year(x, l, r):
	if l <= x and r > x:
		return True
	elif x == 2020 or x == 2040 or x == 2060 or x == 2075 or x == 2036:
		return True
	else:
		return False

class Entry(object):

	def __init__(self, year, lower, upper):
		self.year = year
		self.lower = lower
		self.upper = upper

	def __str__(self):
		return 'year=' + self.year + '; lower=' + self.lower + '; upper=' + self.upper

def print_conflicts(entries, bad):
	good = []
	i = 0
	while i < len(entries):
		entry = entries[i]
		if is_valid_year(entry.year, entry.lower, entry.upper):
			good.append(entry.year)
		i += 1

	seen = []
	for g in good:
		for b in bad:
			if g == b and g not in seen:
				print(str(g) + ' is both a good and bad year')
				seen.append(g)
				
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
], bad = [2017, 2019])


output = generate_rows(
	cols = ['id', 'name', 'age'],
	rows = [
		[1, 'Rick', 23],
		[2, 'Victor', 18],
		[3, 'Alfred', 54]
	]
)

pprint(list(output))