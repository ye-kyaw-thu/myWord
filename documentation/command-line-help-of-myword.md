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


## syllable

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

## build_dict

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

## word

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

## train_phrase

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

## phrase

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

## npmi_train

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
