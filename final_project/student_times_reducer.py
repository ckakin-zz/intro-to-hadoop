#!/usr/bin/python
 
import sys

# counters used for calculations
currentId = None
currentCnt = None
currentHr = None
currentMaxCnt = None
maxHrs = None

## for logging
isLogOn = 0
counter = 0

for line in sys.stdin:

  thisId, thisHr =  line.strip().split("\t")
  thisId = thisId.split("_")[0]
  
  if isLogOn:
    print "Processing line {0}:\tid {1}\thr {2}".format(counter, thisId, thisHr)

  if not currentId:
    currentId = thisId
    currentHr = thisHr
    currentCnt = 1
    currentMaxCnt = 0
    maxHrs = []
  else:
    if thisId == currentId and thisHr == currentHr: 
      #id and hr both the same as previous line 
      currentCnt += 1
    else:
      # id or hour different from previous line
      if currentCnt > currentMaxCnt:
        maxHrs = [currentHr]
        currentMaxCnt = currentCnt
      elif currentCnt == currentMaxCnt:
        maxHrs.append(currentHr)
    
      if(currentId != thisId):
        # id different from previous line
        for hr in maxHrs:
          print "{0}\t{1}".format(currentId, hr)
        currentId = thisId
        currentMaxCnt = 0
        maxHrs = []
       
      currentCnt = 1
      currentHr = thisHr

  counter += 1

for hr in maxHrs:
  print "{0}\t{1}".format(currentId, hr)




