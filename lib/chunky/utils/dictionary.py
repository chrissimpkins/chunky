#!/usr/bin/env python
# -*- coding: utf-8 -*-


def get_filepaths_and_urls(url_dictionary):
    """Generator function for the write file path and URL passed in a dictionary.  Returns (filepath, URL)"""
    for filepath in url_dictionary.keys():
        yield (filepath, url_dictionary[filepath])
