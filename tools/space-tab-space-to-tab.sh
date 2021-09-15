#!/bin/bash

# Written by Ye, LST, NECTEC, Thailand
# Date: 15 Sept 2021
#
# for replacing <space><TAB><space> character sequence into <TAB>
# this shell script will be useful if you used myWord Segmentation Tool with following format
# label<TAB>string1<TAB>string2
# e.g. input file sentence:0 	 ၁ ၁ ဒေါ် လာ ကျ ပါ တယ် ။ 	 ၁ ၁ နာ ရီ လာ ခေါ် မယ် ။
# e.g. after you run this shell script, the output will be:0	၁ ၁ ဒေါ် လာ ကျ ပါ တယ် ။	၁ ၁ နာ ရီ လာ ခေါ် မယ် ။

sed -i $'s/ \t /\t/g' $1;

