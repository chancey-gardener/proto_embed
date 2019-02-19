#!/usr/bin/python3

# a test file for word_embedder.py made
# for tests on randomchance

DATAPATH = 'data'

nhood = 4

prcsr = WordEmbedder(DATAPATH)
intest = 'paradise_lost.txt'
with open(intest) as infile:
    text = infile.read()


