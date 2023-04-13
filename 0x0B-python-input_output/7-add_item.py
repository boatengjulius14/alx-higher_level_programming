#!/usr/bin/python3
"""Adds all arguments to a python list, and then save them to a file"""


if __name__ == "__main__":
    import sys
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = __import__('6-load_from_\
json_file').load_from_json_file

    try:
        _list = load_from_json_file("add_item.json")
    except FileNotFoundError:
        _list = []
    _list.extend(sys.argv[1:])
    save_to_json_file(_list, 'add_item.json')
