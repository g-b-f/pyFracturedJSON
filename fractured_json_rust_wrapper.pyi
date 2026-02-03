"""Internal. Wraps a rust file, that reformats a json string to FracturedJSON"""

def reformat_string(input_string: str, *, indent:int, line_length:int) -> str:
    """Reformat a JSON string.
    
    Args:
        input: A JSON string to reformat.
        
    Returns:
        The reformatted JSON string.        
    """
    ...
