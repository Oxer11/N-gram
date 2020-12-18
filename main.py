#!/usr/bin/python
# -*-coding:utf-8 -*
from __future__ import print_function
import sys
import os
reload(sys)
sys.setdefaultencoding('utf8')

cmd = 'sh ./ngram.sh %d %s'
mv_cmd = 'hadoop fs -text "/user/u17300240035/test/*" > test.txt'


os.system(cmd % (0, 'placeholder'))
os.system(mv_cmd)
word_dict = {}
with open('test.txt', 'r') as f:
    for line in f:
        line = line.strip().decode('utf-8', 'ignore')
        word, count = line.split('\t')
        if len(word) == 1:
            word_dict[word] = int(count)
word_count = len(word_dict)
print('word count: ', word_count)

while True:
    K = input('> K: ')
    input_txt = raw_input('> input: ')

    job = raw_input('> type (predict or inference): ')
    while job not in ['predict', 'inference']:
        job = raw_input('> type (predict or inference): ')

    use_smooth = raw_input('> use smooth (yes or no): ')
    while use_smooth not in ['yes', 'no']:
        use_smooth = raw_input('> use smooth (yes or no): ')
    use_smooth = (use_smooth == 'yes')

    if job == 'predict':
        print('Running Map Reduce Job ...')
        os.system(cmd % (K, input_txt))
        os.system(mv_cmd)
        print('Finish Prediction ...')
        with open('test.txt', 'r') as f:
            gram_dict = {}
            for line in f:
                line = line.strip().decode('utf-8', 'ignore')
                gram, count = line.split('\t')
                gram_dict[gram] = int(count)
        count0 = gram_dict.get(input_txt.decode('utf-8', 'ignore'), 0)
        count1 = gram_dict.get(input_txt[:-3].decode('utf-8', 'ignore'), 0)
        if use_smooth:   
            print('P(%s|%s) = (%d + 1) / (%d + %d) = %.5f' % (input_txt, input_txt[:-3], count0, 
                    count1, word_count, float(count0 + 1) / float(count1 + word_count)))
        else:
            print('P(%s|%s) = %d / %d = %.5f' % (input_txt, input_txt[:-3], count0, 
                    count1, float(count0) / float(count1)))
            
    else:
        os.system(cmd % (K, input_txt))
        os.system(mv_cmd)
        with open('test.txt', 'r') as f:
            gram_dict = {}
            for line in f:
                line = line.strip().decode('utf-8', 'ignore')
                gram, count = line.split('\t')
                gram_dict[gram] = int(count)
        grams = sorted(gram_dict.items(), key=lambda x: (x[1], x[0]), reverse=True)
        cnt = gram_dict.get(input_txt.decode('utf-8', 'ignore'), 0)
        for tup in grams[1:11]:
            if tup[0] == input_txt:
                continue
            if use_smooth:
                print('word: %s\tnum: %d\tprob: %.5f' % (tup[0], tup[1], float(tup[1] + 1) / float(cnt + word_count)))
            else:
                print('word: %s\tnum: %d\tprob: %.5f' % (tup[0], tup[1], float(tup[1]) / float(cnt)))

    

