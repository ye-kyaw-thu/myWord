#!/bin/bash

# character segmentation
# Written by Ye, LST Lab., NECTEC, Thailand
# How to run: char-segmentation.sh <input-filename>
# For example:
# cat chk.tmp
# နန် ကော်ဖီ သော့-က့့့််် ဟှို့လား ဆိုဟှီး ငါ  ပြော ဇာ ။
#
# ./char-segmentation.sh ./chk.tmp
# န န ် က ေ ာ ် ဖ ီ သ ေ ာ ့ - က ် ့ ် ့ ် ့ ဟ ှ ိ ု ့ လ ာ း ဆ ိ ု ဟ ှ ီ း င ါ ပ ြ ေ ာ ဇ ာ ။ 
# By using ./char-segmentation.sh, now you can clearly seen "three athat and auk-ka-myint" typing mistake of a Dawei sentence

sed 's/\(.\)/\1 /g' $1 | sed 's/ \+/ /g';
