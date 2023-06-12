# -*- coding: utf-8 -*-"
from utils import ConfigUtil, DateTimeUtil,FileUtil,CatalogsUtil
from pages.CoverPage import CoverPage
import test
'''
@see: related smoke test cases

'''
#APPNAME = "scanflow \"C:\ProgramData\DEXIS IS\ScanFlow\inputdata.xml\""
#filename = r'Orthodontics.cszx'
#filename=r'common + bites + shadematch + preparation + IS 3800 [1.0.8.300][Res].cszx'

def main():
    source(findFile("scripts","Common.py"))
    
    cleanPCSpace(ConfigUtil.getScanFlowTempFolder(),[],['.dcm','.xml'])
    get_free_space_mb(ConfigUtil.getScanFlowRoot())
    launchStr=ConfigUtil.getScanFlowLaunchStrByCmd()
    tName=FileUtil.getParentFolder(__file__)
    test.log(tName)
    for record in testData.dataset(ConfigUtil.getTestConfig(tName,'.tsv')):
        testname=testData.field(record, "testName")
        filename=testData.field(record, "cszxName")
        filename=ConfigUtil.getTestDataPool()+filename
        refine_type=testData.field(record,"refineType")
        #scanRef=testData.field(record,"scanRef")
        #refineRef=testData.field(record,"refineRef")
        skipFlag=testData.field(record,"skipFlag")
        if skipFlag.lower() in ['n','']:
            test.log("test name: %s file: %s refine with: %s" % (testname, filename, refine_type))
            test_log_folder=ConfigUtil.getTestLogFolder()+DateTimeUtil.get_dateYYYMMDD()+'\\'+tName+'\\'+testname+'\\'
            scanflow_log=ConfigUtil.getScanFlowLog()
            test_before(test_log_folder,scanflow_log)
            
            importData_refine_export_save_send(launchStr,filename,refine_type,test_log_folder)
            test_after(testname,test_log_folder,scanflow_log)
        
    
def importData_refine_export_save_send(launchStr,filename,refine_type,test_log_folder): 
    acqIns=CatalogsUtil.AcqCatalogs()
    acqIns.initialSets(filename)
    test.log(launchStr ) 
    #testSettings.logScreenshotOnFail = True
    #testSettings.logScreenshotOnPass = True
    startApplication(launchStr)
    
    coverPage=CoverPage(test_log_folder)
    
    #Click ok button on the warn message which says it's an internal version
    coverPage.skipInternalVersionDlg()
    
    commonScanPage=coverPage.clickImportButton(filename,acqIns.get_shade(),acqIns.get_pass_30days())
    #scanRef=acqIns.get_scanRef()
    #refineRef=acqIns.get_refineRef()
    test.verify(commonScanPage.isInScanView()==True,"ScanFlow is on scan step view, test data is imported.")
    saveDesktopScreenshot(test_log_folder+"0_import_data.png")
    
    #refineRefs=refineRef.lower().split(',')
    scanToolFile=ConfigUtil.getTools_Import_Scanview()#"tools.import.scanview.csv"
    scanImpressToolFile=ConfigUtil.getTools_Import_Scanview_Impress()#"tools.import.scanview_impress.csv"
    refineToolFile=ConfigUtil.getTools_Import_Refineview()#"tools.import.refineview.csv"
    
    
    
    if commonScanPage.clickPreparation():
        saveDesktopScreenshot(test_log_folder+"1_scanview_preparation.png")  
        verify_tool_status(scanToolFile,"Preparation Scan",acqIns.get_scanRefList())    
        
    verifyImplantWorkflowInScanView(commonScanPage,test_log_folder,scanToolFile,scanImpressToolFile,acqIns) 
    
    verifyDentureWorkflowInScanView(commonScanPage,test_log_folder,scanToolFile,scanImpressToolFile,acqIns)
    
    verifyCommonScanInScanView(commonScanPage,test_log_folder,scanToolFile,scanImpressToolFile,acqIns)    
    
    commonRefinePage=commonScanPage.clickRefineButton(refine_type.lower())
    test.verify(commonRefinePage.isInRefineView()==True, "ScanFlow is on check step view, test data is refined.")
    saveDesktopScreenshot(test_log_folder+"2_refine_data.png")
    
    if commonRefinePage.clickScanBody():
        verifyWorkflowAfterRefine(commonRefinePage,refineToolFile,"Scanbody Scan",acqIns,test_log_folder+"2_refineview_scanBody.png")
        
    if commonRefinePage.clickEmergencyProfile():
        verifyWorkflowAfterRefine(commonRefinePage,refineToolFile,"Emergence Profile Scan",acqIns,test_log_folder+"2_refineview_emergenceProfile.png")
    
    if commonRefinePage.clickDenture():
        verifyWorkflowAfterRefine(commonRefinePage,refineToolFile,"Denture Scan",acqIns,test_log_folder+"2_refineview_denture.png")
        
    if commonRefinePage.clickEdentulous():
        verifyWorkflowAfterRefine(commonRefinePage,refineToolFile,"Edentulous Scan",acqIns,test_log_folder+"2_refineview_edentulous.png")
        
    if commonRefinePage.clickPreparation():
        verifyWorkflowAfterRefine(commonRefinePage,refineToolFile,"Preparation Scan",acqIns,test_log_folder+"2_refineview_preparation.png")
        
    if commonRefinePage.clickCommonScan():
        verifyWorkflowAfterRefine(commonRefinePage,refineToolFile,"Common Scan",acqIns,test_log_folder+"2_refineview_common.png")
        

    commonRefinePage.clickCloseButton()
    

def test_before(test_log_folder,scanflow_log):
    test.log(scanflow_log)
    if FileUtil.fileExist(scanflow_log):
        FileUtil.cleanFileContent(scanflow_log)
    if not FileUtil.fileExist(test_log_folder):
        FileUtil.makedirs(test_log_folder)

def test_after(testname,test_log_folder,scanflow_log):
    if FileUtil.fileExist(scanflow_log):
        #test_log_folder=ConfigUtil.getTestLogFolder()
        scanflow_logname=FileUtil.getFileName(scanflow_log)
        scanflow_logname_bak=scanflow_logname[0]+'['+testname+']'+scanflow_logname[1]
        test_scanflow_log=test_log_folder+scanflow_logname_bak
        test.log("archive scanflow log to test logs %s" % test_scanflow_log)
        FileUtil.renameFile(scanflow_log, test_scanflow_log)
    else:
        test.log("cannot find the scanflow log %s" % scanflow_log)


def removeItemInList(rangeList,removeItems):
    if rangeList:
        for item in rangeList:
            if (isinstance(removeItems,list) and item in removeItems) or item == removeItems:
                rangeList.remove(item) 
            

def addItemInList(rangeList,addItem):
    if rangeList:
        if addItem not in rangeList:
            rangeList.append(addItem)
    else:
        rangeList.append(addItem)  


def verifyImplantWorkflowInScanView(commonScanPage,test_log_folder,scanToolFile,scanImpressToolFile,acqIns):
    impressStr='impress'
    noImpressStr='noimpress'
    scanRefs=acqIns.get_scanRefList()
    if commonScanPage.clickScanBody():
        if acqIns.get_scanbody_upper():
            removeItemInList(scanRefs, 'nodata')
            addItemInList(scanRefs, 'data')
        else:
            removeItemInList(scanRefs, 'data')
            addItemInList(scanRefs, 'nodata')
        saveDesktopScreenshot(test_log_folder+"1_scanview_scanBody.png")
        test.log(','.join(scanRefs))
        verify_tool_status(scanToolFile,"Scanbody Scan",scanRefs)
        
    if commonScanPage.clickEmergencyProfileImpress():
        saveDesktopScreenshot(test_log_folder+"1_scanview_emergenceProfile_impress.png")  
        verify_tool_status(scanImpressToolFile,"Emergence Profile Scan-Impress",scanRefs)
        removeItemInList(scanRefs, noImpressStr)
        addItemInList(scanRefs, impressStr)  
    else:
        removeItemInList(scanRefs, impressStr)
        addItemInList(scanRefs, noImpressStr)
      
    #click Emergency Profile
    if commonScanPage.clickEmergencyProfile():
        if acqIns.get_emergenceProfile_upper():
            removeItemInList(scanRefs, 'nodata')
            addItemInList(scanRefs, 'data')
        else:
            removeItemInList(scanRefs, 'data')
            addItemInList(scanRefs, 'nodata')
        saveDesktopScreenshot(test_log_folder+"1_scanview_emergenceProfile.png")
        test.log(','.join(scanRefs))
        verify_tool_status(scanToolFile,"Emergence Profile Scan",scanRefs)
    
        
def verifyDentureWorkflowInScanView(commonScanPage,test_log_folder,scanToolFile,scanImpressToolFile,acqIns):
    impressStr='impress'
    noImpressStr='noimpress'
    scanRefs=acqIns.get_scanRefList()
    if commonScanPage.clickEdentulousImpress():
        saveDesktopScreenshot(test_log_folder+"1_scanview_edentulous_impress.png")  
        verify_tool_status(scanImpressToolFile,"Edentulous Scan-Impress",scanRefs)
        removeItemInList(scanRefs, noImpressStr)
        addItemInList(scanRefs, impressStr)  
    else:
        removeItemInList(scanRefs, impressStr)
        addItemInList(scanRefs, noImpressStr)
        
    if commonScanPage.clickEdentulous():
        if acqIns.get_edentulous_upper():
            removeItemInList(scanRefs, 'nodata')
            addItemInList(scanRefs, 'data')
        else:
            removeItemInList(scanRefs, 'data')
            addItemInList(scanRefs, 'nodata')
        saveDesktopScreenshot(test_log_folder+"1_scanview_edentulous.png")
        test.log(','.join(scanRefs))
        verify_tool_status(scanToolFile,"Edentulous Scan",scanRefs)
        
    if commonScanPage.clickDenture():
        if acqIns.get_denture_upper():
            removeItemInList(scanRefs, 'nodata')
            addItemInList(scanRefs, 'data')
        else:
            removeItemInList(scanRefs, 'data')
            addItemInList(scanRefs, 'nodata')
        saveDesktopScreenshot(test_log_folder+"1_scanview_denture.png") 
        test.log(','.join(scanRefs))
        verify_tool_status(scanToolFile,"Denture Scan",scanRefs)
        
def verifyCommonScanInScanView(commonScanPage,test_log_folder,scanToolFile,scanImpressToolFile,acqIns):
    impressStr='impress'
    noImpressStr='noimpress'
    scanRefs=acqIns.get_scanRefList()
    if commonScanPage.clickCommonImpress():
        saveDesktopScreenshot(test_log_folder+"1_scanview_common_impress.png") 
        test.log(','.join(scanRefs)) 
        verify_tool_status(scanImpressToolFile,"Common Scan-Impress",scanRefs)
        removeItemInList(scanRefs, noImpressStr)
        addItemInList(scanRefs, impressStr)  
    else:
        removeItemInList(scanRefs, impressStr)
        addItemInList(scanRefs, noImpressStr)
        
    if commonScanPage.clickCommonScan():
        if acqIns.get_common_upper():
            removeItemInList(scanRefs, 'nodata')
            addItemInList(scanRefs, 'data')
        else:
            removeItemInList(scanRefs, 'data')
            addItemInList(scanRefs, 'nodata')
        saveDesktopScreenshot(test_log_folder+"1_scanview_commonScan.png") 
        test.log(','.join(scanRefs)) 
        verify_tool_status(scanToolFile,"Common Scan",scanRefs)

def verifyWorkflowAfterRefine(commonRefinePage,refineToolFile,CatalogStr,acqIns,test_log_fullname):
    onlyLower="onlylower"
    onlyUpper="onlyupper"
    fullarch="fullarch"
    refineRefs=acqIns.get_refineRefList()
    removeItemInList(refineRefs, [onlyLower,onlyUpper,fullarch])
    if commonRefinePage.getStatusUpperJaw()==True:
        if commonRefinePage.getStatusLowerJaw()==True:
            addItemInList(refineRefs, fullarch)
        else:
            addItemInList(refineRefs, onlyUpper)
    else:
        addItemInList(refineRefs, onlyLower) 
    saveDesktopScreenshot(test_log_fullname)  
    test.log(','.join(refineRefs))  
    verify_tool_status(refineToolFile,CatalogStr,refineRefs)