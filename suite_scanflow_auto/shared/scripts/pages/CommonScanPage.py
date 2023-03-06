# -*- coding: utf-8 -*-
''' 
@author: Kun Shen
@since: 20230130
'''
import object
import test
import squish
import locators
from pages.BasePage import BasePage

class CommonScanPage(BasePage):
    '''
    @see: click refine button and do refine with resolution type
    @param resolution_type: it has 3 types(low, standard, high) for selection.
    '''        
    def clickRefineButton(self,resolution_type):
        test.log("click refine step button")
        squish.mouseClick(squish.waitForObject(locators.stepBar_check))
        squish.snooze(2)
        self.refineMesh(resolution_type)


    '''
    @return: 0 means this application is on Check step view, 1 means this application is on Scan step view.
    '''
    def clickAdaptButton(self):
        test.log("click adapt step button")
        flag=0
        squish.mouseClick(squish.waitForObject(locators.stepBar_adapt))
        squish.snooze(2)
        if object.exists(locators.base_notice_ok):
            test.log("click ok button on Check First Dialog")
            squish.mouseClick(squish.waitForObject(locators.base_notice_ok))
            squish.snooze(1)
            flag=1
            return flag

    '''
    @return: 0 means this application is on Check step view, 1 means this application is on Scan step view.
    '''
    def clickExportButton(self):
        test.log("click export step button")
        flag=0
        squish.mouseClick(squish.waitForObject(locators.stepBar_export))
        squish.snooze(2)
        if object.exists(locators.base_notice_ok):
            test.log("click ok button on Check First Dialog")
            squish.mouseClick(squish.waitForObject(locators.base_notice_ok))
            squish.snooze(1)
            flag=1
            return flag

    # Refinement
    def refineMesh(self,resolution_type):
        test.log("Perform refinement with %s." %resolution_type)
    
        # Refine with different resolutions
        if "high" == resolution_type:
            squish.clickButton(squish.waitForObject(locators.refineDlg_resolution_type_high))
        elif "standard" == resolution_type:
            squish.clickButton(squish.waitForObject(locators.refineDlg_resolution_type_standard))
        elif "low" == resolution_type:
            squish.clickButton(squish.waitForObject(locators.refineDlg_resolution_type_low))
        else:
            test.log("refine with default resolution type")
        
        
        squish.clickButton(squish.waitForObject(locators.refineDlg_refine_button))
        squish.snooze(4)
        #Wait until refinement is done
        while object.exists(locators.refineDlg_progress_cancel):
            squish.snooze(10)
            test.log("Wait for another 10s")
        squish.snooze(1)

        test.log("Refinement is done")

    def isInScanView(self):
        return self.getStatusScanStep()==True and self.getStatusRefineStep()==False

    def existShadeMatchingInTopTool(self):
        flag=False
        if object.exists(locators.topBar_shadematching):
            prop_value=squish.waitForObjectExists(locators.topBar_shadematching).visible
            squish.snooze(1)
            flag=prop_value
        return flag

    
