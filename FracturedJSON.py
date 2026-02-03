import fractured_json_rust_wrapper
import json


class Encoder(json.encoder.JSONEncoder):
    def encode(self, o) -> str:
        unformatted = json.dumps(o)
        formatted = fractured_json_rust_wrapper.reformat_string(unformatted)
        return formatted
