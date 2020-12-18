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
parser.add_argument('--input', type=str, help='input for prediction', default='上下')
args = parser.parse_args()

K = args.k
input_txt = args.input.decode('utf-8', 'ignore')
dic = defaultdict(int)

for line in sys.stdin:
    if not line.startswith('<content>'):
        continue
    
    line = line.strip().lstrip("<content>").rstrip("</content>").strip()
    line = line.replace("\t", " ")
    line = line.decode('utf-8', 'ignore')

    if len(line) > 0:
        for i in range(len(line) - K):
            if line[i:i+K] == input_txt[:K]:
                if K > 0:
                    dic[line[i:i+K]] += 1
                    #print("%s\t%d" % (line[i:i+K], 1))
                dic[line[i:i+K+1]] += 1
                #print("%s\t%d" % (line[i:i+K+1], 1))

for k, v in dic.items():
    print("%s\t%d" % (k, v))

