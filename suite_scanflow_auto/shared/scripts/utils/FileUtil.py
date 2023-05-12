#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os, shutil, csv,logging,re
import json
import os.path
import sys
logger = logging.getLogger('utils.FileUtil')



"""
:return true or false
"""
def fileExist(fname):
    flag=False
    if not isEmptyStr(fname):
        if containsStr(fname,'*')>0:
            pass
        else:
            flag=os.path.exists(fname)
    return flag


def deleteFile(path):
    if fileExist(path) and os.path.isfile(path):
        logger.info("delete %s" % path)
        os.remove(path)
        
def cleanFileContent(path):
    if fileExist(path) and os.path.isfile(path):
        logger.info("clean content %s" % path)
        with open(path,'r+', encoding='utf-8', errors='ignore') as f:#for reading chinese charactors
            f.seek(0)
            f.truncate()
            f.write('')
              

def renameFile(src,dst):
    if fileExist(src):
        if fileExist(dst):
            deleteFile(dst)
        logger.info("copy file %s to %s" % (src,dst))
        try:
            shutil.copyfile(src, dst)
        except IOError as e:
            logger.error("Unable to copy file. %s" % e )
        except:
            logger.error("Unexpected error",sys.exc_info())

def makedirs(fpath):
    if not isEmptyStr(fpath):
        if not fileExist(fpath):
            os.makedirs(fpath)

def getFileName(fname):
    basename=''
    if fileExist(fname):
        basename=os.path.basename(fname)
        os.path.splitext(basename)
    return os.path.splitext(basename)

def getFileContentByStr(input,findstr):
    cached=[]
    with open(input,'r', encoding='utf-8', errors='ignore') as fileHd:#for reading chinese charactors
        for line in fileHd.readlines():
            line=line.strip()
            if line=='':
                continue
            if line.find(findstr)>-1:
                cached.append(line)
                print(line)
    return cached
'''
find some string in file content
@param filepath: a full file name
@param findstr: a str which need to find
@param lineCount: the line count means last lines of the file content
@return: return True or False, True means find the string, False means not find it
'''
def existInFileContentByStr(filepath,findstr,lineCount=10):
    flag = False
    strlist=getFileContentByStrList(filepath,[findstr],lineCount)
    if strlist:
        for astring in strlist:
            if astring.find(findstr) > -1:
                flag = True
                break

    return flag

'''
find some string in file content
@param filepath: a full file name
@param findlist: a str List which need to find
@param lineCount: the line count means last lines of the file content  
@return: last lines's file content 
'''
def getFileContentByStrList(filepath,findlist,linesCount=300):
    cached=[]
    rawlines=tail(filepath,linesCount)
    if findlist:
        for line in rawlines:
            line=str(line.strip())
            if line=='':
                continue
            for findstr in findlist:
                if findstr!='' and line.find(findstr)>-1:
                    cached.append(line)
                    print(line)
                    break

    else:
        logger.warning("find string List is empty.")
    return cached



#read last lines of a file
def tail(filepath, n, block=-1024):
    with open(filepath,'rb') as f:
        f.seek(0,2)
        filesize=f.tell()
        while True:
            if filesize>abs(block):
                f.seek(block,2)
                s=f.readlines()
                if len(s) >n:
                    return s[-n:]
                    #break
                else:
                    block *=2
            else:
                if filesize==abs(block):
                    return f.readlines()
                block=-filesize

    

"""
:return the position if (str1 in str), others -3(not run),-2(empty str),-1(not found)
"""
def containsStr(str,str1):
    flag=-3
    if( isEmptyStr(str) or isEmptyStr(str1)):
        flag=-2
    else:
        flag=str.find(str1)
    return flag



"""
:return true or false, string is None or '' or '  ' return true
"""
def isEmptyStr(str):
    flag=False
    if(str==None or str=='' or str.strip()==''):
        logger.debug("String is empty.")
        flag=True
    return flag

"""
default empty str to ''
"""
def defaultEmpty(str):
    if isEmptyStr(str):
        logger.debug("set default empty string to ''.")
        str=""
    return str

if __name__=='__main__':
    #print(str(sys.argv))
    #inputfile=r'C:\ProgramData\TW\AcqAltair\log\acqaltair_20220712.csv'
    inputfile=r'C:\ProgramData\DEXIS IS\ScanFlow\log\ScanFlow_20230201.csv'
    #main(inputfile)
    #print(tail(inputfile, 30))
    flag=existInFileContentByStr(inputfile, 'Save Scan Data, the result is OK.',300)
    print(flag)
    
def getParentFolder(filePath):
    parentFolder=os.path.dirname(os.path.abspath(filePath))#__file__
    basename=os.path.basename(parentFolder)
    return basename