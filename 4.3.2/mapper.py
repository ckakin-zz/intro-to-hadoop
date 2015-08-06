#!/usr/bin/python

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want elements 2 (store name) and 4 (cost)
# We need to write them out to standard output, separated by a tab

import sys
import re
import csv

reader = csv.reader(sys.stdin, delimiter='\t')

for line in reader:
  body = line[4].lower()
  words = re.split(r'[\s.,!\?:;"()<>\[\]#$=\-/]+', body)
  for word in words:
    if len(word) > 0:
      print "{0}\t{1}".format(word.strip(), line[0])
  
