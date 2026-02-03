import pyFracturedJSON
import json

long_list = [f"thing_{i}" for i in range(20)]
data = dict(abcd = "abcd", long_list = long_list)
data_str = json.dumps(data)

print(pyFracturedJSON.reformat(data_str))