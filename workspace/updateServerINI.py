#!/usr/bin/python
# -*- coding: UTF-8 -*-
import configparser
import os.path
import sys
def main(inputFile):
    files=getProductPath(os.path.expandvars('%ProgramFiles%/WindowsApps'),['DEXIS','ScanFlow'])
    productFullName=files[0]
    print(productFullName)
    productFullName_win="\""+productFullName.replace("\\","/")+"\""
    if os.path.isfile(inputFile):
        config = configparser.RawConfigParser()
        config.optionxform=lambda optionstr:optionstr #reserve options' lower/upper cases
        config.read(inputFile)
        general_sec='General'
        if config.has_section(general_sec):
            for key, value in config[general_sec].items():
                if key.lower() in  ['aut/scanflow_standalone','aut/scanflow']:
                    print("key %s, old value %s"%(key,value))
                    config.set(general_sec,key,productFullName_win)
                    print("key %s, new value %s" % (key, productFullName_win))

        else:
            config.add_section(general_sec)
            config.set(general_sec,'AUT/scanflow',productFullName_win)
            config.set(general_sec, 'AUT/scanflow_standalone', productFullName_win)
        config.write(open(inputFile, 'w'))


def getProductPath(parentFolder,keywordsList=['DEXIS','ScanFlow']):
    archiveFiles=[]
    if os.path.isdir(parentFolder):
        revFolder(parentFolder,keywordsList,archiveFiles)
    return archiveFiles

def revFolder(path,keywordsList,archiveFiles):
    subfolders=os.listdir(path)

    for subfolder in subfolders:
        subPath = os.path.join(path, subfolder)
        if not os.path.isdir(subPath):
            continue
        flag = True
        for keyword in keywordsList:
            if keyword not in subfolder:
                #print("keyword  %s not in subfolder %s" % (keyword, subfolder))
                flag = False
                break
        if flag==True:
            #subPath=os.path.join(path,subfolder)
            archiveFiles.append(subPath)
            #print(subPath)

if __name__=='__main__':
    print(str(sys.argv))
    inputFile=os.path.expandvars('%APPDATA%/froglogic/Squish/ver1/server.ini')
    main(inputFile)