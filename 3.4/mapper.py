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
    print reResult.group().split()[1]
    #print re.match(regex,line).groups()[2].split()[1]
  else:
    None
    #print line           


