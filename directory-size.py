#!/usr/bin/env python
# coding: utf-8


import os
import sys


def getSize(startPath = '.'):
    totalSize = 0
    errors = 0
    if not os.path.islink(startPath):
        for dirpath, dirnames, filenames in os.walk(startPath):
            for f in filenames:
                fp = os.path.join(dirpath,f)
                
                if not os.path.islink(fp):
                    try:
                            totalSize += os.path.getsize(fp)
                    except OSError as err:
                            #(print(err, ":", fp)
                            errors+=1         
    return (totalSize, errors)
                
            

#C:\Program Files
homeDir = '\\\\?\\'+sys.argv[1]
print("Analisando "+sys.argv[1])
for simpleDir in os.listdir(homeDir):
    dir = os.path.join(homeDir,simpleDir)
    if os.path.isdir(dir):
        result = getSize(dir)
        sizeInGB =  (((result[0]/1024)/1024)/1024)
        print(simpleDir,' ',sizeInGB, 'GB')
        print('Errors',result[1])
    
