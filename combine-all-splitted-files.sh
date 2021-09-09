#!/bin/bash

# for combining smaller splitted dictionaries into each original big file
# မြန်မာလို ရှင်းပြရရင်တော့ အောက်ပါ bigram အဘိဓာန်တွေက 25MB ထက် ကြီးလို့ 
# GitHub မှာ upload လုပ်တဲ့အခါမှာ ဖိုင်ကို 24MB ဖိုင်တွေအဖြစ် split command နဲ့ ခွဲပြီးတင်မှ ရတယ်
# bigram-phrase.bin,bigram-phrase.txt,bigram-word.bin,bigram-word.txt
# အဲဒါကြောင့် ကိုယ့်စက်ထဲကို git clone နဲ့ ဖြစ်ဖြစ် GitHub site ကနေ Download button နှိပ်ပြီး download လုပ်ပြီးသွားတဲ့အခါမှာ
# myWord ကို run မလုပ်ခင်မှာ ဒီ shell script ကို အရင် run ပြီး original dictionary အဖြစ် ပြောင်းပါ။
#
# Written by Ye Kyaw Thu, LST, NECTEC, Thailand
# How to run: bash ./combine-all-splitted-files.sh

for i in {bigram-phrase.bin,bigram-phrase.txt,bigram-word.bin,bigram-word.txt}
do
    cat $i.small.* > $i
done

rm *.small.*
