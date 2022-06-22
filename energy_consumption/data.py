import csv, json


def read_json_data(json_file):
    with open(json_file, 'r') as myfile:
        data = myfile.read()
    dataset = json.loads(data)
    return dataset
