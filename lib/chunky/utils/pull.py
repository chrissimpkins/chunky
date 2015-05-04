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


def requests_get_text(url, outfile_path, chunk_size):
    """Pulls text files in parameter defined chunk sizes using requests library default encoding format,
        then writes the file locally to parameter defined file path"""
    try:
        r = requests.get(url, stream=True)
        if r.status_code == requests.codes.ok:
            with open(outfile_path, 'w') as f:
                for chunk in r.iter_content(chunk_size=chunk_size):  # pull in chunks & write out (default = 10kb)
                    if chunk:  # filter out keep-alive new chunks
                        f.write(chunk)
                        f.flush()
        elif r.status_code == 404:
            pass
        else:
            pass
    except Exception as e:
        raise e


def requests_get_text_async_runner(url_dict, chunk_size, concurrent_requests):
    monkeypatch_runner()
    semaphore = Semaphore(concurrent_requests)
    the_request_threads = []
    for filepath, url in get_filepaths_and_urls(url_dict):
        request_thread = gevent.spawn(requests_get_text_async_thread_builder, url, filepath, chunk_size, semaphore)
        the_request_threads.append(request_thread)

    for the_response in gevent.iwait(the_request_threads):
        yield the_response


def requests_get_text_async_thread_builder(url, filepath, chunk_size, semaphore):
    with semaphore:
        return requests_get_text(url, filepath, chunk_size)


def requests_get_binary(url, outfile_path, chunk_size):
    """Pulls binary files in parameter defined chunk sizes using requests library,
        then writes the file locally to parameter defined file path"""
    try:
        r = requests.get(url, stream=True)
        if r.status_code == requests.codes.ok:
            with open(outfile_path, 'wb') as f:
                for chunk in r.iter_content(chunk_size=chunk_size):  # pull in chunks & write out (default = 10kb)
                    if chunk:  # filter out keep-alive new chunks
                        f.write(chunk)
                        f.flush()
        elif r.status_code == 404:
            pass
        else:
            pass
    except Exception as e:
        raise e


def requests_get_binary_async(url, outfile_path, chunk_size, concurrent_requests, semaphore):
    pass


# ------------------------------------
# POST request functions
# ------------------------------------


def requests_post_text(url, outfile_path):
    pass


def requests_post_text_async(url, outfile_path, semaphore):
    pass


def requests_post_binary(url, outfile_path):
    pass


def requests_post_binary_async(url, outfile_path, semaphore):
    with semaphore:
        pass
