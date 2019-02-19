#!/usr/local/bin/python3
import word_embedder

### a test file for word_embedder.py made for mac
DATAPATH = 'data'

# params for model tests
nhood = 4

# declare WordEmbedder
prcsr = WordEmbedder('data')
mk = 'test_mod'
# get test text
intest = 'paradise_lost.txt'
# get text
with open(infile) as ifdat:
    text = ifdat.read()

with open('data/paradise_lost.txt.rtf_n_4_table_compress.json') as dfile:
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



