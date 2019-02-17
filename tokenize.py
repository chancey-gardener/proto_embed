#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
<<<<<<< HEAD
from abc import ABC
from os import chdir as cd, getcwd as pwd
=======
from os import chdir as cd, getcwd as pwd, listdir as ls
>>>>>>> ad27b97ff9cc196d178edd7ac2552597830a90ee
cwd = pwd()
#cd('/usr/lib/python3.6')
import sys, json
from collections import Counter
import numpy as np

#from multiprocessing import pool

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
    
        'TSNE': tsne
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

    def updateLexicon(self, newvoc):
        '''newvoc should be a set'''
        if not isinstance(newvoc, set):
            raise TypeError("New vocabulary param should be represented by set")
        else:
            self.lexicon.add(newvoc)
            self.vocab_size = len(self.lexicon)

    def getLexiconSize(self):
        return self._lexicon_size

    def getLexicon():
        return self._lexicon
    
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
        self.updateLexicon(set([i.lower().strip() 
            for i in out]))
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
        for idx in range(len(toks)):
                word = toks[idx]
                envec = [0]*dims
                neighborhood =  range(idx-n, idx+n)
                for i in neighborhood:
                        if 0 <= i < tlim:
                                neighbor = toks[i]
                                schema_idx = schema.index(neighbor)
                                envec[schema_idx] += 1
                out[word].append(envec)
                if idx % 1000 == 0:
                        print('environments computed for {} tokens\n'.format(idx))
        # now flatten le matrices
        print('computing word vectors...')
        out = {k:matrix_mean(out[k]) for k in out}
        return out
    

    def newModel(self, nbrhd, dselect, dredstrat, mkey=None):
        if mkey is None:
                dat_param = '-'.join(dselect)
                mkey = "{}_window_{}_data_{}".format(dredstrat, nbrhd, dat_param)
        self.models[mkey] = Model(nbrhd, dselect, self, 
                                 dimensionality_reduction_mode=dredstrat)
        print("reducing corpus environment vectors via {}...".format(dredstrat))
        # call embedder's compileData method, then apply dimensionality reduction
        # to its output
        # Ok, so the WordEmbedder class should store compressed env vectors,
        # write to file, so 
<<<<<<< HEAD
        for datafield in dselect:
            dset = self.data[datafield]
                            
=======
        dfiles = ls(self.dataPath)
        for datafield in dselect:
                # get all datafiles containing tag in select criteria
                hasfield = [fname for fname in dfiles
                                 if datafield in f]
                
                
                
                
                
                
>>>>>>> ad27b97ff9cc196d178edd7ac2552597830a90ee
        
        
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

    def vDecompress(self, tab):
        # build list of length
        out = [0]*tab['MAX'] 
        del tab['MAX']
        for key in tab:
                out[key] += tab[key]
        return out              


class Model:

    def __init__(self, window, data, embedder, dimensionality_reduction_mode='TSNE'):
            
            self.window = window
            self.data = data
            self._dimredmode = dimred[dimensionality_reduction_mode]
            self._embeddings = []



    def __getitem__(self, key):
        if isinstance(key, str):
            return self.data[key]
        else:
            raise ValueError('Model lookup is by word.')

    def reduceDimensionality(self):
        self._dimredmode() 

    
        
if __name__ == '__main__':
        def update():
                with open('tokenize.py') as pfile:
                        script = pfile.read()
                return script
        ud = lambda: exec(update())
        # declare constants and read text data from file via command line arg
        nhood = 4
        tag = 'table_compress'
        compressed = False
        recompute = False
        prcsr = WordEmbedder()
        mk = 'test_mod'
        #infile = sys.argv[1]
        infile = 'paradise_lost.txt.rtf'
        with open(infile) as ifdat:
                text = ifdat.read()
        if recompute:
                # tokenize and normalize
                tokenized = prcsr.tokenize(text)
                tokenized = [l.lower() for l in tokenized]
                # compute word frequencies. TODO: make this block a WordEmbedder method
                freqs = Counter(tokenized)
                total = len(freqs)
                freqs = {k:freqs[k]/total for k in freqs}
                # compute word embeddings
                w2vs = ngram(tokenized, nhood)
                if compressed:
                        comp = 1
                        print('Compressing...')
                        for word in w2vs:
                                w2vs[word]  = prcsr.vCompress(w2vs[word])
                else:
                        comp = 0
                cmpd_lengths = [len(w2vs[v])-comp for v in w2vs]
                mean_compressed = sum(cmpd_lengths)/total
                print('\nMean compressed embedding length: {}\n'.format(mean_compressed))
        else:
                with open('paradise_lost.txt.rtf_n_4_table_compress.json') as dfile:
                        w2vs = json.loads(dfile.read())
                # so json can't read integer keys. So, change it
                for w in w2vs:
                        print(w)
                        wval = w2vs[w]
                        buff = {}
                        for m in wval: 
                                if m.isnumeric():
                                        buff[int(m)] = wval[m]
                                else:
                                        buff[m] = wval[m]
                        w2vs[w] = buff
        tocp = w2vs['ship']
        print('Decompressing stored vectors...')
        w2vs = {k:prcsr.vDecompress(w2vs[k]) for k in w2vs}
        # convert to numpy stuff
        w2vs = {k:np.array(list(map(np.float64, w2vs[k]))) for k in w2vs}
        # dimensionality reduction stuff here
        #t1 = w2vs ['ship']
        #t2 = w2vs['water']
# feed it to pj_given_i
        ship = 'ship'
        water = 'water'
        prcsr.newModel(4, ('law', 'lit'), 'TSNE', mkey=mk)
        pji = prcsr[mk].reduceDimensionality()
        print('Probability of water given ship: {}'.format(pji))

        # write embeddings to json file
        if recompute:
                outfname = "{}_n_{}_{}.json".format(infile,nhood, tag)
                with open(outfname, 'w') as ofile:
                        js = json.dumps(w2vs)
                        ofile.write(js)
                print('output written to {}'.format(outfname))
                
        
