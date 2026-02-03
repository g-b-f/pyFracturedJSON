import json

class FracturedJson(json.encoder.JSONEncoder):
    def iterencode(self, o, _one_shot=False):
        encoded = super().iterencode(o, _one_shot)
        print("encoded: ", encoded)
        return encoded