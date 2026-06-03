import json
from pathlib import Path
import sys

root = Path(__file__).parent.parent
sys.path.append(str(root))

from fracturedjson import Encoder

def read_file(filename:str) -> tuple[str, dict]:
    file = Path(__file__).parent / filename
    file_contents = file.read_text()
    return (file_contents, json.loads(file_contents))

kwargType = dict[str, str | int]
paramType = tuple[str, kwargType]

_params: list[paramType] = [
    ("default_settings.json", {}),
    ("line_len_100.json", {"line_length":100}),
    ("indent_2.json", {"indent":2}),
]

JSONS_DIR = "JSONs/"
params = [(JSONS_DIR+f, kw) for f, kw in _params]

def generate_jsons():
    for filename, kwargs in params:
        file_str, file_dict = read_file(filename)
        file = "tests/" + filename
        with open(file, "w") as f:
            json.dump(file_dict, f, cls=Encoder, **kwargs)

            json.dump(file_dict, f, cls=Encoder)

if __name__ == "__main__":
    generate_jsons()