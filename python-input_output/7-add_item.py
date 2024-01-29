#!/usr/bin/python3
"""
Module Doc: covert from json
"""
import sys
import os
import json
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def add_item(*args):
    """
    adds arguments to a python list
    """
    filename = "add_item.json"
    #print(os.getcwd())
    # Initialize data_list
    if not os.path.exists(filename):
        data_list = []
    else:
        # Load the existing data
        data_list = load_from_json_file(filename)

    # Add new items from args to the list
    # print("Before extending:", data_list)
    
    # Add new items from command line arguments to the list 
    # (excluding the script name)
    data_list.extend(sys.argv[1:])
    # print("After extending:", data_list)
  
    # save to file
    save_to_json_file(data_list, filename)
    
# Execute the function only when the script is run directly
if __name__ == "__main__":
    add_item()
