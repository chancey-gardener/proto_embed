#!/usr/bin/python3
from os import chdir as cd, getcwd as pwd
cwd = pwd()
cd('/usr/lib/python3.6')
import sys, json
from collections import Counter
from math import sqrt, e
#from multiprocessing import pool
cd(cwd)



PUNCT = '.,;:?!'
APOST = "'"

def tokenize(text):
        out = []
        idx = 0
        print('\ntokenizing...\n')
        try:
                while idx < len(text):
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
                return out
        return out

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
        

def ngram(toks, n):
        '''Compute word embeddings given a tokenized text
                returns hash table mapping unique words in
                text to word embeddings computed from
                that text '''
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
        

def vcomp(emb):
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

def decomp(tab):
        # build list of length
        out = [0]*tab['MAX'] 
        del tab['MAX']
        for key in tab:
                out[key] += tab[key]
        return out              

def vdiff(vi, vj):
        '''computes the difference of two vectors (python lists)'''
#       return [vi[i]-vj[i] for i in range(len(vi))]
        out = []
        for i in range(len(vi)):
                a = vi[i]
                b = vj[i]
               # print("t1[ {} ]: {}".format(i, a))
               # print("t2[ {} ]: {}".format(i, b))
                diff = a - b
                out.append(diff)
        return out
def ev2norm(vec):
        return sqrt(sum(s**2 for s in vec))

def pj_given_i(xi, xj, dist):
        '''where xi and xj are vectors'''
        # compute 2*sigma^2
        tsig = 2*variance(xi)
        # get numerator of expression for p(j|i)
        exper = lambda vec: e** ((0-ev2norm(vdiff(xi, vec)))/tsig)
        numexp = exper(xj)
        # well now? we're gonna compute a motherfuckin denominator
        denexp = 0
        # TODO: the values computed in this for loop have got to be stored
#       warp = pool(4)
#       noti = (dist[k] for k in dist if dist[k] != xi)
        print('Computing covariance matrix...')
        #denexp = sum(warp.map(exper, noti))
        denexp = 0
        count = 0 # just to show us how
        span = len(dist)
        for k in dist:
            dvec = dist[k]
            if dvec != xi:
                diffscore = exper(dvec)
                denexp += diffscore
               # print(diffscore)
            count += 1
            prop = round((count/span)*100, 2)
            if prop%1 == 0:
                print('{}% complete'.format(prop))
                print('{}/{}'.format(numexp,denexp))
        pji = numexp/denexp
        return pji
        
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
        #infile = sys.argv[1]
        infile = 'paradise_lost.txt.rtf'
        with open(infile) as ifdat:
                text = ifdat.read()
        if recompute:
                # tokenize and normalize
                tokenized = tokenize(text)
                tokenized = [l.lower() for l in tokenized]
                # compute word frequencies.
                freqs = Counter(tokenized)
                total = len(freqs)
                freqs = {k:freqs[k]/total for k in freqs}
                # compute word embeddings
                w2vs = ngram(tokenized, nhood)
                if compressed:
                        comp = 1
                        print('Compressing...')
                        for word in w2vs:
                                w2vs[word]  = vcomp(w2vs[word])
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
        w2vs = {k:decomp(w2vs[k]) for k in w2vs}
        # dimensionality reduction stuff here
        t1 = w2vs ['ship']
        t2 = w2vs['water']
        pji = pj_given_i(t1, t2, w2vs)
        print('Probability of water given ship: {}'.format(pji))
        # write embeddings to json file
        if recompute:
                outfname = "{}_n_{}_{}.json".format(infile,nhood, tag)
                with open(outfname, 'w') as ofile:
                        js = json.dumps(w2vs)
                        ofile.write(js)
                print('output written to {}'.format(outfname))
                
        
