"""Internal. Wraps a rust file, that reformats a json string to FracturedJSON"""

def reformat_string(input: str, *, indent=4, line_length=120) -> str:
    """Reformat a JSON string.
    
    Args:
        input: A JSON string to reformat.
        
    Returns:
        The reformatted JSON string.        
    """
    ...
