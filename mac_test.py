#!/usr/local/bin/python3
import word_embedder as we

### a test file for word_embedder.py made for mac
DATAPATH = 'data'
recompute = False


# params for model test 
nhood = 4

# declare WordEmbedder
prcsr = we.WordEmbedder('data')
mk = 'test_mod'
# get test text
intest = 'paradise_lost.txt'
# get text

json_fname = intest[:-4]+"_n_4"


text = prcsr.readFile(intest)
prcsr.newModel(nhood, 'TSNE', mkey=mk)

tparams = {'n_components':300}

reduced = prcsr[mk].reduceDimensionality(tparams)


if recompute:
    envs = prcsr.getEnvsFromTokens(text, nhood)
    prcsr.rawEnvsToJson(envs, json_fname)



stored_vecs = json_fname + ".json"
unpacked = prcsr.unPackJson(stored_vecs)
### print metadata stuff

print(stored_vecs)
print(len(unpacked))




