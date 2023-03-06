# -*- coding: utf-8 -*-

import object
import test
import squish
import locators
from utils import FileUtil
from pages.BasePage import BasePage
class ExportDialog(BasePage):

    def selectSaveTabAndSave(self,file_format):
        test.log("select save tab in Export dialog")
        squish.snooze(1)
        squish.mouseClick(squish.waitForObject(locators.exportDlg_tab_save))
        squish.snooze(2)
        test.log("select %s in Export dialog" % file_format)
        if file_format=='stl':
            squish.mouseClick(squish.waitForObject(locators.exportDlg_local_stl))
        else:
            squish.mouseClick(squish.waitForObject(locators.exportDlg_local_ply))
        squish.snooze(1)
        squish.mouseClick(squish.waitForObject(locators.exportDlg_btn_save))
        squish.snooze(5)
        while object.exists(locators.base_waiting_progress):
            squish.snooze(2)
            test.log("Wait for another 2s")
        squish.snooze(2)
   

    def selectSaveTabAndSaveAll(self):
        test.log("select save tab in Export dialog")
        squish.snooze(1)
        squish.mouseClick(squish.waitForObject(locators.exportDlg_tab_save))
        squish.snooze(2)
        lineedit = squish.waitForObject(locators.exportDlg_local_targetfolder)
        text = lineedit.text
        test.log("target folder %s " % str(text))
    
        for obj in [locators.exportDlg_local_ply,locators.exportDlg_local_stl]:
            objTmp=squish.waitForObject(obj)
            test.log("select %s in Export dialog and save" % objTmp.id)
            squish.mouseClick(objTmp)
            squish.snooze(1)
            squish.mouseClick(squish.waitForObject(locators.exportDlg_btn_save))
            squish.snooze(5)
            while object.exists(locators.base_waiting_progress):
                squish.snooze(2)
                test.log("Wait for another 2s")
            squish.snooze(2)
    
    
    
    def selectSendTabAndSend(self):
        test.log("select send tab in Export dialog")
        squish.snooze(1)
        squish.mouseClick(squish.waitForObject(locators.exportDlg_tab_send))
        squish.snooze(2)
        squish.mouseClick(squish.waitForObject(locators.exportDlg_btn_send))
        squish.snooze(3)
        while object.exists(locators.base_waiting_progress):
            squish.snooze(2)
            test.log("Wait for another 2s")
        squish.snooze(10)
        #return self.getStatusOfSendToISConnect()


    def getResultOfSendToISConnect(self,scanflow_log):
        result="cannot get result of Export-Send data"
        resultList=FileUtil.getFileContentByStrList(scanflow_log,['Save Scan Data, the result is OK.','Save Scan Data, the result is Failed.'],300)
        if resultList:
            astring=resultList[-1]
            if astring.find('Save Scan Data, the result is OK.')>-1:
                result="Export-Send data is OK"
                test.log(result)
            elif astring.find('Save Scan Data, the result is Failed.')>-1:
                result="Export-Send data is Failed"
                test.log(result)
            else:
                test.log(result)
                
        return result


        