# -*- coding: utf-8 -*-"
from utils import ConfigUtil, DateTimeUtil,FileUtil,CatalogsUtil
from pages.CoverPage import CoverPage
import test
'''
@see: related smoke test cases
from commonold import cutOnLowerJaw
from commonold import cutOnLowerJaw
from commonold import cutOnLowerJaw

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
    expected_acqIns=CatalogsUtil.AcqCatalogs()
    for record in testData.dataset(ConfigUtil.getTestConfig(tName,'.tsv')):
        skipFlag=testData.field(record,"skipFlag")
        if skipFlag.lower() not in ['n','']:
            continue
        testname=testData.field(record, "testName")
        filename=testData.field(record, "cszxName")
        filename=ConfigUtil.getTestDataPool()+filename
        refine_type=testData.field(record,"refineType")
        configScan_data=testData.field(record,"configScan.common")
        expected_acqIns.setFuncToTrue(configScan_data,'set_common_upper','set_common_lower')
        configScan_data=testData.field(record,"configScan.emergenceProfile")
        expected_acqIns.setFuncToTrue(configScan_data,'set_emergenceProfile_upper','set_emergenceProfile_lower')
        configScan_data=testData.field(record,"configScan.scanbody")
        expected_acqIns.setFuncToTrue(configScan_data,'set_scanbody_upper','set_scanbody_lower')
        configScan_data=testData.field(record,"configScan.edentulous")
        expected_acqIns.setFuncToTrue(configScan_data,'set_edentulous_upper','set_edentulous_lower')
        configScan_data=testData.field(record,"configScan.denture")
        expected_acqIns.setFuncToTrue(configScan_data,'set_denture_upper','set_denture_lower')
        configScan_data=testData.field(record,"configScan.preparation")
        expected_acqIns.setFuncToTrue(configScan_data,'set_preparation_upper','set_preparation_lower')
            
        
        test.log("test name: %s file: %s refine with: %s" % (testname, filename, refine_type))
        test_log_folder=ConfigUtil.getTestLogFolder()+DateTimeUtil.get_dateYYYMMDD()+'\\'+tName+'\\'+testname+'\\'
        scanflow_log=ConfigUtil.getScanFlowLog()
        test_before(test_log_folder,scanflow_log)
            
        importData_refine_export_save_send(launchStr,filename,refine_type,test_log_folder,expected_acqIns)
        test_after(testname,test_log_folder,scanflow_log)
        
    
def importData_refine_export_save_send(launchStr,filename,refine_type,test_log_folder,expected_acqIns): 
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
    #scanToolFile=ConfigUtil.getTools_Import_Scanview()#"tools.import.scanview.csv"
    #scanImpressToolFile=ConfigUtil.getTools_Import_Scanview_Impress()#"tools.import.scanview_impress.csv"
    #refineToolFile=ConfigUtil.getTools_Import_Refineview()#"tools.import.refineview.csv"
    
    
    commonRefinePage=commonScanPage.clickRefineButton(refine_type.lower())
    test.verify(commonRefinePage.isInRefineView()==True, "ScanFlow is on check step view, test data is refined.")
    saveDesktopScreenshot(test_log_folder+"2_refine_data.png")
    
    acqIns.containsDenture()
    if commonRefinePage.clickScanBody():
        verifyWorkflowAfterRefine(commonRefinePage,expected_acqIns,'get_scanbody_upper','get_scanbody_lower',"Scanbody Scan",test_log_folder+"2_refineview_scanBody.png")
        
    if commonRefinePage.clickEmergencyProfile():
        verifyWorkflowAfterRefine(commonRefinePage,expected_acqIns,'get_emergenceProfile_upper','get_emergenceProfile_lower',"Emergence Profile Scan",test_log_folder+"2_refineview_emergenceProfile.png")
    
    if commonRefinePage.clickDenture():
        verifyWorkflowAfterRefine(commonRefinePage,expected_acqIns,'get_denture_upper','get_denture_lower',"Denture Scan",test_log_folder+"2_refineview_denture.png")
        
    if commonRefinePage.clickEdentulous():
        verifyWorkflowAfterRefine(commonRefinePage,expected_acqIns,'get_edentulous_upper','get_edentulous_lower',"Edentulous Scan",test_log_folder+"2_refineview_edentulous.png")
        
    if commonRefinePage.clickPreparation():
        verifyWorkflowAfterRefine(commonRefinePage,expected_acqIns,'get_preparation_upper','get_preparation_lower',"Preparation Scan",test_log_folder+"2_refineview_preparation.png")
        
    if commonRefinePage.clickCommonScan():
        verifyWorkflowAfterRefine(commonRefinePage,expected_acqIns,'get_common_upper','get_common_lower',"Common Scan",test_log_folder+"2_refineview_common.png")
        
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


 

def verifyWorkflowAfterRefine(commonRefinePage,expected_acqIns,func_get_upper,func_get_lower,CatalogStr,test_log_fullname):
    flag=commonRefinePage.getStatusUpperJaw()
    expected_flag=expected_acqIns.getFuncValue(func_get_upper)
    test.verify(flag==expected_flag, CatalogStr+' upper jaw contains data [real:'+str(flag)+', expected:'+str(expected_flag)+']')
    
    flag=commonRefinePage.getStatusLowerJaw()
    expected_flag=expected_acqIns.getFuncValue(func_get_lower)
    test.verify(flag==expected_flag, CatalogStr+' lower jaw contains data [real:'+str(flag)+', expected:'+str(expected_flag)+']')
    
    saveDesktopScreenshot(test_log_fullname)  