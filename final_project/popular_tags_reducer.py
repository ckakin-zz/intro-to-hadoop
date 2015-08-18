#!/usr/bin/python
 
import sys
import operator

currentTag = None
currentCnt = 0
tagCnt = {}

for line in sys.stdin:

  thisTag, thisCnt =  line.strip().split("\t")
  thisCnt = int(thisCnt)
 
  if currentTag == thisTag:
    currentCnt += thisCnt
  else:
    if currentTag != None:
      tagCnt[currentTag] = currentCnt
      currentCnt = 0
    currentTag = thisTag
  
  currentCnt += thisCnt

tagCnt[currentTag] = currentCnt

sortedTagCnt = sorted(tagCnt.items(), key=operator.itemgetter(1), reverse = True)[:10]

for rec in sortedTagCnt:
  print "{0}\t{1}".format(rec[0], rec[1])


