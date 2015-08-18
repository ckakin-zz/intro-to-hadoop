#!/usr/bin/python
 
import sys

currentNode = None
authorList = []

for line in sys.stdin:

  thisNode, thisAuthor =  line.strip().split("\t")
  
  if thisNode != currentNode:
    if currentNode != None:
      print "{0}\t{1}".format(currentNode, authorList)
      authorList = []
    currentNode = thisNode
  authorList.append(thisAuthor)
   
print "{0}\t{1}".format(currentNode, authorList) 
    


