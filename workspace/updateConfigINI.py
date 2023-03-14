#!/usr/bin/python
# -*- coding: UTF-8 -*-
import configparser
import os.path
import sys
def updateConfig(inputFile,sectionStr,keyStr,valueStr):

    if os.path.isfile(inputFile):
        config = configparser.RawConfigParser()
        config.optionxform=lambda optionstr:optionstr #reserve options' lower/upper cases
        config.read(inputFile)
        if config.has_section(sectionStr):
            for key, value in config[sectionStr].items():
                if key.lower() in  [keyStr.lower()]:
                    print("key %s, value %s"%(key,value))
                    config.set(sectionStr,key,valueStr)
                    config.write(open(inputFile,'w'))

def getVersionFromFile(fname):
    versionStr=''
    if fname != '':
        versionStr=fname.split('_')[1]
        print(versionStr)
    return versionStr

def getFileNameByFolder(buildFolder):
    fname=''
    subfiles=os.listdir(buildFolder)
    for subfile in subfiles:
        sour=os.path.join(buildFolder, subfile)
        if 'ScanFlow_' in subfile and subfile.endswith('.msix') and os.path.isfile(sour):
            fname=subfile
            break
    return fname
def renameInstaller(buildFolder):
    subfiles=os.listdir(buildFolder)
    for subfile in subfiles:
        sour=os.path.join(buildFolder, subfile)
        if 'ScanFlow_' in subfile and subfile.endswith('.msix') and os.path.isfile(sour):
            print(subfile)
            break
    dest=os.path.join(buildFolder, 'scanflow.msix')
    if os.path.exists(dest) and os.path.isfile(dest):
        os.remove(dest)
    os.rename(sour, dest)

if __name__=='__main__':
    print(str(sys.argv))
    inputFile=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+"\\suite_scanflow_auto\\shared\\scripts\\Resources\\config.ini"
    buildFolder=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+"\\build"
    #main(inputFile,'test','test_mode','release')
    ver=getVersionFromFile(getFileNameByFolder(buildFolder))

    updateConfig(inputFile, 'product', 'ScanFlow_Version',ver)
    updateConfig(inputFile, 'test', 'test_mode', 'release')
    renameInstaller(buildFolder)
    #updateConfig(inputFile,sys.argv[1],sys.argv[2],sys.argv[3])