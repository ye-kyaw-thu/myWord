"""
This code is updated version of "http://chasen.org/~daiti-m/diary/misc/phraser.py" by Ye Kyaw Thu, LST, NECTEC, Thailand.
Last Updated: 10 Sept 2021

 ### Experiment Note by Ye
 parameters for NPMI, -l {1..2} -t 0.1 -f {1..3} (ဆိုရင် phrase level ကောင်းကောင်း အလုပ်လုပ်ပေးတယ်)

### References
Experiment Note by Assoc. Prof. Daichi Mochihashi: http://chasen.org/~daiti-m/diary/
Statistically recognize long phrases with Normalized PMI: http://chasen.org/~daiti-m/diary/misc/phraser.py
https://courses.engr.illinois.edu/cs440/fa2018/lectures/lect36.html
https://courses.engr.illinois.edu/cs447/fa2018/Slides/Lecture17HO.pdf
https://en.wikipedia.org/wiki/Pointwise_mutual_information
https://stackoverflow.com/questions/6589814/what-is-the-difference-between-dict-and-collections-defaultdict
https://stackoverflow.com/questions/4406501/change-the-name-of-a-key-in-dictionary
https://stackoverflow.com/questions/47606995/python3-change-dictionary-key-from-string-to-tuple-of-strings

"""

import os
import sys
import tempfile
import numpy as np
from collections import defaultdict
from pylab import *
import pickle
import argparse


def connect (words, bond):
    N = len (words)
    n = 0
    sentence = []
    while (n < N):
        flag = bond[n]
        if flag == 0:
            sentence.append (words[n])
            n += 1
        else:
            sentence.append (words[n] + '_' + words[n+1])
            n += 2
    return sentence


def collocate (words, phrases):
    N = len(words)
    bond = []
    for n in range(N-1):
        (v,w) = (words[n],words[n+1])
        if (v,w) in phrases:
            bond.append (phrases[(v,w)]) # NPMI > 0
        else:
            bond.append (0)
    bond.append (0)
    # collocate max-first
    while True:
        s = max (bond)
        n = bond.index (s)
        if s == 0:
            break
        # connect maximum
        bond[n] = -1
        if n > 0:
            bond[n-1] = 0
        if n < N-2:
            bond[n+1] = 0
    # join words
    return connect (words, bond)


def parse_write (file, phrases, output):
    with open (file, 'r') as fh:
        with open (output, 'w') as oh:
            for line in fh:
                words = line.rstrip('\n').split()
                if len(words) > 0:
                    sentence = collocate (words, phrases)
                    #print("sentence:", sentence)
                    oh.write (' '.join (sentence) + '\n')
    return output


# for Myanmar language, default threshold=0.2 and default minfreq=5 is best with "corpus2" training corpus
# for Japanese language, threshold=0.1 and minfreq=1 set by researcher Daichi Mochihashi.
def compute_phrase (unigram, bigram, threshold, minfreq):
    N = sum (list(unigram.values()))
    phrases = {}
    #print(bigram.items())
    for bi,freq in bigram.items():
        if freq >= minfreq:
            v = bi[0]; w = bi[1]
            # print("N:", N, "v:", v, "w:", w, "unigram[v]:", unigram[v], "unigram[w]:", unigram[w])
            npmi = (log(N) + log(freq) - log(unigram[v]) - log(unigram[w])) \
                    / (log(N) - log(freq))
            if npmi > threshold:
                phrases[bi] = npmi
    #print("phrases: ", phrases)
    return phrases


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
    
    #new_bigram = {} # got error
    new_bigram = defaultdict(int)
    # removed "_" for phrase option or phrase segmentation
    for key, value in bigram.items():
        keyi1 = key[0].replace('_', '')
        keyi2 = key[1].replace('_', '')
        new_bigram[(keyi1,keyi2)]  = value
    
    # write binary dictionary
    fileBI_bin = open(bigram_dict_bin, "wb")
    pickle.dump(new_bigram, fileBI_bin)
    fileBI_bin.close()
    new_bigram.clear()
                
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
    
    #new_unigram = {}, got error
    new_unigram = defaultdict(int)
    # removed "_" for phrase option or phrase segmentation       
    new_unigram = { key.replace('_', ''): value for key, value in unigram.items() }
    # write binary dictionary
    fileUNI_bin = open(unigram_dict_bin, "wb") 
    pickle.dump(new_unigram, fileUNI_bin)

    fileUNI_bin.close()      
    #new_unigram.clear()  
    
    return unigram


def eprint (s,clear=True):
    if clear:
        sys.stderr.write ('\x1b[K')
    sys.stderr.write (s + "\n")
    sys.stderr.flush ()


def train_phrase(iters, threshold, minfreq, uni_dict_txt, bi_dict_txt, uni_dict_bin, bi_dict_bin, file_input, file_output):
    eprint ('computing phrases: threshold = %g minfreq = %d' % (threshold,minfreq))
    filein = file_input    
    for iter in range(1,iters+1):
        eprint ('pass [%d/%d]..' % (iter,iters))
        # count n-grams
        eprint ('- computing phrases..')
        unigram = count_unigram (filein, uni_dict_txt, uni_dict_bin)
        bigram  = count_bigram  (filein, bi_dict_txt, bi_dict_bin)
        phrases = compute_phrase (unigram, bigram, threshold, minfreq)
        # save intermediate file
        if iter == iters:
            fileout = file_output
        else:
            fileout = tempfile.mktemp()
        eprint ('- writing output..')
        parse_write (filein, phrases, fileout)
        if (filein != file_input):
            os.remove (filein)
        filein = fileout
    eprint ('done.')


def read_dict (fileDICT):
    try:
        with open(fileDICT, 'rb') as input_file:
            dictionary = pickle.load(input_file)
            input_file.close()
            
    except FileNotFoundError:
        print('Dictionary file', fileDICT, ' not found!')
    return dictionary


def phrase_segmentation(threshold, minfreq, uni_dict_bin, bi_dict_bin, input, output):
    eprint ('computing phrases: threshold = %g minfreq = %d' % (threshold,minfreq))
    filein = input    

    eprint ('phrase segmentation...')
    eprint ('- read unigram dictionary')
    unigram = read_dict(uni_dict_bin)
    
    #print(unigram)
    eprint ('- read bigram dictionary')    
    bigram = read_dict(bi_dict_bin)
    #print(bigram)
    eprint ('- computing phrases..')    
    phrases = compute_phrase (unigram, bigram, threshold, minfreq)
    #print(phrases)
        # save intermediate file
    fileout = output

    print ('- writing output..., filename: ', output)
    parse_write (filein, phrases, fileout)
    #if (filein != input):
    #    os.remove (filein)
    filein = output    
    eprint ('done.')
    
