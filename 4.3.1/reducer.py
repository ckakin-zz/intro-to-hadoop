#!/usr/bin/python

import sys

pages = set()
oldWord = None
currentCount = 0


for line in sys.stdin:
    data_mapped = line.strip().split("\t")

    thisWord, thisPage = data_mapped

    if oldWord and oldWord != thisWord:
        print oldWord, "\t", currentCount
        oldWord = thisWord;
        currentCount = 0

    oldWord = thisWord
    currentCount += 1

if oldWord != None:
    print oldWord, "\t", currentCount

