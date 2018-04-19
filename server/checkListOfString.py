def check_list_of_string(obj):
    """Method that checks for a list of strings

    :param obj: Variable passed into the function to be tested
    :returns: True if obj is a list of strings, False otherwise
    """
    # Source:
    # https://stackoverflow.com/questions/18495098/
    # how-to-check-if-an-object-is-a-list-of-strings
    if len(obj) == 1 and obj[0] == "":
        return False
    elif obj and isinstance(obj, list):
        return all(isinstance(s, str) for s in obj)
    else:
        return False
