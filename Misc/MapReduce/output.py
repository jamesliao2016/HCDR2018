#!/usr/bin/env python

from operator import itemgetter
import sys

current_word = None
current_count = 0
word = None

# input comes from STDIN
for line in sys.stdin:
    # print(line)
    # print('****')
    word,count = line.split('\t',1)
    # if current_word
    # print(word,count)
    # print(line.split('\t',1))
    # print(line.split('\t',1))
    print(word)