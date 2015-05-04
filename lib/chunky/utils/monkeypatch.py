#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gevent import monkey


def monkeypatch_runner():
    # monkey patch for greenlet support
    # monkey.patch_all() - raising key error in Py 2.7.9
    monkey.patch_socket()
    monkey.patch_dns()
    monkey.patch_ssl()
    monkey.patch_os()
