

#The function below converts different sorts of time units (weeks,days,hours,minutes) to seconds.

def second(time_unit):
	unit_name = time_unit[0].lower()
	number = 1
	if unit_name == 'w':
		number = 7 * 24 * 60 * 60
	elif unit_name == 'd':
		number = 24 * 60 * 60
	elif unit_name == 'h':
		number = 60 * 60
	elif unit_name == 'm':
		number = 60
	elif unit_name == 's':
		pass
	else:
		raise ValueError('unknown unit name {!r}'.format(unit_name))
	unit_number = time_unit[1]
	return unit_number * number

#The function below converts different sorts of time units (weeks,days,hours,seconds) to minutes.

def minute(time_unit):
	unit_name = time_unit[0].lower()
	number = 1
	if unit_name == 'w':
		number = 7 * 24 * 60
	elif unit_name == 'd':
		number = 24 * 60
	elif unit_name == 'h':
		number = 60
	elif unit_name == 'm':
		pass
	elif unit_name == 's':
		number = 1/60
	else:
		raise ValueError('unknown unit name {!r}'.format(unit_name))
	unit_number = time_unit[1]
	return unit_number * number

#The function below converts different sorts of time units (weeks,days,minutes,seconds) to hours.

def hour(time_unit):
	unit_name = time_unit[0].lower()
	number = 1
	if unit_name == 'w':
		number = 7 * 24
	elif unit_name == 'd':
		number = 24
	elif unit_name == 'h':
		pass
	elif unit_name == 'm':
		number = 1/60
	elif unit_name == 's':
		number = 1/3600
	else:
		raise ValueError('unknown unit name {!r}'.format(unit_name))
	unit_number = time_unit[1]
	return unit_number * number
