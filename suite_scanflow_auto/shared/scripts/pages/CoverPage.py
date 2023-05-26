# -*- coding: utf-8 -*-
''' 
@author: Kun Shen
@since: 20230130
'''
import object
import squish
import test
import locators
from pages.CommonScanPage import CommonScanPage
class CoverPage():
    def __init__(self,logfolder):
        self.logfolder=logfolder

    def skipInternalVersionDlg(self):
        #Click ok button on the warn message which says it's an internal version
        squish.snooze(3)
        #test.log(locators.cover_internal_ok)
        if object.exists(locators.cover_internal_ok):
            test.log("Application Under Testing is an internal version")
            squish.mouseClick(squish.waitForObject(locators.cover_internal_ok))
            squish.snooze(3)


    def clickScanButton(self):
        squish.snooze(3)
        self.cancelRecoverDataDlg()
        self.clickLaterOnSoftwareUpdateDialog()
        if object.exists(locators.cover_button_scan):
            test.log("click scan button in cover page")
            squish.mouseClick(squish.waitForObject(locators.cover_button_scan))
        squish.snooze(5)
        return CommonScanPage(self.logfolder)

    '''
    @see: click import and import the scan data into software.
    @param filename: a full name(with path) of cszx file 
    '''
    @DeprecationWarning
    def clickImportButton(self,filename):
        squish.snooze(3)
        self.cancelRecoverDataDlg()
        self.clickLaterOnSoftwareUpdateDialog()
        squish.saveDesktopScreenshot(self.logfolder+"_acquisitionSelectionWindows.png")
        if object.exists(locators.cover_button_import):
            test.log("click import button in cover page")
            squish.mouseClick(squish.waitForObject(locators.cover_button_import))
        test.log("for check running it about 4minutes on windows 11")
        squish.saveDesktopScreenshot(self.logfolder+"_importDialog.png")
        self.importData(filename)
        return CommonScanPage(self.logfolder)
        
    
    '''
    @see: click import and import the scan data into software.
    @param filename: a full name(with path) of cszx file 
    '''
    def clickImportButton(self,filename,shade_flag,passdays_flag):
        squish.snooze(3)
        self.cancelRecoverDataDlg()
        self.clickLaterOnSoftwareUpdateDialog()
        #squish.saveDesktopScreenshot(self.logfolder+"_acquisitionSelectionWindows.png")
        if object.exists(locators.cover_button_import):
            test.log("click import button in cover page")
            squish.mouseClick(squish.waitForObject(locators.cover_button_import))
        test.log("for check running it about 4minutes on windows 11")
        squish.saveDesktopScreenshot(self.logfolder+"_importDialog.png")
        self.importData(filename,shade_flag,passdays_flag)
        return CommonScanPage(self.logfolder)

    def clickIOCameraButton(self):
        squish.snooze(3)
        self.cancelRecoverDataDlg()
        if object.exists(locators.cover_button_iocamera):
            test.log("click io camera button in cover page")
            squish.mouseClick(squish.waitForObject(locators.cover_button_iocamera))
        



    def cancelRecoverDataDlg(self):
        squish.snooze(1)
        if object.exists(locators.base_notice_cancel):
            test.log("click cancel button in recover data dialog")
            squish.saveDesktopScreenshot(self.logfolder+"_cancelrecoverDialog.png")
            squish.mouseClick(squish.waitForObject(locators.base_notice_cancel))
        squish.snooze(1)

    def clickOKImportNoticeDlg(self):
        squish.snooze(1)
        if object.exists(locators.base_notice_ok):
            test.log("click OK button on notice dialog for import file 30 days ago")
            #TODO add a test verify for 30days
            squish.mouseClick(squish.waitForObject(locators.base_notice_ok))
        squish.snooze(2)
    
    def clickOKOnNoticeDlg4Pass30ds(self,flag):
        squish.snooze(1)
        if flag:
            #pass 30 days
            if object.exists(locators.noticeDlg_content):
                test.log("click OK button on Notice dialog for imported file pass 30 days")
                squish.mouseClick(squish.waitForObject(locators.base_notice_ok))
                test.verify(True==flag,"import file pass 30 days, pass 30 days dialog exists.")
                squish.saveDesktopScreenshot(self.logfolder+"_pass30daysDialog.png")
            else:
                test.verify(False==flag,"import file pass 30 days, pass 30 days dialog doesn't exist(expected: exists).")
        else:
            #doesn't pass 30 days
            if object.exists(locators.noticeDlg_content):
                test.log("click OK button on Notice dialog for imported file pass 30 days")
                squish.mouseClick(squish.waitForObject(locators.base_notice_ok))
                test.verify(True==flag,"import file doesn't pass 30 days, pass 30 days dialog exists(expected: doesn't exist).")
                squish.saveDesktopScreenshot(self.logfolder+"_pass30daysDialog.png")
            else:
                test.verify(False==flag,"import file doesn't pass 30 days, pass 30 days dialog doesn't exist.")
        squish.snooze(2)
    
    def clickOKOnShadeMatchingDlg(self,flag):
        squish.snooze(1)
        if flag:
            if object.exists(locators.shadeDlg_title):
                test.log("click OK button on Shade Matching dialog")
                squish.mouseClick(squish.waitForObject(locators.base_notice_ok))
                test.verify(True==flag,"import file contains shade libraries, Shade Matching dialog exists.")
                squish.saveDesktopScreenshot(self.logfolder+"_shadematchingDialog.png")
            else:
                test.verify(False==flag,"import file contains shade libraries, Shade Matching dialog [real: doesn't exist, expected: exists].")
        else:
            if object.exists(locators.shadeDlg_title):
                test.log("click OK button on Shade Matching dialog")
                squish.mouseClick(squish.waitForObject(locators.base_notice_ok))
                test.verify(True==flag,"import file doesn't contains shade libraries, Shade Matching dialog [real:exists, expected: doesn't exist].")
                squish.saveDesktopScreenshot(self.logfolder+"_shadematchingDialog.png")
            else:
                test.verify(False==flag,"import file doesn't contains shade libraries, Shade Matching dialog doesn't exist.")
        
        squish.snooze(2)
    
    '''
     Import data, make sure the scanner isn't plugged in.
     @param filename:full name of *.cszx
     @param flag: shade_on, shade_off  
    '''
    @DeprecationWarning
    def importData(self,filename):
        test.log("Import data with name: %s" % filename)  
        #squish.snooze(5)
        squish.snooze(2)
        squish.nativeType(filename)
        squish.snooze(1)
        squish.nativeType("<Return>")
        squish.nativeType("<Return>")
    
        self.clickOKImportNoticeDlg()      
        squish.snooze(2)
        while object.exists(locators.base_waiting_progress):
            squish.snooze(10)
            test.log("Wait for another 10s")
        self.clickOKImportNoticeDlg()        
        test.log("Import data is done")
        squish.snooze(2)
    '''
     Import data, make sure the scanner isn't plugged in.
     @param filename:full name of *.cszx
     @param flag: shade_on, shade_off  
    '''
    def importData(self,filename,shade_flag,passdays_flag):
        test.log("Import data with name: %s" % filename)  
        #squish.snooze(5)
        squish.snooze(2)
        squish.nativeType(filename)
        squish.snooze(1)
        squish.nativeType("<Return>")
        squish.nativeType("<Return>")
    
        self.clickOKOnNoticeDlg4Pass30ds(passdays_flag)      
        squish.snooze(2)
        while object.exists(locators.base_waiting_progress):
            squish.snooze(10)
            test.log("Wait for another 10s")
        self.clickOKOnShadeMatchingDlg(shade_flag)        
        test.log("Import data is done")
        squish.snooze(2)
        
        
    def clickLaterOnSoftwareUpdateDialog(self):
        squish.snooze(1)
        if object.exists(locators.softwareUpdateDlg_later):
            test.log("click Later on Software Update Dialog")
            squish.saveDesktopScreenshot(self.logfolder+"_clickLaterOnSoftwareUpdateDialog.png")
            squish.mouseClick(squish.waitForObject(locators.softwareUpdateDlg_later))
            squish.snooze(3)