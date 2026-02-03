# pyFracturedJSON

Adds [FracturedJSON](https://github.com/j-brooke/FracturedJson) support to python,
allowing you to create JSON that is both compact and readable.

Using it is easy:

```python
import json
from FracturedJSON import Encoder

long_list = [f"thing_{i}" for i in range(20)]
data = {"abcd": "abcd", "long_list": long_list}

print(json.dumps(data, cls=Encoder))
print(json.dumps(data, cls=Encoder, line_length=50))
print(json.dumps(data, cls=Encoder, indent=2))
```
