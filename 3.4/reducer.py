#!/usr/bin/python

import sys

currentCount = 0
currentKey = None

# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store

for line in sys.stdin:
   if currentKey and currentKey != line:
     print currentCount, ":", currentKey
     currentCount = 0
     
   currentKey = line
   currentCount += 1
   
print currentCount, ":", currentKey

