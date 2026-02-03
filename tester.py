from FracturedJSON import Encoder
import json

long_list = [f"thing_{i}" for i in range(20)]
data = dict(abcd = "abcd", long_list = long_list)

print(json.dumps(data, cls=Encoder))