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
                
 
class Config:

    def __init__(self):
        self.directory = "."
        self.minSizeToShowInResult = -1

class Result:
    def __init__(self):
        self.size = 0
        self.errors = 0
        self.dir = ""

    def __init__(self, dir, size, errors):
        self.size = size
        self.errors = errors
        self.dir = dir              


def initArgs(args):
    
    ret = Config()


    for arg in args:
        if arg.startswith("--dir="):
            ret.directory = arg.replace("--dir=", "")
        elif arg.startswith("--min-size="):
            ret.minSizeToShowInResult = arg.replace("--min-size=", "")    


    return ret 

def printHeaderLine():

    folderNameCol = "Name"
    folderSizeCol = "SIZE"
    errorsCol = "ERRORS"
    line = "-"

    print(folderNameCol.ljust(80,' '),'|', folderSizeCol.ljust(40, ' '),'|',errorsCol.ljust(15, ' ') )
    print(line.rjust(137, '-'))

def printResultLine(result):

    print(result.dir.ljust(80,' '),'|', (str(result.size)+ ' GB').rjust(40, ' '),'|',str(result.errors).ljust(15, ' ') )

  
config = initArgs(sys.argv)

homeDir = '\\\\?\\'+config.directory
minSize = sys.argv[2] 
print('\n\n',"Analisando "+config.directory, '\n\n')

printHeaderLine() 

for simpleDir in os.listdir(homeDir):
    dir = os.path.join(homeDir,simpleDir)
    if os.path.isdir(dir):
        result = getSize(dir)
        sizeInGB =  (((result[0]/1024)/1024)/1024)

        resultFolder = Result(str(simpleDir), float(sizeInGB) , int(result[1]))

        if(int(config.minSizeToShowInResult) != -1):
            if(sizeInGB >= float(config.minSizeToShowInResult)):
                printResultLine(resultFolder)
        else:
            printResultLine(resultFolder)
        

    
