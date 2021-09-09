"""
a python library for building word ngram dictionaries
Written by Ye Kyaw Thu
(Current post: Visiting Professor, NECTEC, Thailand)
Last updated: 1 Sept 2021
Reference: https://www.geeksforgeeks.org/python-handling-recursion-limit/
"""
import os
import sys
import tempfile
import numpy as np
from collections import defaultdict
from pylab import *
import pickle
import math
import functools

sys.setrecursionlimit(10**6)
# recursion limit added by Ye.

def count_bigram (file, bigram_dict_txt, bigram_dict_bin):
    fileBI_txt = open(bigram_dict_txt, "w")
    bigram  = defaultdict (int)
    with open (file, 'r') as fh:
        for line in fh:
            words = line.rstrip('\n').split()
            if len(words) > 0:
                pword = words[0]
                for word in words[1:]:
                    bigram[(pword,word)] += 1
                    pword = word
    for key, value in bigram.items():
        fileBI_txt.write (str(key)+'\t'+str(value)+'\n')

    fileBI_txt.close()
    
    # write binary dictionary
    fileBI_bin = open(bigram_dict_bin, "wb")
    pickle.dump(bigram, fileBI_bin)

    fileBI_bin.close()            
    return bigram

def count_unigram (file, unigram_dict_txt, unigram_dict_bin):
    fileUNI_txt = open(unigram_dict_txt, "w")
    unigram = defaultdict (int)
    with open (file, 'r') as fh:
        for line in fh:
            words = line.rstrip('\n').split()
            for word in words:
                unigram[word] += 1
    for key, value in unigram.items():
        fileUNI_txt.write (str(key)+'\t'+str(value)+'\n')
        
    fileUNI_txt.close()
        
    # write binary dictionary
    fileUNI_bin = open(unigram_dict_bin, "wb")    
    pickle.dump(unigram, fileUNI_bin)
    fileUNI_bin.close()        
    
    return unigram

