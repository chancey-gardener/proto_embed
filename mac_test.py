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
#prcsr.newModel(nhood, 'TSNE', mkey=mk)

tparams = {
	    'n_components':3,
	    'mode':'TSNE',
	    'n_iter':250
	    #'method':'exact'
	    }
prcsr.newModel(nhood, tparams, mkey=mk)
#reduced = prcsr[mk].reduceDimensionality()


if recompute:
    envs = prcsr.getEnvsFromTokens(text, nhood)
    prcsr.rawEnvsToJson(envs, json_fname)



stored_vecs = json_fname + ".json"
unpacked = prcsr.unPackJson(stored_vecs)
unpacked = prcsr.vDecompressAll(unpacked)
### print metadata stuff

print(stored_vecs)
print(len(unpacked))
water = 'water'
waterv = unpacked['water']
print('reshaping')
waterv = waterv.reshape(-1, 1)
print('running TSNE on water vector')
reduced = prcsr[mk].reduceDimensionality(waterv)
print(water)
print(reduced)


