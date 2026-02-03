"""Internal. Wraps a rust file, that reformats a dict to FracturedJSON"""

def reformat_string(input: str) -> str:
    """Reformat a JSON string.
    
    Args:
        input: A JSON string to reformat.
        
    Returns:
        The reformatted JSON string.
        
    Raises:
        Any exceptions raised by the underlying Rust implementation.
    """
    ...
