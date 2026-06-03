"""Internal. Wraps a rust file, that reformats a json string to FracturedJSON"""

def reformat_string(
        input_string: str,
        *,
        indent:int,
        line_length:int,
        max_inline_complexity:int,
        max_compact_array_complexity:int,
        max_table_row_complexity:int,
        number_list_alignment:str
        ) -> str:
    """Reformat a JSON string.
    
    Args:
        input: A JSON string to reformat.
        
    Returns:
        The reformatted JSON string.        
    """
    ...
