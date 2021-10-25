# 𝗆𝔂𝕎◐ℝ𝗗 Segmentation Tool

syllable, word, sub_word and phrase segmenter for Burmese (Myanmar language)  

- [Introduction](#Introduction)  
  - [Features](#Features)   
- [Rule: Syllable Segmentation with Regular Expression](#Rule-Syllable-Segmentation-with-Regular-Expression)  
- [Syllable Segmentation with "myWord" Segmentation Tool](#Syllable-Segmentation-with-myWord-Segmentation-Tool)  
- [Theory: Word Segmentation with Viterbi Algorithm](#Theory-Word-Segmentation-with-Viterbi-Algorithm)  
- [Building Unigram, Bigram Dictionaries for Word Unit](#Building-Unigram-Bigram-Dictionaries-for-Word-Unit)  
- [Word Segmentation with "myWord" Segmentation Tool](#Word-Segmentation-with-myWord-Segmentation-Tool)  
- [Theory: Unsupervised Phrase Segmentation with NPMI](#Theory-Unsupervised-Phrase-Segmentation-with-NPMI)  
- [Phrase Segmentation with "myWord" Segmentation Tool](#Phrase-Segmentation-with-myWord-Segmentation-Tool)  
- [Command-line Help](#Command-line-Help)  
- [Introduction to "npmi_train" Option](#Introduction-to-npmi_train-Option)  
- [Dictionaries for Word and Phrase Segmentation](#Dictionaries-for-Word-and-Phrase-Segmentation)  
  - [for Word Segmentation](#for-Word-Segmentation) 
  - [for Phrase Segmentation](#for-Phrase-Segmentation)
- [Files and Folder Information](#Files-and-Folder-Information)
- [Evaluation of myWord for "Word Segmentation"](#Evaluation-of-myWord-for-Word-Segmentation)  
  - [Closed Test](#Closed-Test)  
  - [Open Test](#Open-Test)  
- [Commands of myWord Segmentation Tool](#Commands-of-myWord-Segmentation-Tool)  
- [Contributors](#Contributors)  
- [To Do](#To-Do)  
- [License](#License)  
- [Citation](#Citation)  
- [Reference](#Reference)  

## Introduction

မြန်မာစာ စာလုံးတွေကို ပေါ့ပေါ့ပါးပါးနဲ့ မြန်မြန်ဆန်ဆန် ဖြတ်ပေးနိုင်ပြီး၊ library တွေ အများကြီးကိုလည်း မှီမနေပဲ Developer တွေက လွယ်လွယ်ကူကူ embedding လုပ်နိုင်ပြီးတော့ ကိုယ့်ဒေတာနဲ့ကိုယ်လည်း extend လုပ်နိုင်တဲ့ word segmentation tool က ဒီနေ့အထိ မရှိသေးဘူးလို့ နားလည်ထားတယ်။ အဲဒီ ကွက်လပ်ကိုဖြည့်နိုင်ဖို့ရည်ရွယ်ပြီးတော့ myWord ကို R&D လုပ်ခဲ့ပြီး release လုပ်ပေးလိုက်ပါတယ်။  

myWord Segmentation Tool ကို သုံးပြီးတော့ မြန်မာစာကြောင်းတွေကို "syllable unit", "sub_word", "word unit", "phrase unit" တွေ အဖြစ် ဖြတ်ပေးတဲ့ ပရိုဂရမ်ပါ။ NLP preprocessing/post-editing အလုပ်တွေ၊ မြန်မာစာနဲ့ ပတ်သက်တဲ့ ဒေတာတွေကို စာလုံးဖြတ်ပြီး model ဆောက်ဖို့အတွက် အသုံးဝင်ပါလိမ့်မယ်။  

### Features:

myWord Segmentation Tool က အဓိက လုပ်ပေးနိုင်တဲ့ အချက်တွေကိုတော့ အင်္ဂလိပ်လိုပဲ ချရေးပေးလိုက်တယ်။  

- Written with Python programming (so... you can hack easily)  
- Used unigram, bigram dictionaries built with "manually segmented twelve million words" training corpus (myWord Corpus Ver. 1.0)
- Yes, myWord supports "syllable", "sub_word", "word" and "phrase" segmentation
- Of course, you can train or build unigram, bigram dictionaries with your segmented corpus
- By default, running word segmentation with Viterbi Algorithm
- By default, running phrase segmentation with NPMI (Normalized Pointwise Mutual Information) Algorithm
- Shared Burmese unigram, bigram dictionaries with MIT License

## Rule: Syllable Segmentation with Regular Expression

မြန်မာစာအတွက် syllable segmentation က အရေးကြီးတဲ့ word segmentation unit တစ်ခုပါ။ အထူးသဖြင့် ဒေတာက ကောင်းကောင်းမရှိတာကြောင့်ရော၊ ငြိမ်တဲ့ word segmenter က မရှိတာကြောင့်ရော Machine Translation သုတေသနမှာဆိုရင် syllable segmentation ဖြတ်ပြီးတော့ ဘာသာပြန်တာက word segmentation လုပ်ပြီး training လုပ်တာထက်တောင် ရလဒ်တွေက ပိုကောင်းနိုင်ကြောင်းကို စာတမ်းတွေရေးပြီးလည်း သက်သေပြခဲ့ပြီးပါပြီ။ myWord Segmentation Tool မှာလည်း syllable breaking လုပ်ပေးတဲ့ option ကိုထည့်ထားပါတယ်။  

Syllable breaking ကိုလည်း Finite State Model ဆောက်ပြီးဖြတ်တာမျိုး၊ syllable list အဘိဓာန်ဆောက်ပြီး ဖြတ်တာမျိုး စသည်ဖြင့် approach အမျိုးမျိုးနဲ့ သွားလို့ရပေမဲ့ 2014 လောက်မှာ propose လုပ်ခဲ့တဲ့ sylbreak [(Link: https://github.com/ye-kyaw-thu/sylbreak)](https://github.com/ye-kyaw-thu/sylbreak) ထဲက Regular Expression (RE) ကိုပဲ သုံးထားပါတယ်။ ဘာကြောင့်လဲဆိုရင် Unicode နဲ့ စာရိုက်ထားတဲ့ မြန်မာစာတွေအတွက်က RE တစ်ကြောင်းတည်းနဲ့ လှလှပပ အလုပ်လုပ် ပေးလို့ပါ။ ပြီးတော့ NLP အလုပ်တွေ အများကြီးအတွက်လည်း လက်ရှိ syllable breaking RE သတ်မှတ်ချက်နဲ့တင် အဆင်ပြေလို့ပါ။ Python code နဲ့ပဲ အလွယ်ရှင်းပြရရင်တော့ အောက်ပါအတိုင်း ဗျည်း (က-အ)၊ အင်္ဂလိပ်စာလုံးနဲ့ အင်္ဂလိပ်ဂဏန်း (a-z,A-Z,0-9)၊ တခြားစာလုံး (ဣဤဥဦတို့လို သရတွေ၊ မြန်မာဂဏန်း၊ သင်္ကေတတချို့)၊ ပါဌ်ဆင့် ဆင့်တဲ့ Unicode သင်္ကေတ နဲ့ အသတ်အက္ခရာ စုစုပေါင်း variable ငါးခုကို သတ်မှတ်လိုက်ပြီးရင် ```((?<!" + ssSymbol + r")["+ myConsonant + r"](?![" + aThat + ssSymbol + r"])" + r"|[" + enChar + otherChar + r"])``` ဆိုတဲ့ RE ကို pass လုပ်ပေးလိုက်ယုံပါပဲ။ ဒီ RE က ပေးထားတဲ့ Rule ကတော့ ပါဌ်ဆင့် ဆင့်တဲ့ သင်္ကေတ နောက်က လိုက်တဲ့ ဗျည်း မဟုတ်ရင်၊ ပြီးတော့ အသတ်နဲ့တွဲနေတဲ့ ဗျည်း မဟုတ်ရင် အဲဒီဗျည်း စာလုံးရဲ့ ရှေ့မှာ break point လုပ်ပါ။ သို့မဟုတ် အင်္ဂလိပ်စာလုံးတို့ otherChar အနေနဲ့ သတ်မှတ်ထားတဲ့ စာလုံးတွေ ဆိုရင်လည်း အဲဒီစာလုံးတွေရဲ့ ရှေ့မှာ break ထည့်ပါလို့ သတ်မှတ်ထားတာ ဖြစ်ပါတယ်။    

```python
myConsonant = r"က-အ"
enChar = r"a-zA-Z0-9"
otherChar = r"ဣဤဥဦဧဩဪဿ၌၍၏၀-၉၊။!-/:-@[-`{-~\s"
ssSymbol = r'္'
aThat = r'်'

#Regular expression pattern for Myanmar syllable breaking
#*** a consonant not after a subscript symbol AND a consonant is not followed by a-That character or a subscript symbol
BreakPattern = re.compile(r"((?<!" + ssSymbol + r")["+ myConsonant + r"](?![" + aThat + ssSymbol + r"])" + r"|[" + enChar + otherChar + r"])", re.UNICODE)
```

⚠️ မှတ်ချက်။ ။ ဒီနေရာမှာ သတ်မှတ်ထားတဲ့ syllable (မြန်မာလို ဝဏ္ဏ လို့လည်း ခေါ်ပါတယ်) ဆိုတာက ဘာသာဗေဒ အရ ကြည့်မယ်ဆိုရင် မလိုက်နာတဲ့အပိုင်းတစ်ခုရှိပါတယ်။ အဲဒါက "တက္ကသိုလ်" လို ပါဌ်ဆင့် စာလုံးတွေဆိုရင် "တက်" "က" "သိုလ်" ဆိုပြီး မဖြတ်ပဲနဲ့ "တက္က" နဲ့ "သိုလ်" ဆိုပြီး syllable နှစ်လုံးအဖြစ်ပဲ break လုပ်ချသွားတာမျိုးပါ။ အဲဒီလိုလုပ်တာက NLP task တွေအတွက် ပိုပြီးအဆင်ပြေလို့ပါ။ post-editing လို အလုပ်တွေကို စဉ်းစားစရာ မလိုအပ်လို့ ပိုကောင်းတာမို့ပါ။ Downstream application တွေပေါ်ကို မူတည်ပြီးတော့ လက်ရှိ RE Rule ကို ပြင်တာ၊ ဖြည့်စွက်တာမျိုးက RE နားလည်တဲ့သူအတွက်က ကြိုက်သလို update လုပ်သွားကြပါ။ ⚠️   

### Syllable Segmentation with "myWord" Segmentation Tool

input file က အောက်ပါအတိုင်းရှိတယ်လို့ ဆိုကြပါစို့...  

```console
$ cat test.txt 
ကျွန်တော်ကသုတေသနသမားပါ။
နေ့ရောညရောမြန်မာစာနဲ့ကွန်ပျူတာနဲ့ပဲအလုပ် များ ပါ တယ်
မင်းကကောဘာအလုပ်လုပ်တာလဲ။
ပြောပြပါအုံး
ကောဖီလည်းထပ်သောက်ချင်ရင်ပြောကွာ
မန္တလေးမှာဒေါ်အောင်ဆန်းစုကြည်မိန့်ခွန်းပြောမယ်တဲ့။
```

syllable segmentation လုပ်ဖို့အတွက်က command line argument ကို syllable လို့ ပေးပြီးနောက် \<input-file\> နဲ့ \<output-file\> တွေရဲ့ နာမည်တွေကို ရိုက်ထည့်ပေးလိုက်ယုံပါပဲ။  
 
```console
$ python ./myword.py syllable ./test.txt ./test.syllable
$ cat ./test.syllable 
ကျွန် တော် က သု တေ သ န သ မား ပါ ။
နေ့ ရော ည ရော မြန် မာ စာ နဲ့ ကွန် ပျူ တာ နဲ့ ပဲ အ လုပ် များ ပါ တယ်
မင်း က ကော ဘာ အ လုပ် လုပ် တာ လဲ ။
ပြော ပြ ပါ အုံး
ကော ဖီ လည်း ထပ် သောက် ချင် ရင် ပြော ကွာ
မန္တ လေး မှာ ဒေါ် အောင် ဆန်း စု ကြည် မိန့် ခွန်း ပြော မယ် တဲ့ ။
```
 
## Theory: Word Segmentation with Viterbi Algorithm

လက်ရှိ ဗားရှင်း myWord ရဲ့ word segmentation လုပ်ပုံကတော့ လက်နဲ့ စာလုံးတစ်လုံးချင်းစီ သေသေချာချာ ဖြတ်ထားတဲ့ စာကြောင်းရေ ၅သိန်းကျော်၊ စာလုံးရေ ၁၂သန်းကျော်ရှိတဲ့ training corpus ကနေ ပထမဆုံး ngram အဘိဓာန်နှစ်ခု (unigram, bigram) ကို ကြိုတင်တည်ဆောက်ထားပြီးတော့ Viterbi algorithm နဲ့  decoding လုပ်တဲ့ approach ကို အသုံးပြုထားပါတယ်။ နည်းနည်း အသေးစိတ် ဖြည့်ပြောရရင် input ဝင်လာတဲ့ စာကြောင်းရဲ့ character တစ်လုံးချင်းစီကို bigram, unigram မော်ဒယ်နှစ်ခုနဲ့ score လုပ်သွားပြီးတော့၊ အဖြစ်နိုင်ဆုံး စာလုံးတွဲ ကို Viterbi algorithm ကိုသုံးပြီးတော့ ရွေးတဲ့ နည်းလမ်းပါ။ Score လုပ်တဲ့အခါမှာ အရင်ဆုံး bigram အဘိဓာန်မှာ ရှိရင် အဲဒီ Probability ကို ယူပြီးတော့၊ bigram အဘိဓာန်မှာ အဲဒီ စာလုံးတွဲက ရှာမတွေ့ရင်တော့ unigram အဘိဓာန်က probability ကို ယူပါတယ်။ 

[Viterbi Algorithm](https://en.wikipedia.org/wiki/Viterbi_algorithm) က 1967 မှာ [Andrew J. Viterbi](https://en.wikipedia.org/wiki/Andrew_Viterbi) ဆိုတဲ့ အင်ဂျင်နီယာက propose လုပ်ခဲ့တဲ့ algorithm ပါ။ ဒီ algorithm က Dynamic Programming Algorithm အုပ်စုထဲမှာ ပါပြီးတော့ Automatic Speech Recognition (ASR), Data recording, Part-Of-Speech (POS) tagging, DNA sequencing, Space Communication စသည်ဖြင့် ဧရိယာမျိုးစုံမှာ အသုံးပြုနေကြပါတယ်။ ကျွန်တော်တို့ နေ့စဉ် အသုံးပြုနေတဲ့ မိုဘိုင်းဖုန်းဆက်သွယ်မှုတွေမှာလည်း Viterbi algorithm ကို သုံးထားပါတယ်။ အဲဒါကြောင့် လွန်ခဲ့တဲ့ နှစ်ပေါင်း ၅၀ အတွင်းမှာ တကယ်ကို နာမည်ကြီးတဲ့ algorithm တစ်ခုဖြစ်ပြီး လက်တွေ့ သိထားရင်လည်း ကိုယ့်အလုပ်တွေအတွက် အသုံးဝင်တာမို့ ကွန်ပျူတာသမားတွေ၊ အင်ဂျင်နီယာတွေအနေနဲ့က မသိမဖြစ်လို့ကို ပြောရပါလိမ့်မယ်။ တကယ်တမ်း အသေးစိတ် လေ့လာချင်တဲ့ သူတွေက သူနဲ့ ဆက်စပ်နေတဲ့ Markov Process, Markov Property, Markov Chain, Hidden Markov Model (HMM) တို့ကို အရင်လေ့လာပါလို့ အကြံပေးချင်ပါတယ်။ ဥပမာ တစ်ခုအနေနဲ့ Viterbi ရဲ့ အလုပ်လုပ်ပုံကို ပြောရရင်... ဆိုကြပါစို့ ကျွန်တော်တို့မှာ HMM POS tagging လုပ်ပေးမဲ့ HMM မော်ဒယ်က ဆောက်ထားပြီးသားဆိုရင် စာကြောင်း အသစ်တစ်ကြောင်းကို အဲဒီ HMM မော်ဒယ်ကို pass လုပ်ပြီးတော့ POS tagging လုပ်ခိုင်းတဲ့အခါမှာ စာကြောင်း ထဲမှာ ပါတဲ့ စာလုံး အရေအတွက်ပေါ်ကို မူတည်ပြီးတော့ ဖြစ်နိုင်ချေရှိတဲ့ tag sequence တွေက အများကြီးမို့လို့ အဖြစ်နိုင်ဆုံးသော POS tag sequence ကို မော်ဒယ်က predict လုပ်တဲ့ အခါမျိုးမှာ Viterbi ကို သုံးပြီး best path ကို ရှာလို့ ရပါတယ်။ အဲဒီလို မလုပ်ပဲ brute force searching နဲ့ ရှိသမျှ path အကုန်ကိုတွက်ပြီးမှသာ ရွေးမယ်ဆိုပြီး စဉ်းစားရင် ကွန်ပျူတာ memory က မနိုင်ပါဘူး။ ဘာကြောင့်လဲဆိုတော့ ngram အဘိဓာန်အပြင်၊ HMM မှာက Observed state နဲ့ Hidden state ဆိုပြီး နှစ်ပိုင်းပါတာကြောင့် ကျွန်တော်တို့က transition probability (POS-tag တစ်ခုနဲ့ တစ်ခုအကြား) ရော emmission probability (POS-tag နဲ့ word အကြား) ရော ကို တွက်ကြရမှာမို့ စာလုံးအရေအတွက်က များလာတာနဲ့ အမျှ operation က exponentially တိုးလာမှာမို့ပါ။ ကွန်ပျူတာသမားတွေ အများစု သိထားကြတဲ့ Computational Complexity အနေနဲ့ ကြည့်မယ်ဆိုရင် Brute Force algorithm က ```O(S^T)``` ဖြစ်ပြီးတော့ Viterbi algorithm က ```O(T*S^2)``` လို့ ဖော်ပြလို့ ရပါတယ်။ ဒီနေရာမှာ ပြောနေတဲ့ "S" က HMM network ထဲမှာ ရှိနေတဲ့ state အရေအတွက် (i.e. the number of states) ကို ကိုယ်စားပြုပြီးတော့၊ "T" ကတော့ စာကြောင်း တစ်ကြောင်းမှာ ရှိတဲ့ စာလုံးအရေအတွက် (i.e. the length of the data sequence) ကို ကိုယ်စားပြုတာကြောင့် Viterbi Algorithm က computational cost ကို အများကြီး လျော့သွားစေပါတယ်။  

Word segmentation အလုပ်ကိုလည်း graph အနေနဲ့ မြင်ကြည့်ပြီး စဉ်းစားကြည့်ကြရအောင်။ ရှင်းပြရတာ လွယ်ကူအောင်လို့ input စာကြောင်းကို မြန်မာစာလုံး "ဆရာက" ဆိုတဲ့ စာလုံး နှစ်လုံးပါတဲ့ စကားစုလေးကိုပဲ ဥပမာသုံးပြီးတော့ ရှင်းပြပါမယ်။ ဝင်လာတဲ့ စာကြောင်းကို character တစ်လုံးချင်းစီ ဖြတ်ပြီးတော့ node တစ်ခုချင်းစီအတွက် probability တွေကို တွက်ပြီး break point ကို စဉ်းစားတဲ့ နေရာမှာ Brute force နဲ့သာဆိုရင် node အကုန်ကို တွက်ပြီးမှ final word boundary ကို ဆုံးဖြတ်နိုင်မှာ ဖြစ်ပါတယ်။ သို့သော် Viterbi algorithm ရဲ့ အလုပ်လုပ်ပုံကတော့ memory မှာ ရှေ့က တွက်ခဲ့တဲ့ node တစ်ခုချင်းစီအထိ probability distribution ကို မှတ်သားထားပြီးတော့ လမ်းတဝက် node တနေရာရာမှာ လက်ရှိ အချိန်အထိ တွက်ခဲ့တဲ့ ရလဒ်တွေထဲကနေ မလိုအပ်တော့တဲ့ path တွေကို ဖြုတ်ချထားခဲ့ပြီး ဖြစ်နိုင်ချေအရှိဆုံး best path ကိုပဲ ဆင့်ဆင့်ပြီး ဦးတည်တွက်သွားတဲ့ ပုံစံပါ။ Algorithm အနေနဲ့ အလုပ်လုပ်ပုံကို တိတိကျကျ ပြောရရင်တော့ forward order နဲ့ backward order ဆိုပြီးတော့ နှစ်ပိုင်းပါဝင်ပြီး၊ forward မှာက node တစ်ခုချင်းစီကို ရောက်ဖို့အတွက် လာတဲ့ best path တွေကို တွက်သွားပါတယ်။ Backward order အပိုင်းကတော့ စာကြောင်း အစကနေ အဆုံးအထိ best path ကို ဖောက်သွားတဲ့ ပုံစံပါ။ Backward operation ရဲ့ calculation လုပ်တဲ့ပုံစံကတော့ စာကြောင်းအဆုံးကနေ စာကြောင်းရှေ့ဆုံးကို ပြောင်းပြန် ပြန်သွားတဲ့ ပုံစံနဲ့တွက်ပါတယ်။ အဲဒါကြောင့်မို့လို့လည်း Backward လို့သုံးတာပါ။  
 
ပထမဆုံး လေ့လာတဲ့သူတွေအတွက်က follow လိုက်ဖို့ ခက်နိုင်တာကြောင့် "ဆရာက" ဆိုတဲ့ စာကြောင်းတို့လေးကိုပဲ graph အနေနဲ့ မြင်ပြီး best path ကို ဘယ်လို တွက်သလဲ ဆိုတာကို အိုက်ဒီယာရသွားဖို့ စဉ်းစားကြည့်ကြရအောင်။ Fig.1 ကိုတည်ပြီးတော့ ရှင်းသွားပါမယ်။ ပုံမှာ ပြထားသလိုပါပဲ graph မှာက node တွေရှိမယ်။ အဲဒီ node တွေကို ဆက်နေတဲ့ path တွေလည်း ရှိပါလိမ့်မယ်။ node တစ်ခုချင်းစီက character တစ်လုံးချင်းစီကို ကိုယ်စားပြုပြီးတော့ path တစ်ခုချင်းစီက input စာကြောင်းကို ဘယ်လို ပုံစံမျိုးနဲ့ segmentation လုပ်သွားမယ်ဆိုတဲ့ လမ်းကြောင်းတွေ ဖြစ်ပါတယ်။ Path တစ်ခုစီမှာ ဖြတ်သွားမယ့်စာလုံးနဲ့အတူ တွဲရေးထားတဲ့ ဂဏန်းတွေက path weight တွေဖြစ်ပြီး၊ လက်ရှိ စာလုံးဖြတ်ဖို့လုပ်နေတဲ့ စာကြောင်းရဲ့ unigram negative log property တွေ လို့ယူဆပေးပါ။  


<p align="center">
<img src="https://github.com/ye-kyaw-thu/myWord/blob/main/documentation/fig/sayarka.png" alt="word segmentation as graph" width="800"/>  
</p>  
<div align="center">
  Fig.1 Word segmentation as graph for the input sentence "ဆရာက"  
</div> 

<br />

ပရိုဂရမ်အနေနဲ့က အလုပ်လုပ်တဲ့အခါမှာ character လေးလုံးဖြစ်တဲ့ "ဆ" "ရ" "ာ" နဲ့ "က" ကို တွဲလို့ ရတဲ့ sequence pattern အကုန်လုံးကို စဉ်းစားရတာမို့ တကယ်က အောက်ပါ path တွေကို ထည့်သွင်းစဉ်းစားရပါတယ်။  
 
- Path1: 0--->1--->2--->3--->4 = 2.0 + 2.5 + 4.1 + 1.0 = 9.6 = ဆ | ရ | ာ | က 
- Path2: 0--->2--->3--->4 = 3.3 + 4.1 + 1.0 = 8.4 = ဆရ | ာ | က
- Path3: 0--->3--->4 = 1.2 + 1.0 = 2.2 = ဆရာ | က
- Path4: 0--->4 = 2.8 = ဆရာက
- Path5: 0--->2--->4 = 3.3 + 3.8 = 7.1 = ဆရ | ာက 
- Path6: 0--->1--->4  = 2.0 + 3.9 = 5.9 = ဆ | ရာက 
- Path7: 0--->1--->3--->4 = 2.0 + 2.6 + 1.0 = 5.6 = ဆ | ရာ | က
 
အထက်မှာ ပြထားတဲ့ path တွေထဲကမှ Viterbi algorithm က best path သို့မဟုတ် shortest path ကိုရွေးမှာ ဖြစ်ပါတယ်။ အဲဒါကြောင့် ```Path3: 0--->3--->4 = 1.2 + 1.0 = 2.2``` က path တွေအားလုံးထဲမှာ တန်ဖိုးအနိမ့်ဆုံးမို့လို့ semented output အနေနဲ့က  "ဆရာ | က" ဆိုပြီးတော့ မှန်မှန်ကန်ကန် word segmentation လုပ်ပေးမှာ ဖြစ်ပါတယ်။ တကယ်တမ်းတွက်တဲ့အခါမှာ စာလုံး တစ်လုံးချင်းစီရဲ့ probability က unigram အဘိဓာန်က လာတာဖြစ်ပြီးတော့ negative log probability ကို သုံးတာကြောင့် အောက်ပါ ပုံစံမျိုးတွက်တာ ဖြစ်ပါတယ်။ Shortest path ကို ရွေးတဲ့ အလုပ်ကို Backward operation မှာ လုပ်သွားတာ ဖြစ်ပါတယ်။  
 
 ```-log(P( ဆရာ )) + -log(P( က )) = 1.2 + 1.0 = 2.2```
 
အထက်က Fig.1 မှာ ပြခဲ့တဲ့ "ဆရာက" ဆိုတဲ့ input စာကြောင်းအတွက် စာလုံး ဖြတ်လို့ရတဲ့ လမ်းကြောင်းတွေ အမျိုးမျိုးရှိတဲ့အထဲကနေ shortest path ကို graph အနေနဲ့ ဆွဲပြရရင်တော့ အောက်ပါလို ပုံမျိုး (Fig. 2) ကို ဆွဲလို့ ရပါလိမ့်မယ်။  
 
<p align="center">
<img src="https://github.com/ye-kyaw-thu/myWord/blob/main/documentation/fig/segment2.png" alt="shortest path" width="340"/>  
</p>  
<div align="center">
  Fig.2 the shortest path for the input sentence "ဆရာက" 
</div> 

<br />
 
တကယ့် လက်တွေ့မှာက ဆရာနဲ့ စတဲ့ မြန်မာစာလုံးတွေက corpus ထဲမှာ အများကြီးရှိမှာမို့ ဒေတာများများနဲ့ ngram အဘိဓာန်ကို ဆောက်ထားရင် ဆောက်ထားသလို စာကြောင်း ရှည်ရင် ရှည်သလို word boundary ကို ခန့်မှန်းဖို့အတွက်က ကွန်ပျူတာက တွက်ရမယ့် path တွေက သန်းနဲ့ချီပြီး ရှိသွားနိုင်ပါတယ်။ အဲဒါကြောင့် HMM လိုမော်ဒယ်တွေရဲ့ decoding မှာ Viterbi algorithm ကို သုံးကြတာဖြစ်ပါတယ်။   
 
မြန်မာစာအတွက် Word Segmentation tool ကို implementation လုပ်ဖို့ စဉ်းစားတဲ့အခါမှာလည်း ဒေတာသာ ရှိမယ်ဆိုရင် လွယ်လွယ်ကူကူနဲ့ training လုပ်ပြီး ရိုးရှင်းပြီး powerful ဖြစ်တဲ့ algorithm နဲ့ စာလုံးတွေကို ဖြတ်ပေးဖို့ စဉ်းစားတဲ့အခါမှာ Viterbi algorithm ကိုပဲ သုံးဖို့ ဆုံးဖြတ်ခဲ့ပါတယ်။ ရှေ့က ဆရာတွေဖြစ်တဲ့ [Dr. Peter Norvig](https://en.wikipedia.org/wiki/Peter_Norvig) (အမေရိကန် ကွန်ပျူတာသိပ္ပံပညာရှင်, Google LLC ရဲ့ ဒါရိုက်တာ) က ရေးသားထားတဲ့ [Beautiful Data](https://github.com/jhulick/bookstuff/blob/master/Oreilly%20-%20Beautiful%20Data.pdf) စာအုပ်ရဲ့ Chapter 14: Natural Language Corpus Data ရဲ့ အခန်းမှာသုံးထားတဲ့ ngram အဘိဓာန်ဆောက်ပြီးတော့ Viterbi table ဆောက်ပြီး စာလုံးဖြတ်ပြထားတာကို မှီငြမ်းထားပါတယ်။ Coding ကလည်း [updated version code, Mark Dong](https://gist.github.com/markdtw/e2a4e2ee7cef8ea6aed33bb47a97fba6) ကို မှီငြမ်းထားပါတယ်။ ကိုယ့် corpus နဲ့ ngram အဘိဓာန်ကို ဆောက်နိုင်အောင် ရေးတဲ့အပိုင်းနဲ့ plain text ဖိုင် ngram အဘိဓာန်တွေအစား binary အဘိဓာန်တွေကို သုံးတဲ့ အပိုင်းတွေကို ဖြည့်စွက် coding လုပ်ခဲ့ပါတယ်။ Recursion limit ကိုလည်း ```sys.setrecursionlimit(10**6)``` ဆိုပြီး ထည့်ခဲ့ပါတယ်။ myWord Segmentation tool မှာ ရေးထားတဲ့ viterbi function က အောက်ပါအတိုင်းပါ။ coding ဖတ်နိုင်တဲ့သူတွေက coding ကိုဖတ်ရင်း Vitabi algorithm နဲ့ word segmentation ကို ဘယ်လို လုပ်သွားတယ်ဆိုတာကို လေ့လာတာက ပိုမြန်ချင်လည်း မြန်နိုင်ပါတယ်။   
 
 
```python
@functools.lru_cache(maxsize=2**10)
#maxlen=20
def viterbi(text, prev='<S>', maxlen=20):
    if not text:
        return 0.0, []
    
    print("text: ", text)
    textlen = min(len(text), maxlen)
    splits = [(text[:i + 1], text[i + 1:]) for i in range(textlen)]

    candidates = []
    for first_word, remain_word in splits:
        #pdb.set_trace()
        first_prob = math.log10(conditionalProb(first_word, prev))
        print("first_prob of condProb(", first_word, ", ", prev, "): ", first_prob )
        remain_prob, remain_word = viterbi(remain_word, first_word)
        print("remain_prob: ", remain_prob, ", remain_word: ", remain_word)
        candidates.append((first_prob + remain_prob, [first_word] + remain_word))
        #print("first_prob: ", str(first_prob), ", remain_prob: ", remain_prob, ", [first_word]:", [first_word], ", remain_word: ", remain_word)
        print("Candidates: ", candidates)
        
    print("max(candidates): " + str(max(candidates)))
    print("====================")
    return max(candidates)
```
 
အလုပ်လုပ်ပုံကို trace လုပ်ရတာ လွယ်အောင်လို့ print statement တွေကိုပါ ထပ်ဖြည့်ပြီး viterbi function ကို "ဆရာက" ဆိုတဲ့ စာကြောင်းတစ်ကြောင်းတည်းကိုပဲ ထည့်ပြီး run ပေးထားပါတယ်။ ကွန်ပျူတာ terminal screen မှာ ရိုက်ထုတ်ပေးလာတဲ့ စာကြောင်းတွေကတော့ အောက်ပါအတိုင်းပါ။ ဒီ function က recursive function အနေနဲ့ ခေါ်သုံးထားတာကိုလည်း ဂရုပြုပါ။   
 
```consloe
$ python ./myword.py word ./one_line.txt ./one_line.word 
text:  ဆရာက
first_prob of condProb( ဆ ,  <S> ):  -2.3682169728893223
text:  ရာက
first_prob of condProb( ရ ,  ဆ ):  0.15368326096895993
text:  ာက
first_prob of condProb( ာ ,  ရ ):  -4.1075915061395
text:  က
first_prob of condProb( က ,  ာ ):  0.39394528587814026
remain_prob:  0.0 , remain_word:  []
Candidates:  [(0.39394528587814026, ['က'])]
max(candidates): (0.39394528587814026, ['က'])
====================
remain_prob:  0.39394528587814026 , remain_word:  ['က']
Candidates:  [(-3.71364622026136, ['ာ', 'က'])]
first_prob of condProb( ာက ,  ရ ):  -6.010681493131443
remain_prob:  0.0 , remain_word:  []
Candidates:  [(-3.71364622026136, ['ာ', 'က']), (-6.010681493131443, ['ာက'])]
max(candidates): (-3.71364622026136, ['ာ', 'က'])
====================
remain_prob:  -3.71364622026136 , remain_word:  ['ာ', 'က']
Candidates:  [(-3.5599629592924003, ['ရ', 'ာ', 'က'])]
first_prob of condProb( ရာ ,  ဆ ):  -0.7926188753050689
text:  က
first_prob of condProb( က ,  ရာ ):  0.39394528587814026
remain_prob:  0.0 , remain_word:  []
Candidates:  [(0.39394528587814026, ['က'])]
max(candidates): (0.39394528587814026, ['က'])
====================
remain_prob:  0.39394528587814026 , remain_word:  ['က']
Candidates:  [(-3.5599629592924003, ['ရ', 'ာ', 'က']), (-0.39867358942692865, ['ရာ', 'က'])]
first_prob of condProb( ရာက ,  ဆ ):  -7.010681493131443
remain_prob:  0.0 , remain_word:  []
Candidates:  [(-3.5599629592924003, ['ရ', 'ာ', 'က']), (-0.39867358942692865, ['ရာ', 'က']), (-7.010681493131443, ['ရာက'])]
max(candidates): (-0.39867358942692865, ['ရာ', 'က'])
====================
remain_prob:  -0.39867358942692865 , remain_word:  ['ရာ', 'က']
Candidates:  [(-2.766890562316251, ['ဆ', 'ရာ', 'က'])]
first_prob of condProb( ဆရ ,  <S> ):  -6.010681493131443
text:  ာက
first_prob of condProb( ာ ,  ဆရ ):  -4.1075915061395
remain_prob:  0.39394528587814026 , remain_word:  ['က']
Candidates:  [(-3.71364622026136, ['ာ', 'က'])]
first_prob of condProb( ာက ,  ဆရ ):  -6.010681493131443
remain_prob:  0.0 , remain_word:  []
Candidates:  [(-3.71364622026136, ['ာ', 'က']), (-6.010681493131443, ['ာက'])]
max(candidates): (-3.71364622026136, ['ာ', 'က'])
====================
remain_prob:  -3.71364622026136 , remain_word:  ['ာ', 'က']
Candidates:  [(-2.766890562316251, ['ဆ', 'ရာ', 'က']), (-9.724327713392803, ['ဆရ', 'ာ', 'က'])]
first_prob of condProb( ဆရာ ,  <S> ):  -1.2541214501247606
text:  က
first_prob of condProb( က ,  ဆရာ ):  0.39394528587814026
remain_prob:  0.0 , remain_word:  []
Candidates:  [(0.39394528587814026, ['က'])]
max(candidates): (0.39394528587814026, ['က'])
====================
remain_prob:  0.39394528587814026 , remain_word:  ['က']
Candidates:  [(-2.766890562316251, ['ဆ', 'ရာ', 'က']), (-9.724327713392803, ['ဆရ', 'ာ', 'က']), (-0.8601761642466204, ['ဆရာ', 'က'])]
first_prob of condProb( ဆရာက ,  <S> ):  -4.709651497467462
remain_prob:  0.0 , remain_word:  []
Candidates:  [(-2.766890562316251, ['ဆ', 'ရာ', 'က']), (-9.724327713392803, ['ဆရ', 'ာ', 'က']), (-0.8601761642466204, ['ဆရာ', 'က']), (-4.709651497467462, ['ဆရာက'])]
max(candidates): (-0.8601761642466204, ['ဆရာ', 'က'])
====================
```

### Building Unigram, Bigram Dictionaries for Word Unit
 
ကိုယ့်မှာ manual word segmentation လုပ်ထားပြီးသား corpus က အဆင့်သင့်ရှိတယ်ဆိုရင် myword နဲ့ n-gram dictionary ဆောက်ဖို့အတွက်က အောက်ပါအတိုင်း command ပေးပါ။  
ဒီနေရာမှာ myword က unigram, bigram အဘိဓာန်တွေကို text file format အနေနဲ့ရော binary file format အနေနဲ့ရော ဆောက်ပေးသွားမှာမို့ အဲဒီ output filename တွေကို ```--unigram_word_txt unigram-word.txt```, ``` --bigram_word_txt bigram-word.txt```,  ```--unigram_word_bin unigram-word.bin```, ``` --bigram_word_bin bigram-word.bin``` ဆိုပြီး ကိုယ်ပေးချင်တဲ့ ဖိုင်နာမည်တွေကို  assign လုပ်သွားလို့ ရပါတယ်။  

Word n-gram dictionary building with full dictionary filenames parameters:  
 
 ```console
 $ python ./myword.py build_dict --unigram_word_txt unigram-word.txt --bigram_word_txt bigram-word.txt --unigram_word_bin unigram-word.bin --bigram_word_bin bigram-word.bin ./corpus2.1k 
 ```
 
 တကယ်လို့ default ngram dictionary နာမည်တွေနဲ့ပဲ ဆောက်သွားမယ်၊ ဖိုင်နာမည်တွေကို သီးသန့် assign လုပ်တာမျိုး မလုပ်ဘူး ဆိုရင်တော့ အောက်ပါအတိုင်း command အတိုနဲ့ပဲ ngram အဘိဓာန်တွေကို ဆောက်သွားလို့ ရပါတယ်။  
Word n-gram dictionary building with default filenames:  
 
 ```console
 $ python ./myword.py build_dict ./corpus2.1k 
 ```
 
 ### Word Segmentation with "myWord" Segmentation Tool
 
 myword နဲ့ word segmentation လုပ်တာကို default n-gram dictionary တွေကိုပဲ သုံးပြီး စာလုံးဖြတ်မယ်ဆိုရင်တော့ အောက်ပါအတိုင်း command ပေးရပါတယ်။  
 ဒီနေရာမှာ ./test.txt ဖိုင်က input file ဖြစ်ပြီးတော့ ./test.word ကတော့ စာလုံးဖြတ်ပြီး ထွက်လာတဲ့ ဖိုင်ကိုသိမ်းစေချင်တဲ့ နာမည်ပါ။  
 
 Word segmentation with default n-gram dictionaries:  
 
 ```console
 $ python ./myword.py word ./test.txt ./test.word
 ```

input ဖိုင်က အောက်ပါအတိုင်း သုံးထားပါတယ်။  
(space တွေပါနေလည်း myword က auto remove လုပ်ပေးသွားမှာမို့ တကူးတက space တွေကို ဖြုတ်ပြီးမှ input လုပ်စရာမလိုပါဘူး။ ခုက ဥပမာအနေနဲ့ မြင်သာအောင်သာ ပြထားတာပါ)  
 
```console
$ cat test.txt
ကျွန်တော်ကသုတေသနသမားပါ။
နေ့ရောညရောမြန်မာစာနဲ့ကွန်ပျူတာနဲ့ပဲအလုပ် များ ပါ တယ်
မင်းကကောဘာအလုပ်လုပ်တာလဲ။
ပြောပြပါအုံး
ကောဖီလည်းထပ်သောက်ချင်ရင်ပြောကွာ
မန္တလေးမှာဒေါ်အောင်ဆန်းစုကြည်မိန့်ခွန်းပြောမယ်တဲ့။
```

word segmented လုပ်ပြီး ထွက်လာတဲ့ output ဖိုင်က အောက်ပါအတိုင်းပါ။  

 ```console
$ cat test.word
ကျွန်တော် က သုတေသန သမား ပါ ။
နေ့ ရော ည ရော မြန်မာ စာ နဲ့ ကွန်ပျူတာ နဲ့ ပဲ အလုပ် များ ပါ တယ်
မင်း က ကော ဘာ အလုပ် လုပ် တာ လဲ ။
ပြော ပြ ပါ အုံး
ကောဖီ လည်း ထပ် သောက် ချင် ရင် ပြော ကွာ
မန္တလေး မှာ ဒေါ်အောင်ဆန်းစုကြည် မိန့်ခွန်း ပြော မယ် တဲ့ ။
```

⚠️ unigram, bigram dictionary တွေကို ဆောက်တဲ့အခါမှာ text file format အနေနဲ့ရော binary file format အနေနဲ့ရော ဆောက်ပေးသွားပေမဲ့ word segmentation လုပ်တဲ့အခါမှာတော့ binary dictionary နှစ်ခုပဲ လိုအပ်ပါတယ်။ text file format အဘိဓာန်တွေက developer/researcher တွေအနေနဲ့ မျက်လုံးနဲ့ စစ်ကြည့်ပြီး corpus ကို update လုပ်တာ သို့မဟုတ် အဘိဓာန်ကို update လုပ်ပြီး binary အဖြစ် ပြောင်းတာတွေ လုပ်နိုင်အောင်လို့ facility အနေနဲ့ ထည့်ပေးထားတာပါ။ ⚠️  
 
 word segmentation လုပ်တဲ့ အခါမှာ unigram, bigram အဘိဓာန်တွေကို assign လုပ်ပြီး ဖြတ်မယ်ဆိုရင်တော့ အောက်ပါအတိုင်း command ပေးပြီး run ပါ။  
 (Word segmentation with unigram, binary n-gram dictionaries)  
 
 ```console
 $ python ./myword.py word --unigram_word_bin ./unigram-word.bin --bigram_word_bin ./bigram-word.bin ./test.txt ./test.word
 ```
 
 Word Segmentation ဖြတ်တဲ့အခါမှာ default က space နဲ့ခြားပေးမှာ ဖြစ်ပေမဲ့ delimiter ကိုလည်း အမျိုးမျိုး ပြောင်းလို့ ရပါတယ်။ ဥပမာ delimiter ကို pipe အဖြစ်ထားပြီး word segmentation လုပ်ချင်တယ် ဆိုရင်တော့ အောက်ပါအတိုင်း command ပေး run ပါ။  
 
 (Word segmentation with delimiter "pipe")  
 
 ```console
 $ python ./myword.py word --delimiter "|" ./test.txt ./test.word
```

ထွက်လာတဲ့ segmented output ဖိုင်က အောက်ပါအတိုင်းပါ။  

```
ကျွန်တော်|က|သုတေသန|သမား|ပါ|။
နေ့|ရော|ည|ရော|မြန်မာ|စာ|နဲ့|ကွန်ပျူတာ|နဲ့|ပဲ|အလုပ်|များ|ပါ|တယ်
မင်း|က|ကော|ဘာ|အလုပ်|လုပ်|တာ|လဲ|။
ပြော|ပြ|ပါ|အုံး
ကောဖီ|လည်း|ထပ်|သောက်|ချင်|ရင်|ပြော|ကွာ
မန္တလေး|မှာ|ဒေါ်အောင်ဆန်းစုကြည်|မိန့်ခွန်း|ပြော|မယ်|တဲ့|။
```

## Theory: Unsupervised Phrase Segmentation with NPMI

Phrase Segmentation လုပ်တာက Normalized pointwise mutual information (NPMI) နဲ့ပါ။  
[Assoc. Prof. Daichi Mochihashi](http://chasen.org/~daiti-m/diary/) ရဲ့ ဂျပန်လိုရေးထားတဲ့ blog ကို တွေ့ပြီး မြန်မာစာအတွက် စမ်းကြည့်ဖို့ အိုက်ဒီယာ ရခဲ့ပါတယ်။ သူ ရှင်းပြထားတာကိုပဲ အခြေခံပြီး ဗမာစာအတွက် စမ်းခဲ့တဲ့ အပိုင်းကို ရှင်းပြသွားပါမယ်။   

Wrod2Vec နဲ့ ပတ်သက်တဲ့ နာမည်ကြီး စာတမ်းနှစ်စောင် ကို အရင်ဆုံး refer လုပ်ကြမှ အသေးစိတ် ဇာတ်ရည်လည်ပါလိမ့်မယ်။  

ပထမစာတမ်း ဖြစ်တဲ့ [Efficient Estimation of Word Representations in Vector Space, (Mikolov et al., 2013)](https://arxiv.org/pdf/1310.4546.pdf) စာတမ်းထဲမှာ အောက်ပါအတိုင်း ဖော်ပြထားတာကို တွေ့ရပါလိမ့်မယ်။

```We have included in our test set only single token words, thus multi-word entities are not present (such as New York).```

ပထမစာတမ်းရဲ့ test set မှာ single token word တွေပဲ သုံးထားကြောင်း ဖော်ပြထားပါတယ်။ ဆိုလိုတာက "New York", "ice cream", "high school", "hot dog", "living room", "full moon", "up to date", "part-time work", "state of the art" တို့လို စာလုံး နှစ်လုံးနဲ့ အထက်တွဲနေတဲ့ စကားလုံးတွေ (word) တွေကို word2vec အနေနဲ့ train လုပ်မယ်ဆိုရင် အရင်ဆုံး အမြဲတမ်း တွဲပြီးသုံးနေတဲ့ စာလုံးတွဲတွေ တနည်းအားဖြင့် phrase တွေကို ငါတို့က ကြိုသိဖို့ လိုအပ်ပါတယ်။ အဲဒီလို သိပြီးမှသာ word2vec ကို train မလုပ်ခင်မှာ preprocessing အနေနဲ့ ဥပမာ "new_york", "ice_cream", ..., "up_to_date", "part_time_work", "state_of_the_art" အဖြစ် underscore နဲ့ တွဲတာမျိုး လုပ်ပြီး စာလုံးတစ်လုံးအနေနဲ့ training corpus ထဲမှာ ကြိုပြင်ထားဖို့ လိုအပ်ပါလိမ့်မယ်။ အဲဒီ လိုမျိုး NLP task အတွက်က supervised approach နဲ့ ဆိုရင် NER (Name Entity Recognition) model နဲ့ လုပ်လို့ ရပေမဲ့ NER model ဆောက်ဖို့အတွက်က NER corpus က ရှိနေမှ ဖြစ်ပါလိမ့်မယ်။ အဲဒါကြောင့် NER corpus ကို မသုံးပဲနဲ့ unsupervised approach အနေနဲ့ သွားမယ်ဆိုရင် ဘယ်လို လုပ်လို့ ရနိုင်တယ် ဆိုတာကို Word2Vec ရဲ့ဒုတိယစာတမ်းလို့ ပြောလို့ရတဲ့ [Distributed Representations of Words and Phrases and their Compositionality, (Mikolov et al., 2013)](https://arxiv.org/pdf/1310.4546.pdf) စာတမ်းရဲ့ Section 4. Learning Phrases မှာ Formula No. 6 အနေနဲ့ အောက်ပါအတိုင်း ဖော်ပြထားတာကို တွေ့ရပါလိမ့်မယ်။  

<p align="center">
<img src="https://github.com/ye-kyaw-thu/myWord/blob/main/documentation/fig/formula-6.png" alt="formula no.6 of Word2Vec Paper" width="350"/>
</p>
  
ဒီနေရာမှာ ပြောနေတဲ့ n (v, w), n (v), n (w) တွေက bigram နဲ့ unigram frequency တွေ ဖြစ်ပြီးတော့ δ က frequency နိမ့်တဲ့ စကားလုံးတွဲတွေက ထိပ်ပိုင်းကို ရောက်မလာဖို့အတွက် ထိန်းညှိတဲ့ discount factor ပါ။ Phrase တွေကို ဆွဲထုတ်နိုင်ဖို့အတွက်က threshold တစ်ခု သတ်မှတ်ထားပြီး အဲဒီ threshold value အထက်မှာ ရှိတဲ့ bigram စကားလုံးတွဲတွေကို ရွေးယူလိုက်ယုံပါပဲ။ Threshold value အထက် ဆိုတာကို probability အနေနဲ့ စဉ်းစားကြည့်ရင် p (v, w) = n (v, w) / N, p (v) = n (v) / N, p (w) = n ဆိုပြီး ဖော်မြူလာအနေနဲ့ ရေးလို့ ရပါတယ်။ ဒီနေရာမှာ "N" ဆိုတာက unigram စုစုပေါင်းတန်ဖိုးပါ။ δ ကို ဖယ်ပြီးတော့ score တွက်ဖို့အတွက် စဉ်းစားရင် အောက်ပါအတိုင်း ရေးလို့ ရပါတယ်

score (v, w) = n (v, w) / (n (v) * n (w)) = (p (v, w) * N) / (p (v) * N * p (w) * N) = p (v, w) / (p (v) * p (w) * N)

ဒါကြောင့် ဒီ score တွက်တဲ့ အပိုင်းက self-mutual information PMI တွက်တဲ့ PMI (v, w) = log p (v, w) / (p (v) * p (w)) ဆိုတဲ့ ဖော်မြူလာနဲ့ အကုန်လုံးလိုလို ဆင်တူဖြစ်တာကို တွေ့ရပါလိမ့်မယ်။ ဒါပေမဲ့ သေသေချာချာ ပြန် နှိုင်းယှဉ်ကြည့်တဲ့ အခါမှာ၊ အော်ရဂျင်နယ် ဖော်မြူလာမှာက 1/N ဆိုတဲ့ factor က ပါဝင်ပြီးတော့ အဲဒါက corpus အပေါ်မှာ မူတည်နေလို့ ထွက်လာမယ့် score က အခြေခံအားဖြင့် corpus ရဲ့ length ပေါ်မှာ သွားပြီး မူတည်နေပါတယ်။ corpus ကို အပြောင်းအလဲ ထပ်တိုးတာမျိုး မလုပ်ပဲ fixed လုပ်ထားပြီးတော့ threshold တန်ဖိုးကို search လုပ်တာမျိုးလုပ်ရင်တော့ အတိုင်းအတာ တစ်ခုအထိ ပြေလည်ပေမဲ့ threshold ရဲ့ အဓိပ္ပါယ်က နားလည်ရခက်တဲ့အပြင် length မတူတဲ့ စာကြောင်းတွေကို သုံးပြီးတော့ score တွေကို နှိုင်းယှဉ်ကြည့်ပြီးသွားမယ်ဆိုရင် ရလာတဲ့ phrase တွေက ပုံမှန် လူတွေက သုံးနေကြတဲ့ phrase နဲ့တော့ တထပ်တည်း ကျမှာ မဟုတ်ပါဘူး။  

corpus ကို independent ဖြစ်ဖို့အတွက်က original score တန်ဖိုးကို N နဲ့ မြှောက်လို့ ရပါတယ်။ သို့သော် အခုပြောနေတဲ့ score ဆိုတာက PMI ကို တွက်တာ ဖြစ်တာကြောင့်   

- PMI ရဲ့က အားနည်းချက်က low frequency word တွေကို အားနည်းတာ  
- PMI scale ကလည်း ဒေတာပေါ်မူတည်ပြီးနေတာ  
 
စတဲ့ အချက်တွေလည်း ရှိတာကြောင့် Normalized PMI (NPMI) (Bouma 2009) ကို သုံးသင့်တယ်လို့ ထင်ပါတယ်။   
NPMI ဆိုတာက အောက်ပါအတိုင်း သတ်မှတ်ထားပါတယ်။  

NPMI (v, w) = log p (v, w) / (p (v) * p (w)) / (-log p (v, w))  

NPMI ကို -1≦NPMI(v,w)≦1 ဆိုတဲ့ range အတွင်းမှာ သတ်မှတ်ထားတာကြောင့် 1 ဖြစ်နေတဲ့ အချိန်မှာ v နဲ့ w တို့ဟာ တိုက်ရိုက် correlation ဖြစ်နေပြီး -1 ဖြစ်နေတဲ့ အချိန်မှာတော့ inverse correlation ဖြစ်နေကြောင်းကို နားလည်ရ လွယ်ကူပါတယ်။ ပြီးတော့ PMI မှာတုန်းက ရှိခဲ့တဲ့ "p(v)" တို့  "p(w)" တို့ရဲ့ တန်ဖိုးတွေက အရမ်း သေးငယ်တဲ့ အခါမှာ score ကို ဖောင်းပွစေနိုင်တဲ့ အားနည်းချက်ကိုလည်း ရှောင်ပြီးသွား ဖြစ်သွားပါလိမ့်မယ်။ အဲဒီလိုသာဆိုရင် Word2vec ရဲ့ အော်ရဂျင်နယ်စာတမ်းမှာ သုံးခဲ့တဲ့ heuristic discount coefficient တန်ဖိုး ဖြစ်တဲ့ δ လည်း မလိုအပ်တော့ပါဘူး။  

အဲဒါကြောင့် script တစ်ပုဒ် ရေးပြီးတော့ phrase အော်တိုဖြတ်တာကို စမ်း ကြည့်ဖြစ်ခဲ့ပါတယ်။ Phrase recognition သို့မဟုတ် phrase segmentation လုပ်တဲ့ core အပိုင်းကိုပဲ ရေးဖို့အတွက် unigram, bigram frequency တွေကို dictionary နှစ်ခုအနေနဲ့ သိမ်းထားခဲ့ပြီး၊ word bigram (v, w) က phrase ဖြစ်မဖြစ်ကို ဆုံးဖြတ်တဲ့ အပိုင်းကိုပဲ Python script နဲ့ ရေးပြရရင် အောက်ပါအတိုင်း ဖြစ်ပါလိမ့်မယ်။  

```python
def compute_phrase (unigram, bigram, threshold = 0.5):
    N = sum (list (unigram.values ​​()))
    phrases = {}
    for bi, freq in bigram.items ():
        if freq> 1:
            v = bi [0]; w = bi [1]
            npmi = (log (N) + log (freq) --log (unigram [v]) --log (unigram [w])) \
                    / (log (N) --log (freq))
            if npmi> threshold:
                phrases [bi] = npmi
    return phrases
``` 
    
Threshold တန်ဖိုးက ဂျပန်စာအတွက်က 0.5 ထားပြီး စမ်းခဲ့ပေမဲ့ မြန်မာစာအတွက်က (0.1...0.5) ထားပြီး အမျိုးမျိုး စမ်းကြည့်ခဲ့ပါတယ်။  
အထက်ပါ algorithm ကို word segmentation လုပ်ထားတဲ့ မြန်မာစာ corpus တစ်ခုလုံးကို pass လုပ်ပြီးသွားတဲ့ အခါမှာ စာလုံးနှစ်လုံးတွဲ စကားစု (two-word phrase) တွေကို ရရှိလာမှာ ဖြစ်ပါတယ်။ တကယ်လို့ ဒုတိယအကြိမ် pass လုပ်ပြီးသွားရင်တော့ စာလုံး နှစ်လုံး ကနေ လေးလုံးအထိ တွဲလျက်ရှိနေတတ်တဲ့ စကားစု (two- to four-word phrase) တွေကို ရရှိလာမှာ ဖြစ်ပါတယ်။ အဲဒါကြောင့် သီအိုရီအရကတော့ passing ကို n pass အထိ လုပ်မယ် ဆိုရင် 2 ကနေ 2^n စာလုံးတွဲ phrase တွေကို ရရှိနိုင်မှာ ဖြစ်ပါတယ်။  

### Phrase Segmentation with "myWord" Segmentation Tool

လက်နဲ့စာလုံး ဖြတ်ထားတဲ့ (i.e. manual word segmentation) လုပ်ထားတဲ့ စာကြောင်းရေ ၅သိန်းကျော် ရှိတဲ့ မြန်မာစာ corpus ကို သုံးပြီး phrase segmentation experiment တချို့ လုပ်ကြည့်ကြရအောင်။  

Threshold value=0.1, frequency=3, 1 time pass အနေနဲ့ run ကြည့်ထားပါတယ်။  
 
```console
$ time python ./myword.py train_phrase -l 1 -t 0.1 -f 3 --unigram_phrase_txt unigram.l1.t0.1f3.txt --bigram_phrase_txt bigram.l1.t0.1f3.txt --unigram_phrase_bin unigram.l1.t0.1f3.bin --bigram_phrase_bin bigram.l1.t0.1f3.bin ./corpus2 ./train.l1t0.1f3.out
{'command': 'train_phrase', 'iteration': 1, 'threshold': 0.1, 'minfreq': 3, 'unigram_phrase_txt': 'unigram.l1.t0.1f3.txt', 'bigram_phrase_txt': 'bigram.l1.t0.1f3.txt', 'unigram_phrase_bin': 'unigram.l1.t0.1f3.bin', 'bigram_phrase_bin': 'bigram.l1.t0.1f3.bin', 'input': './corpus2', 'output': './train.l1t0.1f3.out'}
computing phrases: threshold = 0.1 minfreq = 3
pass [1/1]..
- computing phrases..
- writing output..
done.

real	1m4.555s
user	1m3.892s
sys	0m0.484s
```

pass က တစ်ခါပဲ လုပ်တာမို့ corpus ထဲမှာ ပါဝင်တဲ့ bigram စာလုံးတွဲတွေရဲ့ frequency ပေါ်မူတည်ပြီး threshold value ပေါ်ကို မူတည်ပြီး ဆွဲထုတ်လို့ ရလာတဲ့ မြန်မာစာ phrase ဥပမာ တချို့က အောက်ပါအတိုင်းပါ။  

```console
$ tail ./train.l1t0.1f3.out
သူ_ဟာ လက်ဝှေ့ပွဲ မှာ အနိုင်_ရ နိုင် စရာ_ရှိ တယ်
သူ_ဟာ လက်ဝှေ့ ထိုးသတ်ပွဲ မှာ_ရှုံးနိမ့် ဖို့_မ ဖြစ်_နိုင် လောက် ဘူး
သူငယ်_ကလေး ဟာ ငါး_မျှား နေ_တယ်
သူ ကံကောင်း ရင် ငါး တစ်_ကောင် မိ နိုင် တယ်
သစ်ကိုင်း ဟာ သိပ်_မ ခိုင် ဘူး
၎င်း ဟာ‍ ကျိုး ချင် ကျိုး_သွား နိုင် တယ်
သစ်ကိုင်း_ကျိုး ကျ_သွား ရင်_ကောင်ကလေး ဟာ မြစ်_ထဲ ကို ကျ_သွား ဖို့ အလားအလာ_ရှိ တယ်
သူ မြစ်_ထဲ ကို ကျ_သွား ရင် သူ ရေစို ဖို့ ဖြစ် ကောင်း ဖြစ်_နိုင် လိမ့်_မယ်
ရုပ်ပုံ ထဲ_မှာ ပျား တစ်_ကောင် ရှိ_တယ်
၎င်း ဘာ_လုပ် နိုင် မယ်_လို့ ခင်ဗျား ထင်_သလဲ
```

Threshold value=0.1, frequency=3, 2 time pass ထားပြီး run ထားပါတယ်။  
```console
$ time python ./myword.py train_phrase -l 2 -t 0.1 -f 3 --unigram_phrase_txt unigram.l2.t0.1f3.txt --bigram_phrase_txt bigram.l2.t0.1f3.txt --unigram_phrase_bin unigram.l2.t0.1f3.bin --bigram_phrase_bin bigram.l2.t0.1f3.bin ./corpus2 ./train.l2t0.1f3.out
{'command': 'train_phrase', 'iteration': 2, 'threshold': 0.1, 'minfreq': 3, 'unigram_phrase_txt': 'unigram.l2.t0.1f3.txt', 'bigram_phrase_txt': 'bigram.l2.t0.1f3.txt', 'unigram_phrase_bin': 'unigram.l2.t0.1f3.bin', 'bigram_phrase_bin': 'bigram.l2.t0.1f3.bin', 'input': './corpus2', 'output': './train.l2t0.1f3.out'}
computing phrases: threshold = 0.1 minfreq = 3
pass [1/2]..
- computing phrases..
- writing output..
pass [2/2]..
- computing phrases..
- writing output..
done.

real	1m38.575s
user	1m37.342s
sys	0m1.125s
```

ဒီတစ်ခါတော့ passing ကို နှစ်ခါ လုပ်ထားတာမို့ စာလုံး နှစ်လုံးတွဲ phrase တွေသာမကပဲ သုံးလုံးတွဲ၊ လေးလုံးတွဲ phrase တွေလည်း ဆွဲထုတ်လာနိုင်တာကို တွေ့ရပါလိမ့်မယ်။  

```console
$ tail ./train.l2t0.1f3.out 
သူ_ဟာ လက်ဝှေ့ပွဲ မှာ အနိုင်_ရ နိုင် စရာ_ရှိ_တယ်
သူ_ဟာ လက်ဝှေ့ ထိုးသတ်ပွဲ မှာ_ရှုံးနိမ့် ဖို့_မ_ဖြစ်_နိုင် လောက်_ဘူး
သူငယ်_ကလေး ဟာ ငါး_မျှား နေ_တယ်
သူ ကံကောင်း_ရင် ငါး_တစ်_ကောင် မိ နိုင်_တယ်
သစ်ကိုင်း ဟာ သိပ်_မ ခိုင် ဘူး
၎င်း ဟာ‍ ကျိုး ချင် ကျိုး_သွား နိုင်_တယ်
သစ်ကိုင်း_ကျိုး ကျ_သွား ရင်_ကောင်ကလေး ဟာ မြစ်_ထဲ_ကို ကျ_သွား ဖို့_အလားအလာ_ရှိ တယ်
သူ မြစ်_ထဲ_ကို ကျ_သွား ရင် သူ ရေစို ဖို့ ဖြစ် ကောင်း_ဖြစ်_နိုင် လိမ့်_မယ်
ရုပ်ပုံ_ထဲ_မှာ ပျား_တစ်_ကောင် ရှိ_တယ်
၎င်း ဘာ_လုပ် နိုင်_မယ်_လို့ ခင်ဗျား ထင်_သလဲ
```

Threshold value=0.1, frequency=1, 2 time pass ထားပြီး run ထားပါတယ်။  
```console
$ time python ./myword.py train_phrase -l 2 -t 0.1 -f 1 --unigram_phrase_txt unigram.l2.t0.1f1.txt --bigram_phrase_txt bigram.l2.t0.1f1.txt --unigram_phrase_bin unigram.l2.t0.1f1.bin --bigram_phrase_bin bigram.l2.t0.1f1.bin ./corpus2 ./train.l2t0.1f1.out
{'command': 'train_phrase', 'iteration': 2, 'threshold': 0.1, 'minfreq': 1, 'unigram_phrase_txt': 'unigram.l2.t0.1f1.txt', 'bigram_phrase_txt': 'bigram.l2.t0.1f1.txt', 'unigram_phrase_bin': 'unigram.l2.t0.1f1.bin', 'bigram_phrase_bin': 'bigram.l2.t0.1f1.bin', 'input': './corpus2', 'output': './train.l2t0.1f1.out'}
computing phrases: threshold = 0.1 minfreq = 1
pass [1/2]..
- computing phrases..
- writing output..
pass [2/2]..
- computing phrases..
- writing output..
done.

real	1m57.006s
user	1m55.366s
sys	0m1.373s
```

ဒီ တစ်ခါတော့ frequency ကို တစ်ကြိမ်ပါတာနဲ့ phrase အဖြစ် ထည့်သွင်းစဉ်းစားတဲ့အုပ်စုအထဲကို ဝင်လာမှာမို့ ဆွဲထုတ်ပြီး ရလာတဲ့ phrase တွဲတွေမှာ အပြောင်းအလဲ ဖြစ်လာတာကိုလည်း မြင်တွေ့ရမှာ ဖြစ်ပါတယ်။ ဥပမာ "ခင်ဗျား_ထင်_သလဲ" ကို phrase တစ်ခုအနေနဲ့ တွဲပေးသွားတာမျိုးပါ။  

```console
$ tail ./train.l2t0.1f1.out 
သူ_ဟာ_လက်ဝှေ့ပွဲ မှာ အနိုင်_ရ နိုင် စရာ_ရှိ_တယ်
သူ_ဟာ လက်ဝှေ့_ထိုးသတ်ပွဲ_မှာ_ရှုံးနိမ့် ဖို့_မ_ဖြစ်_နိုင် လောက်_ဘူး
သူငယ်_ကလေး_ဟာ ငါး_မျှား_နေ_တယ်
သူ_ကံကောင်း ရင် ငါး_တစ်_ကောင် မိ နိုင်_တယ်
သစ်ကိုင်း_ဟာ သိပ်_မ_ခိုင် ဘူး
၎င်း_ဟာ‍_ကျိုး ချင်_ကျိုး_သွား နိုင်_တယ်
သစ်ကိုင်း_ကျိုး ကျ_သွား_ရင်_ကောင်ကလေး ဟာ_မြစ်_ထဲ ကို ကျ_သွား ဖို့_အလားအလာ_ရှိ တယ်
သူ_မြစ်_ထဲ ကို ကျ_သွား ရင် သူ ရေစို_ဖို့ ဖြစ် ကောင်း_ဖြစ်_နိုင် လိမ့်_မယ်
ရုပ်ပုံ_ထဲ_မှာ ပျား_တစ်_ကောင် ရှိ_တယ်
၎င်း ဘာ_လုပ် နိုင်_မယ်_လို့ ခင်ဗျား_ထင်_သလဲ

```
Threshold value=0.1, frequency=3, 2 time pass ဆိုတဲ့ training နဲ့ပဲ corpus ထဲကနေ ရှည်တဲ့ စာကြောင်းတွေကို ကနေ ရလာတဲ့ phrase တွေကိုလည်း လေ့လာကြည့်ရင် အောက်ပါလိုမျိုး စိတ်ဝင်စားစရာကောင်းတဲ့ မြန်မာစာ phrase အတွဲတွေ ရနိုင်တာကို မြင်တွေ့ရပါလိမ့်မယ်။  

```console
$ shuf ./train.l2t0.1f3.out | head
ဒါ_ကြောင့်_က_ကျွန်တော် ဟာ ဩဇာ_လွှမ်းမိုး ရေး_လမ်းကြောင်း_ကို ပဲ လိုက် ခဲ့_တယ်_။
သီးခြား အကောင့်_တစ်_ခု နှင့်_ပူးတွဲ စာရင်း အကောင့်_ဖွင့် ထား_ခြင်း_သည် ငွေကြေး ပြဿနာ_အနည်းငယ် ကို_ကျော်လွှား ရန်_အမှန်တကယ် အထောက်အကူ_ပြု_နိုင် ပါ_တယ်_။
ဘယ်_သန် ဆို_ရင်_ကော 😝_😝_😜
မိန်းကလေး အတွက် လား_ဒါမှမဟုတ် ယောက်ျားလေး_အတွက် လား
ဝမ်းသာ_လိုက်_တာ ကိုရင်_တို့ ရယ်_၊ ဆွမ်း_ကွမ်း အပြင်_မှာ အခြား_ပစ္စည်း လေး_ပါး လည်း_လိုအပ် သမျှ_မိန့် ကြ_ပါ ၊_တပည့်တော်မ ကို ကုသိုလ် ပေး_ကြ_ပါ
ပျား ဆို_တဲ့_သတ္တဝါ လေး_တွေ_ဟာ သူ့_ဘာသာ_ဆို ဘာ_မှ_မ_လုပ် ပေ_မယ့် သူ နေ_တဲ့ အုံ_ကို များ သွား ထိမိ လိုက် လို့_က_တော့ အပြုံလိုက် ထွက်_လာ ပြီး_တုပ် တယ်_ဆို_တာ အားလုံး_သိ_ကြ မှာ_ပါ_။
နှုတ်ခမ်းနီ_လေး ဘယ်တော့_ရ_မလဲ ခု_လေး_တင် ဝယ်_လာ_တာ ပါ ကုန်_သွား မှာ_ဆိုး_လို့ ဘူး သေး ရော ဘူး ကြီး ရော_ဝယ် ခဲ့_တယ် ချစ်_သွား_ပြီ အဆင်ပြေ_လား_ကြိုက် လား_ရှင့် အသား_လတ် တယ်_ဆို နံပါတ်_၂၀_သုံး နော်
Football_Observatory ဆွန်ဟောင်မင် ကို_ယူရို_သန်း ၇ဝ_အနိမ့်ဆုံး_အပြောင်းအရွှေ့_ဈေး အဖြစ်_သတ်မှတ်_ဖော်ပြ_ထား ပါ_တယ်_။
ဟံသာဝတီ မြေ ကို_နင်း_မိ ပေ_ပြီ_။
၂၀၁၈_ခုနှစ် တရားမကြီး_မှု_အမှတ်_- ၃၅
```

ကိုယ်မှာက manual word segmentation လုပ်ထားတဲ့ corpus လည်း မရှိဘူး ဆိုရင်တော့ myword က version အလိုက် default အနေနဲ့ training လုပ်ပြီး သုံးထားတဲ့ dictionary ကိုပဲ သုံးပြီး phrase segmentation လုပ်ချင်တယ် ဆိုရင်တော့ အောက်ပါအတိုင်း command ပေးပါ။  

```console
$ python ./myword.py phrase ./test.space.txt ./test.phrase
{'command': 'phrase', 'threshold': 0.1, 'minfreq': 1, 'unigram_phrase_bin': 'unigram-phrase.bin', 'bigram_phrase_bin': 'bigram-phrase.bin', 'input': './test.space.txt', 'output': './test.phrase'}
computing phrases: threshold = 0.1 minfreq = 1
phrase segmentation...
- read unigram dictionary
- read bigram dictionary
- computing phrases..
- writing output..., filename:  ./test.phrase
done.
```

လက်ရှိ default ထားထားတဲ့ dictionary နဲ့ ဖြတ်ပြီး ရလာတဲ့ output က အောက်ပါအတိုင်းပါ။  

```console
$ cat ./test.phrase
ကျွန်တော်_က သုတေသန သမား ပါ_။
နေ့ ရော ည ရော_မြန်မာစာ နဲ့ ကွန်ပျူတာ_နဲ့ ပဲ အလုပ် များ ပါ_တယ်
မင်း_က ကော_ဘာ အလုပ်_လုပ် တာ_လဲ ။
ပြော_ပြ ပါ_အုံး
ကောဖီ လည်း ထပ်_သောက် ချင်_ရင် ပြော ကွာ
မန္တလေး_မှာ ဒေါ်_အောင်ဆန်းစုကြည် မိန့်ခွန်း_ပြော မယ် တဲ့ ။
```

⚠️ တစ်ခု သတိထားရမှာက input ဖိုင်က word ဖြတ်ထားတဲ့ ဖိုင်ကိုပေးမှသာ phrase အဖြစ် ဖြတ်ပေးမှာပါ ⚠️  

```console
$ cat test.space.txt 
ကျွန်တော် က သုတေသန သမား ပါ ။
နေ့ ရော ည ရော မြန်မာစာ နဲ့ ကွန်ပျူတာ နဲ့ ပဲ အလုပ် များ ပါ တယ်
မင်း က ကော ဘာ အလုပ် လုပ် တာ လဲ ။
ပြော ပြ ပါ အုံး
ကောဖီ လည်း ထပ် သောက် ချင် ရင် ပြော ကွာ
မန္တလေး မှာ ဒေါ် အောင်ဆန်းစုကြည် မိန့်ခွန်း ပြော မယ် တဲ့ ။
```

တကယ်လို့ ကိုယ့် word segmented corpus နဲ့ အမျိုးမျိုး training/experiment လုပ်ထားပြီး ကိုယ်သုံးချင်တဲ့ dictionary ကို command line argument အနေနဲ့ assign လုပ်ပြီး သုံးချင်တယ် ဆိုရင်တော့ အောက်ပါအတိုင်း run ပါ။  

```console
python ./myword.py phrase --unigram_phrase_bin ./unigram-phrase.bin --bigram_phrase_bin ./bigram-phrase.bin ./test2.txt ./test2.phrase
```

## Command-line Help

```$ python myword.py -h``` ဆိုပြီး command ပေးလိုက်ရင် myWord Segmentation Tool ရဲ့ "main-help screen" ကို မြင်ရမှာ ဖြစ်ပါတယ်။  
 
```console
$ python myword.py -h
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

ဒီ နေရာမှာ sub_option တစ်ခု ချင်းစီရဲ့ အလုပ်ကို အကြမ်းရှင်းရရင် အောက်ပါအတိုင်းပါ။  

- syllable (syllable segmentation လုပ်ဖို့အတွက် သုံးတဲ့ option ပါ)
- build_dict (unigram, bigram အဘိဓာန်တွေကို ဆောက်ဖို့အတွက် သုံးတဲ့ option ပါ)
- word (Viterbi algorithm ကို သုံးပြီ word segmentation လုပ်ဖို့အတွက် သုံးတဲ့ option ပါ)
- train_phrase (unigram, bigram စာလုံးအဘိဓာန် နှစ်ခုဆောက်ပြီး NPMI နဲ့ စကားလုံးတွဲတွေ သို့မဟုတ် phrase တွေကို ဆွဲထုတ်ဖို့အတွက် သုံးတဲ့ option ပါ)
- phrase (NPMI algorithm နဲ့ phrase segmentation လုပ်ဖို့အတွက် သုံးတဲ့ option ပါ)
- npmi_train (ဒီ option က NPMI algorithm နဲ့ training, segmentation ကို တကြိမ်ထက်မက လုပ်ဖို့အတွက် သုံးတဲ့ option ပါ)
 
"syllable", "build_dict", "word", "train_phrase", "phrase" and "npmi_train" option တစ်ခုချင်းစီအတွက် help screen ကို [command-line-help-of-myword](https://github.com/ye-kyaw-thu/myWord/blob/main/documentation/command-line-help-of-myword.md) page ကို ဝင်ရောက်ပြီး လေ့လာပါ။  

## Introduction to "npmi_train" Option

တကယ်က NPMI unsupervised approach နဲ့ phrase တွေသာ မကပဲ character sequence, syllable, sub_word, word စတဲ့ segmentation unit တွေကိုလည်း learn လုပ်ပြီး ဆွဲထုတ်ပေးနိုင်ပါတယ်။ အဲဒီအတွက် learning/segmentation အလုပ်ကို အမျိုးမျိုး experiment လုပ်နိုင်ဖို့အတွက် "npmi_train" ကို myWord Segmentation Tool ရဲ့ facility တစ်ခုအနေနဲ့ ထည့်ပေးထားတာပါ။   

နားလည်လွယ်အောင် corpus အသေးလေးတစ်ခုဆောက်ပြီးတော့ run ကြည့်ကြရအောင်။ ဆိုကြပါစို့ ကျွန်တော်တို့ရဲ့ corpus မှာက ငယ်ငယ်ကဆိုခဲ့ကြတဲ့ ကဗျာဆရာကြီး ဦးတင်မိုးရဲ့ "မမ ဝဝ" ကဗျာကို ရိုက်ထည့်ထားတဲ့ စာကြောင်းတွေရှိတယ်လို့။ တစ်ခုရှိတာက npmi_train နဲ့ learn လုပ်ဖို့က segmentation boundary တစ်ခုတော့ ပေးရမှာမို့ syllable တစ်ခုချင်းစီကို space ခြားပြီး ရိုက်ထည့်ထားပါတယ်။ အဲဒီ corpus ဖိုင်အသေးလေးက အောက်ပါအတိုင်းပါ။   
```console
$ cat ./mama_wawa_poem.txt
မ မ ဝ ဝ
ထ ထ က
အ က ပ ထ မ ။
က ပါ က ပါ
မ မ ရာ
ည ည လ သာ သာ
ည အ ခါ
ငါ စာ ရ
မ မ ဝ ဝ
ထ ထ က ။
```

myWord Segmentation Tool ရဲ့ npmi_train option ကို သုံးပြီးတော့ segmentation experiment အသေးလေးတစ်ခု လုပ်ကြည့်ကြရအောင်။  
- -lr သို့မဟုတ် --iteration_range ကို "1,2" ထားမယ်။ ဆွဲထုတ်မယ့် စာလုံး length က 2 to 4 ဆိုပြီး သတ်မှတ်ပေးလိုက်တာပါ။  
- -tr သို့မဟုတ် --threshold_range ကိုတော့ "0.1,0.1" ဆိုပြီး ထားလိုက်မယ်။ ဆိုလိုတာက corpus ကလည်း စာကြောင်းရေ ၁၀ကြောင်းပဲ ရှိပြီး အရမ်းသေးတာကြောင့် threshold value ကိုတော့ မကစားတော့ဘူး။  
- -fr သို့မဟုတ် --minfreq_range ကိုတော့ "2,3" ဆိုပြီး သတ်မှတ်လိုက်မယ်။ corpus ထဲမှာ အနည်းဆုံး နှစ်ခါ ကနေ သုံးခါကြား ပါမှပဲ phrase အဖြစ်သတ်မှတ်ဖို့ ထည့်သွင်းစဉ်းစားပါ လို့ setting လုပ်တာပါ။ ဒီနေရာမှာတော့ phrase ဆိုတာက syllable တွဲတွေ ပဲဖြစ်လာမှာပါ။ ဘာကြောင့်လဲ ဆိုတော့ input လုပ်မယ့် training corpus ထဲမှာ ဖြတ်ထားတာက အထက်မှာ ပြခဲ့သလို syllable breaking လုပ်ထားတာကြောင့်ပါ။  

တကယ်တမ်း run တဲ့အခါမှာတော့ အောက်ပါ အတိုင်း command ပေးပြီးတော့ myword.py ကို run ကြည့်ပါ။  
```
$ time python ./myword.py npmi_train -lr "1,2" -tr "0.1,0.1" -fr "2,3" ./mama_wawa_poem.txt 
```

corpus ကလည်း တအားသေးတာကြောင့် training လုပ်တဲ့ အချိန်က ၁စက္ကန့်အတွင်းမှာပဲ ပြီးသွားပါလိမ့်မယ်။  
learning လုပ်ပြီး ရလာတဲ့ စာလုံးတွေဖြတ်ပေးထားတဲ့ (i.e. segmented output file) ဖိုင်တွေကို command-line မှာ ရိုက်ထုတ်ပေးဖို့အတွက် အောက်ပါလိုမျိုး command ပေးလို့ ရပါတယ်။  
 
```bash
for i in mama_wawa_poem.txt.l{1..2}.t0.1.f{2..3}.seg;do echo -e "\n"$i":"; cat $i; done;
```

ပထမဆုံး အနေနဲ့ "l1.t0.1.f2" (i.e. iteration=1, threshold=0.1, minfreq=2) နဲ့ "l1.t0.1.f3" (i.e. iteration=1, threshold=0.1, minfreq=3) တို့နှစ်ခု အကြား ရလာတဲ့ segmented output ဖိုင် နှစ်ဖိုင်ကို side-by-side နှိုင်းယှဉ်ကြည့်ကြရအောင်။ Underscore "_" နဲ့ တွဲပေးထားတာက NPMI algorithm နဲ့ learn လုပ်ပြီး ရလာတဲ့ စာလုံးတွဲတွေပါ။ frequency=3 အဖြစ် တိုးလိုက်တဲ့အခါမှာ ဆွဲထုတ်နိုင်တဲ့ စာလုံးအရေအတွက်က နည်းသွားတာကို မြင်တွေ့ရပါလိမ့်မယ်။ အဲဒါကြောင့် "npmi_train" ကို သုံးပြီး phrase တွေကို ဆွဲထုတ်တဲ့ အခါမှာ frequency ဆိုတဲ့ setting ကလည်း ကိုယ့် corpus ရဲ့ ပမာဏအပေါ်ကို မူတည်ပြီး ချိန်ဆပြီးမှ သတ်မှတ်ပါ။  
 
<table>
<tr>
<th>mama_wawa_poem.txt.l1.t0.1.f2.seg</th>
<th>mama_wawa_poem.txt.l1.t0.1.f3.seg</th>
</tr>
<tr>
<td>
 
```
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
```
 
</td>
<td>

```
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
 
</td>
</tr>
</table> 

ဒီတစ်ခါတော့ အနေနဲ့ "l2.t0.1.f2" (i.e. iteration=2, threshold=0.1, minfreq=2) နဲ့ "l2.t0.1.f3" (i.e. iteration=1, threshold=0.1, minfreq=3) တို့နှစ်ခု အကြား NPMI က learn လုပ်ပြီး ရလာတဲ့ segmented output ဖိုင် နှစ်ဖိုင်ကို side-by-side နှိုင်းယှဉ်ကြည့်ကြရအောင်။ "iteration" ကို two pass လုပ်လိုက်တာကြောင့် syllable လေးလုံးတွဲစာလုံးတွေ အထိ ဆွဲထုတ်ယူလာနိုင်တာကို "mama_wawa_poem.txt.l2.t0.1.f2.seg" ဖိုင်ထဲမှာ ထင်ထင်ရှားရှား မြင်ရပါလိမ့်မယ်။ သို့သော် "min-freq" ကို "3" အဖြစ် ထားထားလိုက်တဲ့ အခါမှာတော့ corpus ထဲမှာက သုံးခါ မရှိတာကြောင့် syllable နှစ်လုံးတွဲစာလုံးတွေ (i.e. မ_မ) ကိုပဲ "mama_wawa_poem.txt.l2.t0.1.f3.seg" ဖိုင်ထဲမှာ ပါလာတာကို တွေ့ရပါလိမ့်မယ်။ ပြောရရင်တော့ "npmi_train" argument ကို သုံးတဲ့အခါမှာ option သုံးခုဖြစ်တဲ့ "--iteration_range", "--threshold_range" နဲ့ "--minfreq_range" သုံးခုစလုံးက အရေးကြီးပါတယ်။ အဲဒီ parameter သုံးခုအပေါ်ကို မူတည်ပြီးတော့ ရလာတဲ့ phrase တွေကလည်း အပြောင်းအလဲ ဖြစ်သွားမှာ ဖြစ်ပါတယ်။ Experiment ကို အမျိုးမျိုး လုပ်ကြည့်ကြပါလို့ အကြံပေးချင်ပါတယ်။     
 
<table>
<tr>
<th>mama_wawa_poem.txt.l2.t0.1.f2.seg</th>
<th>mama_wawa_poem.txt.l2.t0.1.f3.seg</th>
</tr>
<tr>
<td>

```
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
```

</td>
<td>

```
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

</td>
</tr>
</table> 
 
ဒီ README ဖိုင်မှာ မှတ်မိလွယ်ပြီးတော့ မြင်သာအောင် ရှင်းပြနိုင်ဖို့အတွက် တကယ်လုပ်ခဲ့တဲ့ "မမ ဝဝ" experiment log ဖိုင်ကို လည်းတင်ပေးထားပါတယ်။  
Link: [https://github.com/ye-kyaw-thu/myWord/blob/main/documentation/mama_wawa-exp1.md](https://github.com/ye-kyaw-thu/myWord/blob/main/documentation/mama_wawa-exp1.md)  
 
စာကြောင်းရေ တစ်ထောင်ရှိတဲ့ corpus နဲ့ စမ်းပြထားတာကိုလည်း လေ့လာနိုင်အောင် တင်ပေးထားပါတယ်။ အောက်ပါ link မှာ ဝင်ကြည့်ပါ။  
[https://github.com/ye-kyaw-thu/myWord/blob/main/documentation/npmi_train-option-test-with-1k-corpus.md](https://github.com/ye-kyaw-thu/myWord/blob/main/documentation/npmi_train-option-test-with-1k-corpus.md)    

 
## Dictionaries for Word and Phrase Segmentation
 
Current Version: Version 1.0  
 
Word အတွက်ရော Phrase အတွက်ရော default ဆောက်ပေးထားတဲ့ ngram dictionary တွေက ./dict_ver1/ ဆိုတဲ့ folder အောက်မှာ ရှိနေပါလိမ့်မယ်။  

### for Word Segmentation
 - unigram-word.bin
 - unigram-word.txt
 - bigram-word.bin
 - bigram-word.txt

### for Phrase Segmentation
 - unigram-phrase.bin
 - unigram-phrase.txt
 - bigram-phrase.bin
 - bigram-phrase.txt

⚠️ Segmentation လုပ်ဖို့အတွက်က Binary dictionary တွေကိုပဲ myWord Segmentation Tool က သုံးပါတယ်။  
☝ myWord Segmentation Tool ကို ကိုယ့်စက်ထဲမှာ download လုပ်ပြီးလို့ run မလုပ်ခင်မှာ combine-all-splitted-files.sh ကို အရင် run ဖို့ မမေ့ပါနဲ့။  
  (split-lt-24mb.sh က ဖိုင်တွေကို small ဖိုင်တွေအဖြစ်ခွဲဖို့အတွက် run ခဲ့တဲ့ script, ဒီ ဖိုင်က run စရာ မလိုဘူး)  
  
## Files and Folder Information

Coding ကို ဝင်ပြင်ချင်တဲ့ သူများအတွက်က...  
  
  - myword.py (main program of myWord Segmentation Tool)
  - phrase_segment.py (module for phrase segmentation and training with NPMI Algorithm)
  - syl_segment.py (module for syllable segmentation)
  - word_dict.py (module for word unit ngram dictionary building)
  - word_segment.py (module for word segmentation with Viterbi Algorithm)

myWord Segmentation Tool ကို download လုပ်ပြီးတာနဲ့ ကိုယ့်စက်ထဲမှာ testing လုပ်ကြည့်ဖို့အတွက် မြန်မာစာဒေတာဖိုင်တွေက...  
  
  - test1.txt (စာကြောင်း ခြောက်ကြောင်းပဲ ရှိတဲ့ မြန်မာစာ UTF-8 text ဖိုင်၊ space တွေကို စာကြောင်းတိုင်းလိုလို ဖြုတ်ထားပြီးသား)
  - test2.txt (word ဖြတ်ထားတဲ့ မြန်မာစာ UTF-8 text ဖိုင်၊ စာကြောင်း အရေအတွက်က စုစုပေါင်း အကြောင်း ၃၀ နဲ့ word အရေအတွက်က ၅၅၄လုံး ရှိတယ်)
  - mama_wawa_poem.txt (syllable segmentation ဖြတ်ထားတဲ့ ကဗျာဆရာကြီး ဦးတင်မိုးရဲ့ "မမ ဝဝ" ကဗျာဖိုင်ပါ။ npmi_train experiment အတွက် နမူနာ သုံးပြထားတဲ့ input ဖိုင်ပါ)  
  
လက်ရှိ Folder တွေနဲ့ ပတ်သက်ပြီး ပြောပြရရင်...  
  
  - dict_ver1/ (myWord corpus ကို သုံးပြီးတော့ ဆောက်ထားတဲ့ ngram dictionary version.1.0 ကို သိမ်းထားတဲ့ folder)
  - documentation/ (README ဖိုင်မှာ သုံးထားတဲ့ figures တွေ, experiment/running log files တချို့)
  - tools/ (ဒီ folder အောက်မှာတော့ preprocessing အလုပ်တို့၊ myWord Segmentation Tool ကို run ဖို့အတွက် ပြင်ရတာနဲ့ ဆိုင်တဲ့ script တွေ၊ input ဖိုင်အပေါ်ကို မူတည်ပြီး segmentation လုပ်ပြီးသွားတဲ့အခါမှာ ပိုနေတဲ့ space တွေရှိရင် space cleaning လုပ်ရတာမျိုးလည်း ရှိတတ်လို့... အသုံးဝင်နိုင်မယ့် script တွေကို ထည့်ပေးထားပါတယ်)   
  
## Evaluation of myWord for "Word Segmentation"
 
လက်ရှိ release မလုပ်ခင် စမ်းနေတဲ့ ngram dictionary တွေနဲ့ evaluation လုပ်ထားတဲ့ ရလဒ်တွေကိုလည်း လေ့လာလို့ ရအောင် README ဖိုင်မှာ တင်ပေးထားလိုက်ပါမယ်။
(အချိန်ရခဲ့ရင်တော့ ngram အဘိဓာန်တွေကို cleaning ထပ်လုပ်ပြီး တင်ဖို့ ရည်ရွယ်ထားပါတယ်။ အဲဒါဆိုရင် ရလဒ်တွေက လက်ရှိ ထက်တောင် ပိုကောင်းလာနိုင်ပါတယ်)
  
 
### Closed Test

"Closed testing" ဆိုတာက ngram အဘိဓာန်ကို ဆောက်တဲ့အချိန်မှာ သုံးထားတဲ့ corpus ထဲက စာကြောင်းတွေနဲ့ပဲ word segmentation လုပ်ကြည့်ပြီး test လုပ်တာ ဖြစ်ပါတယ်။
Closed test အတွက် သုံးခဲ့တဲ့ test ဖိုင်က စာကြောင်းရေ စုစုပေါင်း ၁၀၀၀ ပါ။ အသေးစိတ် information က အောက်ပါအတိုင်းပါ။    
 
 - 1000 (no. of sentences)
 - 38451 (no. of words)
 - 477524 (no. of characters)
 
```console
$ wc corpus2.1k
  1000  38451 477524 corpus2.1k
```

word segmentation လုပ်ပြီး ထွက်လာတဲ့ output ဖိုင်နဲ့ ပတ်သက်တဲ့ စာကြောင်းရေ အရေအတွက်၊ စာလုံးရေအရေအတွက်စတဲ့ information က အောက်ပါအတိုင်းပါ။  
```console
$ wc ./corpus2.1k.word 
  1000  40280 479353 ./corpus2.1k.word
```

Closed test အတွက် evaluation result တွေက အောက်ပါအတိုင်းပါ။  
 
```console
$ perl ./gradews.pl ./corpus2.1k ./corpus2.1k.word 
Sent Accuracy: 32.00% (320/1000)
Word Prec: 86.14% (34692/40275)
Word Rec: 90.24% (34692/38446)
F-meas: 88.14%
Bound Accuracy: 97.50% (141622/145257)
```

### Open Test
 
```console
$ time python ./myword.py word ./corpus2.shuf.open-test ./corpus2.shuf.open-test.word

real	6m45.903s
user	6m45.519s
sys	0m0.316s
```
 
open test ဒေတာက စာကြောင်းရေ စုစုပေါင်း 5,626 ကြောင်းရှိပြီးတော့ စာလုံးအရေအတွက်က 135,810 (တစ်သိန်း သုံးသောင်း ငါးထောင် ကျော်) ရှိပါတယ်။  

```console
$ wc ./corpus2.shuf.open-test
   5626  135810 1775923 ./corpus2.shuf.open-test
```
 
```console
$ wc ./corpus2.shuf.open-test.word 
   5626  144232 1784344 ./corpus2.shuf.open-test.word
```

input ဖိုင်ရဲ့ စာကြောင်းတချို့ကို ဥပမာအနနဲ့ ကြည့်နိုင်ဖို့အတွက် head command နဲ့ print လုပ်ထားပါတယ်။
 
```console
$ head ./corpus2.shuf.open-test
ညဉ့်
ငါ စဉ်းစား သလို စဉ်းစား ပါ ။
သူ့ ရဲ့ အပျက်အစီး ဘေး ပတ်ဝန်းကျင် မှာ ဒီ လို သာမန် ထက် မြင့်မား တဲ့ radiation level ကို တွေ့ ရ တာ ဒါ ပထမဆုံး အကြိမ် တော့ မ ဟုတ် ပါ ဘူး ။
ပရီးမီးယား လိဂ် သည် COVID - 19 ကြောင့် မတ် လ နောက်ပိုင်း ပြိုင်ပွဲ ရွှေ့ဆိုင်း ထား ရ သည် ။
သမိန်ဗြတ်ဇ
ကျွန်တော် က စိတ်ထား မ ကောင်း ခဲ့ လို့ လား
တိုက် ချင် လို့ တိုက် နေ တာ မ ဟုတ် ဘူး ကွ မင်း အမေ တွေ မင်း အစ်မ တွေ ကို တိုင်းတစ်ပါးသား တွေ က ဟင်း နော်
ညနေစာ ဆို ရင် ဂေါ်ဖီ စွပ်ပြုတ် နဲ့ သတ်သတ်လွတ် ဂျုံ ဝက်အူချောင်း နဲ့ ၊ ဟော ညလယ်စာ စား တော့ မယ် ဆို ရင် လည်း ဒီ အတိုင်း ပဲ ။
ကျွန်တော် ဘယ်သူ့ ကို မှာ ခဲ့ တာ လဲ
အထူးခြားဆုံး ကား သူ ၏ မျက်လုံး များ ပင် ။
```

myword segmentation tool က စာလုံးဖြတ်ပေးပြီးတော့ ထွက်လာတဲ့ oputput ဖိုင်ရဲ့ စာကြောင်း တစ်ချို့ကိုလည်း input လုပ်ခဲ့တဲ့ဖိုင်နဲ့ နှိုင်းယှဉ်ပြီး လေ့လာနိုင်အောင်လို့ head command သုံးပြီး print လုပ်ပေးထားပါတယ်။  
 
```console
$ head ./corpus2.shuf.open-test.word 
ညဉ့်
ငါ စဉ်းစား သလို စဉ်းစား ပါ ။
သူ့ ရဲ့ အပျက်အစီး ဘေး ပတ်ဝန်းကျင် မှာ ဒီ လို သာမန် ထက် မြင့်မား တဲ့ radiation level ကို တွေ့ ရ တာ ဒါ ပထမဆုံး အကြိမ် တော့ မ ဟုတ် ပါ ဘူး ။
ပရီးမီးယားလိဂ် သည် COVID-19 ကြောင့် မတ် လ နောက်ပိုင်း ပြိုင်ပွဲ ရွှေ့ဆိုင်း ထား ရ သည် ။
သမိန်ဗြတ်ဇ
ကျွန်တော် က စိတ် ထား မ ကောင်း ခဲ့ လို့ လား
တိုက် ချင် လို့ တိုက် နေ တာ မ ဟုတ် ဘူး ကွ မင်း အမေ တွေ မင်း အစ်မ တွေ ကို တိုင်း တစ် ပါး သား တွေ က ဟင်း နော်
ည နေ စာ ဆို ရင် ဂေါ်ဖီ စွပ်ပြုတ် နဲ့ သတ်သတ်လွတ် ဂျုံ ဝက်အူချောင်း နဲ့ ၊ ဟော ညလယ်စာ စား တော့ မယ် ဆို ရင် လည်း ဒီ အတိုင်း ပဲ ။
ကျွန်တော် ဘယ် သူ့ ကို မှာ ခဲ့ တာ လဲ
အထူးခြားဆုံး ကား သူ ၏ မျက်လုံး များ ပင် ။
```

Open test အတွက် evaluation result တွေက အောက်ပါအတိုင်းပါ။  

```console
$ perl ./gradews.pl ./corpus2.shuf.open-test ./corpus2.shuf.open-test.word 
Sent Accuracy: 33.99% (1912/5626)
Word Prec: 85.52% (123295/144179)
Word Rec: 90.81% (123295/135773)
F-meas: 88.08%
Bound Accuracy: 97.60% (531488/544530)
```

## Commands of myWord Segmentation Tool
 
အထက်မှာ syllable, word, phrase segmentation တွေနဲ့ ပတ်သက်ပြီး အသေးစိတ် ရှင်းပြခဲ့ပြီးသား ဖြစ်ပေမဲ့ advanced user တွေ၊ သုံးဖူးပြီးသားသူတွေက ရုတ်တရက် ကောက်သုံးတဲ့အခါမှာ အဆင်ပြေနိုင်စေဖို့အတွက် output တွေ ပြပေးမနေတော့ပဲ run ရမယ့် command တွေကိုပဲ ဒီနေရာမှ စုပြီးချရေးပေးထားပါတယ်။    
 
 <ins> **Syllable segmentation** </ins>  
 
 Syllable segmentation နဲ့ ဆိုင်တဲ့ command များ  
 
 - $ python myword.py syllable -h
 - $ python myword.py syllable one_line.txt one_line.syllable
 - $ python myword.py syllable -d "|" one_line.txt one_line.syllable
 
 <ins> **Word segmentation** </ins>  
 
 Word segmentation နဲ့ ဆိုင်တဲ့ command များ  
 
 - $ python myword.py word -h
 - $ python myword.py word one_line.txt one_line.word
 - $ python myword.py word -d "|" one_line.txt one_line.word
 - $ python myword.py word --unigram_word_bin ./dict_ver1/unigram-word.bin --bigram_word_bin ./dict_ver1/bigram-word.bin -d "/" one_line.txt one_line.word
 
 <ins> **Phrase segmentation** </ins>  
 
 Phrase segmentation အလုပ်နဲ့ ဆိုင်တဲ့ command များ  
 
 - $ python ./myword.py phrase -h
 - $ python ./myword.py phrase ./one_line.txt  ./one_line.phrase
 - $ python ./myword.py phrase --unigram_phrase_bin ./dict_ver1/unigram-phrase.bin --bigram_phrase_bin ./dict_ver1/bigram-phrase.bin ./one_line.txt  ./one_line.phrase
 
 <ins> **ngram dictionary building for word segmentation** </ins>
 
 ကိုယ့်မှာ ရှိတဲ့ corpus နဲ့ ngram အဘိဓာန်တွေ ဆောက်ပြီး word segmentation လုပ်မယ့် သူများအတွက်  
 
 - $ python myword.py build_dict -h
 - $ python ./myword.py build_dict ./corpus2.1k
 - $ python ./myword.py build_dict --unigram_word_txt ./unigram-word.txt --bigram_word_txt ./bigram-word.txt --unigram_word_bin ./unigram-word.bin --bigram_word_bin ./bigram-word.bin ./corpus2.1k

 <ins> **training for phrase segmentation** </ins>

 ကိုယ့်ဒေတာနဲ့ ကိုယ် manual word segmentation လုပ်ထားတဲ့ corpus သုံးပြီးတော့ ngram အဘိဓာန်တွေဆောက်မယ်၊ phrase တွေကို ဆွဲထုတ်ကြည့်ချင်တဲ့ သူများအတွက်   
 
 - $ python myword.py train_phrase -h
 - $ python ./myword.py train_phrase -l 2 -t 0.1 -f 3 --unigram_phrase_txt unigram.l2.t0.1f3.txt --bigram_phrase_txt bigram.l2.t0.1f3.txt --unigram_phrase_bin unigram.l2.t0.1f3.bin --bigram_phrase_bin bigram.l2.t0.1f3.bin ./corpus.txt ./corpus.l2t0.1f3.phrase
 - $ python ./myword.py train_phrase -l 2 -t 0.1 -f 2  ./corpus2.1k ./corpus2.1k.l2t0.1f2.phrase
 
 <ins> **Unsupervised segmentation experiment with NPMI** </ins>

 ကိုယ်လက်ထဲမှာ ရှိတဲ့ Corpus တစ်ခုခုကို သုံးပြီးတော့ NPMI training, x-unit segmentation နဲ့ ပတ်သက်တဲ့ experiment တွေကို လုပ်ကြည့်ချင်တဲ့ သူများအတွက်  
 
 - $ python myword.py npmi_train -h
 - $ python ./myword.py npmi_train -lr "1,2" -tr "0.1,0.1" -fr "2,3" ./mama_wawa_poem.txt

 
## Contributors
 
### For Developing myWord Corpus

myWord Corpus ကို သေသေချာချာ develop လုပ်ဖြစ်ခဲ့တာကတော့ အနည်းဆုံး ၄နှစ်လောက် ရှိနေပါပြီ။ စာကြောင်းတွေက ကျွန်တော်ကိုယ်တိုင် BBC, VOA က စုဆောင်းထားခဲ့တဲ့ သတင်းဆောင်းပါးတွေ၊ ကျောင်းသားတချို့နဲ့ အတူလုပ်ခဲ့တဲ့ NLP project တွေအတွက် ပြင်ဆင်ခဲ့ကြတဲ့ မြန်မာစာ စာကြောင်းတွေ၊ 2019 တုန်းက UTYCC မှာ သင်ကြားခဲ့တဲ့ NLP class က ကျောင်းသားတွေနဲ့ NLP Lab., UTYCC က member တွေကို manual word segmentation အတွေ့အကြုံရအောင် တစ်ယောက်ကို စာကြောင်းရေ တစ်ထောင်စီ ရှာဖွေ ဖြတ်ခိုင်းခဲ့တာတွေ... စသည်ဖြင့် အမျိုးမျိုးမို့လို့ ဒိုမိန်း အနေနဲ့က general domain ပါပဲ။ myWord Word Segmentation Corpus အတွက် ကူညီခဲ့တဲ့သူအားလုံးကို ကျေးဇူးတင်ကြောင်း ဒီနေရာကနေ ပြောကြားလိုပါတယ်။ နာမည်နောက်က လိုက်တဲ့ affiliation တွေက ကူညီခဲ့တဲ့အချိန်တုန်းက ရှိနေတဲ့ affiliation တွေပါ။ မှတ်မိသလောက် နာမည်တွေကို အောက်ပါအတိုင်း အက္ခရာအစီအစဉ်နဲ့ ချရေးပြီး မှတ်တမ်းတင်ပေးလိုက်ပါတယ်။ တကယ်လို့ ကူညီခဲ့ပြီးတော့ ဖော်ပြဖို့ကျန်ရစ်ခဲ့တဲ့ နာမည်တွေရှိရင်လည်း ခွင့်လွှတ်ပေးကြပါ။ corpus ထဲက ဒေတာတွေကို ပြန်စစ်ရင်း နာမည်တိုးဖို့လိုအပ်ရင်လည်း ထပ်တိုးသွားပါမယ်။    
 
 
|<!-- -->|<!-- -->|<!-- -->|
|:--- |:---- |:---- |
| 🌺 ကျော့ကေခိုင် (UTYCC, Myanmar)| 🌻 ကောင်းထက်စံ (NLP Lab., UTYCC, Myanmar) | 🌹ခင်ခန့်ခန့်လှိုင် (NLP Lab., UTYCC, Myanmar) |
| 🌱 ခင်ဝါဝါထိုက် (CSU, China) | 🌼 ခန့်ခန့်ဝင်းတင့် (UTYCC, Myanmar) | 🌸 ချိုဇင်ဦး (UTYCC, Myanmar) | 
|💐 ချိုဝါ (UTYCC, Myanmar) | 🌷 ခိုင်ဆုဝေ (UTYCC, Myanmar) | 🍀 ခိုင်ဇာမွန် (UTYCC, Myanmar) |
| 🌺 ဇွန်လှိုင်မိုး (UTYCC, Myanmar) | 🌻 ဇာဇာလှိုင် (KMITL, Thailand) | 🌹ထက်ရတနာဦး (NLP Lab., UTYCC, Myanmar) |
| 🌱 နန်းယုလှိုင် (UTYCC, Myanmar) | 🌼 နန်းရွှေစင်ဖူး (NLP Lab., UTYCC, Myanmar) | 🌸 နန်းအိန္ဒြေကျော် (UTYCC, Myanmar) |
| 💐 နှင်းယုလှိုင် (UTYCC, Myanmar) | 🌷 နှင်းအိအိချို (UTYCC, Myanmar) | 🍀 နှင်းအေးသန့် (UTYCC, Myanmar) |
| 🌺 နော်အလ်ထူးအေး (YEC4Blind, Myanmar) | 🌻 ပဒုမ္မာ (UTYCC, Myanmar) | 🌹 ဖြိုးသူထက် (NLP Lab., UTYCC, Myanmar) |
| 🌱 ဖြိုးဟေမာဝေ (UTYCC, Myanmar) | 🌼 ဖြူစင်ဌေး (NLP Lab., UTYCC, Myanmar) | 🌸 မျိုးမာသင်း (UTYCC, Myanmar) |
| 💐 မြင့်မြင့်ဌေး (UTYCC, Myanmar) | 🌷 မြတ်ငြိမ်းချမ်း (UTYCC, Myanmar) | 🍀 မြအိစံ (SIIT, Thailand) |
| 🌺 မှုံနံသာကျော် (NLP Lab., UTYCC, Myanmar) | 🌻 မေဇင်ထွန်း (NLP Lab., UTYCC, Myanmar) | 🌹 မေဖြိုးအောင် (UTYCC, Myanmar) |
| 🌱 မေဖြူခင် (UTYCC, Myanmar) | 🌼 မေမြတ်မြတ်ခိုင် (UTYCC, Myanmar) | 🌸 ရဲကျော်သိန်း (LU Lab., Myanmar) |
| 💐 လှလှဌေး (UCSY, Myanmar) | 🌷 လှသစ်ဝေ (NLP Lab., UTYCC, Myanmar) | 🍀 လှိုင်မေတင် (UTYCC, Myanmar) |
| 🌺 ဝင့်သိင်္ဂီ (YTU, Myanmar) | 🌻 ဝင်းသူဇာကျော် (Waseda Univ., Japan) | 🌹 ဝေနှင်းအိန္ဒြာမောင် (UTYCC, Myanmar) |
| 🌱 သဇင်မြင့်ဦး (UCSY, Myanmar) | 🌼 သီတာစန်း (UTYCC, Myanmar) | 🌸 ဟေမာန်ထွန်း (UTYCC, Myanmar) | 
| 💐 ဟေမာဖြိုး (NLP Lab., UTYCC, Myanmar) | 🌷 အိဖြူဖြူမွန် (UTYCC, Myanmar) | 🍀 အိသန္တာဖြူ (UTYCC, Myanmar) | 
| 🌺 အေးမြတ်သော်တာဦး (NLP Lab., UTYCC, Myanmar) | 🌻 ဥမ္မာထွန်း (Nagaoka Univ., Japan) | |

🐞 လှိုင်မြတ်နွယ် (NLP Lab., UTYCC, Myanmar) the highest contribution for myWord Corpus (Version 1.0) developing
 
### Coding and the Project Leader
 
 🐝 Ye Kyaw Thu (Visiting Professor, LST, NECTEC, Thailand)  
 
## To Do
 
- [ ] writing brief English README file
- [ ] adding sub_word unit for NMT
- [ ] upload Word Segmentation Guideline for Burmese (Myanmar language)
- [ ] automatic spelling checking running on myWord corpus
- [ ] adding Beam decoding
- [ ] evaluation tool for segmentation?!
- [ ] dealing punctuation characters
- [ ] -z,  --compress (enable compression of output e.g. zlib)  
- [ ] -s,  --split (Split segmented output file into small blocks)
- [ ] plan to support input with "folder" and "stdin"  

## License

myWord is MIT-licensed. The license applies to the pre-built unigram, bigram dictionaries as well.  
 
## Citation
 
Currently, please cite as:
 
```
myWord: Syllable, Word and Phrase Segmenter for Burmese, Ye Kyaw Thu, Sept 2021, GitHub Link: https://github.com/ye-kyaw-thu/myWord  
```
 
## Reference
 
1. Viterbi, Andrew. Error bounds for convolutional codes and an asymptotically optimum decoding algorithm. <i>IEEE transactions on Information Theory</i>, 13(2):260–269, 1967 [[Paper]](https://ieeexplore.ieee.org/document/1054010)
2. Slade, George. (2013). The Viterbi algorithm demystified. Link:[https://www.researchgate.net/publication/235958269_The_Viterbi_algorithm_demystified](https://www.researchgate.net/publication/235958269_The_Viterbi_algorithm_demystified) 
3. The Viterbi Algorithm Demystified, By Andrew J. Viterbi, March 16, 2017, Link: [https://viterbischool.usc.edu/news/2017/03/viterbi-algorithm-demystified/](https://viterbischool.usc.edu/news/2017/03/viterbi-algorithm-demystified/)
 4. Forney, G David. The Viterbi algorithm. <i>Proceedings of the IEEE</i>, 61(3):268–278, 1973, [https://www2.isye.gatech.edu/~yxie77/ece587/viterbi_algorithm.pdf](https://www2.isye.gatech.edu/~yxie77/ece587/viterbi_algorithm.pdf)
5. The Viterbi Algorithm at 50: [https://viterbischool.usc.edu/news/2017/03/viterbi-algorithm-50/](https://viterbischool.usc.edu/news/2017/03/viterbi-algorithm-50/)
6. Backurs, A. &amp; Tzamos, C.. (2017). Improving Viterbi is Hard: Better Runtimes Imply Faster Clique Algorithms. <i>Proceedings of the 34th International Conference on Machine Learning</i>, in <i>Proceedings of Machine Learning Research</i>, 70:311-321 [http://proceedings.mlr.press/v70/backurs17a/backurs17a.pdf](http://proceedings.mlr.press/v70/backurs17a/backurs17a.pdf)
7. Python implementation of Viterbi algorithm for word segmentation
A clean-up of this: [(http://norvig.com/ngrams/ch14.pdf)](http://norvig.com/ngrams/ch14.pdf), [https://gist.github.com/markdtw/e2a4e2ee7cef8ea6aed33bb47a97fba6](https://gist.github.com/markdtw/e2a4e2ee7cef8ea6aed33bb47a97fba6)
8. Python Word Segmentation: [https://github.com/grantjenks/python-wordsegment](https://github.com/grantjenks/python-wordsegment)
9. Beautiful Data, The Stories Behind Elegant Data Solutions, Toby Segaran, Jeff Hammerbacher, O'Reilly, 2009, Link: [https://github.com/jhulick/bookstuff/blob/master/Oreilly%20-%20Beautiful%20Data.pdf](https://github.com/jhulick/bookstuff/blob/master/Oreilly%20-%20Beautiful%20Data.pdf)
10. Viterbi Algorithm for HMM Decoding, Link:[https://www.cl.cam.ac.uk/teaching/1718/MLRD/slides/slides9.pdf](https://www.cl.cam.ac.uk/teaching/1718/MLRD/slides/slides9.pdf)  
11. Implement Viterbi Algorithm in Hidden Markov Model using Python and R Link: [http://www.adeveloperdiary.com/data-science/machine-learning/implement-viterbi-algorithm-in-hidden-markov-model-using-python-and-r/](http://www.adeveloperdiary.com/data-science/machine-learning/implement-viterbi-algorithm-in-hidden-markov-model-using-python-and-r/)
12. Yining Wang, Long Zhou, Jiajun Zhang and Chengqing Zong, Word, Subword or Character? An Empirical Study of Granularity in Chinese-English NMT, CoRR, abs/1711.04457, 2017. [[Paper]](https://arxiv.org/pdf/1711.04457.pdf)
13. Evaluation perl script for word segmentation: [https://raw.githubusercontent.com/neubig/nlptutorial/master/script/gradews.pl](https://raw.githubusercontent.com/neubig/nlptutorial/master/script/gradews.pl) 
14. Experiment Note by Assoc. Prof. Daichi Mochihashi: [http://chasen.org/~daiti-m/diary/](http://chasen.org/~daiti-m/diary/)  
15. Statistically recognize long phrases with Normalized PMI: [http://chasen.org/~daiti-m/diary/misc/phraser.py](http://chasen.org/~daiti-m/diary/misc/phraser.py)  
16. Vector Semantics: [https://courses.engr.illinois.edu/cs440/fa2018/lectures/lect36.html](https://courses.engr.illinois.edu/cs440/fa2018/lectures/lect36.html)  
17. Lecture 17: Vector-space semantics (distributional similarities), Julia Hockenmaier: [https://courses.engr.illinois.edu/cs447/fa2018/Slides/Lecture17HO.pdf](https://courses.engr.illinois.edu/cs447/fa2018/Slides/Lecture17HO.pdf)  
18. Pointwise_mutual_information: [https://en.wikipedia.org/wiki/Pointwise_mutual_information](https://en.wikipedia.org/wiki/Pointwise_mutual_information)  
19. Dr. Thein Tun, Acoustic Phonetics and The Phonology of the Myanmar Language
20. Romanization: https://en.wikipedia.org/wiki/Romanization
21. Myanmar Unicode: http://unicode.org/charts/PDF/U1000.pdf
22. Syllable segmentation algorithm of Myanmar text: http://gii2.nagaokaut.ac.jp/gii/media/share/20080901-ZMM%20Presentation.pdf
23. Zin Maung Maung and Yoshiki Makami,"A rule-based syllable segmentation of Myanmar Text", in Proceeding of the IJCNLP-08 workshop of NLP for Less Privileged Language, January, 2008, Hyderabad, India, pp. 51-58. [Paper](https://github.com/ye-kyaw-thu/sylbreak/blob/master/reference/I08-3010.pdf)
24. Tin Htay Hlaing, "Manually constructed context-free grammar for Myanmar syllable structure", in Proceedings of the Student Research Workshop at the 13th Conference of the European Chapter of the Association for Computational Linguistics (EACL '12), Association for Computational Linguistics, Stroudsburg, PA, USA, pp. 32-37. [Paper](https://github.com/ye-kyaw-thu/sylbreak/blob/master/reference/E12-3004.pdf)
25. Ye Kyaw Thu, Andrew Finch, Yoshinori Sagisaka and Eiichiro Sumita, "A Study of Myanmar Word Segmentation Schemes for Statistical Machine Translation", in Proceedings of the 11th International Conference on Computer Applications (ICCA 2013), February 26~27, 2013, Yangon, Myanmar, pp. 167-179. [Paper](https://github.com/ye-kyaw-thu/sylbreak/blob/master/reference/my2Others-CameraReady.pdf)
26. Ye Kyaw Thu, Andrew Finch, Win Pa Pa, and Eiichiro Sumita, "A Large-scale Study of Statistical Machine Translation Methods for Myanmar Language", in Proceedings of SNLP2016, February 10-12, 2016, Phranakhon Si Ayutthaya, Thailand. [Paper](https://github.com/ye-kyaw-thu/sylbreak/blob/master/reference/SNLP-3-A%20Large-scale%20Study%20of%20Statistical%20Machine%20Translation%20Methods%20for%20Myanmar%20Language.pdf)
27. Regular Expression: https://en.wikipedia.org/wiki/Regular_expression
25. DebuggexBeter: https://www.debuggex.com/  
28. Chenchen Ding, Ye Kyaw Thu, Masao Utiyama, Eiichiro Sumita: Word Segmentation for Burmese (Myanmar). ACM Trans. Asian Low Resour. Lang. Inf. Process. 15(4): 22:1-22:10 (2016)
27. Shaoning Zhang and Cunli Mao and Zhengtao Yu and Hongbin Wang and Z. Li and Jiafu Zhang, Word Segmentation for Burmese Based on Dual-Layer CRFs, ACM Transactions on Asian and Low-Resource Language Information Processing (TALLIP), Volume 18, 2019, pp. 1-11 
29. Burmese word segmentation program using Foma-generated Finite State Automata, Link: [https://github.com/lwinmoe/segment](https://github.com/lwinmoe/segment)  





