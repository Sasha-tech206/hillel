import string
import keyword

variable_names = ["_", "__", "___", "x", "get_value", "get value", "get!value","some_super_puper_value", "Get_value", "get_Value", "getValue","3m", "m3", "assert", "assert_exception"]

for variable_name in variable_names:
    is_valid = True

    if variable_name[0].isdigit():
        is_valid = False

    for char in variable_name:
        if char in string.punctuation.replace("_", "") or char.isupper() or char.isspace():
            is_valid = False
            
    if variable_name in keyword.kwlist:
        is_valid = False

    if variable_name.count("_") > 1:
        is_valid = False

    print(f"{variable_name} => {is_valid}")