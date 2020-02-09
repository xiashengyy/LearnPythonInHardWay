#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from sys import argv
from os.path import exists

script, from_file, to_file = argv

print("Copying from %s to %s" % (from_file, to_file))
inputFile = open(from_file) 
indata = inputFile.read()

print("The input file is %d bytes long" % len(indata))
print("Does the output file exist? %r" % exists(to_file))
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

outputFile = open(to_file, 'w')
outputFile.write(indata)
print("Alright, all done.")

outputFile.close()
inputFile.close()

