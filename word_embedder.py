#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
from abc import ABC
from os import chdir as cd, getcwd as pwd, listdir as ls
import sys, json
from collections import Counter
from sklearn.manifold import TSNE
from multiprocessing import pool
import numpy as np
rroot=pwd()

PUNCT = '.,;:?!'
APOST = "'"


def shannon_entropy(vec):
    n_nodes = len(vec)
    if n_nodes <= 1:
        return 0
    else:
        counts = np.bincount(vec)
        nzeros = counts[np.nonzero(counts)] / n_nodes
        n_nonzero = len(nzeros)
        if n_nonzero <= 1:
            return 0
        else:
            return - np.sum(nzeros*np.log(np.nzeros))/np.log(n_nonzero)


def ev2norm(vec):
        '''return the square root of the sum of squares of a list'''
        return np.sqrt(sum(s**2 for s in vec))

def matrix_mean(mat):
        out = []
        rowlength = len(mat[0])
        for i in range(rowlength):
                mean = sum(row[i] for row in mat)/rowlength
                out.append(mean)
        return out
                
def vector_mean(vec):
        '''compute mean value of vector'''
        return sum(vec)/len(vec)
# REMINDER: computing len(vec twice in variance may cause a bottleneck.
def variance(v):
        mean = vector_mean(v)
        return  sum((i-mean)**2 for i in v)/len(v)
        
# below starts the word embedder class ##############

#############DIMENSIONALITY REDUCTION FUNCTIONS:

def tsne(dist):
    exper = lambda vec: np.e** ((0-np.linalg.norm(xiv-vec)**2)/tsig)
    outmat = []
    for k in dist:
        dvec = dist[k]
        diffscore = exper(dvec)
        denexp += diffscore
           # print(diffscore)
        count += 1
        prop = round((count/span)*100, 2)
        if prop%1 == 0:
            print('{}% complete'.format(prop))
            print('{}/{}'.format(numexp,denexp))

def tsne(xiv, xjv, dist, sig_squared_i=1/np.sqrt(2)):
        '''where xi and xj are word keys pointing to vector values in dist.
            NOTE: sig_squred_i is set to constant for now, fix when
            a better strategy can be decided on'''
        tsig = sig_squared_i * 2
            ####################
            # NOTE: Ok, so the main
            # problem here is that 
            # tsig (the variance of 
            # the p value being conditioned
            # on (pretty much any vector
            # from this set)) is turning
            # out to be so close to 0
            # that dividing by it produces
            # a massive number, taking 
            # its negative and exp-ing it
            # produces a value too close to 0
            # for python to handle (is there a double type?
            ##############################################
            # get numerator of expression for p(j|i)
        
        numexp = exper(xjv)
        print("numexp: {}".format(numexp))
        print("tsig: {}".format(tsig))
        # well now? we're gonna compute a motherfuckin denominator
        denexp = 0
     # TODO: the values computed in this for loop have got to be stored
    #   warp = pool(4)
    #   noti = (dist[k] for k in dist if dist[k] != xi)
        print('Computing covariance matrix...')
        #denexp = sum(warp.map(exper, noti))
        denexp = 0
        count = 0 # just to show us how
        span = len(dist)
        
        pji = numexp/denexp
        return pji


dimred = {
    
        'TSNE': TSNE
}


class WordEmbedder:

    '''feed me raw text via the tokenize method,
    '''
    def __init__(self, datpath):
        self.models={}
        self._lexicon = set()
        self._lexicon_size = len(self._lexicon)
        self.data = {}
        self.dataPath = datpath
    
    def __getitem__(self, key):
        return self.models[key]

    def updateLexicon(self, newvoc):
        '''newvoc should be a set'''
        if not isinstance(newvoc, set):
            raise TypeError("New vocabulary param should be represented by set")
        else:
            self._lexicon.union(newvoc)
            self._lexicon_size = len(self._lexicon)

    def getLexiconSize(self):
        return self._lexicon_size

    def getLexicon(self):
        return self._lexicon
    def readFile(self, fpath):
	    # fpath should be relative to DATAPATH
	    fullpath = self.dataPath+'/'+fpath
	    with open(fullpath) as dfile:
	        out = self.tokenize(dfile.read())
	    return out
    
    def unPackJson(self, fpath, rpath=None):
        if rpath is not None:
            rpath = rpath + '/' if not rpath[-1] == '/' else rpath
            full_path = rpath + fpath
        else:
            full_path = self.dataPath+'/'+fpath
        with open(full_path) as cdat:
            dat = json.loads(cdat.read())
        for wkey in dat:
            wval = dat[wkey]
            buff = {}
            for nz in wval: # nz refers to nonzero
                if nz.isnumeric(): #  index
                    buff[int(nz)] = np.float64(wval[nz])
                else:
                    buff[nz] = wval[nz]
                    #dat[w] = buff
            dat[wkey] = buff
        return dat
    
    def rawEnvsToJson(self, envs, ftag):
        cmpd = self.vCompressAll(envs)
        fname = "{}.json".format(ftag)
        with open(self.dataPath+'/'+fname, 'w') as jfile:
            jfile.write(json.dumps(cmpd))
        
        

    def tokenize(self, text):
        out = []
        idx = 0
        print('\ntokenizing...\n')
        while idx < len(text):
            try:
                wordbuff = ''
                char = text[idx]
                # check id of character and do stuff accordingly
                while char.isspace():
                        idx += 1
                        char = text[idx]
                while char.isalnum():
                        wordbuff += char
                        idx += 1
                        char = text[idx]
                # this allows us to descend to the correct blocks when necessary
                if wordbuff != '':
                        idx += 1
                        out.append(wordbuff)
                        continue
                if char == APOST:
                        # the conditional below allows the tokenizer to 
                        # group "n't" as a token, rather than 't
                        # TODO make this generalize a bit more
                        if text[idx-1].lower() == 'n':
                                wordbuff = 'n' + wordbuff
                                # put the word sans "n't" in there
                        wordbuff += char # add the apostrophe to wordbuff
                        # increment to post-apostrophe stuff
                        idx += 1
                        char = text[idx]
                        while char.isalnum():
                                wordbuff += char
                                idx += 1
                                char = text[idx]
                if wordbuff == '':
                        while char in PUNCT:
                                wordbuff += char
                                idx += 1
                                char = text[idx]
                        idx += 1
                        continue
                # fallback increment
                idx +=1
                out.append(wordbuff)
            except IndexError:
                out.append(wordbuff)
                break
        # update lexicon
        out = [i.lower().strip() for i in out]
        self.updateLexicon(set(out))
        return out

    def unpack(self, fpath):
        with open(fpath) as f:
            dat = fpath.read()
            dat = json.loads.read()
        dat = dict(map(self.vDecompress, dat))
        dat = {k:np.array(list(map(np.float64, w2vs[k]))) for k in dat}
        

    def getEnvsFromTokens(self, toks, n):
        '''Compute word embeddings given a tokenized text
        returns hash table mapping unique words in
        text to word embeddings computed from
        that text'''
        out = {word:[] for word in set(toks)}
        schema = sorted(out.keys())
        dims = len(schema)
        tlim = len(toks)
        for idx in range(tlim):
                word = toks[idx]
                envec = np.zeros(dims)
                neighborhood =  range(idx-n, idx+n)
                for i in neighborhood:
                        if 0 <= i < tlim:
                                neighbor = toks[i]
                                schema_idx = schema.index(neighbor)
                                envec[schema_idx] += 1
                # append
                out[word].append(envec)
                if idx % 1000 == 0:
                        print('environments computed for {} tokens\n'.format(idx))
        # now flatten le matrices
        print('compiling recorded environments...')
        # len(out[k] == tlim  : always? confirm and quit
        # computing that shit every time
        out = {k:sum(out[k])/len(out[k]) for k in out}
        return out
    

    def newModel(self, nbrhd, dredstrat,  mkey=None):
        if mkey is None:
                dat_param = '-'.join(dselect) if dselect is not None else 'custom-text'
                mkey = "{}_window_{}_data_{}".format(dredstrat, nbrhd, dat_param)
        self.models[mkey] = Model(nbrhd, self, 
                                 dimensionality_reduction_mode=dredstrat)
        
    def getModelData(self, dselect):
        dfiles = ls(self.dataPath)
        for datafield in dselect:
            # get all datafiles containing tag in select criteria
            hasfield = [fname for fname in dfiles
                             if datafield in fname]
        # now get the stored preprocessed data from the selected files
        all_dat = {}
        for fname in hasfield:
            with open(fname) as dfile:
                fdat = json.loads(dfile.read())
                all_dat[fname] = fdat
        return all_dat        
        
    def vCompress(self, emb):
        '''Compress sparse vector to hash table w/idx for keys and nonzero values as table values '''
        i = 0
        max_ind = len(emb)
        out = {}
        while i < max_ind:
                val = emb[i]
                if val != 0:
                        out[i] = val
                i += 1
        # add max length to compressed value to reconstruct
        out['MAX'] = max_ind
        return out
    
    def vCompressAll(self, embs):
        return {wkey: self.vCompress(embs[wkey]) 
                    for wkey in embs}

    def vDecompress(self, tab):
        # build list of length
        out = [0]*tab['MAX'] 
        del tab['MAX']
        for key in tab:
                out[key] += tab[key]
        return out              


class Model:

    def __init__(self, window, embedder, dimensionality_reduction_mode='TSNE'):
            
            self.window = window
            self.data = []
            self._dimredmode = dimred[dimensionality_reduction_mode]
            self._embeddings = []



    def __getitem__(self, key):
        if isinstance(key, str):
            return self.data[key]
        else:
            raise ValueError('Model lookup is by word.')

    def reduceDimensionality(self, kwargs):
        self._dimredmode(**kwargs) 

    
        

        
        
