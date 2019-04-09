#!/usr/bin/python3

from os import listdir as ls
import json
import codecs
import ElementTree as et


def getSet(fpath):
    with codecs.open(fpath) as stream:
        dat = stream.read().split()
    return set(word.lower() for word in dat)

def writeMetaDataToXml(corpusName, outset):
    root = et.Element("root")
    ftag = et.Subelement(root, "fname")
    # organize le data here
    tree = et.ElementTree(root)
    tree.write("{}.xml".format(corpusName))

def main(dirpath):
    out = {"TOTAL":set()}
    driter = (f for f in ls(dirpath) if f.endswith('.csv'))
    for fl in driter:
        token_set = getSet(fl)
        out[f] = token_set
        out["TOTAL"].add(token_set)
    writeMetaDataToXml(out)

    
        
