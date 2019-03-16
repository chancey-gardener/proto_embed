#!/usr/bin/python3

import os.path
from os import listdir as ls
import word_embedder as we

DPATH = '/home/chanceygardener/repos/probed/data'

class TextFileIterator:
    '''Iterate over a buncha dirs full'a text files without storing
    shit-tons in memory; tokenizeing included.'''
    def __init__(self, dirname):
        self.dirname=dirname
        self.embedder=we.WordEmbedder(DPATH)
        self.func = self.embedder.bigrams

    def __iter__(self):
        files = [os.path.join(self.dirname, p) for p in ls(self.dirname)]
        #print(files)
        for f in files:
            with open(f) as tfile:
                yield self.func(tfile.read())
    
                
