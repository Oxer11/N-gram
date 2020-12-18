#!/usr/bin/python
# -*-coding:utf-8 -*
from __future__ import print_function
import sys
import argparse
reload(sys)
sys.setdefaultencoding('utf8')


total = 0
dic = {}

for line in sys.stdin:
    line = line.strip().decode('utf-8', 'ignore')

    word, count = line.split('\t')
    count = int(count)

    if word not in dic:
        dic[word] = 0
    dic[word] += count

for k, v in dic.items():
    print("%s\t%d" % (k, v))