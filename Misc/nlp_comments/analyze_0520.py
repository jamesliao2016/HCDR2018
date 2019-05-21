#!/usr/bin/env python2
# coding:utf-8
import jieba

import os



# txt = open(os.getcwd() + "复仇者联盟4短评_好评.txt", "r", encoding='utf-8').read()
txt = open(os.getcwd() + "复仇者联盟4短评_好评.txt", "r", encoding='utf-8').read()

words = jieba.lcut(txt)

counts = {}



for word in words:

    if len(word) == 1:

        continue

    else:

        counts[word] = counts.get(word, 0) + 1



items = list(counts.items())

items.sort(key=lambda x: x[1], reverse=True)



for i in range(0, 10):

    word, count = items[i]

    print("{0:<6}{1:>6}".format(word, count))