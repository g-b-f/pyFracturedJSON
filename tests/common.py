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

default_settings = "default_settings.json"
_params: list[paramType] = [
    (default_settings, {}),

    ("line_len_100.json", {"line_length":100}),
    ("line_len_40.json", {"line_length":40}),

    ("indent_2.json", {"indent":2}),
    ("indent_3.json", {"indent":3}),

    ("inline_complexity_-1.json", {"max_inline_complexity":-1}),
    ("inline_complexity_0.json", {"max_inline_complexity":0}),
    ("inline_complexity_1.json", {"max_inline_complexity":1}),

    ("compact_array_complexity_-1.json", {"max_compact_array_complexity":-1}),
    ("compact_array_complexity_0.json", {"max_compact_array_complexity":0}),
    ("compact_array_complexity_1.json", {"max_compact_array_complexity":1}),

    ("table_row_complexity_-1.json", {"max_table_row_complexity":-1}),
    ("table_row_complexity_0.json", {"max_table_row_complexity":0}),
    ("table_row_complexity_1.json", {"max_table_row_complexity":1}),

    ("number_list_alignment_left.json", {"number_list_alignment":"left"}),
    ("number_list_alignment_decimal.json", {"number_list_alignment":"decimal"}),
    ("number_list_alignment_right.json", {"number_list_alignment":"right"}),
    ("number_list_alignment_normalize.json", {"number_list_alignment":"normalize"}),
]

JSONS_DIR = "JSONs/"
params = [(JSONS_DIR+f, kw) for f, kw in _params]

def generate_jsons():
    """Running this function will render the tests useless if you're not careful!
    Check that the results are as expected!
    """
    file_str, file_dict = read_file(JSONS_DIR + default_settings)
    for filename, kwargs in params:
        file = "tests/" + filename
        with open(file, "w") as f:
            json.dump(file_dict, f, cls=Encoder, **kwargs) #type: ignore[arg-type]

if __name__ == "__main__":
    generate_jsons()