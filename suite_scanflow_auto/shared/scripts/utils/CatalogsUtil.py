# -*- coding: utf-8 -*-
from utils import ZipUtil, DateTimeUtil

acqDict={'3':'Scanbody Lower','4':'Scanbody Upper','6':'Preparation Lower','7':'Preparation Upper',
              '8':'Edentulous Lower','9':'Edentulous Upper','130':'Emergence Profile Lower','131':'Emergence Profile Upper',
              '140':'Denture Lower','141':'Denture Upper'} #not include common for judged flag=notonlycommon or not.

'''
def acqCatalogsDict():
        acqDict={'3':'Scanbody Lower','4':'Scanbody Upper','6':'Preparation Lower','7':'Preparation Upper',
              '8':'Edentulous Lower','9':'Edentulous Upper','130':'Emergence Profile Lower','131':'Emergence Profile Upper',
              '140':'Denture Lower','141':'Denture Upper'}
        return acqDict
'''

def getRefList(zipFile):
    return ZipUtil.getRefsFromZipFile(zipFile,acqDict)
    

'''
outer func
'''
def getRefs(zipFile):
    acqIdentifiers=ZipUtil.getRefsFromZipFile(zipFile,acqDict)
    
    return setRefsString(acqIdentifiers)
'''
inner func
'''
def setRefsString(acqIdentifiers):
    #ScanRef: data/nodata,Ref:bite/nobite,fullarch/onlylower/onlyupper
    reflist=['data']#0:lower,1:upper
    if '0' in acqIdentifiers:
        if '1' in acqIdentifiers:
            if 'bite' in acqIdentifiers:
                reflist.append('fullarch')
            else:
                reflist.append('fullarchwithoutbite')
        else:
            reflist.append('onlylower')
    else:
        if '1' in acqIdentifiers:
            reflist.append('onlyupper')
        else:
            reflist.remove('data')
            reflist.append('nodata')
            #common doesn't contains data, maybe only edentulous
    
    if 'bite' in acqIdentifiers:
        reflist.append('bite')
    else:
        if 'fullarchwithoutbite' in reflist:
            pass
        else:
            reflist.append('nobite')
    
    if 'shade' in acqIdentifiers:
        reflist.append('shade')
    else:
        reflist.append('noshade')
    if 'notonlycommon' in acqIdentifiers:
        reflist.append('notonlycommon')
    else:
        reflist.append('onlycommon')
    refStr=','.join(reflist)
    scanRef=refStr.replace(',notonlycommon', '').replace(',onlycommon', '').replace(',noshade', '').replace(',shade', '')
    refineRef=refStr.replace(',nodata', '').replace(',data', '')
    return (scanRef,refineRef)

def setRefsString1(acqIdentifiers):
    #ScanRef: data/nodata,Ref:bite/nobite,fullarch/onlylower/onlyupper
    reflist=['data']#0:lower,1:upper
    if '0' in acqIdentifiers:
        if '1' in acqIdentifiers:
            reflist.append('fullarch')
        else:
            reflist.append('onlylower')
    else:
        if '1' in acqIdentifiers:
            reflist.append('onlyupper')
        else:
            reflist.remove('data')
            reflist.append('nodata')
            #common doesn't contains data, maybe only edentulous
    
    if 'bite' in acqIdentifiers:
        reflist.append('bite')
    else:
        reflist.append('nobite')
    
    if 'shade' in acqIdentifiers:
        reflist.append('shade')
    else:
        reflist.append('noshade')
    if 'notonlycommon' in acqIdentifiers:
        reflist.append('notonlycommon')
    else:
        reflist.append('onlycommon')
    refStr=','.join(reflist)
    scanRef=refStr.replace(',notonlycommon', '').replace(',onlycommon', '').replace(',noshade', '').replace(',shade', '')
    refineRef=refStr.replace(',nodata', '').replace(',data', '')
    return (scanRef,refineRef)

def containsOtherWorkflows(acqIdentifiers):
    flag=False
    if containsDenture(acqIdentifiers):
        flag=True
    elif containsImplant(acqIdentifiers):
        flag=True
    elif containsPreparation(acqIdentifiers):
        flag=True
    return flag

def isNotOnlyCommon(acqIdentifiers):
    flag=True
    if 'notonlycommon' in acqIdentifiers:
        flag=True
    else:
        flag=False
    return flag

def containsDenture(acqIdentifiers):
    flag=False
    #denture['8','9','140','141']
    if '8' in acqIdentifiers:
        flag=True
    elif '9' in acqIdentifiers:
        flag=False
    elif '140' in acqIdentifiers:
        flag=True
    elif '141' in acqIdentifiers:
        flag=True
    return flag

def containsPreparation(acqIdentifiers):
    flag=False 
    #denture['8','9','140','141']
    if '6' in acqIdentifiers:
        flag=True
    elif '7' in acqIdentifiers:
        flag=False
    
    return flag

def containsImplant(acqIdentifiers):
    flag=False
    
    #denture['8','9','140','141']
    if '3' in acqIdentifiers:
        flag=True
    elif '4' in acqIdentifiers:
        flag=False
    elif '130' in acqIdentifiers:
        flag=True
    elif '131' in acqIdentifiers:
        flag=True
    return flag

def containsShadeLibs(acqIdentifiers):
    flag=False
    if 'shade' in acqIdentifiers:
        flag=True
    return flag

def pass30Days(fname):
    flag=False
    diffdays=DateTimeUtil.getDiffDays(fname)
    if diffdays>30:
        flag=True
    return flag