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
#  Asynchronous, concurrent, chunked HTTP requests for files
#  Copyright 2015 Christopher Simpkins
#  MIT license
#
# ------------------------------------------------------------------------------

# TODO: allow calling code to set headers
# TODO: add option to return hash digest of the downloaded file

import itertools
from multiprocessing import Pool

from chunky.utils.dictionary import get_filepaths_and_urls, grouper
from chunky.utils.processes import number_of_cpu
from chunky.utils.pull import get_text, get_text_async, get_binary, get_binary_async


def get(url_dict, response_data="text", chunk_size=10240, asynchronous=True, concurrent_requests=100,
        number_processes=None):
    """Multi-process GET requests for file data and local file writes"""
    # set the number of CPU if not defined by calling code (default to 4 if cannot determine)
    if number_processes is None:
        number_processes = number_of_cpu()

    # confirm that we are not going to generate more processes than existing requests, if so revise spawned process no.
    url_dict_length = len(url_dict)
    if url_dict_length < number_processes:
        number_processes = url_dict_length

    # determine number of URL to assign to each process
    chunk_number = int(round(len(url_dict) / number_processes))
    list_of_dicts = grouper(url_dict, chunk_number)

    # create the request worker process pool
    pool = Pool(number_processes)

    # start the request workers
    list_of_response_lists = pool.map(_get_star,
                                      itertools.izip(list_of_dicts,
                                                     itertools.repeat(response_data),
                                                     itertools.repeat(chunk_size),
                                                     itertools.repeat(asynchronous),
                                                     itertools.repeat(concurrent_requests)))

    response_list = [response for sublist in list_of_response_lists for response in sublist]  # flatten the LoL

    return response_list


def _get_star(params):
    """Converts list of parameters to tuple of parameters for execution of the chunky.getsp() function.  Called from
       chunky.get().  [PRIVATE]"""
    return getsp(*params)


def getsp(url_dict, response_data, chunk_size, asynchronous, concurrent_requests):
    """Single process GET request for file data and local file write"""
    if response_data.lower() == "text":
        if asynchronous:
            response_futures = get_text_async(url_dict, chunk_size, concurrent_requests)
            response_list = []
            for r in response_futures:
                response_list.append(r.value)  # add the requests response object to a list
            return response_list  # return the requests response objects to caller
        else:
            response_list = []
            for filepath, url in get_filepaths_and_urls(url_dict):
                the_response = get_text(url, filepath, chunk_size)
                response_list.append(the_response)
            return response_list
    elif response_data.lower() == "binary":
        if asynchronous:
            response_futures = get_binary_async(url_dict, chunk_size, concurrent_requests)
            response_list = []
            for r in response_futures:
                response_list.append(r.value)  # add the requests response object to a list
            return response_list  # return the requests response objects to caller
        else:
            response_list = []
            for filepath, url in get_filepaths_and_urls(url_dict):
                the_response = get_binary(url, filepath, chunk_size)
                response_list.append(the_response)
            return response_list


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


