# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 09:37:53 2020

@author: justino
"""

file_path = "C:\\Users\\justino\\OneDrive\\#py_4_everyone\\"
file_name = "mbox-short.txt"

print(file_path + file_name)

fh = open(file_path + file_name)
for line in fh:
    line = line.rstrip()
    if not line.startswith('From '): continue
    words = line.split()
    print(words[2])