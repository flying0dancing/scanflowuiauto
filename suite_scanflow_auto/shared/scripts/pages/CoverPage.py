# -*- coding: utf-8 -*-
''' 
@author: Kun Shen
@since: 20230130
'''
import object
import squish
import test
import locators
class CoverPage():
    #testdata_pool=ConfigUtil.getTestDataPool()

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
        if object.exists(locators.cover_button_scan):
            test.log("click scan button in cover page")
            squish.mouseClick(squish.waitForObject(locators.cover_button_scan))
        
        squish.snooze(5)

    '''
    @see: click import and import the scan data into software.
    @param filename: a full name(with path) of cszx file 
    '''
    def clickImportButton(self,filename):
        squish.snooze(3)
        self.cancelRecoverDataDlg()
        if object.exists(locators.cover_button_import):
            test.log("click import button in cover page")
            squish.mouseClick(squish.waitForObject(locators.cover_button_import))
        
        self.importData(filename)

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
            squish.mouseClick(squish.waitForObject(locators.base_notice_cancel))
        squish.snooze(1)

    def clickOKImportNoticeDlg(self):
        squish.snooze(1)
        if object.exists(locators.base_notice_ok):
            test.log("click OK button on notice dialog for import file 30 days ago")
            squish.mouseClick(squish.waitForObject(locators.base_notice_ok))
        squish.snooze(2)
    
    
    '''
     Import data, make sure the scanner isn't plugged in.
     @param filename:full name of *.cszx
     @param flag: shade_on, shade_off  
    '''
    def importData(self,filename):
        test.log("Import data with name: %s" % filename)  
        squish.snooze(5)
        squish.snooze(2)
        squish.nativeType(filename)
        squish.snooze(2)
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
    
