#!/usr/bin/python
# -*-coding:utf-8 -*
from __future__ import print_function
import sys
import argparse
from collections import defaultdict
reload(sys)
sys.setdefaultencoding('utf8')


parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('-k', type=int, help='run the k-gram algorithm', default=2)
args = parser.parse_args()

K = args.k
dic = defaultdict(dict)

for line in sys.stdin:
    if not line.startswith('<content>'):
        continue
    
    line = line.strip().lstrip("<content>").rstrip("</content>").strip()
    line = line.replace("\t", " ")
    line = line.decode('utf-8', 'ignore')

    if len(line) > 0:
        for i in range(len(line) - K - 1):
            if line[i+K] not in dic[line[i:i+K]]:
                dic[line[i:i+K]][line[i+K]] = 1
            else:
                dic[line[i:i+K]][line[i+K]] += 1

    mem = float(sys.getsizeof(dic)) / 1024 / 1024 / 1024
    if mem > 0.02:
        for k, v in dic.items():
            print(k, end="")
            for _k, _v in v.items():
                print("\t%s\t%d" % (_k, _v), end="")
            print("")
        dic.clear()




