import os
import json

file_path = os.path.join(os.path.dirname(__file__), "../data.json")

uni_names = set()
duplicate_uni_names = set()

with open(file_path) as json_file:
    unis = json.load(json_file)
    for uni in unis:
        uni_name = uni["uniName"]
        if uni_name in uni_names:
            duplicate_uni_names.add(uni_name)
        else:
            uni_names.add(uni_name)

if len(duplicate_uni_names) > 0:
    print("Duplicate university names:", duplicate_uni_names)
    exit(1)
