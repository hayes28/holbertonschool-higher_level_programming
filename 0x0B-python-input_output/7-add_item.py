#!/usr/bin/python3
""" adds all arguments to a Python list,
and then save them to a file: """


import sys

save_json = __import__("5-save_to_json_file").save_to_json_file
load_json = __import__("6-load_from_json_file").load_from_json_file

filename = "add_item.json"

try:
    json_list = load_json(filename)

except(TypeError, FileNotFoundError):
    json_list = []

json_list.extend(iter(sys.argv[1:]))
save_json(json_list, filename)
