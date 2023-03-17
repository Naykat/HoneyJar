def get_type(variable) -> str:
    return str(type(variable)).split("'")[1]

def remove_repeats(variable: str or list) -> str or list: 
    if type(variable) is str:
        clean_string = ''
        for letter in variable:
            if not(letter in clean_string):
                clean_string+=letter
        return clean_string

    elif type(variable) is list:
        clean_array = []
        for item in variable:
            if not(item in clean_array):
                clean_array.append(item)
        return clean_array 
    else:
        raise TypeError(f"variable's type can be str or list, not {get_type(var)}")
