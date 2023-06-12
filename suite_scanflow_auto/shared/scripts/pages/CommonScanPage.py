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
from pages.CommonRefinePage import CommonRefinePage

class CommonScanPage(BasePage):
    
    def __init__(self,logfolder):
        super().__init__(logfolder)
        
        
    '''
    @see: click refine button and do refine with resolution type
    @param resolution_type: it has 3 types(low, standard, high) for selection.
    '''        
    def clickRefineButton(self,resolution_type):
        test.log("click refine step button")
        squish.mouseClick(squish.waitForObject(locators.stepBar_check))
        squish.snooze(2)
        self.refineMesh(resolution_type)
        return CommonRefinePage(self.logfolder)

    '''
    @return: 0 means this application is on Check step view, 1 means this application is on Scan step view.
    '''
    def clickAdaptButton(self):
        test.log("click adapt step button")
        flag=False
        squish.mouseClick(squish.waitForObject(locators.stepBar_adapt))
        squish.snooze(2)
        if object.exists(locators.base_notice_ok):
            test.log("click ok button on Check First Dialog")
            squish.mouseClick(squish.waitForObject(locators.base_notice_ok))
            squish.snooze(1)
            flag=True
        return flag

    '''
    @return: 0 means this application is on Check step view, 1 means this application is on Scan step view.
    '''
    def clickExportButton(self):
        test.log("click export step button")
        flag=False
        squish.mouseClick(squish.waitForObject(locators.stepBar_export))
        squish.snooze(2)
        if object.exists(locators.base_notice_ok):
            test.log("click ok button on Check First Dialog")
            squish.mouseClick(squish.waitForObject(locators.base_notice_ok))
            squish.snooze(1)
            flag=True
        return flag

    # Refinement
    def refineMesh(self,resolution_type):
        test.log("Perform refinement with %s" %resolution_type)
    
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
            squish.snooze(20)
            test.log("Wait for another 20s")
        self.waitingProgress(10)
        squish.snooze(5)
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
    '''
    @since: 20230414
    '''
    def clickConfigScan(self):
        test.log("click config scan on workflow bar")
        flag=False
        if not object.exists(locators.workflow_add_configscan):
            test.warning("miss config scan button")
            return flag
        squish.mouseClick(squish.waitForObject(locators.workflow_add_configscan))
        squish.snooze(1)
        return flag
    
    def addDenture(self):
        test.log("click Denture on workflow panel")
        flag=False
        if object.exists(locators.workflow_panel_denture):
            prop_value=squish.waitForObjectExists(locators.workflow_panel_denture).enabled
            if prop_value==True:
                test.log("add Denture workflow")
                squish.mouseClick(squish.waitForObject(locators.workflow_panel_denture))
                squish.snooze(1)
                squish.saveDesktopScreenshot(self.logfolder+"_AddDenture.png")
                premiumDlg_exist=self.clickCancelOnPremiumDlg()
                if premiumDlg_exist==True:
                    test.verify(False==premiumDlg_exist,"Cannot add denture workflow, Premium Feature Dialog exists.")
                    squish.saveDesktopScreenshot(self.logfolder+"_PremiumFeatureDialog.png")
                else:
                    self._click_ok_on_workflow_Tip(locators.workflow_tip_denture,'Denture')
                    squish.mouseClick(squish.waitForObject(locators.workflow_denture))
                    squish.snooze(1)
                    super()._select_a_way_for_denture(0)
                    self._clickNextOnMeshQualityDlg()
                flag=True
            else:
                test.log("Denture workflow is disable")
        return flag
    
    def clickCancelOnPremiumDlg(self):
        flag=False
        if object.exists(locators.premiumDlg_title):
            squish.mouseClick(squish.waitForObject(locators.premiumDlg_later))
            squish.snooze(1)
            flag=True
        return flag
    
    def _clickNextOnMeshQualityDlg(self):
        flag=False
        squish.snooze(1)
        if object.exists(locators.meshQualityDlg_title):
            test.log("click next button on Mesh Quality dialog")
            prop_value=squish.waitForObjectExists(locators.meshQualityDlg_next).visible
            if prop_value==True:
                squish.saveDesktopScreenshot(self.logfolder+"_MeshQuality.png")
                test.log("click next button")
                squish.mouseClick(squish.waitForObject(locators.meshQualityDlg_next))
                squish.snooze(1)
                flag=True
        else:
            test.log("Mesh Quality dialog is hidden, mesh quality is ok")
        self.waitingProgress(10)    
        return flag  
    
    def addImplant(self):
        test.log("click Implant on workflow panel")
        flag=False
        if object.exists(locators.workflow_panel_implant):
            prop_value=squish.waitForObjectExists(locators.workflow_panel_implant).enabled
            if prop_value==True:
                test.log("add Implant workflow")
                squish.mouseClick(squish.waitForObject(locators.workflow_panel_implant))
                squish.snooze(1)
                
                self._click_ok_on_workflow_Tip(locators.workflow_tip_implant,'Implant')
                squish.mouseClick(squish.waitForObject(locators.workflow_implant_emergenceProfile))
                squish.snooze(1)
                super()._select_a_way_for_EmergencyProfile(0)
                self._clickNextOnMeshQualityDlg()
                self._click_next_on_cuthole()
                squish.saveDesktopScreenshot(self.logfolder+"_AddEmergenceProfile.png")
                
                squish.mouseClick(squish.waitForObject(locators.workflow_implant_scanbody))
                squish.snooze(1)
                super()._select_a_way_for_scanbody(0)
                self._clickNextOnMeshQualityDlg()
                self._click_next_on_cuthole()
                squish.saveDesktopScreenshot(self.logfolder+"_AddScanbody.png")
                flag=True
            else:
                test.log("Implant workflow is disable")
        return flag
    
    #inner
    def _click_next_on_cuthole(self):
        test.log("click next on Cut hole page")
        flag=False
        squish.snooze(1)
        locator=locators.workflow_cutHole_next
        if object.exists(locator):
            test.log("set the next button's status to enabled.")
            squish.waitForObjectExists(locator).enabled=True
            prop_value=squish.waitForObjectExists(locator).enabled
            squish.saveDesktopScreenshot(self.logfolder+"_cuthole.png")
            if prop_value==True:
                test.log("click next button")
                squish.mouseClick(squish.waitForObject(locator))
                flag=True
            else:
                test.log("next button is disabled on Cut hole page, click back to scan view")
                squish.mouseClick(squish.waitForObject(locators.workflow_cutHole_back))
            squish.snooze(1)
        return flag
    
    #inner
    def _click_ok_on_workflow_Tip(self,locator,workflow4Short):
        test.log("click OK, got it on %s Scan workflow tip" % workflow4Short)
        flag=False
        squish.snooze(1)
        if object.exists(locator):
            prop_value=squish.waitForObjectExists(locator).visible
            if prop_value==True:
                squish.saveDesktopScreenshot(self.logfolder+"_"+workflow4Short+"Tip.png")
                test.log("click OK, got it")
                squish.mouseClick(squish.waitForObject(locator))
                squish.snooze(1)
            else:
                test.log(workflow4Short+" Scan workflow tip is hidden")
            flag=True #both visible or hidden are ok.
        return flag
    
    def addPreparation(self):
        test.log("click Preparation on workflow panel")
        flag=False
        if object.exists(locators.workflow_panel_preparation):
            prop_value=squish.waitForObjectExists(locators.workflow_panel_preparation).enabled
            if prop_value==True:
                test.log("add Preparation workflow")
                squish.mouseClick(squish.waitForObject(locators.workflow_panel_preparation))
                squish.snooze(1)
                squish.saveDesktopScreenshot(self.logfolder+"_AddPreparation.png")
                squish.mouseClick(squish.waitForObject(locators.workflow_preparation))
                #self._click_ok_on_workflow_Tip(locators.workflow_tip_denture,'Preparation')
                #self._select_a_way_for_denture(0)
                self._clickNextOnMeshQualityDlg()
                flag=True
            else:
                test.log("Preparation workflow is disable")
        return flag
    def addExtra(self):
        pass
    def addImpress(self):
        pass
    
