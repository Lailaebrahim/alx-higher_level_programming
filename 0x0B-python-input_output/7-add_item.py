#!/usr/bin/python3
"""

"""
import sys

if __name__ == "__main__":
    load_from_json_file = \
        (__import__('6-load_from_json_file').load_from_json_file)
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
i = 0
new_data = []
try:
    old_data = load_from_json_file("add_item.json")
except FileNotFoundError:
    old_data = []
for arg in sys.argv:
    if i == 0:
        continue
    else:
        new_data[i] = arg
        i += 1
data = old_data.extend(new_data)
save_to_json_file(data, "add_item.json")
