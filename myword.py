"""
Syllable, Word, Phrase Segmenter for Burmese (Myanmar language)
Written by Ye Kyaw Thu
(Visiting Professor, LST, NECTEC, Thailand)
Last Updated: 5 Sept 2021

 How to run:
 
 ### Syllable segmentation ###
 
 Syllable segmentation with default delimiter "space"
 $ python ./myword.py syllable ./test.txt ./test.syl
 
 Syllable segmentation with delimiter "pipe"
 $ python ./myword.py syllable --delimiter "|" ./test.txt ./test.syl

 ### n-gram Dictionary Building for Word Segmentation ###
 
 Word n-gram dictionary building with full dictionary filenames parameters:
 $ python ./myword.py build_dict --unigram_word_txt unigram-word.txt --bigram_word_txt bigram-word.txt --unigram_word_bin unigram-word.bin --bigram_word_bin bigram-word.bin ./corpus2.1k 
 
 Word n-gram dictionary building with default filenames:
 $ python ./myword.py build_dict ./corpus2.1k 

 ### Word Segmentation ###
 
 Word segmentation with default n-gram dictionaries:
 $ python ./myword.py word ./test.txt ./test.word
 
 Word segmentation with binary n-gram dictionaries:
 $ python ./myword.py word --unigram_word_bin ./unigram-word.bin --bigram_word_bin ./bigram-word.bin ./test.txt ./test.word
 
 Word segmentation with delimiter "pipe"
 $ python ./myword.py word --delimiter "|" ./test.txt ./test.word
 
### Phrase Segmentation ###

Phrase segmentation with default unigram and bigram dictionaries:
python ./myword.py phrase ./test.space.txt ./test.phrase

Phrase segmentation with assigned unigram and bigram dictionaries:
python ./myword.py phrase --unigram_phrase_bin ./unigram-phrase.bin --bigram_phrase_bin ./bigram-phrase.bin ./test2.txt ./test2.phrase

### Training or Building Phrase Unit Unigram, Bigram Dictionaries

time python ./myword.py train_phrase -l 10 -t 0.1 -f 3 --unigram_phrase_txt unigram.l10.t0.1f3.txt --bigram_phrase_txt bigram.l10.t0.1f3.txt --unigram_phrase_bin unigram.l10.t0.1f3.bin --bigram_phrase_bin bigram.l10.t0.1f3.bin ./corpus2.1k ./train.l10t0.1f3.out

### NPMI Training Experiment

time python ./myword.py npmi_train -lr "1,3" -tr "0.1,0.3" -fr "1,3" ./corpus2.1k
time python ./myword.py npmi_train -lr "1,3" -tr "0.1,0.3" -fr "1,3" ./corpus2.1k.syl


### Reference
https://www.delftstack.com/howto/python/python-range-float/
https://docs.python.org/3/library/decimal.html

"""

import os
import sys
import argparse
#import itertools
from decimal import *
getcontext().prec = 1

# library for syllable segmentation
import syl_segment as syl

# library for phrase segmentation
import phrase_segment as phr

# library for word ngram dictionary building
import word_dict as wdict
# library for word segmentation (wsg)
import word_segment as wseg

def make_range(start, stop, step):
    while start < stop:
        yield start
        start = start + step

def main (command_line=None):

    # Initialize parser
    parser = argparse.ArgumentParser(prog='myword', description='Syllable, Word, Phrase Segmenter for Burmese (Myanmar language)')
    parser.add_argument('-v', '--version', action='version', version='%(prog)s 1.0', help="output version information and exit")   
    subprasers = parser.add_subparsers(dest='command')        
    
    syllable = subprasers.add_parser('syllable', help='syllable segmentation with Regular Expression')

    syllable.add_argument('-d', '--delimiter', type=str, default=' ', help='the delimiter option for syllable unit e.g. using piple "|", the default delimiter is "space"') 
    syllable.add_argument('input', type=str, help="input filename for word segmentation")
    syllable.add_argument('output', type=str, help="output filename")       

    train = subprasers.add_parser('build_dict', help='building n-gram dictionaries for word segmentation')
    train.add_argument('-ut', '--unigram_word_txt', type=str, default='./dict_ver1/unigram-word.txt', help="set output filename of the unigram word dictionary (text-file), the default name is \"unigram-word.txt\"")
    train.add_argument('-bt', '--bigram_word_txt', type=str, default='./dict_ver1/bigram-word.txt', help="set output filename of the bigram word dictionary (text-file), the default name is \"bigram-word.txt\"")        
    train.add_argument('-ub', '--unigram_word_bin', type=str, default='./dict_ver1/unigram-word.bin', help="set output filename of the unigram word dictionary (binary-file), the default name is \"unigram-word.bin\"")
    train.add_argument('-bb', '--bigram_word_bin', type=str, default='./dict_ver1/bigram-word.bin', help="set output filename of the bigram word dictionary (binary-file), the default name is \"bigram-word.bin\"")    
    train.add_argument('input', type=str, help="input filename for training")

    word = subprasers.add_parser('word', help='word segmentation with Vitabi algorithm proposed by Andrew James Viterbi, 1967')
    word.add_argument('-d', '--delimiter', type=str, default=' ', help='the delimiter option for word unit e.g. using piple "|", the default is "space"')     
    word.add_argument('-ub', '--unigram_word_bin', type=str, default='./dict_ver1/unigram-word.bin', help="set filename of the unigram word dictionary for segmentation (binary-file), the default name is \"unigram-word.bin\"")
    word.add_argument('-bb', '--bigram_word_bin', type=str, default='./dict_ver1/bigram-word.bin', help="set filename of the bigram word dictionary for segmentation (binary-file), the default name is \"bigram-word.bin\"")        
    word.add_argument('input', type=str, help="input filename for word segmentation")
    word.add_argument('output', type=str, help="output filename")        
          
    train_phrase = subprasers.add_parser('train_phrase', help='training or building n-gram dictionaries for phrase segmentation')
    #parser.add_argument('--train', action='store_const', const=False, default=False, help="run with training mode")
    train_phrase.add_argument('-l', '--iteration', type=int, default=2, help="the number of training iterations, the default is 2")    
    train_phrase.add_argument('-t', '--threshold', type=float, default=0.1, help="set the threshold value, the default is 0.1")
    train_phrase.add_argument('-f', '--minfreq', type=int, default=3, help="set the minimum frequency value, the default is 3")
    
    train_phrase.add_argument('-ut', '--unigram_phrase_txt', type=str, default='./dict_ver1/unigram-phrase.txt', help="set output filename of the unigram dictionary (text-file), the default name is \"unigram-phrase.txt\"")
    train_phrase.add_argument('-bt', '--bigram_phrase_txt', type=str, default='./dict_ver1/bigram-phrase.txt', help="set output filename of the bigram dictionary (text-file), the default name is \"bigram-phrase.txt\"")        
    train_phrase.add_argument('-ub', '--unigram_phrase_bin', type=str, default='./dict_ver1/unigram-phrase.bin', help="set output filename of the unigram dictionary (binary-file), the default name is \"unigram-phrase.bin\"")
    train_phrase.add_argument('-bb', '--bigram_phrase_bin', type=str, default='./dict_ver1/bigram-phrase.bin', help="set output filename of the bigram dictionary (binary-file), the default name is \"bigram-phrase.bin\"")    
    train_phrase.add_argument('input', type=str, help="input filename for training")
    train_phrase.add_argument('output', type=str, help="output filename")    

    phrase = subprasers.add_parser('phrase', help='phrase segmentation with NPMI (Normalized Pointwise Mutual Information) proposed by Bouma Gerlof, 2009')
    phrase.add_argument('-t', '--threshold', type=float, default=0.1, help="set the threshold value, the default is 0.1")
    phrase.add_argument('-f', '--minfreq', type=int, default=3, help="set the minimum frequency value, the default is 3")    
    phrase.add_argument('-ub', '--unigram_phrase_bin', type=str, default='./dict_ver1/unigram-phrase.bin', help="set filename of the unigram dictionary for segmentation (binary-file), the default name is \"unigram-phrase.bin\"")
    phrase.add_argument('-bb', '--bigram_phrase_bin', type=str, default='./dict_ver1/bigram-phrase.bin', help="set filename of the bigram dictionary for segmentation (binary-file), the default name is \"bigram-phrase.bin\"")        
    phrase.add_argument('input', type=str, help="input filename for phrase segmentation")
    phrase.add_argument('output', type=str, help="output filename")        

    npmi_train = subprasers.add_parser('npmi_train', help='training or building n-gram dictionaries with NPMI and run segmentation experiment for x-unit (e.g. character, syllable, sub_word, word) with built dictionaries, the learning x-unit will depends on your input file segmentation')
    npmi_train.add_argument('-lr', '--iteration_range', type=str, default="1,3", help="the training iterations range (e.g. \"1,5\"), the default is \"1,3\"")    
    npmi_train.add_argument('-tr', '--threshold_range', type=str, default="0.1,0.3", help="set the threshold value range (e.g. \"0.1,0.5\"), the default is \"0.1,0.3\"")
    npmi_train.add_argument('-fr', '--minfreq_range', type=str, default="1,3", help="set the minimum frequency value range (e.g. \"1,5\"), the default is \"1,3\"")   
    npmi_train.add_argument('input', type=str, help="input filename for training")

    args = parser.parse_args(command_line)
    filein = args.input        # input file for all segmentation units (i.e. syllable, phrase, word)
    
    if args.command == 'build_dict':
        uni_dict_txt = args.unigram_word_txt
        bi_dict_txt = args.bigram_word_txt
        uni_dict_bin = args.unigram_word_bin    
        bi_dict_bin = args.bigram_word_bin        
        
        unigram = wdict.count_unigram (filein, uni_dict_txt, uni_dict_bin)
        bigram  = wdict.count_bigram  (filein, bi_dict_txt, bi_dict_bin)
        
    elif args.command == 'word':
        uni_dict_bin = args.unigram_word_bin
        bi_dict_bin = args.bigram_word_bin
        fileout = args.output
        wordDelimiter= args.delimiter # assign local variable delimiter        
        outputFILE = open(fileout, "w")        
  
        wseg.P_unigram = wseg.ProbDist(uni_dict_bin, True)
        wseg.P_bigram = wseg.ProbDist(bi_dict_bin, False)
        
        with open (filein, 'r') as fh:
            for line in fh:
                    listString = wseg.viterbi(line.replace(" ", "").strip()) # remove space between words and pass to viterbi()
                    #print("listString: " + str(listString))
                    wordStr = wordDelimiter.join(listString[1])
                    wordClean1=wordStr.strip()
                    wordClean2=wordClean1.strip(wordDelimiter)                    
                    outputFILE.write (wordClean2+"\n")                    
        outputFILE.close()
        
    elif args.command == 'syllable':
        fileout = args.output
        outputFILE = open(fileout, "w")          
        syl.delimiter = args.delimiter # assign syl_break module variable delimiter

        with open (filein, 'r') as fh:
            for line in fh:
                    syllableString = syl.syllable(line.replace(" ", "")) # remove space between words and pass to syllable()
                    #print(syllableString)
                    sylClean1=syllableString.strip()
                    sylClean2=sylClean1.strip(args.delimiter)
                    outputFILE.write (sylClean2+"\n")
        outputFILE.close()

    elif args.command == 'train_phrase':
        iters = args.iteration
        threshold = args.threshold
        minfreq = args.minfreq
        fileout = args.output            
            
        uni_dict_txt = args.unigram_phrase_txt
        bi_dict_txt = args.bigram_phrase_txt
        uni_dict_bin = args.unigram_phrase_bin
        bi_dict_bin = args.bigram_phrase_bin

        # training for phrase segmentation with word segmented corpus
        print(vars(args))
        phr.train_phrase(iters, threshold, minfreq, uni_dict_txt, bi_dict_txt, uni_dict_bin, bi_dict_bin, filein, fileout)

    elif args.command == 'phrase':
        threshold = args.threshold
        minfreq = args.minfreq
        fileout = args.output            
        uni_dict_bin = args.unigram_phrase_bin
        bi_dict_bin = args.bigram_phrase_bin
            
        print(vars(args))            
        phr.phrase_segmentation(threshold, minfreq, uni_dict_bin, bi_dict_bin, filein, fileout)
        
    elif args.command == 'npmi_train':
        iters_start, iters_end = args.iteration_range.split(',')
        iters_seq = range(int(iters_start), int(iters_end)+1)
        threshold_start, threshold_end = args.threshold_range.split(',')
        t_end = Decimal(threshold_end) + Decimal(0.1)
        threshold_seq = make_range(Decimal(threshold_start), t_end, Decimal(0.1))
        minfreq_start, minfreq_end = args.minfreq_range.split(',')
        minfreq_seq = range(int(minfreq_start), int(minfreq_end)+1)
        #print ('iters_seq: ' + str(iters_seq) + ', threshold_seq: ' + str(threshold_seq) + ', minfreq_seq: ', str(minfreq_seq))
        
#        for i in iters_seq: # I have to move iters_seq to third looping ... a trap of Python programming ?!
        for j in threshold_seq:
            for k in minfreq_seq:
                for i in iters_seq:
                    fileout = filein + '.l' +  str(i) + '.t' + str(j) + '.f' + str(k) + '.seg'  # assigning output filename such as 
                    uni_dict_txt = 'unigram' + '.l' +  str(i) + '.t' + str(j) + '.f' + str(k) + '.txt'
                    bi_dict_txt = 'bigram' + '.l' +  str(i) + '.t' + str(j) + '.f' + str(k) + '.txt'
                    uni_dict_bin = 'unigram' + '.l' +  str(i) + '.t' + str(j) + '.f' + str(k) + '.bin'
                    bi_dict_bin = 'bigram' + '.l' +  str(i) + '.t' + str(j) + '.f' + str(k) + '.bin'

                    # training for x segmentation with the input corpus
                    #print(vars(args))
                    print('iters: ' + str(i) + ', threshold:'  + str(j) + ', minfreq: ' + str(k) + ', ' + uni_dict_txt  + ', ' + bi_dict_txt  + ', ' + uni_dict_bin  + ', ' + bi_dict_bin  + ', ' + filein  + ', ' + fileout)
                    phr.train_phrase(i, j, k, uni_dict_txt, bi_dict_txt, uni_dict_bin, bi_dict_bin, filein, fileout)    


if __name__ == "__main__":
    main ()


