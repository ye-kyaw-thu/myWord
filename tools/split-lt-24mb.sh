#!/bin/bash

# for splitting bigram-phrase.bin,bigram-phrase.txt,bigram-word.bin and bigram-word.txt files into <=24MB files
# Written by Ye Kyaw Thu, LST, NECTEC, Thailand

for i in {bigram-phrase.bin,bigram-phrase.txt,bigram-word.bin,bigram-word.txt}
do
    split -b 24M $i $i.small.
done
