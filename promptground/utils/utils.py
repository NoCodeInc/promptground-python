def is_flat(data):
    """
    Check if the data object is flat, i.e., it doesn't have any nested lists or subobjects.

    Args:
    data: The data object to check.

    Returns:
    bool: True if the data object is flat, False otherwise.
    """
    def is_nested(value):
        return isinstance(value, (dict, list, tuple, set))

    if isinstance(data, dict):
        items = data.values()
    elif isinstance(data, (list, tuple, set)):
        items = data
    else:
        return True

    for item in items:
        if is_nested(item):
            return False

    return True