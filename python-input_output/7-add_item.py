#!/usr/bin/python3
"""
Module Doc: covert from json
"""
import json
import os
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def add_item(*args):
    """
    adds arguments to a python list
    """
    filename = "add_item.json"
    
     # Initialize data_list
    if not os.path.exists(filename):
        data_list = []
    else:
        # Load the existing data
        data_list = load_from_json_file(filename)

    # Add new items from args to the list
    data_list.extend(args)
      
    # save to file
    save_to_json_file(data_list, filename)
