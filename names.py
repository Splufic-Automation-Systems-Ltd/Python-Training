"""Help on Names Module.
NAME:
	Names.py
DESCRIPTION:
	This module helps to oeprate on names. It is a helper module
	to use on names of people.

FUNCTIONS:
	cap(name):
		capitalize a person's name and return it.

	title(name);
		title a person's name and return it

	getFullname(first_name, second_name):
		takes two args: first_name and second_name
		and returns the full name of a person.
"""


def cap(name):
	"""Function Cap
		@args: name -> string
		@returns: string
	"""
	return name.upper()

def title(name):
	"""Function Title
		@args: name -> string
		@returns: string
	"""
	return name.title()


def getFullName(f_name, s_name):
	"""Function getFullname 
		It takes two args: first_name and second_name
		and returns the full name of a person
		@args: f_name -> string
		@args: s_name -> string
		@returns: string
	"""
	return ' '.join([f_name.title(), s_name.title()])
	# return f_name + ' ' + s_name