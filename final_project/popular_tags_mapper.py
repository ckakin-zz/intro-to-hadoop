#!/usr/bin/python

import sys
import csv
import operator

reader = csv.reader(sys.stdin, delimiter='\t')

tagCnt = {}

for line in reader:
  tags = line[2]
  type = line[5]

  if type == "question":
    for tag in tags.split():
      if tag in tagCnt:
        tagCnt[tag] += 1
      else:
        tagCnt[tag] = 1 

#sortedTagCnt = sorted(tagCnt.items(), key=operator.itemgetter(1), reverse = True)[:10]

for key, val in tagCnt.items():
  print "{0}\t{1}".format(key, val)

