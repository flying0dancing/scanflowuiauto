# -*- coding: utf-8 -*-
import test
import ctypes
import os
import sys 
import platform
from pages.LeftBarTool import LeftBarTool 

leftBarTool=LeftBarTool()

def get_free_space_mb(folerpath):
    if platform.system() == 'Windows':
        free_bytes=ctypes.c_ulonglong(0)
        ctypes.windll.kernel32.GetDiskFreeSpaceExW(ctypes.c_wchar_p(folerpath),None,None,ctypes.pointer(free_bytes))
        test.log(str(round(free_bytes.value/1024/1024/1024*100,2)))
        return round(free_bytes.value/1024/1024/1024*100,2)
    else:
        st=os.statvfs('/')
        free_size=st.f_bsize * st.f_bavail/1024/1024
        return round(free_size*100,2)
    
def exitScanFlowNormally():
    scanflow_log=ConfigUtil.getScanFlowLog()      
    return FileUtil.existInFileContentByStr(scanflow_log,'Application exit normally',10)
#deprecated
def tool_status(locatorFileName,testScenario):
    for record in testData.dataset(locatorFileName):
        locatorName=testData.field(record, "locatorName")
        locatorExist=testData.field(record,'locatorExist')
        toolTip=testData.field(record, "toolTip")
        premium=testData.field(record, "premium")
        checked=testData.field(record, "checked")
        enabled=testData.field(record, "enabled")
        visible=testData.field(record, "visible")
        verifiedDict={'toolTip':toolTip,'premium':premium,'checked':checked,'enabled':enabled,'visible':visible}
        skiptFlag=testData.field(record, "skipFlag")
        coverRange=testData.field(record, "ref")
        
        if skiptFlag.lower() in ['n',''] and (coverRange == '' or testScenario.lower() in coverRange.lower().split(',')):
            if locatorExist.lower()== 'n':
                trp=leftBarTool.verifyLeftTool(locatorName,verifiedDict)
                test.verify(trp[0]==False,trp[1])
            else:
                trp=leftBarTool.verifyLeftTool(locatorName,verifiedDict)
                test.verify(trp[0]==True,trp[1])
                
def verify_tool_status(locatorFileName,acqCatalog,testRefs):
    logPrefix="["+locatorFileName.split('.')[-2]+"]"+"["+acqCatalog+"] "
    for record in testData.dataset(locatorFileName):
        skipFlag=testData.field(record, "skipFlag")
        if skipFlag.lower()=='y':
            continue
        acqCatalogFlag=testData.field(record, "acqCatalogFlag")
        acqCatalogNames=testData.field(record, "acqCatalogNames")
        if (acqCatalogFlag == '' and acqCatalogNames == ''):
            pass
        elif acqCatalogFlag.lower()=='y' and acqCatalog in acqCatalogNames.split(','):
            pass
        elif acqCatalogFlag.lower()=='n' and acqCatalog not in acqCatalogNames.split(','):
            pass
        else:
            continue
        
        refRange=testData.field(record, "ref")
        if refRange == '':
            verify_locator_status(record,logPrefix)
        elif testRefs:
            refs=refRange.lower().split(',')
            for testRef in testRefs:
                if testRef in refs:
                    verify_locator_status(record,logPrefix)

def verify_locator_status(record, logPrefix):       
    locatorName=testData.field(record, "locatorName")
    locatorExist=testData.field(record,'locatorExist').lower()
    
    if locatorExist == 'n':
        trp=leftBarTool.verifyLeftTool(locatorName)
        test.verify(trp[0]==False,logPrefix+trp[1] )
    else:
        toolTip=testData.field(record, "toolTip")
        premium=testData.field(record, "premium")
        checked=testData.field(record, "checked")
        enabled=testData.field(record, "enabled")
        visible=testData.field(record, "visible")
        verifiedDict={'toolTip':toolTip,'premium':premium,'checked':checked,'enabled':enabled,'visible':visible}
        trp=leftBarTool.verifyLeftTool(locatorName,verifiedDict)
        test.verify(trp[0]==True, logPrefix+trp[1])
                      
