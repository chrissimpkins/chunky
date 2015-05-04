#!/usr/bin/env python
# -*- coding: utf-8 -*-

import chunky
import time

test_dict = {'google.txt': 'http://google.com',
             'cnn.txt': 'http://www.cnn.com',
             'yahoo.txt': 'http://www.yahoo.com',
             'github.txt': 'https://github.com',
             'python.txt': 'http://www.python.org',
             'reddit.txt': 'http://www.reddit.com',
             'amazon.txt': 'http://www.amazon.com',
             'youtube.txt': 'http://www.youtube.com',
             'wiki.txt': 'http://www.wikipedia.org',
             'twitter.txt': 'https://twitter.com'
             }

start = time.time()
chunky.get(test_dict, asynchronous=False)
end = time.time()
print ("Execution Time: " + str(end-start))

