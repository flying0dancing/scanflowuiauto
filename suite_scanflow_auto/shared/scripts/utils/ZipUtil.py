# -*- coding: utf-8 -*-
from utils import FileUtil
import zipfile
import os
import test


'''
unzip files to unzipFolder, if unzipFolder=None, unzipFolder starts with extracFiles_
'''
def unzip(zipFile, unzipFolder=None):
    zip_file=zipfile.ZipFile(zipFile)
    if unzipFolder and os.path.isdir(unzipFolder):
        os.removedirs(unzipFolder)
    else:
        unzipFolder=os.path.join(os.path.dirname(zipFile),'extracFiles_'+FileUtil.getFileName(zipFile)[0])
    FileUtil.makedirs(unzipFolder)
    test.log(unzipFolder)
    if zipfile.is_zipfile(zipFile):
        for name in zip_file.namelist():
            zip_file.extract(name,unzipFolder)
    zip_file.close()

'''
unzip file which name=extractName to unzipFolder, if unzipFolder=None, unzipFolder starts with extracFiles_
@return: extract's file full name
'''  
def extractFile(zipFile, extractName, unzipFolder=None):
    zip_file=zipfile.ZipFile(zipFile)
    if unzipFolder and os.path.isdir(unzipFolder):
        os.removedirs(unzipFolder)
    else:
        unzipFolder=os.path.join(os.path.dirname(zipFile),'extracFiles_temp')#'extracFiles_'+FileUtil.getFileName(zipFile)[0]
    FileUtil.makedirs(unzipFolder)
    test.log(unzipFolder)
    if zipfile.is_zipfile(zipFile):
        for name in zip_file.namelist():
            if name.lower()==extractName.lower():
                zip_file.extract(name,unzipFolder)
                break
    zip_file.close()
    return os.path.join(unzipFolder,name)

def existBiteCatalog(zipFile):
    filePath=extractFile(zipFile, 'Version.ini')
    flag=FileUtil.existInFileContentByStr(filePath,'Bite',10)
    FileUtil.deleteFile(filePath)
    return flag
    
'''
@return the file names in zip file
'''
def getNamesOfZipFile(zipFile):
    nameList=[]
    zip_file=zipfile.ZipFile(zipFile)
    if zipfile.is_zipfile(zipFile):
        for name in zip_file.namelist():
            nameList.append(name)
    zip_file.close()   
    return nameList   





'''
inner func
'''
def getRefsFromZipFile(zipFile,acqCatalogsDict):
    acqIdentifiers=[]
    zip_file=zipfile.ZipFile(zipFile)
    if zipfile.is_zipfile(zipFile):
        for name in zip_file.namelist():
            #test.log(name)#Ref:bite/nobite,fullarch/onlylower/onlyupper,,,,,onlycommon/notonlycommon,shade/noshade
            if 'multiviews_' in name.lower():
                #test.log(name)
                tmpName=name.replace('.bin','')
                tmpName=tmpName.split('_')[1]
                if tmpName in acqCatalogsDict.keys() and 'notonlycommon' not in acqIdentifiers:
                    acqIdentifiers.append('notonlycommon')
                else:
                    acqIdentifiers.append(tmpName)
            #if 'Bite' in name and 'bite' not in acqIdentifiers:
                #acqIdentifiers.append('bite')
            if 'shadelibraries.bin' in name.lower():
                acqIdentifiers.append('shade')
        if existBiteCatalog(zipFile):
            acqIdentifiers.append('bite')
    test.log(str(acqIdentifiers)) 
    return acqIdentifiers
