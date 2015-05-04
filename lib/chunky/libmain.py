#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ------------------------------------------------------------------------------
#
#   _______  __   __  __   __  __    _  ___   _  __   __
#  |       ||  | |  ||  | |  ||  |  | ||   | | ||  | |  |
#  |       ||  |_|  ||  | |  ||   |_| ||   |_| ||  |_|  |
#  |       ||       ||  |_|  ||       ||      _||       |
#  |      _||       ||       ||  _    ||     |_ |_     _|
#  |     |_ |   _   ||       || | |   ||    _  |  |   |
#  |_______||__| |__||_______||_|  |__||___| |_|  |___|
#
#  Asynchronous chunked HTTP requests for files
#  Copyright 2015 Christopher Simpkins
#  MIT license
#
# ------------------------------------------------------------------------------


from chunky.utils.dictionary import get_filepaths_and_urls
from chunky.utils.pull import requests_get_text, requests_get_text_async_runner, requests_get_binary, requests_get_binary_async

# PUBLIC FUNCTIONS


def get(url_dict, chunk_size=10240, response_data="text", asynchronous=True, concurrent_requests=100):
    if response_data.lower() == "text":
        if asynchronous:
            requests_get_text_async_runner(url_dict, chunk_size, concurrent_requests)
        else:
            for filepath, url in get_filepaths_and_urls(url_dict):
                requests_get_text(url, filepath, chunk_size)
    elif response_data.lower() == "binary":
        if asynchronous:
            pass
        else:
            for filepath, url in get_filepaths_and_urls(url_dict):
                requests_get_binary(url, filepath, chunk_size)


def post(url_dict, chunk_size=10240, response_data="text", asynchronous=True, concurrent_requests=100):
    if response_data.lower() == "text":
        if asynchronous:
            pass
        else:
            pass
    elif response_data.lower() == "binary":
        if asynchronous:
            pass
        else:
            pass


