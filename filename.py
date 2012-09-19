#!/usr/bin/env python


import os


if os.path.exists('/home/manimaran/Desktop/task'):
    
    print "dirctory is correct"
    
else:
    print "check your directroy"


name = raw_input("enter your file name  ")

if os.path.isfile("name"):
     
    
    a = open('text.txt','r')
    
    b = a.read()
    a.close()
    print b
else:
    print "file name is not corrct"