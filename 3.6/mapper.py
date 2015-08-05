#!/usr/bin/python

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want elements 2 (store name) and 4 (cost)
# We need to write them out to standard output, separated by a tab

import sys
import re

#regex = '([(\d\.)]+) - - \[(.*?)\] "(.*?)" (\d+) (.*?)'
regex = '"(.*?)"'

for line in sys.stdin:
  reResult = re.search(r'"GET .*"', line)
  if reResult != None:
    #None
    output = reResult.group().split()[1]
    output = re.sub(r'http://www.the-associates.co.uk', "", output)
    print output
  else:
    None
    #print line           


