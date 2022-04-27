def __get_nested_value(dict, dict_keys):
    if len(dict_keys) == 0:
        return dict

    key, *keys = dict_keys

    return __get_nested_value(dict[key], keys)


def get_nested_value(dict, property_string):
    """Allows you to get a value from a nested dictionary
    Example: nested_dict(nested, "one.two.three") would equate to nested['one']['two']['three']
    Returns None if any values in the tree do not exist
    """

    try:
        dict_keys = property_string.split(".")
        return get_nested_value(dict, dict_keys)
    except:
        return None
