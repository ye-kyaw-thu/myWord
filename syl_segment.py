#-*- coding:utf-8 -*- 
"""
Last updated: 21 July 2016
Written by Ye Kyaw Thu, Visiting Researcher, Waseda University
Homepage:https://sites.google.com/site/yekyawthunlp/

Reference of Myanmar Unicode: http://unicode.org/charts/PDF/U1000.pdf
"""

import os, sys, codecs
import fileinput
import argparse
import re
   
myConsonant = r"က-အ"
enChar = r"a-zA-Z0-9"
otherChar = r"ဣဤဥဦဧဩဪဿ၌၍၏၀-၉၊။!-/:-@[-`{-~\s"
ssSymbol = r'္'
aThat = r'်'

global delimiter

#Regular expression pattern for Myanmar syllable breaking
#*** a consonant not after a subscript symbol AND a consonant is not followed by a-That character or a subscript symbol
BreakPattern = re.compile(r"((?<!" + ssSymbol + r")["+ myConsonant + r"](?![" + aThat + ssSymbol + r"])" + r"|[" + enChar + otherChar + r"])", re.UNICODE)


def syllable(line):
    return BreakPattern.sub(delimiter + r"\1", line)

