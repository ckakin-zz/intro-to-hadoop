#!/usr/bin/python

import sys
import csv
import operator

reader = csv.reader(sys.stdin, delimiter='\t')


for line in reader:
  node = line[0]
  author = line[3]
  type = line[5]
  absParent = line[7]

  if type == "question":
    print "{0}\t{1}".format(node, author)
  else:
    print "{0}\t{1}".format(absParent, author)

  


