from .utils import is_flat

def ensure_object_is_flat(data, name="data"):
    """
    Ensure that the provided object is flat.

    Args:
    data: The data object to check.
    name (str): The name of the data object for error messaging.

    Raises:
    Exception: If the data object is not flat.
    """
    if isinstance(data, str) or not is_flat(data):
        raise Exception(f"`{name}` must be flat.")
    
def ensure_is_string(data, name='data'):
    """
    Ensure that the provided data is a string.

    Args:
    data: The data to check.
    name (str): The name of the data for error messaging.

    Raises:
    TypeError: If the data is not a string.
    """
    if not isinstance(data, str):
        raise TypeError(f"The `{name}` must be a string")