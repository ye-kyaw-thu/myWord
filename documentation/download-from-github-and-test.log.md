# Download from GitHub and Testing Log

Run by Ye @LST  
Date: 10 Sept 2021  

## Unzip

```
(base) ye@administrator-HP-Z2-Tower-G4-Workstation:/media/ye/SP PHD U3/test-myWord$ unzip ./myWord-main.zip 
Archive:  ./myWord-main.zip
e6903cd57c627e35600f75b6cd1bb8f722644fa5
   creating: myWord-main/
  inflating: myWord-main/LICENSE     
  inflating: myWord-main/README.md   
  inflating: myWord-main/combine-all-splitted-files.sh  
   creating: myWord-main/dict_ver1/
  inflating: myWord-main/dict_ver1/README.md  
  inflating: myWord-main/dict_ver1/bigram-phrase.bin.small.aa  
  inflating: myWord-main/dict_ver1/bigram-phrase.bin.small.ab  
  inflating: myWord-main/dict_ver1/bigram-phrase.bin.small.ac  
  inflating: myWord-main/dict_ver1/bigram-phrase.bin.small.ad  
  inflating: myWord-main/dict_ver1/bigram-phrase.bin.small.ae  
  inflating: myWord-main/dict_ver1/bigram-phrase.bin.small.af  
  inflating: myWord-main/dict_ver1/bigram-phrase.txt.small.aa  
  inflating: myWord-main/dict_ver1/bigram-phrase.txt.small.ab  
  inflating: myWord-main/dict_ver1/bigram-phrase.txt.small.ac  
  inflating: myWord-main/dict_ver1/bigram-phrase.txt.small.ad  
  inflating: myWord-main/dict_ver1/bigram-phrase.txt.small.ae  
  inflating: myWord-main/dict_ver1/bigram-word.bin.small.aa  
  inflating: myWord-main/dict_ver1/bigram-word.bin.small.ab  
  inflating: myWord-main/dict_ver1/bigram-word.bin.small.ac  
  inflating: myWord-main/dict_ver1/bigram-word.txt.small.aa  
  inflating: myWord-main/dict_ver1/bigram-word.txt.small.ab  
  inflating: myWord-main/dict_ver1/bigram-word.txt.small.ac  
  inflating: myWord-main/dict_ver1/combine-all-splitted-files.sh  
  inflating: myWord-main/dict_ver1/split-lt-24mb.sh  
  inflating: myWord-main/dict_ver1/unigram-phrase.bin  
  inflating: myWord-main/dict_ver1/unigram-phrase.txt  
  inflating: myWord-main/dict_ver1/unigram-word.bin  
  inflating: myWord-main/dict_ver1/unigram-word.txt  
   creating: myWord-main/documentation/
  inflating: myWord-main/documentation/command-line-help-of-myword.md  
   creating: myWord-main/documentation/fig/
  inflating: myWord-main/documentation/fig/formula-6.png  
  inflating: myWord-main/documentation/fig/lexicon.pdf  
  inflating: myWord-main/documentation/fig/lexicon.png  
  inflating: myWord-main/documentation/fig/sayarka.pdf  
  inflating: myWord-main/documentation/fig/sayarka.png  
  inflating: myWord-main/documentation/fig/segment2.pdf  
  inflating: myWord-main/documentation/fig/segment2.png  
  inflating: myWord-main/documentation/mama_wawa-exp1.md  
  inflating: myWord-main/documentation/npmi-word-segmentation-experiment1.md  
  inflating: myWord-main/documentation/npmi_train-option-test-with-1k-corpus.md  
  inflating: myWord-main/myword.py   
  inflating: myWord-main/phrase_segment.py  
  inflating: myWord-main/syl_segment.py  
  inflating: myWord-main/test1.txt   
  inflating: myWord-main/test2.txt   
  inflating: myWord-main/word_dict.py  
  inflating: myWord-main/word_segment.py  
(base) ye@administrator-HP-Z2-Tower-G4-Workstation:/media/ye/SP PHD U3/test-myWord$
```
## Testing for Syllable Segmentation

```
(base) ye@administrator-HP-Z2-Tower-G4-Workstation:/media/ye/SP PHD U3/test-myWord/myWord-main$ ls
combine-all-splitted-files.sh  documentation  myword.py          README.md       test1.txt  word_dict.py
dict_ver1                      LICENSE        phrase_segment.py  syl_segment.py  test2.txt  word_segment.py
(base) ye@administrator-HP-Z2-Tower-G4-Workstation:/media/ye/SP PHD U3/test-myWord/myWord-main$ tree
.
├── combine-all-splitted-files.sh
├── dict_ver1
│   ├── bigram-phrase.bin.small.aa
│   ├── bigram-phrase.bin.small.ab
│   ├── bigram-phrase.bin.small.ac
│   ├── bigram-phrase.bin.small.ad
│   ├── bigram-phrase.bin.small.ae
│   ├── bigram-phrase.bin.small.af
│   ├── bigram-phrase.txt.small.aa
│   ├── bigram-phrase.txt.small.ab
│   ├── bigram-phrase.txt.small.ac
│   ├── bigram-phrase.txt.small.ad
│   ├── bigram-phrase.txt.small.ae
│   ├── bigram-word.bin.small.aa
│   ├── bigram-word.bin.small.ab
│   ├── bigram-word.bin.small.ac
│   ├── bigram-word.txt.small.aa
│   ├── bigram-word.txt.small.ab
│   ├── bigram-word.txt.small.ac
│   ├── combine-all-splitted-files.sh
│   ├── README.md
│   ├── split-lt-24mb.sh
│   ├── unigram-phrase.bin
│   ├── unigram-phrase.txt
│   ├── unigram-word.bin
│   └── unigram-word.txt
├── documentation
│   ├── command-line-help-of-myword.md
│   ├── fig
│   │   ├── formula-6.png
│   │   ├── lexicon.pdf
│   │   ├── lexicon.png
│   │   ├── sayarka.pdf
│   │   ├── sayarka.png
│   │   ├── segment2.pdf
│   │   └── segment2.png
│   ├── mama_wawa-exp1.md
│   ├── npmi_train-option-test-with-1k-corpus.md
│   └── npmi-word-segmentation-experiment1.md
├── LICENSE
├── myword.py
├── phrase_segment.py
├── README.md
├── syl_segment.py
├── test1.txt
├── test2.txt
├── word_dict.py
└── word_segment.py

3 directories, 45 files
(base) ye@administrator-HP-Z2-Tower-G4-Workstation:/media/ye/SP PHD U3/test-myWord/myWord-main$
```

```
(base) ye@administrator-HP-Z2-Tower-G4-Workstation:/media/ye/SP PHD U3/test-myWord/myWord-main$ python ./myword.py -h
usage: myword [-h] [-v]
              {syllable,build_dict,word,train_phrase,phrase,npmi_train} ...

Syllable, Word, Phrase Segmenter for Burmese (Myanmar language)

positional arguments:
  {syllable,build_dict,word,train_phrase,phrase,npmi_train}
    syllable            syllable segmentation with Regular Expression
    build_dict          building n-gram dictionaries for word segmentation
    word                word segmentation with Vitabi algorithm proposed by
                        Andrew James Viterbi, 1967
    train_phrase        training or building n-gram dictionaries for phrase
                        segmentation
    phrase              phrase segmentation with NPMI (Normalized Pointwise
                        Mutual Information) proposed by Bouma Gerlof, 2009
    npmi_train          training or building n-gram dictionaries with NPMI and
                        run segmentation experiment for x-unit (e.g.
                        character, syllable, sub_word, word) with built
                        dictionaries, the learning x-unit will depends on your
                        input file segmentation

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         output version information and exit
  ```
  
 ```
(base) ye@administrator-HP-Z2-Tower-G4-Workstation:/media/ye/SP PHD U3/test-myWord/myWord-main$ python ./myword.py syllable -d "|" ./test1.txt ./test1.syllable
(base) ye@administrator-HP-Z2-Tower-G4-Workstation:/media/ye/SP PHD U3/test-myWord/myWord-main$ cat ./test1.syllable 
ကျွန်|တော်|က|သု|တေ|သ|န|သ|မား|ပါ|။
နေ့|ရော|ည|ရော|မြန်|မာ|စာ|နဲ့|ကွန်|ပျူ|တာ|နဲ့|ပဲ|အ|လုပ်|များ|ပါ|တယ်
မင်း|က|ကော|ဘာ|အ|လုပ်|လုပ်|တာ|လဲ|။
ပြော|ပြ|ပါ|အုံး
ကော|ဖီ|လည်း|ထပ်|သောက်|ချင်|ရင်|ပြော|ကွာ
မန္တ|လေး|မှာ|ဒေါ်|အောင်|ဆန်း|စု|ကြည်|မိန့်|ခွန်း|ပြော|မယ်|တဲ့|။
(base) ye@administrator-HP-Z2-Tower-G4-Workstation:/media/ye/SP PHD U3/test-myWord/myWord-main$
```

OK!!!

## Testing for Word Segmentation

```
(base) ye@administrator-HP-Z2-Tower-G4-Workstation:/media/ye/SP PHD U3/test-myWord/myWord-main$ python ./myword.py word ./test1.txt ./test1.word
Dictionary file ./dict_ver1/bigram-word.bin  not found!
Traceback (most recent call last):
  File "./myword.py", line 235, in <module>
    main ()
  File "./myword.py", line 157, in main
    wseg.P_bigram = wseg.ProbDist(bi_dict_bin, False)
  File "/media/ye/SP PHD U3/test-myWord/myWord-main/word_segment.py", line 46, in __init__
    data = read_dict(datafile)
  File "/media/ye/SP PHD U3/test-myWord/myWord-main/word_segment.py", line 38, in read_dict
    return dictionary
UnboundLocalError: local variable 'dictionary' referenced before assignment
(base) ye@administrator-HP-Z2-Tower-G4-Workstation:/media/ye/SP PHD U3/test-myWord/myWord-main$

Yes, I have to combine all small dictionaries!!!
```

```
(base) ye@administrator-HP-Z2-Tower-G4-Workstation:/media/ye/SP PHD U3/test-myWord/myWord-main$ cd dict_ver1/
(base) ye@administrator-HP-Z2-Tower-G4-Workstation:/media/ye/SP PHD U3/test-myWord/myWord-main/dict_ver1$ ./combine-all-splitted-files.sh 
(base) ye@administrator-HP-Z2-Tower-G4-Workstation:/media/ye/SP PHD U3/test-myWord/myWord-main/dict_ver1$ ls
bigram-phrase.bin  bigram-word.bin  combine-all-splitted-files.sh  split-lt-24mb.sh    unigram-phrase.txt  unigram-word.txt
bigram-phrase.txt  bigram-word.txt  README.md                      unigram-phrase.bin  unigram-word.bin
(base) ye@administrator-HP-Z2-Tower-G4-Workstation:/media/ye/SP PHD U3/test-myWord/myWord-main/dict_ver1$
```

```
(base) ye@administrator-HP-Z2-Tower-G4-Workstation:/media/ye/SP PHD U3/test-myWord/myWord-main$ time python ./myword.py word -d "|" ./test1.txt ./test1.word

real	0m1.307s
user	0m1.131s
sys	0m0.177s
(base) ye@administrator-HP-Z2-Tower-G4-Workstation:/media/ye/SP PHD U3/test-myWord/myWord-main$ cat ./test1.word 
ကျွန်တော်|က|သုတေသန|သမား|ပါ|။
နေ့|ရော|ည|ရော|မြန်မာ|စာ|နဲ့|ကွန်ပျူတာ|နဲ့|ပဲ|အလုပ်|များ|ပါ|တယ်
မင်း|က|ကော|ဘာ|အလုပ်|လုပ်|တာ|လဲ|။
ပြော|ပြ|ပါ|အုံး
ကောဖီ|လည်း|ထပ်|သောက်|ချင်|ရင်|ပြော|ကွာ
မန္တလေး|မှာ|ဒေါ်အောင်ဆန်းစုကြည်|မိန့်ခွန်း|ပြော|မယ်|တဲ့|။
```

```
(base) ye@administrator-HP-Z2-Tower-G4-Workstation:/media/ye/SP PHD U3/test-myWord/myWord-main$ time python ./myword.py word ./test1.txt ./test1.word

real	0m1.308s
user	0m1.164s
sys	0m0.145s
(base) ye@administrator-HP-Z2-Tower-G4-Workstation:/media/ye/SP PHD U3/test-myWord/myWord-main$ cat ./test1.word 
ကျွန်တော် က သုတေသန သမား ပါ ။
နေ့ ရော ည ရော မြန်မာ စာ နဲ့ ကွန်ပျူတာ နဲ့ ပဲ အလုပ် များ ပါ တယ်
မင်း က ကော ဘာ အလုပ် လုပ် တာ လဲ ။
ပြော ပြ ပါ အုံး
ကောဖီ လည်း ထပ် သောက် ချင် ရင် ပြော ကွာ
မန္တလေး မှာ ဒေါ်အောင်ဆန်းစုကြည် မိန့်ခွန်း ပြော မယ် တဲ့ ။
(base) ye@administrator-HP-Z2-Tower-G4-Workstation:/media/ye/SP PHD U3/test-myWord/myWord-main$ 
```

OK!!!

## Testing for Phrase Segmentation

```
(base) ye@administrator-HP-Z2-Tower-G4-Workstation:/media/ye/SP PHD U3/test-myWord/myWord-main$ time python ./myword.py phrase ./test1.word ./test1.phrase
{'command': 'phrase', 'threshold': 0.1, 'minfreq': 3, 'unigram_phrase_bin': './dict_ver1/unigram-phrase.bin', 'bigram_phrase_bin': './dict_ver1/bigram-phrase.bin', 'input': './test1.word', 'output': './test1.phrase'}
computing phrases: threshold = 0.1 minfreq = 3
phrase segmentation...
- read unigram dictionary
- read bigram dictionary
- computing phrases..
- writing output..., filename:  ./test1.phrase
done.

real	0m4.228s
user	0m3.976s
sys	0m0.252s
```

```
(base) ye@administrator-HP-Z2-Tower-G4-Workstation:/media/ye/SP PHD U3/test-myWord/myWord-main$ cat ./test1.phrase 
ကျွန်တော် က သုတေသန သမား ပါ ။
နေ့_ရော ည ရော_မြန်မာ စာ နဲ့ ကွန်ပျူတာ နဲ့ ပဲ အလုပ်_များ ပါ တယ်
မင်း က ကော ဘာ အလုပ် လုပ် တာ လဲ ။
ပြော ပြ ပါ အုံး
ကောဖီ လည်း ထပ် သောက် ချင် ရင် ပြော ကွာ
မန္တလေး မှာ_ဒေါ်အောင်ဆန်းစုကြည် မိန့်ခွန်း ပြော_မယ် တဲ့ ။
```

```
(base) ye@administrator-HP-Z2-Tower-G4-Workstation:/media/ye/SP PHD U3/test-myWord/myWord-main$ time python ./myword.py phrase -t 0.1 -f 1 ./test1.word ./test1.phrase
{'command': 'phrase', 'threshold': 0.1, 'minfreq': 1, 'unigram_phrase_bin': './dict_ver1/unigram-phrase.bin', 'bigram_phrase_bin': './dict_ver1/bigram-phrase.bin', 'input': './test1.word', 'output': './test1.phrase'}
computing phrases: threshold = 0.1 minfreq = 1
phrase segmentation...
- read unigram dictionary
- read bigram dictionary
- computing phrases..
- writing output..., filename:  ./test1.phrase
done.

real	0m13.355s
user	0m13.033s
sys	0m0.320s
```

```
(base) ye@administrator-HP-Z2-Tower-G4-Workstation:/media/ye/SP PHD U3/test-myWord/myWord-main$ cat ./test1.phrase 
ကျွန်တော် က သုတေသန သမား ပါ ။
နေ့_ရော ည ရော_မြန်မာ စာ နဲ့ ကွန်ပျူတာ နဲ့ ပဲ အလုပ်_များ ပါ တယ်
မင်း က ကော ဘာ အလုပ် လုပ် တာ လဲ ။
ပြော ပြ ပါ အုံး
ကောဖီ လည်း ထပ် သောက် ချင် ရင် ပြော ကွာ
မန္တလေး မှာ_ဒေါ်အောင်ဆန်းစုကြည် မိန့်ခွန်း ပြော_မယ် တဲ့ ။
(base) ye@administrator-HP-Z2-Tower-G4-Workstation:/media/ye/SP PHD U3/test-myWord/myWord-main$ 
```

```
(base) ye@administrator-HP-Z2-Tower-G4-Workstation:/media/ye/SP PHD U3/test-myWord/myWord-main$ time python ./myword.py phrase -t 0.1 -f 1 ./test2.txt ./test2.phrase
{'command': 'phrase', 'threshold': 0.1, 'minfreq': 1, 'unigram_phrase_bin': './dict_ver1/unigram-phrase.bin', 'bigram_phrase_bin': './dict_ver1/bigram-phrase.bin', 'input': './test2.txt', 'output': './test2.phrase'}
computing phrases: threshold = 0.1 minfreq = 1
phrase segmentation...
- read unigram dictionary
- read bigram dictionary
- computing phrases..
- writing output..., filename:  ./test2.phrase
done.

real	0m13.460s
user	0m13.169s
sys	0m0.280s
```

```
(base) ye@administrator-HP-Z2-Tower-G4-Workstation:/media/ye/SP PHD U3/test-myWord/myWord-main$ cat ./test2.phrase 
တစ် နေ့ က ကျွန်တော် အိမ် ပြန် သွား ချိန် တွင် အဖေ နှင့် သူ့ မိန်းမ ရန် ဖြစ် နေ သည်_ကို တွေ့ ရ လေ သည်_။
သစ်သီး ဖျော်ရည် ၊_မစ်ရှိတ် ၊ ကော်ဖီ နဲ့_လက်ဖက်ရည် ရှိ ပါ တယ် ။
မြန်မာ တပ်မတော် နဲ့ ရက္ခိုင့် တပ်မတော် ( အေအေ )_တို့ အကြား တိုက်ပွဲ တွေ ဟာ ရခိုင် ပြည်နယ် ၊ ဘူးသီးတောင် မြို့နယ် မှာ သာ မက ချင်း_ပြည်နယ် ၊ ပလက်ဝ မြို့နယ် တဝိုက် မှာ လည်း ဆက်လက် ဖြစ် သွား နေ ပြီး_ဒေသခံ တွေ ဟာ နေရပ် စွန့်ခွာ နေ ရ ပြီး ဒုက္ခသည် စခန်း တွေ မှာ ခိုလှုံ နေ ရ ပါ တယ် ။
အမှု_၂၇၈၈ မှု တရားခံ ၄၃၄၉ ဦး_ဖမ်းဆီးရမိခဲ့ သည် ဟု ပြည်ထောင်စု ဝန်ကြီး_က တင်ပြ သည်_။
ရဃုပတိ က ပြော လေ သည်_။
ဤ ကြေကြား ချက် မှာ က ကျွန်တော် တို့ အတွက် ဟာသ ဖြစ်_သည် ။
ကိုယ်တိုင် ယူ ရ တဲ့_စတိုးဆိုင် နဲ့ ရိုးရာ_ဆိုင် မင်း ဘယ် ဟာ ကို ပို ကြိုက်_လဲ
ဝေးလံ_ဒေသ များ နှင့် အထူး လိုအပ် ချက် ရှိ သော ဒေသ များ_ရှိ ပညာ ရေး နယ်ပယ် များ တွင် ပညာ သင်ကြား နိုင် ရန်_အတွက် အထူး စီမံချက် များ လုပ်ဆောင် ပေး_၍ ပညာ ရေး ရံပုံငွေ_များ ပိုမို တိုးမြှင့် ပေး ရ မည် ။
ထို့အပြင် မြန်မာ နိုင်ငံ အမျိုးသား အဆင့် စွန့်ပစ်ပစ္စည်း စီမံ ခန့်ခွဲ မှု_မဟာ ဗျူဟာ နှင့် ပင်မ လုပ်ငန်း အစီအစဉ် ( ၂၀၁၈ - ၂၀၃၀ ) ကို လည်း ရေးဆွဲ ပြီး ဖြစ် သည့် အတွက် မကြာမီ ထုတ်ပြန်_သွား မည် ဖြစ် ပါ ကြောင်း ။
အော် မ ငို_ပါ နဲ့ ။
ဖောက် ဖျောက်
သာဒီးလူ သီချင်း_က ဘာ တဲ့ သူခိုး တက် တော့ ဆူ တယ် အမျိုးဖျက် တော့ ပူ တယ် မဟုတ်မဟတ် ပြော တတ် တဲ့ စကား မ_လှပ တယ် နင် ဟာ အလိမ်အညာ များ ထဲ က တစ် ယောက်_တော့ ဖြစ် နေ_မလား
နိန္ဒ_က သမိန်ဓမ္မ ကို ဝင် ၍ ကူ_သည် ။
ကားဘီး တွေ မှာ ရွှံ့ ပေ လို့ စိတ်ညစ် ကြ တယ် ။
ကိုယ့် ကို ကိုယ် တောင် နားမလည် နိုင် ပါ ဘူး
သင့် ရဲ့ တစ် နေ့ တာ လုံး မှာ စိတ် ခွန်အား အပြည့် ၊ စိတ် တည်တည်ငြိမ်ငြိမ် ရှိ နေ စေ ဖို့ အတွက်_ဘုရား ဝတ်ပြု တာ ၊ တရား ရှုမှတ် တာ_တွေ က ကူညီ ပေး နိုင် ပါ တယ် ။
သမိုင်း_ရေး အယူအဆ တင် မ ဟုတ် ပါ ဘူး ။
ပြည်ခိုင်ဖြိုး ပါတီ က တစ်ဦး_ဦး ပြဿနာ ရှိ လာ ရင် သူ က ပါတီ က_နေ ထွက်_တာ ကြာ ပြီ တဲ့ ။
ငါ ဆိုလို တာ က တစ် မျိုး ပါ ၊ သူ ရုတ်တရက် စကား_ဖြတ် ပြီး ထွက် သွား ပုံ_က တစ်မျိုးကြီး ပဲ
မြွေဟောက် ကြီး_၏ ခေါင်းပိုင်း ကား မ လှုပ် နိုင် တော့ ။
အင်း လေ ၊ ဒါကြောင့် အင်းလျားလိတ် မှာ နှစ် လ နေ ကြ ဖို့ စီစဉ်_ရ တာ ပေါ့ ။
ဂယ်ရီကာဟေးလ် သည်_ချယ်လ်ဆီး အသင်း ခေါင်းဆောင် အဖြစ် ကစား ခဲ့ ရ_သော်လည်း နည်းပြ ဆာရီ လက်ထက် တွင် ပုံမှန်ပွဲ ကစား ခွင့် ပျောက်ဆုံး ခဲ့ ပြီး ၂၀၁၈ - ၁၉ တစ်ရာသီ_လုံး တွင် ပရီးမီးယား လိဂ်ပွဲစဉ် (၂_) ပွဲ အပါအဝင် ပြိုင်ပွဲ စုံ ( ၈ ) ပွဲ သာ ကစား ခွင့် ရရှိ ခဲ့ သည်_။
စိန်တစ်လုံး သရက် တွေ လည်း သီး လို့ သံပုရာသီး တွေ လည်း ဝေ လို့ နေ_ချင် စဖွယ် ယာတဲ_လေး ဖြစ် လာ_ပါ တယ် ။
လူ တွေ ဘတ်စ်ကား ပေါ် တိုးဝှေ့ တက် ပြီး ကား ထွက် သွား လေ သည်_။
ဖြစ် မှ ကု_တာ ထက်_မ ဖြစ် ခင် ကျန်းမာ ရေး နဲ့ ညီညွတ် တဲ့ အနေအထိုင် အစားအသောက် ဒါ တွေ က အရေးကြီး ပါ တယ် ။
ကား ထဲ မှာ_ကျွန်တော် တို့ အတွက်_နေရာ ရှိ_လား ။
သူ ပျင်း_တယ် နော် ၊ မ ပျင်း ဘူး လား ။
ပြော သာ ပြော ရ တယ် ဘာ မှ လည်း အရေး မ ယူ ကြ ဘူး လေ အဲ့ဒါ ကြောင့် အပြစ် လုပ်_တဲ့ သူ တွေ က ၆ ရေး တောင် မ လုပ် ဘူး
စက်မှု တိုင်း ( ၁ ) ၊ ဆည်မြောင်း နှင့် ရေ အသုံး ချ မှု စီမံ ခန့်ခွဲ ရေး_ဦးစီးဌာန
သူ ကြည့် ကောင်း မလား ။
(base) ye@administrator-HP-Z2-Tower-G4-Workstation:/media/ye/SP PHD U3/test-myWord/myWord-main$ 
```


