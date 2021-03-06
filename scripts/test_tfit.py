#!/usr/bin/python3
from utils.DistScan import TextFileIterator as ftiter
from os import listdir as ls
from os.path import join
from collections import Counter
import json

path = '/home/chanceygardener/LegalNLP/legal_database/data/online_legal_source/test_II'

tokenize = True
proc = 'getEnvsFromTokens'
params = {
        'pack':True
        }
this = ls(path)
this = [join(path, i) for i in this]
file_count = sum(len(ls(yr)) for yr in this)
dist = Counter()
year_count = len(this)
fc = 0
print('\n\nAnalyzing {} files...\n\n'.format(file_count))
for year in this:
    for f in ftiter(year, func=proc):
        if tokenize:
            try:
                with open('token_dat/bill_{}_{}.json'.format(proc, fc+1), 'w') as dfile:
                    dfile.write(json.dumps(f))
            except TypeError:
                print(f)
                raise ValueError("let's see what's up here.")
        for word in f:
            dist[word] += 1
            #print(dist.keys())

    #print('\n\nEND {} ##\n\n'.format(year))
        fc += 1
    #if fc % 10 == 0:
        perc = fc/file_count
        perc *= 100
        perc = round(perc, 2)
        print('{} % complete\n'.format(perc))


