#!/usr/bin/python3

from os import listdir as ls
import sys

targets = []

for pdir in sys.path:
    files = ls(pdir)
    select = [i for i in files if 'thread' in i]
    targets += select
for m in targets:
    print(m)


