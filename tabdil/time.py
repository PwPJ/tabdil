

def seconds(time_unit):
	unit_name = time_unit[0].lower()
	number = 1
	number = Switcher(unit_name)
	unit_number = time_unit[1]
	return unit_number * number


def Switcher(unit):
    return {
        'w': 7 * 24 * 60 * 60,
        'd': 24 * 60 * 60,
        'h': 60 * 60,
        'm': 60,
		's': 1
    }.get(unit, f'unknown unit name: {unit}!')
