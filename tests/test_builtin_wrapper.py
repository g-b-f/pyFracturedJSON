import json as builtin_json
from pathlib import Path

import pytest

import FracturedJSON as json

params = [
    ("default_settings.json", {}),
    ("line_len_100.json", {"line_length":100}),
    ("indent_2.json", {"indent":2}),
]

def read_file(filename) -> tuple[str, dict]:
    file = Path(__file__).parent / filename
    file_contents = file.read_text()
    return (file_contents, builtin_json.loads(file_contents))

@pytest.mark.parametrize(("filename", "kwargs"), params)
def test_dumps(filename:str, kwargs:dict):
    file_str, file_dict = read_file(filename)
    formatted = json.dumps(file_dict, **kwargs)
    assert formatted == file_str

@pytest.mark.parametrize(("filename", "kwargs"), params)
def test_dump(filename:str, kwargs:dict, tmp_path:Path):
    file_str, file_dict = read_file(filename)
    file = tmp_path / "test.json"
    with open(file, "w") as f:
        json.dump(file_dict, f, **kwargs)
    assert file.read_text() == file_str

@pytest.mark.parametrize(("filename", "kwargs"), params)
def test_load(filename:str, kwargs:dict, tmp_path:Path):
    file_str, file_dict = read_file(filename)
    with open(Path(__file__).parent / filename) as f:
        data = json.load(f)
    assert file_dict == data

@pytest.mark.parametrize(("filename", "kwargs"), params)
def test_loads(filename:str, kwargs:dict, tmp_path:Path):
    file_str, file_dict = read_file(filename)
    data = json.loads(file_str)
    assert file_dict == data