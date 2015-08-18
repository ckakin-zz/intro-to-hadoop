#!/usr/bin/python
 
import sys
from decimal import Decimal

currentNode = None
questionLength = 0
totalAnsLength = 0
answerCount = 0

for line in sys.stdin:

  thisNode, thisType, thisLength =  line.strip().split("\t")
 
 
  if thisNode != currentNode and currentNode != None:
    print "{0}\t{1}\t{2}".format(currentNode, questionLength, 0 if answerCount == 0 else round(Decimal(totalAnsLength) / answerCount, 2))
    questionLength = 0
    totalAnsLength = 0
    answerCount = 0  

  if thisType == "0":
    questionLength = int(thisLength)
  elif thisType == "1":
    totalAnsLength += int(thisLength)
    answerCount += 1

  currentNode = thisNode

print "{0}\t{1}\t{2}".format(currentNode, questionLength, 0 if answerCount == 0 else round(Decimal(totalAnsLength) / answerCount, 2))



