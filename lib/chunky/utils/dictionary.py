#!/usr/bin/env python
# -*- coding: utf-8 -*-


def get_filepaths_and_urls(url_dictionary):
    """Generator function for the write file path and URL passed in a dictionary.  Returns (filepath, URL)"""
    for filepath in url_dictionary.keys():
        yield (filepath, url_dictionary[filepath])


def grouper(dictionary, group_size):
    x = 0
    list_of_dictionaries = []
    dict_size = len(dictionary)
    key_counter = 0
    temp_dict = {}

    for key in dictionary.keys():
        if x < group_size:
            temp_dict[key] = dictionary[key]
            x += 1
            key_counter += 1
            if key_counter == dict_size:
                list_of_dictionaries.append(temp_dict)
        else:
            list_of_dictionaries.append(temp_dict)
            temp_dict = {}
            temp_dict[key] = dictionary[key]
            x = 1
            key_counter += 1
            if key_counter == dict_size:
                list_of_dictionaries.append(temp_dict)

    return list_of_dictionaries

