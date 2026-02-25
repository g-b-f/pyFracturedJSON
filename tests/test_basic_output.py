import json
from pathlib import Path

import pytest

from fracturedjson import Encoder

params = [
    ("default_settings.json", {}),
    ("line_len_100.json", {"line_length":100}),
    ("indent_2.json", {"indent":2}),
]

def read_file(filename) -> tuple[str, dict]:
    file = Path(__file__).parent / filename
    file_contents = file.read_text()
    return (file_contents, json.loads(file_contents))

@pytest.mark.parametrize(("filename", "kwargs"), params)
def test_roundtrip(filename:str, kwargs:dict):
    file_str, file_dict = read_file(filename)
    formatted = json.dumps(file_dict, cls=Encoder, **kwargs)
    assert formatted == file_str

@pytest.mark.parametrize(("filename", "kwargs"), params)
def test_negative_roundtrip(filename:str, kwargs:dict):
    file_str, file_dict = read_file(filename)    
    formatted = json.dumps(file_dict)
    assert formatted != file_str

@pytest.mark.parametrize(("filename", "kwargs"), params)
def test_dump(filename:str, kwargs:dict, tmp_path:Path):
    file_str, file_dict = read_file(filename)
    file = tmp_path / "test.json"
    with open(file, "w") as f:
        json.dump(file_dict, f, cls=Encoder, **kwargs)
    assert file.read_text() == file_str