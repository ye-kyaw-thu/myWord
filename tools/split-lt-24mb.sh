#!/bin/bash

for i in {bigram-phrase.bin,bigram-phrase.txt,bigram-word.bin,bigram-word.txt}
do
    split -b 24M $i $i.small.
done
