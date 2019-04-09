<<<<<<< Local Changes
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
        dpath = 'data'
        prcsr = WordEmbedder('data')
        mk = 'test_mod'
        #infile = sys.argv[1]
        infile = 'data/paradise_lost.txt.rtf'
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
                =======
#!/usr/bin/python3

# a test file for word_embedder.py made
# for tests on randomchance

DATAPATH = 'data'

nhood = 4

prcsr = WordEmbedder(DATAPATH)
intest = 'paradise_lost.txt'
with open(intest) as infile:
    text = infile.read()


>>>>>>> External Changes
