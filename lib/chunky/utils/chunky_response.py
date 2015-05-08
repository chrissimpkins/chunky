#!/usr/bin/env python
# -*- coding: utf-8 -*-


class CResponse(object):
    def __init__(self, chunky_write_path=None, chunky_url=None, chunky_write_success=None, chunky_exception=None,
                 chunky_error_message=None, requests_response=None):
        self.chunky_write_path = chunky_write_path
        self.chunky_url = chunky_url
        self.chunky_write_success = chunky_write_success
        self.chunky_exception = chunky_exception
        self.chunky_error_message = chunky_error_message
        self.response = requests_response

    def __repr__(self):
        if self.chunky_write_success is not None:
            if self.chunky_write_success is True:
                return "<Chunky Response [" + self.chunky_write_path + " = SUCCESS]>"
            elif self.chunky_write_success is False:
                return "<Chunky Response [" + self.chunky_write_path + " = FAIL]>"
        else:
            return "<Chunky Response [NONE]"
