# Command-line Help of "myWord" Segmentation Tool

## Main Help Screen

```
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

အထက်မှာ မြင်ရတဲ့ အတိုင်းပါပဲ myword.py ကို run မယ်ဆိုရင် command-line ပေးရတဲ့ ပုံစံက အကြမ်းမျဉ်းအားဖြင့် အောက်ပါအတိုင်းပါ။  

```$ python myword.py {positional argument} ... <input-filename> <output-filename>```

ဆိုလိုတာက positional argument နေရာမှာ ကိုယ်လုပ်ချင်တဲ့ အလုပ်နဲ့သက်ဆိုင်တဲ့ argument ကို ပေးပြီး သူနောက်မှာတော့ သက်ဆိုင်ရာ option တွေကို ပေးသွားရတဲ့ ပုံစံဖြစ်ပါတယ်။  
option တွေရဲ့ နောက်မှာတော့ "input-filename" နဲ့ "output-filename" ကို ပေးကို ပေးရပါတယ်။ ခြွင်းချက် တစ်ခု အနေနဲ့ "npmi_train" option မှာတော့ "output-filename" က ပေးစရာ မလိုပါဘူး။ ပရိုဂရမ်က "pass-time", "threshold", "minimum-frequency" တွေကို အခြေခံပြီး "output-filename" ကို အော်တိုပေးသွားပြီး ဖိုင်အနေနဲ့ သိမ်းပေးသွားမှာ ဖြစ်ပါတယ်။   

နောက်တစ်ခု က coding ကို ဝင်ကြည့်ရင် သိနိုင်မှာဖြစ်ပေမဲ့ ... လက်ရှိ python code က Python version 3.0 နဲ့ အထက်နဲ့ run ရပါလိမ့်မယ်။ ဆိုလိုတာက python2.7 လို ဗားရှင်းနဲ့ run ရင် syntax error စတဲ့ minor error တွေ တက်လာပါလိမ့်မယ်။  

## syllable

မြန်မာ စာလုံးတွေကို syllable segmentation လုပ်ဖို့အတွက် ဆိုရင်တော့ myword.py ရဲ့ နောက်မှာ space ခြားပြီးတော့ "syllable" ဆိုတဲ့ argument ကို ပေးရပါလိမ့်မယ်။  

```
$ python myword.py syllable -h
usage: myword syllable [-h] [-d DELIMITER] input output

positional arguments:
  input                 input filename for word segmentation
  output                output filename

optional arguments:
  -h, --help            show this help message and exit
  -d DELIMITER, --delimiter DELIMITER
                        the delimiter option for syllable unit e.g. using
                        piple "|", the default delimiter is "space"
```

README ဖိုင်မှာလည်း example running လုပ်ပြထားသလို syllable segmentation အတွက်က အောက်ပါအတိုင်း command ပေးပါ။  

```
$ python myword.py syllable input output
```
input နေရာမှာ ကိုယ်က syllable ဖြတ်ချင်တဲ့ မြန်မာစာတွေရိုက်ထားတဲ့ text ဖိုင်ရဲ့နာမည် ကို ပေးရမှာ ဖြစ်ပြီးတော့...  
output နေရာမှာတော့ syllable ဖြတ်ပြီးတော့ ထွက်လာတဲ့ output ဖိုင်ကို သိမ်းစေချင်တဲ့ ဖိုင်နာမည်ကို ရိုက်ထည့်ပေးရမှာ ဖြစ်ပါတယ်။  
syllable ဖြတ်တဲ့အခါမှာ default delimiter ကတော့ space ဖြစ်လို့ syllable တစ်လုံးနဲ့ တစ်လုံးအကြားမှာ space နဲ့ ခြားပြီး ဖြတ်ပေးပါလိမ့်မယ်။ တကယ်လို့ ကိုယ်က အကြောင်းတစ်ခုခုကြောင့် space ကို မသုံးချင်ဘူး ဆိုရင်တော့ ကိုယ်သုံးချင်တဲ့ delimiter ကို -d သို့မဟုတ် --delimiter ဆိုတဲ့ option နဲ့ ပေးလို့ ရပါတယ်။ ဥပမာ pipe character နဲ့ ခြားပေးစေချင်ရင် ```--delimiter "|"``` ဆိုပြီး ပေးပါ။ တကယ်လို့ underscore နဲ့ ခြားပေးစေချင်ရင် ```-d "_"``` ဆိုပြီး ပေးလို့ရပါတယ်။  

**NLP လုပ်နေတဲ့ သူတွေ အများစုကတော့ သိပြီးသားဖြစ်မှာ ဖြစ်ပေမဲ့၊ တချို့ မသိသေးတဲ့ သူတွေလည်း ရှိနိုင်လည်း ဖြည့်စွက်ပြောရရင် input လုပ်တဲ့ ဖိုင်က UTF-8 encoding နဲ့ သိမ်းထားတဲ့ text ဖိုင်ဖြစ်မှ ရပါလိမ့်မယ်။ Microsoft Winword (.docx, doc) ဖိုင်တို့လို့ LibreOffice Writer တို့ရဲ့ (.odt) ဖိုင်တို့ကို input အနေနဲ့ပေးရင် segmentation ကို မှန်မှန်ကန်ကန် လုပ်ပေးမှာ မဟုတ်ပါဘူး။**  

## build_dict

ကိုယ်မှာ manual word segmentation သေသေချာချာ လုပ်ထားတဲ့ စာကြောင်းရေအရေအတွက်ကိုလည်း အများကြီး သိမ်းထားတဲ့ corpus ဖိုင် ရှိရင်တော့ အဲဒီ corpus ဖိုင်ကိုသုံးပြီးတော့ မြန်မာစာလုံးတွေကို ဖြတ်ဖို့အတွက် ပြင်ဆင်ရတဲ့ အဆင့်တစ်ခု ဖြစ်တဲ့ unigram, bigram အဘိဓာန်တွေကို ဆောက်မယ်ဆိုရင်တော့ အောက်မှာ ရိုက်ပြထားတဲ့အတိုင်း python myword.py ရဲ့ နောက်မှာ "build_dict" ဆိုတဲ့ command-line argument ကို ပေးပြီး သုံးရပါလိမ့်မယ်။  

```
$ python myword.py build_dict -h
usage: myword build_dict [-h] [-ut UNIGRAM_WORD_TXT] [-bt BIGRAM_WORD_TXT]
                         [-ub UNIGRAM_WORD_BIN] [-bb BIGRAM_WORD_BIN]
                         input

positional arguments:
  input                 input filename for training

optional arguments:
  -h, --help            show this help message and exit
  -ut UNIGRAM_WORD_TXT, --unigram_word_txt UNIGRAM_WORD_TXT
                        set output filename of the unigram word dictionary
                        (text-file), the default name is "unigram-word.txt"
  -bt BIGRAM_WORD_TXT, --bigram_word_txt BIGRAM_WORD_TXT
                        set output filename of the bigram word dictionary
                        (text-file), the default name is "bigram-word.txt"
  -ub UNIGRAM_WORD_BIN, --unigram_word_bin UNIGRAM_WORD_BIN
                        set output filename of the unigram word dictionary
                        (binary-file), the default name is "unigram-word.bin"
  -bb BIGRAM_WORD_BIN, --bigram_word_bin BIGRAM_WORD_BIN
                        set output filename of the bigram word dictionary
                        (binary-file), the default name is "bigram-word.bin"
```

build_dict နဲ့အတူ တွဲသုံးရတဲ့ option တွေကို အထက်မှာလည်း အင်္ဂလိပ်လို ရှင်းပြထားပေမဲ့ myword segmentation tool ကို သုံးကြတဲ့ user တွေအတွက် အဆင်ပြေအောင် မြန်မာလိုလည်း ဖြည့်စွက်ရှင်းပြရရင် အောက်ပါအတိုင်းပါ။  

- -ut (သို့) --unigram_word_txt (unigram အဘိဓာန်ဖိုင်ကို text ဖိုင်အနေနဲ့ သိမ်းတဲ့အခါမှာ သိမ်းပေးစေချင်တဲ့ ဖိုင်နာမည်ကို ပေးဖို့အတွက်ပါ)   
- -bt (သို့) --bigram_word_txt (bigram အဘိဓာန်ဖိုင်ကို text ဖိုင်အနေနဲ့ သိမ်းတဲ့အခါမှာ သိမ်းပေးစေချင်တဲ့ ဖိုင်နာမည်ကို ပေးဖို့အတွက်ပါ)  
- -ub (သို့) --unigram_word_bin (unigram အဘိဓာန်ဖိုင်ကို binary ဖိုင်အနေနဲ့ သိမ်းတဲ့အခါမှာ သိမ်းပေးစေချင်တဲ့ ဖိုင်နာမည်ကို ပေးဖို့အတွက်ပါ)   
- -bb (သို့) --bigram_word_bin (bigram အဘိဓာန်ဖိုင်ကို binary ဖိုင်အနေနဲ့ သိမ်းတဲ့အခါမှာ သိမ်းပေးစေချင်တဲ့ ဖိုင်နာမည်ကို ပေးဖို့အတွက်ပါ)  

Linux command-line တွေရဲ့ ထုံးစံအတိုင်း option တွေကို အတိုပေးတာမျိုး (e.g. -ut)၊ အရှည်ပေးတာမျိုး (e.g. --unigram_word_txt) အဆင်ပြေသလို သုံးကြပါ။  
 
## word

unigram, bigram အဘိဓာန်တွေက ရှိပြီးသားအခြေအနေမှာ မြန်မာစာလုံးတွေကို word segmentation လုပ်ဖို့အတွက်ဆိုရင်တော့ "python myword.py" ရဲ့ နောက်မှာ "word" ဆိုတဲ့ option ကို ပေးပြီး run ပါ။  
word နဲ့ တွဲသုံးတဲ့ တခြား option တွေကို အောက်မှာ ပြထားတဲ့အတိုင်း ```python myword.py word -h``` ဆိုပြီး ခေါ်ကြည့်ရင် help-screen ပြပေးပါလိမ့်မယ်။  

```
$ python myword.py word -h
usage: myword word [-h] [-d DELIMITER] [-ub UNIGRAM_WORD_BIN]
                   [-bb BIGRAM_WORD_BIN]
                   input output

positional arguments:
  input                 input filename for word segmentation
  output                output filename

optional arguments:
  -h, --help            show this help message and exit
  -d DELIMITER, --delimiter DELIMITER
                        the delimiter option for word unit e.g. using piple
                        "|", the default is "space"
  -ub UNIGRAM_WORD_BIN, --unigram_word_bin UNIGRAM_WORD_BIN
                        set filename of the unigram word dictionary for
                        segmentation (binary-file), the default name is
                        "unigram-word.bin"
  -bb BIGRAM_WORD_BIN, --bigram_word_bin BIGRAM_WORD_BIN
                        set filename of the bigram word dictionary for
                        segmentation (binary-file), the default name is
                        "bigram-word.bin"
```

တစ်ခု သိထားစေချင်တာက myWord Segmentation Tool မှာက word segmentation ကို လုပ်တဲ့အခါမှာပဲဖြစ်ဖြစ်၊ phrase segmentation ကို လုပ်တဲ့ အခါမှာပဲဖြစ်ဖြစ် text ဖိုင်နဲ့ ဆောက်ထားတဲ့ unigram, bigram အဘိဓာန်တွေကို မသုံးပါဘူး။ အလုပ်လုပ်ရတာ ပိုမြန်ဆန်အောင် binary file-format နဲ့ သိမ်းထားတဲ့ အဘိဓာန်တွေကိုပဲ သုံးပါလိမ့်မယ်။ အဲဒါကြောင့် word argument နဲ့ တွဲပြီး ပေးရတဲ့ အဘိဓာန်နဲ့ ဆိုင်တဲ့ option တွေက binary အတွက်ပဲ ရှိတာ ဖြစ်ပါတယ်။  

- -ub သို့မဟုတ် --unigram_word_bin ဆိုတဲ့ option နဲ့ unigram binary word dictionary ဖိုင်နာမည်ကို ပေးပါ
- -bb သို့မဟုတ် --bigram_word_bin ဆိုတဲ့ option နဲ့ bigram binary word dictionary ဖိုင်နာမည်ကို ပေးပါ
- -d သို့မဟုတ် --delimiter ကတော့ စာလုံးဖြတ်ပေးတဲ့ boundary ကို ကိုယ်သုံးချင်တဲ့ character ကို သုံးဖို့အတွက် သုံးတဲ့ option ပါ

**တစ်ခုရှိတာက binary dictionary ဖိုင်နာမည်တွေကို မပေးရင် myWord Segmentation Tool နဲ့အတူ တွဲပါလာတဲ့ လက်ရှိ binary word dictionary (latest version) ကို အသုံးပြုသွားမှာ ဖြစ်ပါတယ်**

## train_phrase

train_phrase ဆိုတဲ့ argument ကတော့ phrase segmentation လုပ်ဖို့အတွက် ကြိုတင်ပြင်ဆင်တဲ့ အခါမှာ သုံးတဲ့ option ပါ။ ဒီ option ကို သုံးမယ် ဆိုရင်တော့ ကိုယ့်ဆီမှာ manual word segmentation ဖြတ်ထားတဲ့ corpus က အဆင့်သင့်ရှိနေရမှာဖြစ်ပါတယ်။ အဲဒီလို ရှိတယ်ဆိုရင်တော့ "train_phrase" option ကို သုံးပြီးတော့ NPMI (Normalized Pointwise Mutual Information) algorithm နဲ့ unigram, bigram အဘိဓာန်တွေကိုလည်း pass တစ်ခေါက်တိုင်းမှာ စာလုံးရေအတွဲကို တိုးတိုးဆောက်သွားပြီးတော့ (-l 2 ဆိုရင် training corpus ကို နှစ်ခေါက် pass လုပ်ပြီး၊ စာလုံးတွဲကလည်း နှစ်လုံးကနေ လေးလုံးတွဲအထိ ရှာမှာ) input corpus ကိုပဲ phrase segmentation လုပ်ပေးသွားမှာ ဖြစ်ပါတယ်။  

```
$ python myword.py train_phrase -h
usage: myword train_phrase [-h] [-l ITERATION] [-t THRESHOLD] [-f MINFREQ]
                           [-ut UNIGRAM_PHRASE_TXT] [-bt BIGRAM_PHRASE_TXT]
                           [-ub UNIGRAM_PHRASE_BIN] [-bb BIGRAM_PHRASE_BIN]
                           input output

positional arguments:
  input                 input filename for training
  output                output filename

optional arguments:
  -h, --help            show this help message and exit
  -l ITERATION, --iteration ITERATION
                        the number of training iterations, the default is 2
  -t THRESHOLD, --threshold THRESHOLD
                        set the threshold value, the default is 0.1
  -f MINFREQ, --minfreq MINFREQ
                        set the minimum frequency value, the default is 3
  -ut UNIGRAM_PHRASE_TXT, --unigram_phrase_txt UNIGRAM_PHRASE_TXT
                        set output filename of the unigram dictionary (text-
                        file), the default name is "unigram-phrase.txt"
  -bt BIGRAM_PHRASE_TXT, --bigram_phrase_txt BIGRAM_PHRASE_TXT
                        set output filename of the bigram dictionary (text-
                        file), the default name is "bigram-phrase.txt"
  -ub UNIGRAM_PHRASE_BIN, --unigram_phrase_bin UNIGRAM_PHRASE_BIN
                        set output filename of the unigram dictionary (binary-
                        file), the default name is "unigram-phrase.bin"
  -bb BIGRAM_PHRASE_BIN, --bigram_phrase_bin BIGRAM_PHRASE_BIN
                        set output filename of the bigram dictionary (binary-
                        file), the default name is "bigram-phrase.bin"
```

အဘိဓာန် ဖိုင်နာမည်တွေနဲ့ ပတ်သက်တဲ့ option တွေကတော့ အထက်မှာ ရှင်းပြခဲ့တဲ့အတိုင်းပါပဲ။ unigram, bigram အဘိဓာန်တွေကို ကိုယ်သိမ်းပေးစေချင်တဲ့ နာမည်တွေကို ပေးဖို့အတွက် သုံးတာ ဖြစ်ပါတယ်။ training လုပ်သွားရင်းနဲ့ အဘိဓာန်တွေကို text ဖိုင်အနေနဲ့ရော binary ဖိုင်အနေနဲ့ရော သိမ်းပေးသွားမှာဖြစ်လို့ အောင်အောင်မြင်မြင်နဲ့ phrase learning လုပ်ပြီးသွားတယ် ဆိုရင် စုစုပေါင်း အဘိဓာန်က လေးဖိုင် အနေနဲ့ output လုပ်ပေးမှာ ဖြစ်ပါတယ်။ text ဖိုင်ကတော့ researcher တွေ developer တွေအနေနဲ့ ngram value တွေ ngram word တွေကို မျက်လုံးနဲ့ ကြည့်ပြီး ပြင်စရာရှိရင် ပြင်နိုင်ဖို့အတွက် ထုတ်ပေးထားတာ ဖြစ်ပါတယ်။ binary file-format နဲ့ ထွက်လာတဲ့ အဘိဓာန် နှစ်ဖိုင် (i.e. unigram, bigram) ကတော့ နောက်ပိုင်းမှာ ဆက်ပြောမယ့် phrase segmentation လုပ်တဲ့အခါမှာ သုံးရတဲ့ option ဖြစ်တဲ့ "phrase" နဲ့ တွဲသုံးဖို့အတွက် ပြင်ဆင်ထားတာ ဖြစ်ပါတယ်။  

**တစ်ခု သိထားစေချင်တာက pass တစ်ခု ပြီးသွားတိုင်းမှာ dictionary လေးခုစလုံးကို overwrite လုပ်သွားမှာ ဖြစ်ပါတယ်။ training လုပ်နေတာမို့ နောက်ဆုံး pass ရဲ့ dictionary တွေကိုပဲ ရလဒ်အနေနဲ့ ရလာမှာ ဖြစ်ပါတယ်။ တကယ်လို့ experiment အနေနဲ့ training အမျိုးမျိုးလုပ်သွားရင်းနဲ့ segmentation လုပ်ပေးတဲ့ output တွေကိုလည်း ကြည့်ချင်တယ်၊ သိမ်းထားချင်တယ် ဆိုရင်တော့ npmi_train ဆိုတဲ့ option နဲ့ run ရမှာ ဖြစ်ပါတယ်။**

လက်ရှိ ပြောနေတဲ့ "train_phrase" argument နဲ့တွဲသုံးတဲ့ option တွေအထဲမှာမှ NPMI algorithm ကို တကယ်နားလည်ပြီး၊ setting လုပ်ပေးရတဲ့ အရေးကြီးတဲ့ option သုံးခုနဲ့ သူတို့ရဲ့ အခန်းကဏ္ဍက အောက်ပါအတိုင်းပါ။  

- -l သို့မဟုတ် --iteration (training corpus ကို ဘယ်နှစ်ခါ pass လုပ်မှာလည်း ဆိုတဲ့ option ပါ။ တနည်းအားဖြင့် phrase ရဲ့ length အရှည်အတိုကလည်း ဒီ option နဲ့ သက်ဆိုင်ပါတယ်)
- -t သို့မဟုတ် --threshold (NPMI algorithm က ဆုံးဖြတ်ချက်ချတဲ့အခါမှာ သုံးတဲ့ threshold value ကို setting လုပ်ဖို့အတွက် သုံးတဲ့ option ပါ)
- -f သို့မဟုတ် --minfreq (minimum frequency ကို သတ်မှတ်ဖို့အတွက် သုံးတဲ့ option ပါ)
 **frequency ရဲ့ တန်ဖိုးက ကိုယ့် training corpus ထဲမှာက စာကြောင်းရေ ဘယ်နှစ်ကြောင်းပါသလဲ ဆိုတဲ့ အပေါ်ကို မူတည်ပြီးတော့ လည်း စဉ်းစားဆုံးဖြတ်ရပါလိမ့်မယ်။ မဟုတ်ရင် frequency က များနေပြီး တကယ်တမ်း ကိုယ့် corpus ထဲမှာက အဲဒီ သတ်မှတ်ထားတဲ့ အကြိမ်အရေအတွက် မရှိရင် phrase အနေနဲ့ တွဲပေးမှာ မဟုတ်ပါဘူး**  

myWord Segmentation Tool မှာ လက်ရှိ "-l", "-t", "-f" အတွက် setting လုပ်ပေးထားတဲ့ default value တွေက training လုပ်ထားတဲ့ corpus ဖိုင်ပေါ်ကို မူတည်ပြီး လုပ်ခဲ့တဲ့ experiment တွေရဲ့ ရလဒ်တွေကို ကြည့်ပြီးတော့ အကောင်းဆုံးလို့ ယူဆထားတဲ့ တန်ဖိုးတွေကို ထားထားပေး ထားတာ ဖြစ်ပါတယ်။ ကိုယ် domain အပေါ်မှာ၊ ကိုယ့် training corpus အပေါ်မှာ မူတည်ပြီး လေ့လာပြီး ပေးသွားရမယ့် setting တွေဖြစ်လို့ အရေးကြီးပါတယ်။   

## phrase

"phrase" positional argument ကတော့ မြန်မာစာလုံးတွေကို phrase အနေနဲ့ ဆွဲထုတ်ဖို့ တနည်းအားဖြင့် phrase segmentation လုပ်ဖို့အတွက် သုံးတာပါ။  
သူနဲ့အတူ တွဲသုံးရတဲ့ option တွေကို ကြည့်ချင်ရင်တော့ အောက်မှာလည်း ရိုက်ပြထားတဲ့အတိုင်း ```python myword.py phrase -h``` ဆိုတဲ့ command နဲ့ help-screen ခေါ်ကြည့်ပါ။  

```
$ python myword.py phrase -h
usage: myword phrase [-h] [-t THRESHOLD] [-f MINFREQ] [-ub UNIGRAM_PHRASE_BIN]
                     [-bb BIGRAM_PHRASE_BIN]
                     input output

positional arguments:
  input                 input filename for phrase segmentation
  output                output filename

optional arguments:
  -h, --help            show this help message and exit
  -t THRESHOLD, --threshold THRESHOLD
                        set the threshold value, the default is 0.1
  -f MINFREQ, --minfreq MINFREQ
                        set the minimum frequency value, the default is 3
  -ub UNIGRAM_PHRASE_BIN, --unigram_phrase_bin UNIGRAM_PHRASE_BIN
                        set filename of the unigram dictionary for
                        segmentation (binary-file), the default name is
                        "unigram-phrase.bin"
  -bb BIGRAM_PHRASE_BIN, --bigram_phrase_bin BIGRAM_PHRASE_BIN
                        set filename of the bigram dictionary for segmentation
                        (binary-file), the default name is "bigram-phrase.bin"
```

phrase ဖြတ်ဖို့အတွက်က binary format နဲ့ ဆောက်ထားတဲ့ unigram, bigram အဘိဓာန်တွေ လိုအပ်ပါတယ်။  
--threshold, --minfreq တို့ကို option အနေနဲ့ မပေးရင် default value တွေဖြစ်တဲ့ --threshold 0.1 နဲ့ --minfreq 3 တို့နဲ့ phrase segmentation လုပ်ပေးပါလိမ့်မယ်။  
ထိုနည်းလည်းကောင်း --unigram_phrase_bin, --bigram_phrase_bin အဘိဓာန် နာမည်တွေကို ရိုက်မထည့်ပဲ run မယ်ဆိုရင် default dictionary ဖိုင်နာမည်တွေ ဖြစ်တဲ့ "unigram-phrase.bin" တို့ "bigram-phrase.bin" တို့နဲ့ မြန်မာစာလုံးတွဲတွေ (i.e. phrase) ကို ဖြတ်ပေးပါလိမ့်မယ်။  

## npmi_train

ဒီ "npmi_train" argument ကတော့ advanced user တွေအတွက် ရည်ရွယ်ပါတယ်။  
တကယ်က train_phrase နဲ့ အခြေခံအားဖြင့်က အတူတူပါပဲ။ မတူတာက တစ်ခေါက်တည်း training လုပ်ဖို့အတွက် မဟုတ်ပဲ iteration, threshold နဲ့ frequency တို့ကို အမျိုးမျိုး အပြောင်းအလဲ လုပ်ပြီးတော့ x-unit segmentation experiment လုပ်နိုင်ဖို့အတွက် ရည်ရွယ်ပါတယ်။  

```
$ python myword.py npmi_train -h
usage: myword npmi_train [-h] [-lr ITERATION_RANGE] [-tr THRESHOLD_RANGE]
                         [-fr MINFREQ_RANGE]
                         input

positional arguments:
  input                 input filename for training

optional arguments:
  -h, --help            show this help message and exit
  -lr ITERATION_RANGE, --iteration_range ITERATION_RANGE
                        the training iterations range (e.g. "1,5"), the
                        default is "1,3"
  -tr THRESHOLD_RANGE, --threshold_range THRESHOLD_RANGE
                        set the threshold value range (e.g. "0.1,0.5"), the
                        default is "0.1,0.3"
  -fr MINFREQ_RANGE, --minfreq_range MINFREQ_RANGE
                        set the minimum frequency value range (e.g. "1,5"),
                        the default is "1,3"
```

iteration, threshold နဲ့ minimum-frequency တို့ကို train_phrase တုန်းကလို တစ်ခုချင်းစီ သတ်မှတ်ပြီး run တာမဟုတ်ပဲနဲ့ range ပေးပြီး run ကြရပါလိမ့်မယ်။ option တွေရဲ့ နာမည်တွေလည်း အပြောင်းအလဲ ဖြစ်သွားတာကို ဂရုပြုပါ။ "npmi_train" အတွက်က အောက်ပါအတိုင်း အဓိက option သုံးခု ရှိပါတယ်။  

- -lr သို့မဟုတ် --iteration_range က iteration ကို ဘယ်လောက်က စတင်ပြီး ဘယ်လောက်အထိ တိုးသွားမလဲ ဆိုတာနဲ့ ပတ်သက်ပါတယ်။ ဥပမာ "--iteration_range "1,5" ဆိုရင် pass လုပ်သွားမှာက 1-pass, 2-pass, 3-pass, 4-pass, 5-pass ဆိုပြီး passing အသီးသီး လုပ်သွားမှာ ဖြစ်ပါတယ်။  
- -tr သို့မဟုတ် --threshold_range ကလည်း threshold value ကို ဘယ်နှစ်မျိုးကစားပြီး training လုပ်မယ် ဆိုတဲ့ range ကို ပြောပေးဖို့ သုံးတဲ့ option ပါ။ ဥပမာ "--threshold value "0.1,0.5" ဆိုရင် 0.1, 0.2, 0.3, 0.4, 0.5 ဆိုပြီး threshold value ကို ၅မျိုး ကစားပြီး training လုပ်ပေးမှာ ဖြစ်ပါတယ်။ ကိုယ့် corpus ရဲ့ အနေအထားပေါ်မူတည်ပြီးတော့ ဒီ threshold value ကလည်း အပြောင်းအလဲ ဖြစ်နိုင်တာမို့ အမျိုးမျိုး ကစားကြည့်ပြီး segmentation output တွေကို ကြည့်ပြီး သင့်တော်တာကို ရှာဖွေရမှာ ဖြစ်ပါတယ်။   
- -fr သို့မဟုတ် --minfreq_range ကိုလည်း range တစ်ခုပေးပြီး သတ်မှတ် ပေးရပါမယ်။ ဥပမာ "--minfreq_range 1, 3"  

input ဖိုင်ကတော့ training လုပ်မယ့် corpus ဖိုင်ရဲ့ နာမည်ပါ။ x-unit training/segmentation လို့ ပြောရတဲ့ အကြောင်းအရင်းက syllable ဖြတ်ထားတဲ့ input ဖိုင်နဲ့ training လုပ်ရင် syllable တွဲတွေကို phrase ပုံစံအနေနဲ့ ဆွဲထုတ်သွားမှာ ဖြစ်သလို word segmentation ဖြတ်ထားတဲ့ ဖိုင်နဲ့ training လုပ်ရင် word တစ်လုံးထက်မက တွဲနိုင်တာတွေကို တွဲပြီး phrase အနေနဲ့ ဆွဲထုတ် ပေးမှာ ဖြစ်ပါတယ်။ အဲဒါကြောင့် NPMI နဲ့ training အမျိုးမျိုး လုပ်ကြည့်ကြပြီး syllable အတွဲတွေ၊ character တွဲတွေ sub_word unit အတွဲတွေ၊ phrase အတွဲတွေ စသည်ဖြင့် segmentation မျိုးစုံကို study လုပ်လို့ ရမှာ ဖြစ်ပါတယ်။  

output ဖိုင်နာမည်ကို ပေးစရာမလိုပါဘူး။ myWord Segmentation Tool က ပေးလိုက်တဲ့ -lr, -tr, -fr option တွေနဲ့ original input ဖိုင်နာမည်ကို ကြည့်ပြီး training တစ်ခုစီအတွက် ဖိုင်နာမည်တစ်ခုစီ နဲ့ unigram, bigram အဘိဓာန်တွေကို သိမ်းပေးသွားပါလိမ့်မယ်။ ဥပမာ unigram.l2.t0.1f3.txt, unigram.l2.t0.1f3.bin, bigram.l2.t0.1f3.txt, bigram.l2.t0.1f3.bin, ...  

စိတ်ဝင်စားသူတွေက ဥပမာအနေနဲ့ တင်ပေးထားတဲ့ [NPMI training/segmentation log](https://github.com/ye-kyaw-thu/myWord/blob/main/documentation/npmi_train-option-test-with-1k-corpus.md) ဖိုင်ကို အသေးစိတ် လေ့လာကြည့်ကြပါ။   
