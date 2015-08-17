#!/usr/bin/python

import sys
import re
import csv
from datetime import datetime

reader = csv.reader(sys.stdin, delimiter='\t')

for line in reader:
  nodeId = line[0]
  body = line[4]
  type = line[5]
  parent = line[6]

  if type == "question":
    print "{0}\t{1}\t{2}".format(nodeId, 0, len(body))
  elif type == "answer":
    print "{0}\t{1}\t{2}".format(parent, 1, len(body))
