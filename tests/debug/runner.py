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

# test_dict = {'enwik1': 'https://github.com/bit-store/testfiles/releases/download/bigfiles/enwik8_1MB',
#              'enwik2': 'https://github.com/bit-store/testfiles/releases/download/bigfiles/enwik8_2MB',
#              'enwik5': 'https://github.com/bit-store/testfiles/releases/download/bigfiles/enwik8_5MB',
#              'enwik10': 'https://github.com/bit-store/testfiles/releases/download/bigfiles/enwik8_10MB',
# }

start = time.time()
# rl = chunky.get(test_dict, asynchronous=True)
rl = chunky.get(test_dict, number_processes=10)
end = time.time()
print(rl)
print ("Execution Time: " + str(end-start))


