import json
from pathlib import Path

import pytest

from fracturedjson import Encoder
from tests.common import params, read_file


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