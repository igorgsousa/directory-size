#!/usr/bin/env python
# coding: utf-8


import os
import sys


def getSize(startPath = '.'):
    totalSize = 0
    for dirpath, dirnames, filenames in os.walk(startPath):
        for f in filenames:
            fp = os.path.join(dirpath,f)
            
            if not os.path.islink(fp):
                totalSize += os.path.getsize(fp)
    return totalSize
                
            

#C:\Program Files
homeDir = '\\\\?\\'+sys.argv[1]
print("Analisando "+sys.argv[1])
for simpleDir in os.listdir(homeDir):
    dir = os.path.join(homeDir,simpleDir)
    if os.path.isdir(dir):
        sizeInGB =  (((getSize(dir)/1024)/1024)/1024)
        print(simpleDir,' ',sizeInGB, 'GB')
    
