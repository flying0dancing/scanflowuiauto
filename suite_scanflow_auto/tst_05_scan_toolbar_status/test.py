# -*- coding: utf-8 -*-"
from utils import ConfigUtil
from pages.CoverPage import CoverPage
from pages.LeftBarTool import LeftBarTool
#APPNAME = "scanflow \"C:\ProgramData\DEXIS IS\ScanFlow\inputdata.xml\""

def main():
    source(findFile("scripts", "common.py"))
    #test.log(os.environ["SQUISH_PREFIX"])
    launchStr=ConfigUtil.getScanFlowLaunchStrByCmd()
    startApplication(launchStr)
    coverPage=CoverPage()
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

    #scanViewButtonsCheck()
    

