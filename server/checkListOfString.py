def check_list_of_string(obj):
    """Method that checks for a list of strings
    """
    # Source:
    # https://stackoverflow.com/questions/18495098/
    # how-to-check-if-an-object-is-a-list-of-strings
    if obj and isinstance(obj, list):
        return all(isinstance(s, str) for s in obj)
    else:
        return False
