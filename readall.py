#!/usr/bin/env python3

import os
import sys

def usage():
    print('Starting from the given directory, read all the files recursively.')
    print(f'python3 {sys.argv[0]} <starting_dir>')
    exit(-1)

if len(sys.argv) != 2:
    usage()

start = sys.argv[1]

for dpath,dirs,files in os.walk(start):
    for f in files:
        try:
            with open(os.path.join(dpath,f), 'r') as f:
                for i in f.readlines(): print(i.strip())
        except:
            pass
