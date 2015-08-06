#!/usr/bin/python

import sys

pages = set()
oldWord = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")

    thisWord, thisPage = data_mapped

    if oldWord and oldWord != thisWord:
        print oldWord, "\t", sorted(pages)
        oldWord = thisWord;
        pages.clear()

    oldWord = thisWord
    try: 
      pages.add(int(thisPage))
    except ValueError:
      None

if oldWord != None:
    print oldWord, "\t", sorted(pages)

