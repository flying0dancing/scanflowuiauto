# -*- coding: utf-8 -*-"
from utils import ConfigUtil, DateTimeUtil, FileUtil,CatalogsUtil
from pages.CoverPage import CoverPage

'''
@see: related smoke test cases
1.08 Smoke Testing_Denture workflow
1.15 Smoke Testing_Import csz file
1.30 Smoke Testing_Save Files By TypeZipUtil
1.16 Smoke Testing_Export DCM file to IS Connect

'''

def main():
    source(findFile("scripts","Common.py"))
    launchStr=ConfigUtil.getScanFlowLaunchStrByCmd()
    tName=FileUtil.getParentFolder(__file__)
    test.log(tName)
    for record in testData.dataset(ConfigUtil.getTestConfig(tName,'.tsv')):
        skipFlag=testData.field(record,"skipFlag")
        if skipFlag.lower()=='y':
            continue
        cleanPCSpace(ConfigUtil.getScanFlowTempFolder(),[],['.dcm','.xml'])
        get_free_space_mb(ConfigUtil.getScanFlowRoot())
        testname=testData.field(record, "testName")
        filename=testData.field(record, "cszxName")
        filename=ConfigUtil.getTestDataPool()+filename
        refine_type=testData.field(record,"refineType")
        
        test.log("test name: %s file: %s refine with: %s" % (testname, filename, refine_type))
        test_log_folder=ConfigUtil.getTestLogFolder()+DateTimeUtil.get_dateYYYMMDD()+'\\'+tName+'\\'+testname+'\\'
        scanflow_log=ConfigUtil.getScanFlowLog()
        test_before(test_log_folder,scanflow_log)
        importData_refine_export_save_send(launchStr,filename,refine_type.lower(),test_log_folder)
        test_after(testname,test_log_folder,scanflow_log)
        
def importData_refine_export_save_send(launchStr,filename,refine_type,test_log_folder): 
    #verify here is only common jaws.
    acqIns=CatalogsUtil.AcqCatalogs()
    acqIns.initialSets(filename)
    if acqIns.containsOtherWorkflows():
        test.fail("import cszx file contains other workflows")
    else:
        test.log(launchStr ) 
        #testSettings.logScreenshotOnFail = True
        #testSettings.logScreenshotOnPass = True
        startApplication(launchStr)
        coverPage=CoverPage(test_log_folder)
    
        #Click ok button on the warn message which says it's an internal version
        coverPage.skipInternalVersionDlg()
        commonScanPage=coverPage.clickImportButton(filename,acqIns.get_shade(),acqIns.get_pass_30days())
        test.verify(commonScanPage.isInScanView()==True,"ScanFlow is on scan step view, test data is imported.")
        saveDesktopScreenshot(test_log_folder+"0_import_data.png")
        
        commonScanPage.clickConfigScan()
        commonScanPage.addDenture()
    
        commonRefinePage=commonScanPage.clickRefineButton(refine_type)
        test.verify(commonRefinePage.isInRefineView()==True, "ScanFlow is on check step view, test data is refined.")
        saveDesktopScreenshot(test_log_folder+"1_refine_data.png")
    
        exportDialog=commonRefinePage.clickExportButton()
        exportDialog.selectSaveTabAndSaveAll()
        saveDesktopScreenshot(test_log_folder+"2_export_save.png")
    
        exportDialog.selectSendTabAndSend()
        result=exportDialog.getResultOfSendToISConnect(ConfigUtil.getScanFlowLog())
        test.verify(result=="Export-Send data is OK", "Export-Send data is OK")
        #testSettings.logScreenshotOnFail = False
        #testSettings.logScreenshotOnPass = False
 
        test.verify(exitScanFlowNormally()==True, "ScanFlow exits normally.")
    

    

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
    
    
    