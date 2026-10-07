<div align="center">

# pyFracturedJSON

**Adds [FracturedJSON](https://github.com/j-brooke/FracturedJson) support to python,
letting you create JSON that is both compact and readable.**

<a href="https://pypi.org/project/pyfracturedjson">
<img alt="PyPI Version" src="https://img.shields.io/pypi/v/pyfracturedjson?cacheSeconds=3600">
<img alt="minimum python version" src="https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fpypi.org%2Fpypi%2Fpyfracturedjson%2Fjson&query=%24.info.requires_python&label=requires%20python&cacheSeconds=3600">
</a>
</div>
</br>

You can trivially use it as a drop-in replacement for the built-in `json` module:

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

Or, if you'd prefer:

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

This is largely a wrapper around [fracturedjson-rs](https://github.com/fcoury/fracturedjson-rs),
so credit to the creator.