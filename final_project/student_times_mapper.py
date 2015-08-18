#!/usr/bin/python

import sys
import re
import csv
from datetime import datetime

reader = csv.reader(sys.stdin, delimiter='\t')

for line in reader:
  authorId = line[3]
  if authorId.isdigit(): 
    addedAt = line[8][:-3]
    addedAtDate = datetime.strptime(addedAt, "%Y-%m-%d %H:%M:%S.%f") 
    print "{0}_{1}\t{1}".format(authorId, addedAtDate.hour)
