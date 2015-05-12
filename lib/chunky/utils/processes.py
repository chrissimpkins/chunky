#!/usr/bin/env python
# -*- coding: utf-8 -*-

from multiprocessing import cpu_count


def number_of_cpu():
    """Returns the number of CPU or 4 if check not implemented by the system"""
    try:
        return cpu_count()
    except NotImplementedError:
        return 4