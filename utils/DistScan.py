#!/usr/bin/python3

import os.path
from os import listdir as ls
import word_embedder as we

DPATH = '/home/chanceygardener/repos/probed/data'

class TextFileIterator:
    '''Iterate over a buncha dirs full'a text files without storing
    shit-tons in memory; tokenizeing included.'''
    def __init__(self, dirname, func='tokenize', fparams=None):
        self.dirname=dirname
        self.func=func
        self.embedder=we.WordEmbedder(DPATH)
        # pass any kwargs to embedder method
        if fparams is not None:
            fn = getattr(self.embedder, func)
            self.func = lambda txt: fn(txt, **fparams)
        else:
            self.func = getattr(self.embedder, func)

    def __iter__(self):
        files = [os.path.join(self.dirname, p) for p in ls(self.dirname)]
        #print(files)
        for f in files:
            with open(f) as tfile:
                yield self.func(tfile.read())
    
                
