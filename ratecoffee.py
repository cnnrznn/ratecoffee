#!/usr/bin/python3

'''
This program reads some user input about coffee and
writes the output to a time-stamped file.
'''

import datetime as dt
import getpass
import rootdir

_rootdir = rootdir._rootdir + '/ratings/'

_type = ''
_taste_sour = -1
_taste_bitter = -1

def is_clean(user_input, valid):
	try:
		result = int(user_input)
		if result not in valid:
			raise
		return 0    # Looks good
	except:
		return 1    # Error

def error():
	print('\n============================')
	print('Nice try...')
	print('============================\n')

def get_type():
	global _type
	_type = input('1: Latte\n'\
		      '2: Espresso\n\n' \
		      'Type: ')

	return is_clean(_type, [1, 2])

def get_sour():
	global _taste_sour
	_taste_sour = input('Sour [0-10]: ')
	return is_clean(_taste_sour, range(0, 11))

def get_bitter():
	global _taste_bitter
	_taste_bitter = input('Bitter [0-10]: ')
	return is_clean(_taste_bitter, range(0, 11))

if __name__ == '__main__':
	while get_type():
		error()
	while get_sour():
		error()
	while get_bitter():
		error()

	now = dt.datetime.now()
	fn = '{}-{}-{}-{}-{}-{}'.format(now.year,
				     	now.month,
				     	now.day,
				     	now.hour,
				     	now.minute,
					getpass.getuser())

	with open(_rootdir + fn, 'w') as f:
		f.write('type:{}\nsour:{}\nbitter:{}\n'
                            .format(_type, _taste_sour, _taste_bitter))

	print('Thanks')
