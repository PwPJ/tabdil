

def fahrenheit(tem_unit):
    unit_tem = tem_unit[0].lower()
    number = 1
    unit_number = tem_unit[1]
    unit_name = tem_unit[0].lower()
    if unit_tem == 'c':
        number = unit_number * 1.8 +32
    elif unit_tem == 'k':
        number = unit_number * 1.8 -459.67
    elif unit_tem == 'ra':
        number = unit_number - 459.67
    elif unit_tem == 're':
        number = unit_number * 2.25 + 32
    elif unit_tem == 'f':
        number = unit_number
        pass
    else:
         raise ValueError('unknown unit name {!r}'.format(unit_name))
    return number
