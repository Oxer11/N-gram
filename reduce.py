#!/usr/bin/python
# -*-coding:utf-8 -*
from __future__ import print_function
import sys
import argparse
reload(sys)
sys.setdefaultencoding('utf8')
from collections import defaultdict


total = 0
dic = defaultdict(dict)
tot = defaultdict(int)

for line in sys.stdin:
    line = line.strip().decode('utf-8', 'ignore')

    kvs = line.split('\t')
    word, words, counts = kvs[0], kvs[1::2], map(int, kvs[2::2])
    tot[word] += sum(counts)
    for w, c in zip(words, counts):
        if w not in dic[word]:
            dic[word][w] = c
        else:
            dic[word][w] += c

    mem = float(sys.getsizeof(dic)) / 1024 / 1024 / 1024
    if mem > 0.02:
        for k in dic.keys():
            print("%s\t%d" % (k, tot[k]), end="")
            for w, c in dic[k].items():
                print("\t%s\t%d" % (w, c), end="")
            print("")
        dic.clear()
        tot.clear()

for k in dic.keys():
    print("%s\t%d" % (k, tot[k]), end="")
    for w, c in dic[k].items():
        print("\t%s\t%d" % (w, c), end="")
    print("")
dic.clear()
tot.clear()