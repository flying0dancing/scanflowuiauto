# -*- coding: utf-8 -*-"
from utils import ConfigUtil
from utils import FileUtil
from utils import DateTimeUtil
from pages.CoverPage import CoverPage
from pages.LeftBarTool import LeftBarTool
#APPNAME = "scanflow \"C:\ProgramData\DEXIS IS\ScanFlow\inputdata.xml\""

def main():
    source(findFile("scripts", "common.py"))
    #test.log(os.environ["SQUISH_PREFIX"])
    tName=FileUtil.getParentFolder(__file__)
    cleanPCSpace(ConfigUtil.getScanFlowTempFolder(),[],['.dcm','.xml'])
    get_free_space_mb(ConfigUtil.getScanFlowRoot())
    test.log(tName)
    test_log_folder=ConfigUtil.getTestLogFolder()+DateTimeUtil.get_dateYYYMMDD()+'\\'+tName+'\\'
    scanflow_log=ConfigUtil.getScanFlowLog()
    test_before(test_log_folder,scanflow_log)
    launchStr=ConfigUtil.getScanFlowLaunchStrByCmd()
    startApplication(launchStr)
    coverPage=CoverPage(test_log_folder)
    #Click ok button on the warn message which says it's an internal version
    coverPage.skipInternalVersionDlg()
    
        
    coverPage.clickScanButton()
    for record in testData.dataset(ConfigUtil.getTools_Scan_Scanview()):#"tools.scan.scanview.csv"
        locatorName=testData.field(record, "locatorName")
        locatorExist=testData.field(record,'locatorExist')
        toolTip=testData.field(record, "toolTip")
        premium=testData.field(record, "premium")
        checked=testData.field(record, "checked")
        enabled=testData.field(record, "enabled")
        visible=testData.field(record, "visible")
        verifiedDict={'toolTip':toolTip,'premium':premium,'checked':checked,'enabled':enabled,'visible':visible}
        skipFlag=testData.field(record, "skipFlag")
        coverRange=testData.field(record, "ref")
        leftBarTool=LeftBarTool()
        if skipFlag.lower() in ['n',''] and (coverRange == '' or 'default' in coverRange.lower().split(',')):
            if locatorExist.lower()== 'n':
                trp=leftBarTool.verifyLeftTool(locatorName,verifiedDict)
                test.verify(trp[0]==False,trp[1])
            else:
                trp=leftBarTool.verifyLeftTool(locatorName,verifiedDict)
                test.verify(trp[0]==True,trp[1])
    test_after(test_log_folder,scanflow_log)
    #scanViewButtonsCheck()
    
def test_before(test_log_folder,scanflow_log):
    test.log(scanflow_log)
    if FileUtil.fileExist(scanflow_log):
        FileUtil.cleanFileContent(scanflow_log)
    if not FileUtil.fileExist(test_log_folder):
        FileUtil.makedirs(test_log_folder)

def test_after(test_log_folder,scanflow_log):
    if FileUtil.fileExist(scanflow_log):
        #test_log_folder=ConfigUtil.getTestLogFolder()
        scanflow_logname=FileUtil.getFileName(scanflow_log)
        scanflow_logname_bak=scanflow_logname[0]+scanflow_logname[1]
        test_scanflow_log=test_log_folder+scanflow_logname_bak
        test.log("archive scanflow log to test logs %s" % test_scanflow_log)
        FileUtil.renameFile(scanflow_log, test_scanflow_log)
    else:
        test.log("cannot find the scanflow log %s" % scanflow_log)
    
    
