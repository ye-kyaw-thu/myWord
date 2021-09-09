# For your Information

File size information of word ngram dictionaries are as follows:
```
(base) ye@administrator-HP-Z2-Tower-G4-Workstation:~/tool/word-seg-tool/python-wordsegment/wordsegment/y-test/ref/viterbi/dev4github/4release/dict_ver1$ ls *word* -lh
-rw-rw-r-- 1 ye ye  56M စက်    9 19:36 bigram-word.bin
-rw-rw-r-- 1 ye ye  49M စက်    9 19:36 bigram-word.txt
-rw-rw-r-- 1 ye ye 4.4M စက်    9 19:36 unigram-word.bin
-rw-rw-r-- 1 ye ye 3.3M စက်    9 19:36 unigram-word.txt
```

File size information of phrase ngram dictionaries are as follows:
```
(base) ye@administrator-HP-Z2-Tower-G4-Workstation:~/tool/word-seg-tool/python-wordsegment/wordsegment/y-test/ref/viterbi/dev4github/4release/dict_ver1$ ls *phrase* -lh
-rwxr-xr-x 1 ye ye 132M စက်    9 19:28 bigram-phrase.bin
-rw-rw-r-- 1 ye ye 155M စက်    9 19:28 bigram-phrase.txt
-rwxr-xr-x 1 ye ye  25M စက်    9 19:28 unigram-phrase.bin
-rw-rw-r-- 1 ye ye  21M စက်    9 19:28 unigram-phrase.txt
```

GitHub allows uploading files < 50 MB.
And thus, I can only upload smoothly following files:

(base) ye@administrator-HP-Z2-Tower-G4-Workstation:~/tool/word-seg-tool/python-wordsegment/wordsegment/y-test/ref/viterbi/dev4github/4release/dict_ver1$ ls *unigram* -lh
-rwxr-xr-x 1 ye ye  25M စက်    9 19:28 unigram-phrase.bin
-rw-rw-r-- 1 ye ye  21M စက်    9 19:28 unigram-phrase.txt
-rw-rw-r-- 1 ye ye 4.4M စက်    9 19:36 unigram-word.bin
-rw-rw-r-- 1 ye ye 3.3M စက်    9 19:36 unigram-word.txt

*** For the files > 50 MB, I have to splitted as several small files.

```
(base) ye@administrator-HP-Z2-Tower-G4-Workstation:~/tool/word-seg-tool/python-wordsegment/wordsegment/y-test/ref/viterbi/dev4github/4release/dict_ver1/split-test$ ls
bigram-phrase.bin  bigram-phrase.txt  bigram-word.bin  bigram-word.txt  split-lt-24mb.sh
```

```
(base) ye@administrator-HP-Z2-Tower-G4-Workstation:~/tool/word-seg-tool/python-wordsegment/wordsegment/y-test/ref/viterbi/dev4github/4release/dict_ver1/split-test$ ./split-lt-24mb.sh 
```

```
(base) ye@administrator-HP-Z2-Tower-G4-Workstation:~/tool/word-seg-tool/python-wordsegment/wordsegment/y-test/ref/viterbi/dev4github/4release/dict_ver1/split-test$ ls
bigram-phrase.bin           bigram-phrase.bin.small.ad  bigram-phrase.txt.small.aa  bigram-phrase.txt.small.ae  bigram-word.bin.small.aa  bigram-word.txt.small.aa
bigram-phrase.bin.small.aa  bigram-phrase.bin.small.ae  bigram-phrase.txt.small.ab  bigram-phrase.txt.small.af  bigram-word.bin.small.ab  bigram-word.txt.small.ab
bigram-phrase.bin.small.ab  bigram-phrase.bin.small.af  bigram-phrase.txt.small.ac  bigram-phrase.txt.small.ag  bigram-word.bin.small.ac  bigram-word.txt.small.ac
bigram-phrase.bin.small.ac  bigram-phrase.txt           bigram-phrase.txt.small.ad  bigram-word.bin             bigram-word.txt           split-lt-24mb.sh
```

## Do This

Just run this shell script.
$ ./combine-all-splitted-files.sh 

You will get the combined ngram dictionaries:
$ ls
bigram-phrase.bin  bigram-phrase.txt  bigram-word.bin  bigram-word.txt  bk  combine-all-splitted-files.sh  split-lt-24mb.sh




