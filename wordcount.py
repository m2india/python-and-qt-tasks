#!/usr/bin/env python


import os.path


e_input = raw_input("Enter your file name ")

if os.path.isfile(e_input):
    e_input = open('text.txt','r')
    text = e_input.read()
    w_list = text.split()
    w_freq = [w_list.count(p) for p in w_list]

    
    dictionary = dict(zip(w_list,w_freq))
    va_u =  [(dictionary[key],key) for key in dictionary ]
    va_u.sort()
    va_u.reverse()
    for a in va_u:
        print a
else:
    print "Please enter your correct  file name"
