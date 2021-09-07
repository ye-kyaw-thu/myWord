# မမ ဝဝ Experiment

Date: 7 Sept 2021  


```
(base) ye@administrator-HP-Z2-Tower-G4-Workstation:~/tool/word-seg-tool/python-wordsegment/wordsegment/y-test/ref/viterbi/dev4github/4release/syl-learning-exp$ time python ./myword.py npmi_train -lr "1,2" -tr "0.1,0.2" -fr "1,3" ./mama_wawa.txt
iters: 1, threshold:0.1, minfreq: 1, unigram.l1.t0.1.f1.txt, bigram.l1.t0.1.f1.txt, unigram.l1.t0.1.f1.bin, bigram.l1.t0.1.f1.bin, ./mama_wawa.txt, ./mama_wawa.txt.l1.t0.1.f1.seg
computing phrases: threshold = 0.1 minfreq = 1
pass [1/1]..
- computing phrases..
- writing output..
done.
iters: 2, threshold:0.1, minfreq: 1, unigram.l2.t0.1.f1.txt, bigram.l2.t0.1.f1.txt, unigram.l2.t0.1.f1.bin, bigram.l2.t0.1.f1.bin, ./mama_wawa.txt, ./mama_wawa.txt.l2.t0.1.f1.seg
computing phrases: threshold = 0.1 minfreq = 1
pass [1/2]..
- computing phrases..
- writing output..
pass [2/2]..
- computing phrases..
- writing output..
done.
iters: 1, threshold:0.1, minfreq: 2, unigram.l1.t0.1.f2.txt, bigram.l1.t0.1.f2.txt, unigram.l1.t0.1.f2.bin, bigram.l1.t0.1.f2.bin, ./mama_wawa.txt, ./mama_wawa.txt.l1.t0.1.f2.seg
computing phrases: threshold = 0.1 minfreq = 2
pass [1/1]..
- computing phrases..
- writing output..
done.
iters: 2, threshold:0.1, minfreq: 2, unigram.l2.t0.1.f2.txt, bigram.l2.t0.1.f2.txt, unigram.l2.t0.1.f2.bin, bigram.l2.t0.1.f2.bin, ./mama_wawa.txt, ./mama_wawa.txt.l2.t0.1.f2.seg
computing phrases: threshold = 0.1 minfreq = 2
pass [1/2]..
- computing phrases..
- writing output..
pass [2/2]..
- computing phrases..
- writing output..
done.
iters: 1, threshold:0.1, minfreq: 3, unigram.l1.t0.1.f3.txt, bigram.l1.t0.1.f3.txt, unigram.l1.t0.1.f3.bin, bigram.l1.t0.1.f3.bin, ./mama_wawa.txt, ./mama_wawa.txt.l1.t0.1.f3.seg
computing phrases: threshold = 0.1 minfreq = 3
pass [1/1]..
- computing phrases..
- writing output..
done.
iters: 2, threshold:0.1, minfreq: 3, unigram.l2.t0.1.f3.txt, bigram.l2.t0.1.f3.txt, unigram.l2.t0.1.f3.bin, bigram.l2.t0.1.f3.bin, ./mama_wawa.txt, ./mama_wawa.txt.l2.t0.1.f3.seg
computing phrases: threshold = 0.1 minfreq = 3
pass [1/2]..
- computing phrases..
- writing output..
pass [2/2]..
- computing phrases..
- writing output..
done.
iters: 1, threshold:0.2, minfreq: 1, unigram.l1.t0.2.f1.txt, bigram.l1.t0.2.f1.txt, unigram.l1.t0.2.f1.bin, bigram.l1.t0.2.f1.bin, ./mama_wawa.txt, ./mama_wawa.txt.l1.t0.2.f1.seg
computing phrases: threshold = 0.2 minfreq = 1
pass [1/1]..
- computing phrases..
- writing output..
done.
iters: 2, threshold:0.2, minfreq: 1, unigram.l2.t0.2.f1.txt, bigram.l2.t0.2.f1.txt, unigram.l2.t0.2.f1.bin, bigram.l2.t0.2.f1.bin, ./mama_wawa.txt, ./mama_wawa.txt.l2.t0.2.f1.seg
computing phrases: threshold = 0.2 minfreq = 1
pass [1/2]..
- computing phrases..
- writing output..
pass [2/2]..
- computing phrases..
- writing output..
done.
iters: 1, threshold:0.2, minfreq: 2, unigram.l1.t0.2.f2.txt, bigram.l1.t0.2.f2.txt, unigram.l1.t0.2.f2.bin, bigram.l1.t0.2.f2.bin, ./mama_wawa.txt, ./mama_wawa.txt.l1.t0.2.f2.seg
computing phrases: threshold = 0.2 minfreq = 2
pass [1/1]..
- computing phrases..
- writing output..
done.
iters: 2, threshold:0.2, minfreq: 2, unigram.l2.t0.2.f2.txt, bigram.l2.t0.2.f2.txt, unigram.l2.t0.2.f2.bin, bigram.l2.t0.2.f2.bin, ./mama_wawa.txt, ./mama_wawa.txt.l2.t0.2.f2.seg
computing phrases: threshold = 0.2 minfreq = 2
pass [1/2]..
- computing phrases..
- writing output..
pass [2/2]..
- computing phrases..
- writing output..
done.
iters: 1, threshold:0.2, minfreq: 3, unigram.l1.t0.2.f3.txt, bigram.l1.t0.2.f3.txt, unigram.l1.t0.2.f3.bin, bigram.l1.t0.2.f3.bin, ./mama_wawa.txt, ./mama_wawa.txt.l1.t0.2.f3.seg
computing phrases: threshold = 0.2 minfreq = 3
pass [1/1]..
- computing phrases..
- writing output..
done.
iters: 2, threshold:0.2, minfreq: 3, unigram.l2.t0.2.f3.txt, bigram.l2.t0.2.f3.txt, unigram.l2.t0.2.f3.bin, bigram.l2.t0.2.f3.bin, ./mama_wawa.txt, ./mama_wawa.txt.l2.t0.2.f3.seg
computing phrases: threshold = 0.2 minfreq = 3
pass [1/2]..
- computing phrases..
- writing output..
pass [2/2]..
- computing phrases..
- writing output..
done.

real	0m0.255s
user	0m0.207s
sys	0m0.048s
```

```
(base) ye@administrator-HP-Z2-Tower-G4-Workstation:~/tool/word-seg-tool/python-wordsegment/wordsegment/y-test/ref/viterbi/dev4github/4release/syl-learning-exp$ for i in mama_wawa.txt.l{1..2}.t{0.1,0.2}.f{1..3}.seg;do echo -e "\n"$i":"; cat $i; done;

mama_wawa.txt.l1.t0.1.f1.seg:
မ_မ ဝ_ဝ ထ_ထ က
အ က_ပ ထ မ
က_ပါ က_ပါ မ_မ ရာ_ည ည လ_သာ သာ
ည_အ ခါ_ငါ စာ_ရ မ_မ ဝ_ဝ ထ_ထ က

mama_wawa.txt.l1.t0.1.f2.seg:
မ_မ ဝ_ဝ ထ_ထ က
အ က ပ ထ မ
က_ပါ က_ပါ မ_မ ရာ ည ည လ သာ သာ
ည အ ခါ ငါ စာ ရ မ_မ ဝ_ဝ ထ_ထ က

mama_wawa.txt.l1.t0.1.f3.seg:
မ_မ ဝ ဝ ထ ထ က
အ က ပ ထ မ
က ပါ က ပါ မ_မ ရာ ည ည လ သာ သာ
ည အ ခါ ငါ စာ ရ မ_မ ဝ ဝ ထ ထ က

mama_wawa.txt.l1.t0.2.f1.seg:
မ_မ ဝ_ဝ ထ_ထ က
အ က_ပ ထ မ
က_ပါ က_ပါ မ_မ ရာ_ည ည လ_သာ သာ
ည_အ ခါ_ငါ စာ_ရ မ_မ ဝ_ဝ ထ_ထ က

mama_wawa.txt.l1.t0.2.f2.seg:
မ_မ ဝ_ဝ ထ_ထ က
အ က ပ ထ မ
က_ပါ က_ပါ မ_မ ရာ ည ည လ သာ သာ
ည အ ခါ ငါ စာ ရ မ_မ ဝ_ဝ ထ_ထ က

mama_wawa.txt.l1.t0.2.f3.seg:
မ_မ ဝ ဝ ထ ထ က
အ က ပ ထ မ
က ပါ က ပါ မ_မ ရာ ည ည လ သာ သာ
ည အ ခါ ငါ စာ ရ မ_မ ဝ ဝ ထ ထ က

mama_wawa.txt.l2.t0.1.f1.seg:
မ_မ ဝ_ဝ_ထ_ထ က
အ_က_ပ ထ_မ
က_ပါ_က_ပါ မ_မ ရာ_ည_ည လ_သာ_သာ
ည_အ_ခါ_ငါ စာ_ရ_မ_မ ဝ_ဝ_ထ_ထ က

mama_wawa.txt.l2.t0.1.f2.seg:
မ_မ ဝ_ဝ_ထ_ထ က
အ က ပ ထ မ
က_ပါ က_ပါ မ_မ ရာ ည ည လ သာ သာ
ည အ ခါ ငါ စာ ရ မ_မ ဝ_ဝ_ထ_ထ က

mama_wawa.txt.l2.t0.1.f3.seg:
မ_မ ဝ ဝ ထ ထ က
အ က ပ ထ မ
က ပါ က ပါ မ_မ ရာ ည ည လ သာ သာ
ည အ ခါ ငါ စာ ရ မ_မ ဝ ဝ ထ ထ က

mama_wawa.txt.l2.t0.2.f1.seg:
မ_မ ဝ_ဝ_ထ_ထ က
အ_က_ပ ထ_မ
က_ပါ_က_ပါ မ_မ ရာ_ည_ည လ_သာ_သာ
ည_အ_ခါ_ငါ စာ_ရ_မ_မ ဝ_ဝ_ထ_ထ က

mama_wawa.txt.l2.t0.2.f2.seg:
မ_မ ဝ_ဝ_ထ_ထ က
အ က ပ ထ မ
က_ပါ က_ပါ မ_မ ရာ ည ည လ သာ သာ
ည အ ခါ ငါ စာ ရ မ_မ ဝ_ဝ_ထ_ထ က

mama_wawa.txt.l2.t0.2.f3.seg:
မ_မ ဝ ဝ ထ ထ က
အ က ပ ထ မ
က ပါ က ပါ မ_မ ရာ ည ည လ သာ သာ
ည အ ခါ ငါ စာ ရ မ_မ ဝ ဝ ထ ထ က
```

--------------

```
(base) ye@administrator-HP-Z2-Tower-G4-Workstation:~/tool/word-seg-tool/python-wordsegment/wordsegment/y-test/ref/viterbi/dev4github/4release/syl-learning-exp$ time python ./myword.py npmi_train -lr "1,2" -tr "0.1,0.2" -fr "1,2" ./mama_wawa.txt
iters: 1, threshold:0.1, minfreq: 1, unigram.l1.t0.1.f1.txt, bigram.l1.t0.1.f1.txt, unigram.l1.t0.1.f1.bin, bigram.l1.t0.1.f1.bin, ./mama_wawa.txt, ./mama_wawa.txt.l1.t0.1.f1.seg
computing phrases: threshold = 0.1 minfreq = 1
pass [1/1]..
- computing phrases..
- writing output..
done.
iters: 2, threshold:0.1, minfreq: 1, unigram.l2.t0.1.f1.txt, bigram.l2.t0.1.f1.txt, unigram.l2.t0.1.f1.bin, bigram.l2.t0.1.f1.bin, ./mama_wawa.txt, ./mama_wawa.txt.l2.t0.1.f1.seg
computing phrases: threshold = 0.1 minfreq = 1
pass [1/2]..
- computing phrases..
- writing output..
pass [2/2]..
- computing phrases..
- writing output..
done.
iters: 1, threshold:0.1, minfreq: 2, unigram.l1.t0.1.f2.txt, bigram.l1.t0.1.f2.txt, unigram.l1.t0.1.f2.bin, bigram.l1.t0.1.f2.bin, ./mama_wawa.txt, ./mama_wawa.txt.l1.t0.1.f2.seg
computing phrases: threshold = 0.1 minfreq = 2
pass [1/1]..
- computing phrases..
- writing output..
done.
iters: 2, threshold:0.1, minfreq: 2, unigram.l2.t0.1.f2.txt, bigram.l2.t0.1.f2.txt, unigram.l2.t0.1.f2.bin, bigram.l2.t0.1.f2.bin, ./mama_wawa.txt, ./mama_wawa.txt.l2.t0.1.f2.seg
computing phrases: threshold = 0.1 minfreq = 2
pass [1/2]..
- computing phrases..
- writing output..
pass [2/2]..
- computing phrases..
- writing output..
done.
iters: 1, threshold:0.2, minfreq: 1, unigram.l1.t0.2.f1.txt, bigram.l1.t0.2.f1.txt, unigram.l1.t0.2.f1.bin, bigram.l1.t0.2.f1.bin, ./mama_wawa.txt, ./mama_wawa.txt.l1.t0.2.f1.seg
computing phrases: threshold = 0.2 minfreq = 1
pass [1/1]..
- computing phrases..
- writing output..
done.
iters: 2, threshold:0.2, minfreq: 1, unigram.l2.t0.2.f1.txt, bigram.l2.t0.2.f1.txt, unigram.l2.t0.2.f1.bin, bigram.l2.t0.2.f1.bin, ./mama_wawa.txt, ./mama_wawa.txt.l2.t0.2.f1.seg
computing phrases: threshold = 0.2 minfreq = 1
pass [1/2]..
- computing phrases..
- writing output..
pass [2/2]..
- computing phrases..
- writing output..
done.
iters: 1, threshold:0.2, minfreq: 2, unigram.l1.t0.2.f2.txt, bigram.l1.t0.2.f2.txt, unigram.l1.t0.2.f2.bin, bigram.l1.t0.2.f2.bin, ./mama_wawa.txt, ./mama_wawa.txt.l1.t0.2.f2.seg
computing phrases: threshold = 0.2 minfreq = 2
pass [1/1]..
- computing phrases..
- writing output..
done.
iters: 2, threshold:0.2, minfreq: 2, unigram.l2.t0.2.f2.txt, bigram.l2.t0.2.f2.txt, unigram.l2.t0.2.f2.bin, bigram.l2.t0.2.f2.bin, ./mama_wawa.txt, ./mama_wawa.txt.l2.t0.2.f2.seg
computing phrases: threshold = 0.2 minfreq = 2
pass [1/2]..
- computing phrases..
- writing output..
pass [2/2]..
- computing phrases..
- writing output..
done.

real	0m0.258s
user	0m0.234s
sys	0m0.024s
```

```
(base) ye@administrator-HP-Z2-Tower-G4-Workstation:~/tool/word-seg-tool/python-wordsegment/wordsegment/y-test/ref/viterbi/dev4github/4release/syl-learning-exp$ for i in mama_wawa.txt.l{1..2}.t{0.1,0.2}.f{1..2}.seg;do echo -e "\n"$i":"; cat $i; done;

mama_wawa.txt.l1.t0.1.f1.seg:
မ_မ ဝ_ဝ ထ_ထ က
အ က_ပ ထ မ
က_ပါ က_ပါ မ_မ ရာ_ည ည လ_သာ သာ
ည_အ ခါ_ငါ စာ_ရ မ_မ ဝ_ဝ ထ_ထ က

mama_wawa.txt.l1.t0.1.f2.seg:
မ_မ ဝ_ဝ ထ_ထ က
အ က ပ ထ မ
က_ပါ က_ပါ မ_မ ရာ ည ည လ သာ သာ
ည အ ခါ ငါ စာ ရ မ_မ ဝ_ဝ ထ_ထ က

mama_wawa.txt.l1.t0.2.f1.seg:
မ_မ ဝ_ဝ ထ_ထ က
အ က_ပ ထ မ
က_ပါ က_ပါ မ_မ ရာ_ည ည လ_သာ သာ
ည_အ ခါ_ငါ စာ_ရ မ_မ ဝ_ဝ ထ_ထ က

mama_wawa.txt.l1.t0.2.f2.seg:
မ_မ ဝ_ဝ ထ_ထ က
အ က ပ ထ မ
က_ပါ က_ပါ မ_မ ရာ ည ည လ သာ သာ
ည အ ခါ ငါ စာ ရ မ_မ ဝ_ဝ ထ_ထ က

mama_wawa.txt.l2.t0.1.f1.seg:
မ_မ ဝ_ဝ_ထ_ထ က
အ_က_ပ ထ_မ
က_ပါ_က_ပါ မ_မ ရာ_ည_ည လ_သာ_သာ
ည_အ_ခါ_ငါ စာ_ရ_မ_မ ဝ_ဝ_ထ_ထ က

mama_wawa.txt.l2.t0.1.f2.seg:
မ_မ ဝ_ဝ_ထ_ထ က
အ က ပ ထ မ
က_ပါ က_ပါ မ_မ ရာ ည ည လ သာ သာ
ည အ ခါ ငါ စာ ရ မ_မ ဝ_ဝ_ထ_ထ က

mama_wawa.txt.l2.t0.2.f1.seg:
မ_မ ဝ_ဝ_ထ_ထ က
အ_က_ပ ထ_မ
က_ပါ_က_ပါ မ_မ ရာ_ည_ည လ_သာ_သာ
ည_အ_ခါ_ငါ စာ_ရ_မ_မ ဝ_ဝ_ထ_ထ က

mama_wawa.txt.l2.t0.2.f2.seg:
မ_မ ဝ_ဝ_ထ_ထ က
အ က ပ ထ မ
က_ပါ က_ပါ မ_မ ရာ ည ည လ သာ သာ
ည အ ခါ ငါ စာ ရ မ_မ ဝ_ဝ_ထ_ထ က
```

--------------

```
(base) ye@administrator-HP-Z2-Tower-G4-Workstation:~/tool/word-seg-tool/python-wordsegment/wordsegment/y-test/ref/viterbi/dev4github/4release/syl-learning-exp$ time python ./myword.py npmi_train -lr "1,2" -tr "0.1,0.1" -fr "1,2" ./mama_wawa.txt
iters: 1, threshold:0.1, minfreq: 1, unigram.l1.t0.1.f1.txt, bigram.l1.t0.1.f1.txt, unigram.l1.t0.1.f1.bin, bigram.l1.t0.1.f1.bin, ./mama_wawa.txt, ./mama_wawa.txt.l1.t0.1.f1.seg
computing phrases: threshold = 0.1 minfreq = 1
pass [1/1]..
- computing phrases..
- writing output..
done.
iters: 2, threshold:0.1, minfreq: 1, unigram.l2.t0.1.f1.txt, bigram.l2.t0.1.f1.txt, unigram.l2.t0.1.f1.bin, bigram.l2.t0.1.f1.bin, ./mama_wawa.txt, ./mama_wawa.txt.l2.t0.1.f1.seg
computing phrases: threshold = 0.1 minfreq = 1
pass [1/2]..
- computing phrases..
- writing output..
pass [2/2]..
- computing phrases..
- writing output..
done.
iters: 1, threshold:0.1, minfreq: 2, unigram.l1.t0.1.f2.txt, bigram.l1.t0.1.f2.txt, unigram.l1.t0.1.f2.bin, bigram.l1.t0.1.f2.bin, ./mama_wawa.txt, ./mama_wawa.txt.l1.t0.1.f2.seg
computing phrases: threshold = 0.1 minfreq = 2
pass [1/1]..
- computing phrases..
- writing output..
done.
iters: 2, threshold:0.1, minfreq: 2, unigram.l2.t0.1.f2.txt, bigram.l2.t0.1.f2.txt, unigram.l2.t0.1.f2.bin, bigram.l2.t0.1.f2.bin, ./mama_wawa.txt, ./mama_wawa.txt.l2.t0.1.f2.seg
computing phrases: threshold = 0.1 minfreq = 2
pass [1/2]..
- computing phrases..
- writing output..
pass [2/2]..
- computing phrases..
- writing output..
done.

real	0m0.255s
user	0m0.231s
sys	0m0.025s
```

```
(base) ye@administrator-HP-Z2-Tower-G4-Workstation:~/tool/word-seg-tool/python-wordsegment/wordsegment/y-test/ref/viterbi/dev4github/4release/syl-learning-exp$ for i in mama_wawa.txt.l{1..2}.t0.1.f{1..2}.seg;do echo -e "\n"$i":"; cat $i; done;

mama_wawa.txt.l1.t0.1.f1.seg:
မ_မ ဝ_ဝ ထ_ထ က
အ က_ပ ထ မ
က_ပါ က_ပါ မ_မ ရာ_ည ည လ_သာ သာ
ည_အ ခါ_ငါ စာ_ရ မ_မ ဝ_ဝ ထ_ထ က

mama_wawa.txt.l1.t0.1.f2.seg:
မ_မ ဝ_ဝ ထ_ထ က
အ က ပ ထ မ
က_ပါ က_ပါ မ_မ ရာ ည ည လ သာ သာ
ည အ ခါ ငါ စာ ရ မ_မ ဝ_ဝ ထ_ထ က

mama_wawa.txt.l2.t0.1.f1.seg:
မ_မ ဝ_ဝ_ထ_ထ က
အ_က_ပ ထ_မ
က_ပါ_က_ပါ မ_မ ရာ_ည_ည လ_သာ_သာ
ည_အ_ခါ_ငါ စာ_ရ_မ_မ ဝ_ဝ_ထ_ထ က

mama_wawa.txt.l2.t0.1.f2.seg:
မ_မ ဝ_ဝ_ထ_ထ က
အ က ပ ထ မ
က_ပါ က_ပါ မ_မ ရာ ည ည လ သာ သာ
ည အ ခါ ငါ စာ ရ မ_မ ဝ_ဝ_ထ_ထ က
```

--------------

```
(base) ye@administrator-HP-Z2-Tower-G4-Workstation:~/tool/word-seg-tool/python-wordsegment/wordsegment/y-test/ref/viterbi/dev4github/4release/syl-learning-exp$ time python ./myword.py npmi_train -lr "1,2" -tr "0.1,0.1" -fr "2,3" ./mama_wawa.txt
iters: 1, threshold:0.1, minfreq: 2, unigram.l1.t0.1.f2.txt, bigram.l1.t0.1.f2.txt, unigram.l1.t0.1.f2.bin, bigram.l1.t0.1.f2.bin, ./mama_wawa.txt, ./mama_wawa.txt.l1.t0.1.f2.seg
computing phrases: threshold = 0.1 minfreq = 2
pass [1/1]..
- computing phrases..
- writing output..
done.
iters: 2, threshold:0.1, minfreq: 2, unigram.l2.t0.1.f2.txt, bigram.l2.t0.1.f2.txt, unigram.l2.t0.1.f2.bin, bigram.l2.t0.1.f2.bin, ./mama_wawa.txt, ./mama_wawa.txt.l2.t0.1.f2.seg
computing phrases: threshold = 0.1 minfreq = 2
pass [1/2]..
- computing phrases..
- writing output..
pass [2/2]..
- computing phrases..
- writing output..
done.
iters: 1, threshold:0.1, minfreq: 3, unigram.l1.t0.1.f3.txt, bigram.l1.t0.1.f3.txt, unigram.l1.t0.1.f3.bin, bigram.l1.t0.1.f3.bin, ./mama_wawa.txt, ./mama_wawa.txt.l1.t0.1.f3.seg
computing phrases: threshold = 0.1 minfreq = 3
pass [1/1]..
- computing phrases..
- writing output..
done.
iters: 2, threshold:0.1, minfreq: 3, unigram.l2.t0.1.f3.txt, bigram.l2.t0.1.f3.txt, unigram.l2.t0.1.f3.bin, bigram.l2.t0.1.f3.bin, ./mama_wawa.txt, ./mama_wawa.txt.l2.t0.1.f3.seg
computing phrases: threshold = 0.1 minfreq = 3
pass [1/2]..
- computing phrases..
- writing output..
pass [2/2]..
- computing phrases..
- writing output..
done.

real	0m0.251s
user	0m0.231s
sys	0m0.020s
```

```
(base) ye@administrator-HP-Z2-Tower-G4-Workstation:~/tool/word-seg-tool/python-wordsegment/wordsegment/y-test/ref/viterbi/dev4github/4release/syl-learning-exp$ for i in mama_wawa.txt.l{1..2}.t0.1.f{2..3}.seg;do echo -e "\n"$i":"; cat $i; done;

mama_wawa.txt.l1.t0.1.f2.seg:
မ_မ ဝ_ဝ ထ_ထ က
အ က ပ ထ မ
က_ပါ က_ပါ မ_မ ရာ ည ည လ သာ သာ
ည အ ခါ ငါ စာ ရ မ_မ ဝ_ဝ ထ_ထ က

mama_wawa.txt.l1.t0.1.f3.seg:
မ_မ ဝ ဝ ထ ထ က
အ က ပ ထ မ
က ပါ က ပါ မ_မ ရာ ည ည လ သာ သာ
ည အ ခါ ငါ စာ ရ မ_မ ဝ ဝ ထ ထ က

mama_wawa.txt.l2.t0.1.f2.seg:
မ_မ ဝ_ဝ_ထ_ထ က
အ က ပ ထ မ
က_ပါ က_ပါ မ_မ ရာ ည ည လ သာ သာ
ည အ ခါ ငါ စာ ရ မ_မ ဝ_ဝ_ထ_ထ က

mama_wawa.txt.l2.t0.1.f3.seg:
မ_မ ဝ ဝ ထ ထ က
အ က ပ ထ မ
က ပါ က ပါ မ_မ ရာ ည ည လ သာ သာ
ည အ ခါ ငါ စာ ရ မ_မ ဝ ဝ ထ ထ က
(base) ye@administrator-HP-Z2-Tower-G4-Workstation:~/tool/word-seg-tool/python-wordsegment/wordsegment/y-test/ref/viterbi/dev4github/4release/syl-learning-exp$
```

--------------

```
(base) ye@administrator-HP-Z2-Tower-G4-Workstation:~/tool/word-seg-tool/python-wordsegment/wordsegment/y-test/ref/viterbi/dev4github/4release/syl-learning-exp$ time python ./myword.py npmi_train -lr "1,2" -tr "0.1,0.2" -fr "2,3" ./mama_wawa_poem.txt 
iters: 1, threshold:0.1, minfreq: 2, unigram.l1.t0.1.f2.txt, bigram.l1.t0.1.f2.txt, unigram.l1.t0.1.f2.bin, bigram.l1.t0.1.f2.bin, ./mama_wawa_poem.txt, ./mama_wawa_poem.txt.l1.t0.1.f2.seg
computing phrases: threshold = 0.1 minfreq = 2
pass [1/1]..
- computing phrases..
- writing output..
done.
iters: 2, threshold:0.1, minfreq: 2, unigram.l2.t0.1.f2.txt, bigram.l2.t0.1.f2.txt, unigram.l2.t0.1.f2.bin, bigram.l2.t0.1.f2.bin, ./mama_wawa_poem.txt, ./mama_wawa_poem.txt.l2.t0.1.f2.seg
computing phrases: threshold = 0.1 minfreq = 2
pass [1/2]..
- computing phrases..
- writing output..
pass [2/2]..
- computing phrases..
- writing output..
done.
iters: 1, threshold:0.1, minfreq: 3, unigram.l1.t0.1.f3.txt, bigram.l1.t0.1.f3.txt, unigram.l1.t0.1.f3.bin, bigram.l1.t0.1.f3.bin, ./mama_wawa_poem.txt, ./mama_wawa_poem.txt.l1.t0.1.f3.seg
computing phrases: threshold = 0.1 minfreq = 3
pass [1/1]..
- computing phrases..
- writing output..
done.
iters: 2, threshold:0.1, minfreq: 3, unigram.l2.t0.1.f3.txt, bigram.l2.t0.1.f3.txt, unigram.l2.t0.1.f3.bin, bigram.l2.t0.1.f3.bin, ./mama_wawa_poem.txt, ./mama_wawa_poem.txt.l2.t0.1.f3.seg
computing phrases: threshold = 0.1 minfreq = 3
pass [1/2]..
- computing phrases..
- writing output..
pass [2/2]..
- computing phrases..
- writing output..
done.
iters: 1, threshold:0.2, minfreq: 2, unigram.l1.t0.2.f2.txt, bigram.l1.t0.2.f2.txt, unigram.l1.t0.2.f2.bin, bigram.l1.t0.2.f2.bin, ./mama_wawa_poem.txt, ./mama_wawa_poem.txt.l1.t0.2.f2.seg
computing phrases: threshold = 0.2 minfreq = 2
pass [1/1]..
- computing phrases..
- writing output..
done.
iters: 2, threshold:0.2, minfreq: 2, unigram.l2.t0.2.f2.txt, bigram.l2.t0.2.f2.txt, unigram.l2.t0.2.f2.bin, bigram.l2.t0.2.f2.bin, ./mama_wawa_poem.txt, ./mama_wawa_poem.txt.l2.t0.2.f2.seg
computing phrases: threshold = 0.2 minfreq = 2
pass [1/2]..
- computing phrases..
- writing output..
pass [2/2]..
- computing phrases..
- writing output..
done.
iters: 1, threshold:0.2, minfreq: 3, unigram.l1.t0.2.f3.txt, bigram.l1.t0.2.f3.txt, unigram.l1.t0.2.f3.bin, bigram.l1.t0.2.f3.bin, ./mama_wawa_poem.txt, ./mama_wawa_poem.txt.l1.t0.2.f3.seg
computing phrases: threshold = 0.2 minfreq = 3
pass [1/1]..
- computing phrases..
- writing output..
done.
iters: 2, threshold:0.2, minfreq: 3, unigram.l2.t0.2.f3.txt, bigram.l2.t0.2.f3.txt, unigram.l2.t0.2.f3.bin, bigram.l2.t0.2.f3.bin, ./mama_wawa_poem.txt, ./mama_wawa_poem.txt.l2.t0.2.f3.seg
computing phrases: threshold = 0.2 minfreq = 3
pass [1/2]..
- computing phrases..
- writing output..
pass [2/2]..
- computing phrases..
- writing output..
done.

real	0m0.252s
user	0m0.220s
sys	0m0.032s
```

```
(base) ye@administrator-HP-Z2-Tower-G4-Workstation:~/tool/word-seg-tool/python-wordsegment/wordsegment/y-test/ref/viterbi/dev4github/4release/syl-learning-exp$ for i in mama_wawa_poem.txt.l{1..2}.t{0.1,0.2}.f{2..3}.seg;do echo -e "\n"$i":"; cat $i; done;

mama_wawa_poem.txt.l1.t0.1.f2.seg:
မ_မ ဝ_ဝ
ထ_ထ က
အ က ပ ထ မ ။
က_ပါ က_ပါ
မ_မ ရာ
ည ည လ သာ သာ
ည အ ခါ
ငါ စာ ရ
မ_မ ဝ_ဝ
ထ_ထ က ။

mama_wawa_poem.txt.l1.t0.1.f3.seg:
မ_မ ဝ ဝ
ထ ထ က
အ က ပ ထ မ ။
က ပါ က ပါ
မ_မ ရာ
ည ည လ သာ သာ
ည အ ခါ
ငါ စာ ရ
မ_မ ဝ ဝ
ထ ထ က ။

mama_wawa_poem.txt.l1.t0.2.f2.seg:
မ_မ ဝ_ဝ
ထ_ထ က
အ က ပ ထ မ ။
က_ပါ က_ပါ
မ_မ ရာ
ည ည လ သာ သာ
ည အ ခါ
ငါ စာ ရ
မ_မ ဝ_ဝ
ထ_ထ က ။

mama_wawa_poem.txt.l1.t0.2.f3.seg:
မ_မ ဝ ဝ
ထ ထ က
အ က ပ ထ မ ။
က ပါ က ပါ
မ_မ ရာ
ည ည လ သာ သာ
ည အ ခါ
ငါ စာ ရ
မ_မ ဝ ဝ
ထ ထ က ။

mama_wawa_poem.txt.l2.t0.1.f2.seg:
မ_မ_ဝ_ဝ
ထ_ထ_က
အ က ပ ထ မ ။
က_ပါ က_ပါ
မ_မ ရာ
ည ည လ သာ သာ
ည အ ခါ
ငါ စာ ရ
မ_မ_ဝ_ဝ
ထ_ထ_က ။

mama_wawa_poem.txt.l2.t0.1.f3.seg:
မ_မ ဝ ဝ
ထ ထ က
အ က ပ ထ မ ။
က ပါ က ပါ
မ_မ ရာ
ည ည လ သာ သာ
ည အ ခါ
ငါ စာ ရ
မ_မ ဝ ဝ
ထ ထ က ။

mama_wawa_poem.txt.l2.t0.2.f2.seg:
မ_မ_ဝ_ဝ
ထ_ထ_က
အ က ပ ထ မ ။
က_ပါ က_ပါ
မ_မ ရာ
ည ည လ သာ သာ
ည အ ခါ
ငါ စာ ရ
မ_မ_ဝ_ဝ
ထ_ထ_က ။

mama_wawa_poem.txt.l2.t0.2.f3.seg:
မ_မ ဝ ဝ
ထ ထ က
အ က ပ ထ မ ။
က ပါ က ပါ
မ_မ ရာ
ည ည လ သာ သာ
ည အ ခါ
ငါ စာ ရ
မ_မ ဝ ဝ
ထ ထ က ။
```

ဒေတာကလည်း တအားနည်းလို့... Threshold ကို မကစားပဲ လုပ်ထားတာကို ကြည့်ရတာက ပိုမြင်သာနိုင်လို့ အဲဒါကိုပဲ GitHub မှာ npmi_train ဆိုတာကို ရှင်းပြတဲ့အခါမှာ သုံးတော့မယ်။

```
(base) ye@administrator-HP-Z2-Tower-G4-Workstation:~/tool/word-seg-tool/python-wordsegment/wordsegment/y-test/ref/viterbi/dev4github/4release/syl-learning-exp$ time python ./myword.py npmi_train -lr "1,2" -tr "0.1,0.1" -fr "2,3" ./mama_wawa_poem.txt 
iters: 1, threshold:0.1, minfreq: 2, unigram.l1.t0.1.f2.txt, bigram.l1.t0.1.f2.txt, unigram.l1.t0.1.f2.bin, bigram.l1.t0.1.f2.bin, ./mama_wawa_poem.txt, ./mama_wawa_poem.txt.l1.t0.1.f2.seg
computing phrases: threshold = 0.1 minfreq = 2
pass [1/1]..
- computing phrases..
- writing output..
done.
iters: 2, threshold:0.1, minfreq: 2, unigram.l2.t0.1.f2.txt, bigram.l2.t0.1.f2.txt, unigram.l2.t0.1.f2.bin, bigram.l2.t0.1.f2.bin, ./mama_wawa_poem.txt, ./mama_wawa_poem.txt.l2.t0.1.f2.seg
computing phrases: threshold = 0.1 minfreq = 2
pass [1/2]..
- computing phrases..
- writing output..
pass [2/2]..
- computing phrases..
- writing output..
done.
iters: 1, threshold:0.1, minfreq: 3, unigram.l1.t0.1.f3.txt, bigram.l1.t0.1.f3.txt, unigram.l1.t0.1.f3.bin, bigram.l1.t0.1.f3.bin, ./mama_wawa_poem.txt, ./mama_wawa_poem.txt.l1.t0.1.f3.seg
computing phrases: threshold = 0.1 minfreq = 3
pass [1/1]..
- computing phrases..
- writing output..
done.
iters: 2, threshold:0.1, minfreq: 3, unigram.l2.t0.1.f3.txt, bigram.l2.t0.1.f3.txt, unigram.l2.t0.1.f3.bin, bigram.l2.t0.1.f3.bin, ./mama_wawa_poem.txt, ./mama_wawa_poem.txt.l2.t0.1.f3.seg
computing phrases: threshold = 0.1 minfreq = 3
pass [1/2]..
- computing phrases..
- writing output..
pass [2/2]..
- computing phrases..
- writing output..
done.

real	0m0.297s
user	0m0.268s
sys	0m0.029s
```

```
(base) ye@administrator-HP-Z2-Tower-G4-Workstation:~/tool/word-seg-tool/python-wordsegment/wordsegment/y-test/ref/viterbi/dev4github/4release/syl-learning-exp$ for i in mama_wawa_poem.txt.l{1..2}.t0.1.f{2..3}.seg;do echo -e "\n"$i":"; cat $i; done;

mama_wawa_poem.txt.l1.t0.1.f2.seg:
မ_မ ဝ_ဝ
ထ_ထ က
အ က ပ ထ မ ။
က_ပါ က_ပါ
မ_မ ရာ
ည ည လ သာ သာ
ည အ ခါ
ငါ စာ ရ
မ_မ ဝ_ဝ
ထ_ထ က ။

mama_wawa_poem.txt.l1.t0.1.f3.seg:
မ_မ ဝ ဝ
ထ ထ က
အ က ပ ထ မ ။
က ပါ က ပါ
မ_မ ရာ
ည ည လ သာ သာ
ည အ ခါ
ငါ စာ ရ
မ_မ ဝ ဝ
ထ ထ က ။

mama_wawa_poem.txt.l2.t0.1.f2.seg:
မ_မ_ဝ_ဝ
ထ_ထ_က
အ က ပ ထ မ ။
က_ပါ က_ပါ
မ_မ ရာ
ည ည လ သာ သာ
ည အ ခါ
ငါ စာ ရ
မ_မ_ဝ_ဝ
ထ_ထ_က ။

mama_wawa_poem.txt.l2.t0.1.f3.seg:
မ_မ ဝ ဝ
ထ ထ က
အ က ပ ထ မ ။
က ပါ က ပါ
မ_မ ရာ
ည ည လ သာ သာ
ည အ ခါ
ငါ စာ ရ
မ_မ ဝ ဝ
ထ ထ က ။
(base) ye@administrator-HP-Z2-Tower-G4-Workstation:~/tool/word-seg-tool/python-wordsegment/wordsegment/y-test/ref/viterbi/dev4github/4release/syl-learning-exp$ 
```

I hope you enjoyed...  
The End of "မမ ဝဝ experiment". :P  
