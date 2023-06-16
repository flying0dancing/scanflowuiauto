# -*- coding: utf-8 -*-"
from utils import ConfigUtil, DateTimeUtil, FileUtil,CatalogsUtil
from pages.CoverPage import CoverPage

'''
@see: related smoke test cases
1.15 Smoke Testing_Import csz file

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
        #refine_type=testData.field(record,"refineType")
        
        test.log("test name: %s file: %s" % (testname, filename))
        test_log_folder=ConfigUtil.getTestLogFolder()+DateTimeUtil.get_dateYYYMMDD()+'\\'+tName+'\\'+testname+'\\'
        scanflow_log=ConfigUtil.getScanFlowLog()
        test_before(test_log_folder,scanflow_log)
        importData(launchStr,filename,test_log_folder)
        test_after(testname,test_log_folder,scanflow_log)
        
    
def importData(launchStr,filename,test_log_folder): 
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
    
    
    