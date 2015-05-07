#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gevent
from gevent.lock import Semaphore
import requests

from chunky.utils.dictionary import get_filepaths_and_urls
from chunky.utils.monkeypatch import monkeypatch_runner

# -------------------------------------
# GET request functions
# -------------------------------------

# Text files

def get_text(url, outfile_path, chunk_size):
    """Pulls text files in parameter defined chunk sizes using requests library default encoding format,
        then writes the file locally to parameter defined file path."""
    try:
        r = requests.get(url, stream=True, timeout=5)
        if r.status_code == requests.codes.ok:
            with open(outfile_path, 'w') as f:
                for chunk in r.iter_content(chunk_size=chunk_size):  # pull in chunks & write out (default = 10kb)
                    if chunk:  # filter out keep-alive new chunks
                        f.write(chunk)
                        f.flush()
            # modify requests library response object with new data
            r.chunky_write_path = outfile_path
            r.chunky_url = url
            r.chunky_write_success = True
            r.chunky_error_message = None
            return r   # return requests library response object
        else:
            # modify requests library response object with new data
            r.chunky_write_path = outfile_path
            r.chunky_url = url
            r.chunky_write_success = False
            r.chunky_error_message = "GET request error.  Status code " + str(r.status_code)
            return r   # return requests library response object
    except Exception as e:
        raise e


def get_text_async(url_dict, chunk_size, concurrent_requests):
    """Asynchronous GET requests for text files"""
    monkeypatch_runner()
    semaphore = Semaphore(concurrent_requests)
    the_request_threads = []
    for filepath, url in get_filepaths_and_urls(url_dict):
        request_thread = gevent.spawn(_get_text_async_thread_builder, url, filepath, chunk_size, semaphore)
        the_request_threads.append(request_thread)

    for the_response in gevent.iwait(the_request_threads):
        yield the_response


def _get_text_async_thread_builder(url, filepath, chunk_size, semaphore):
    """Execute the get_text() function with a semaphore that limits the number of concurrent threaded requests.
       Called from get_text_async()"""
    with semaphore:
        return get_text(url, filepath, chunk_size)


# Binary files

def get_binary(url, outfile_path, chunk_size):
    """Pulls binary files in parameter defined chunk sizes using requests library,
        then writes the file locally to parameter defined file path"""
    try:
        r = requests.get(url, stream=True, timeout=5)
        if r.status_code == requests.codes.ok:
            with open(outfile_path, 'wb') as f:
                for chunk in r.iter_content(chunk_size=chunk_size):  # pull in chunks & write out (default = 10kb)
                    if chunk:  # filter out keep-alive new chunks
                        f.write(chunk)
                        f.flush()
            # modify requests library response object with new data
            r.chunky_write_path = outfile_path
            r.chunky_url = url
            r.chunky_write_success = True
            r.chunky_error_message = None
            return r   # return requests library response object
        else:
            # modify requests library response object with new data
            r.chunky_write_path = outfile_path
            r.chunky_url = url
            r.chunky_write_success = False
            r.chunky_error_message = "GET request error.  Status code " + str(r.status_code)
            return r   # return requests library response object
    except Exception as e:
        raise e


def get_binary_async(url_dict, chunk_size, concurrent_requests):
    """Asynchronous requests for binary files"""
    monkeypatch_runner()
    semaphore = Semaphore(concurrent_requests)
    the_request_threads = []
    for filepath, url in get_filepaths_and_urls(url_dict):
        request_thread = gevent.spawn(_get_binary_async_thread_builder, url, filepath, chunk_size, semaphore)
        the_request_threads.append(request_thread)

    for the_response in gevent.iwait(the_request_threads):
        yield the_response


def _get_binary_async_thread_builder(url, filepath, chunk_size, semaphore):
    """Execute the get_binary() function with a semaphore that limits the number of concurrent threaded requests.
       Called from get_binary_async()"""
    with semaphore:
        return get_binary(url, filepath, chunk_size)


# ------------------------------------
# POST request functions
# ------------------------------------


def post_text(url, outfile_path):
    pass


def post_text_async(url, outfile_path, semaphore):
    pass


def post_binary(url, outfile_path):
    pass


def post_binary_async(url, outfile_path, semaphore):
    with semaphore:
        pass
