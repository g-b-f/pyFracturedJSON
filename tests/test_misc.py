import inspect
import json
import pytest
import fracturedjson
from typing import Any

@pytest.fixture
def exports() -> tuple[dict[str, Any], dict[str, Any]]:
    json_exports = {k: v for k, v in json.__dict__.items() if not k.startswith("_")}
    frac_exports = {k: v for k, v in fracturedjson.__dict__.items() if not k.startswith("_")}
    return json_exports, frac_exports

@pytest.fixture
def export_keys(exports) -> tuple[set[str], set[str]]:
    json_exports, frac_exports = exports
    return set(json_exports.keys()), set(frac_exports.keys())


def test_wrapper_has_same_exports_as_builtin(export_keys):
    json_exports, frac_exports = export_keys
    assert json_exports.issubset(frac_exports), f"fracturedjson is missing exports: {json_exports - frac_exports}"

def test_wrapper_exports_have_same_signatures_as_builtin(exports):
    json_exports, frac_exports = exports
    for export_name, export in json_exports.items():
        if export_name in {"detect_encoding"}: # it's correct, but not explicit in the source
            continue
        try:
            expected_sig = inspect.signature(export)
        except TypeError:
            continue
        actual_sig = inspect.signature(frac_exports[export_name])
        msg = f"fracturedjson export '{export_name}' has a different signature than the built-in json module\n" \
        f"expected: {expected_sig}\nactual: {actual_sig}\n"
        assert expected_sig == actual_sig, msg

def test_wrapper_exports_have_same_docstrings_as_builtin(exports):
    json_exports, frac_exports = exports
    for export_name, export in json_exports.items():
        if export_name in {"codecs"}:
            continue
        expected_doc = inspect.getdoc(export)
        actual_doc = inspect.getdoc(frac_exports[export_name])
        msg = f"fracturedjson export '{export_name}' has a different docstring than the built-in json module\n" \
        f"expected: {expected_doc}\nactual: {actual_doc}\n"

        if not expected_doc == actual_doc:
            actual_doc = str(actual_doc).replace("FracturedJSON.Encoder", "JSONEncoder")
            msg = f"fracturedjson export '{export_name}' has a different docstring than the built-in json module"
        assert expected_doc == actual_doc, msg
