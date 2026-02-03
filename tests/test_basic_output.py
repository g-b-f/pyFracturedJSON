import json
from pathlib import Path

import pytest

from FracturedJSON import Encoder

params = [
    ("default_settings.json",{}),
    ("line_len_100.json",{"line_length":100}),
    ("indent_2.json",{"indent":2}),
]

@pytest.mark.parametrize(("filename", "kwargs"), params)
def test_roundtrip(filename:str, kwargs:dict):
    file = Path(__file__).parent / filename
    file_contents = file.read_text()
    data = json.loads(file_contents)
    
    formatted = json.dumps(data, cls=Encoder, **kwargs)
    assert formatted == file_contents

@pytest.mark.parametrize(("filename", "kwargs"), params)
def test_negative_roundtrip(filename:str, kwargs:dict):
    file = Path(__file__).parent / filename
    file_contents = file.read_text()
    data = json.loads(file_contents)
    
    formatted = json.dumps(data)
    assert formatted != file_contents