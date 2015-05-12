#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os


def confirm_dir_exists(filepath):
    """Checks a file write path for an existing directory path to the file, creates new directory if it does not
    exist.  Raises OSError for failures."""
    dir_path = os.path.dirname(filepath)

    # if it is the current working directory, do nothing
    if dir_path == '':
        return True

    # else, check for path and create it if necessary
    if os.path.exists(dir_path):
        if os.path.isdir(dir_path):
            return True
        else:
            raise OSError("The requested directory path '" + dir_path + "' is an existing file.")
    else:
        os.mkdir(dir_path)
        if os.path.isdir(dir_path):
            return True
        else:
            raise OSError("Unable to create the directory path '" + dir_path + "'")



