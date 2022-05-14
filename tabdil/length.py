


# this function converts sort of length units (kilometers,metres,centimetre,inch) to millimeters

def millimeter(length_unit):
	unit_name = length_unit[0].lower()
	number = 1
	if unit_name == 'km':
		number = 1000 * 100 * 10 
	elif unit_name == 'm':
		number = 100 * 10 
	elif unit_name == 'cm':
		number = 10 
	elif unit_name == 'mi':
		number = 1.60934 * 1000 * 100 * 10
	elif unit_name == 'mm':
		pass
	elif unit_name == 'inch':
		number=25.4
	else:
		raise ValueError('unknown unit name {!r}'.format(unit_name))
	unit_number = length_unit[1]
	return unit_number * number

# this function converts sort of length units (kilometers,metres,millimeter,inch) to centimetre

def centimeter(length_unit):
	unit_name = length_unit[0].lower()
	number = 1
	if unit_name == 'km':
		number = 1000 * 100 
	elif unit_name == 'm':
		number = 100 
	elif unit_name == 'cm':
		pass 
	elif unit_name == 'mm':
		number = 1/10
	elif unit_name == 'inch':
		number=2.54
	else:
		raise ValueError('unknown unit name {!r}'.format(unit_name))
	unit_number = length_unit[1]
	return unit_number * number	

# this function converts sort of length units (kilometers,millimetres,centimetre,inch) to meter

def meter(length_unit):
	unit_name = length_unit[0].lower()
	number = 1
	if unit_name == 'km':
		number = 1000 
	elif unit_name == 'm':
		pass
	elif unit_name == 'cm':
		number = 1/100 
	elif unit_name == 'mm':
		number = 1/1000
	elif unit_name == 'inch':
		number=0.0254

	elif unit_name == 'mi':
		number = 1.60934 * 1000 * 100
	else:
		raise ValueError('unknown unit name {!r}'.format(unit_name))
	unit_number = length_unit[1]
	return unit_number * number

# this function converts sort of length units (millimeters,metres,centimetre,inch) to kilometers

def kilometer(length_unit):
	unit_name = length_unit[0].lower()
	number = 1
	if unit_name == 'km':
		pass 
	elif unit_name == 'm':
		number = 0.001
	elif unit_name == 'cm':
		number = 0.00001 
	elif unit_name == 'mm':
		number = 0.000001
	elif unit_name == 'inch':
		number=0.0000254
	else:
		raise ValueError('unknown unit name {!r}'.format(unit_name))
	unit_number = length_unit[1]
	return unit_number * number

# this function converts sort of length units (kilometers,metres,centimetre,millimeters) to inch

def inch(length_unit):
	unit_name = length_unit[0].lower()
	number = 1
	if unit_name == 'km':
		number = 39370 
	elif unit_name == 'm':
		number = 39.37
	elif unit_name == 'cm':
		number = 0.3937 
	elif unit_name == 'mm':
		number = 0.03937
	elif unit_name == 'inch':
		pass
	else:
		raise ValueError('unknown unit name {!r}'.format(unit_name))
	unit_number = length_unit[1]
	return unit_number * number
