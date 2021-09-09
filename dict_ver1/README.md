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

```
(base) ye@administrator-HP-Z2-Tower-G4-Workstation:~/tool/word-seg-tool/python-wordsegment/wordsegment/y-test/ref/viterbi/dev4github/4release/dict_ver1$ ls *unigram* -lh
-rwxr-xr-x 1 ye ye  25M စက်    9 19:28 unigram-phrase.bin
-rw-rw-r-- 1 ye ye  21M စက်    9 19:28 unigram-phrase.txt
-rw-rw-r-- 1 ye ye 4.4M စက်    9 19:36 unigram-word.bin
-rw-rw-r-- 1 ye ye 3.3M စက်    9 19:36 unigram-word.txt
```

*** For the files > 50 MB, I have to splitted as several small files.  

for Myanmar users:  
GitHub က 25MB ထက်ကြီးတဲ့ ဖိုင်တွေကို upload ပေးမလုပ်ဘူး။  
အဲဒါကြောင့် bigram dictionary တွေကို 24MB ပဲရှိတဲ့ ဖိုင်အသေးလေးတွေအဖြစ် split လုပ်ပြီးမှ upload လုပ်ထားတယ်။  

ကိုယ့်စက်ထဲကို myWord Segmentation Tool ကို download လုပ်ပြီးသွားတဲ့အခါမှာ ./dict_ver1/ ဖိုလ်ဒါအောက်ကို ဝင်ပြီးတော့ ./combine-all-splitted-files.sh ကို run ပါ။  
$bash ./combine-all-splitted-files.sh လိုမျိုး run ပြီးသွားတဲ့အခါမှာတော့ original bigram dictionary တွေ အဖြစ် ပြန်ရလာပါလိမ့်မယ်။  

*** အခု ပြောတဲ့ အဆင့်ကို မလုပ်ပဲနဲ့ default dictionary တွေကို သုံးပြီးတော့ myWord.py နဲ့ word သို့မဟုတ် phrase segmentation ဖြတ်ဖို့ ကြိုးစားရင် error ပေးပါလိမ့်မယ်။

## Do This

And thus, after you downloaded or git clone...  
Just run this shell script.  
```
$ ./combine-all-splitted-files.sh 
```

You will get the combined ngram dictionaries:  

```
$ ls
bigram-phrase.bin  bigram-phrase.txt  bigram-word.bin  bigram-word.txt
```

