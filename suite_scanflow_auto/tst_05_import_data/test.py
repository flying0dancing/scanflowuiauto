# -*- coding: utf-8 -*-"
from utils import ConfigUtil, DateTimeUtil, FileUtil
from pages.CoverPage import CoverPage
from pages.CommonScanPage import CommonScanPage
'''
@see: related smoke test cases
1.15 Smoke Testing_Import csz file
1.20 Smoke Testing_Next and Back
1.30 Smoke Testing_Save Files By Type
1.16 Smoke Testing_Export DCM file to IS Connect
'''



def main():
    source(findFile("scripts","Common.py"))
    get_free_space_mb(ConfigUtil.getScanFlowRoot())
    launchStr=ConfigUtil.getScanFlowLaunchStrByCmd()
    
    for record in testData.dataset("inputdata.tsv"):
        testname=testData.field(record, "testName")
        filename=testData.field(record, "cszxName")
        filename=ConfigUtil.getTestDataPool()+filename
        #refine_type=testData.field(record,"refineType")
        skipFlag=testData.field(record,"skipFlag")
        if skipFlag.lower()=='y':
            continue
        #test.log("%s %s" % (filename, refine_type))
        test_log_folder=ConfigUtil.getTestLogFolder()+DateTimeUtil.get_dateYYYMMDD()+'\\'+testname+'\\'
        scanflow_log=ConfigUtil.getScanFlowLog()
        test_before(test_log_folder,scanflow_log)
        importData_refine_export_save_send(launchStr,filename,test_log_folder)
        test_after(testname,test_log_folder,scanflow_log)
        
    
def importData_refine_export_save_send(launchStr,filename,test_log_folder): 
    test.log(launchStr ) 
    #testSettings.logScreenshotOnFail = True
    #testSettings.logScreenshotOnPass = True
    startApplication(launchStr)
    coverPage=CoverPage()
    commonScanPage=CommonScanPage()
    
    #Click ok button on the warn message which says it's an internal version
    coverPage.skipInternalVersionDlg()
    
    coverPage.clickImportButton(filename)
    test.verify(commonScanPage.isInScanView()==True,"ScanFlow is on scan step view, test data is imported.")
    saveDesktopScreenshot(test_log_folder+"0_import_data.png")
    
    commonScanPage.clickCloseButton()
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
    
    
    