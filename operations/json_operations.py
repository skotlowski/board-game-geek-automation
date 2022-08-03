import json


def json_file():
    pass_file = './pass.json'
    with open(pass_file) as json_file:
        data = json.load(json_file)
        return data
