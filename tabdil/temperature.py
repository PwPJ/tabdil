#Convert Celsius to other units of temperature

def celsius(temp_unit):
	unit_name = temp_unit[0].lower()
	number = 1
	unit_number = temp_unit[1]
	if unit_name == 'k':
		return unit_number + 273.15
	elif unit_name == 'f':
		return unit_number * 9.5 + 32
	else:
		raise ValueError('unknown unit name {!r}'.format(unit_name))
