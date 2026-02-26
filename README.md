# pyFracturedJSON

Adds [FracturedJSON](https://github.com/j-brooke/FracturedJson) support to python,
allowing you to create JSON that is both compact and readable.

Using it is easy:

```python
import json
from fracturedjson import Encoder

long_list = [f"thing_{i}" for i in range(20)]
data = {"abcd": "abcd", "long_list": long_list}

print(json.dumps(data, cls=Encoder))
print(json.dumps(data, cls=Encoder, line_length=50))
print(json.dumps(data, cls=Encoder, indent=2))

with open("file.json", "w") as f:
    json.dump(data, f, cls=Encoder)
```

You can also use it as a drop-in replacement for the built-in `json` module:

```python
import fracturedjson as json

long_list = [f"thing_{i}" for i in range(20)]
data = {"abcd": "abcd", "long_list": long_list}

print(json.dumps(data))
print(json.dumps(data, line_length=50))
print(json.dumps(data, indent=2))

with open("file.json", "w") as f:
    json.dump(data, f)

with open("file.json") as f:
    json.load(f)

json.loads('{"foo":"bar"}')
```

This is mostly a wrapper around [fracturedjson-rs](https://github.com/fcoury/fracturedjson-rs),
so all credit goes to the creator.