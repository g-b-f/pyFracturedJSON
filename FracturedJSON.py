import fractured_json_rust_wrapper
import json
from typing import Callable


class Encoder(json.encoder.JSONEncoder):
    def __init__(
            self,
            *,
            skipkeys: bool = False,
            ensure_ascii: bool = True,
            check_circular: bool = True,
            allow_nan: bool = True,
            sort_keys: bool = False,
            indent = 4,
            separators: tuple[str, str] | None = None,
            default: Callable | None = None,
            **kwargs
        ):
        super().__init__(
            skipkeys=skipkeys,
            ensure_ascii=ensure_ascii,
            check_circular=check_circular,
            allow_nan=allow_nan,
            sort_keys=sort_keys,
            indent=indent,
            separators=separators,
            default=default
            )
        
        if indent is None:
            indent = 4
        self._indent = indent
        self.line_length = kwargs.get("line_length", 120)
        
    
    def encode(self, o) -> str:
        unformatted = json.dumps(o)
        formatted = fractured_json_rust_wrapper.reformat_string(
            unformatted,
            indent=self._indent,
            line_length=self.line_length
        )
        return formatted
