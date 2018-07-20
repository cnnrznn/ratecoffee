#!/usr/bin/python3

import datetime as dt
import getpass

_rootdir = './'

def clean(user_input, valid):
	try:
		result = int(user_input)
		if result not in valid:
			raise
		return result
	except:
		return 0

def error():
	print('\n============================')
	print('Nice try...')
	print('============================\n')

def get_type():
	global _type
	_type = input('1: Latte\n'\
		      '2: Espresso\n\n' \
		      'Type: ')

	return clean(_type, [1, 2])

def get_sour():
	global _taste_sour
	_taste_sour = input('Sour [1-10]: ')
	return clean(_taste_sour, range(1, 11))

def get_bitter():
	global _taste_bitter
	_taste_bitter = input('Bitter [1-10]: ')
	return clean(_taste_bitter, range(1, 11))

if __name__ == '__main__':
	while not(get_type()):
		error()
	while not(get_sour()):
		error()
	while not(get_bitter()):
		error()

	# TODO store information
	#with open('./'
	#	f.write((_type, _taste_sour, _taste_bitter)
	now = dt.datetime.now()
	fn = '{}-{}-{}-{}-{}-{}'.format(now.year,
				     	now.month,
				     	now.day,
				     	now.hour,
				     	now.minute,
					getpass.getuser())

	with open(_rootdir + fn, 'w') as f:
		f.write('{} {} {}'.format(_type, _taste_sour, _taste_bitter))

	print('Thanks')
