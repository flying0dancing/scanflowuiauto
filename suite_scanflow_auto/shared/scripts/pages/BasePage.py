# -*- coding: utf-8 -*-
''' 
@author: Kun Shen
@since: 20230130
'''
import object
import test
import squish
import locators
class BasePage():
    def waitingProgress(self,seconds):
        while object.exists(locators.base_waiting_progress):
            squish.snooze(seconds)
            test.log("Wait for another "+str(seconds)+"s")
            
    def clickMenuButton(self):
        test.log("click menu on top bar")  
        squish.mouseClick(squish.waitForObject(locators.titleBar_menu))  
        squish.snooze(2) 
    
    def clickCloseButton(self):
        test.log("click close on top bar")  
        squish.mouseClick(squish.waitForObject(locators.titleBar_close))  
        squish.snooze(2) 
        self.clickExitButton()
        
    
    def clickExitButton(self):
        test.log("click exit button on Exit Dialog")
        squish.snooze(1)
        squish.mouseClick(squish.waitForObject(locators.exitDlg_exit_button))
        squish.snooze(10)

    def getStatusScanStep(self):
        prop_value=squish.waitForObject(locators.stepBar_scan).checked
        test.log("locators.stepBar_scan [checked: %s]" % prop_value)
        return prop_value

    def getStatusRefineStep(self):
        prop_value=squish.waitForObject(locators.stepBar_check).checked
        test.log("locators.stepBar_check [checked: %s]" % prop_value)
        return prop_value

    def getStatusAdaptStep(self):
        prop_value=squish.waitForObject(locators.stepBar_adapt).checked
        test.log("locators.stepBar_adapt [checked: %s]" % prop_value)
        return prop_value

    def getStatusExportStep(self):
        prop_value=squish.waitForObject(locators.stepBar_export).checked
        test.log("locators.stepBar_export [checked: %s]" % prop_value)
        return prop_value


    def visibleCommonImpress(self):
        return self.isVisibleInBasePage(locators.workflow_common_impress)
    def visibleEmergencyProfileImpress(self):
        return self.isVisibleInBasePage(locators.workflow_implant_emergencyProfile_impress)
    def visibleEdentulousImpress(self):
        return self.isVisibleInBasePage(locators.workflow_edentulous_impression)


    def isVisibleInBasePage(self,locator):
        flag=False
        if object.exists(locator):
            prop_value=squish.waitForObjectExists(locator).visible
            squish.snooze(1)
            flag=prop_value
        return flag
        
    def getToolTipAndClickWhenVisible(self,locator,tipStr):
        flag=False
        if object.exists(locator):
            obj=squish.waitForObjectExists(locator)
            prop_value=obj.visible
            squish.snooze(1)
            if prop_value==True:
                #id=getPropValue(obj,'id')
                test.log("click acquisition catalog: %s" % tipStr)
                squish.mouseClick(obj)
                squish.snooze(2)
                self.waitingProgress(10)
                flag=True
        return flag

    def clickCommonScan(self):
        return self.getToolTipAndClickWhenVisible(locators.workflow_common,"Common Scan")

    def clickCommonImpress(self):
        return self.getToolTipAndClickWhenVisible(locators.workflow_common_impress,"Common Scan-Impress")

    def clickEmergencyProfile(self):
        return self.getToolTipAndClickWhenVisible(locators.workflow_implant_emergencyProfile,"Emergence Profile Scan")

    def clickEmergencyProfileImpress(self):
        return self.getToolTipAndClickWhenVisible(locators.workflow_implant_emergencyProfile_impress,"Emergence Profile Scan-Impress")
    
    def clickImplantMatching(self):
        return self.getToolTipAndClickWhenVisible(locators.workflow_implant_emergencyProfile_impress,"Implant Matching")
    def clickScanBody(self):
        return self.getToolTipAndClickWhenVisible(locators.workflow_implant_scanbody,"Scanbody Scan")    

    def clickEdentulous(self):
        return self.getToolTipAndClickWhenVisible(locators.workflow_edentulous,"Edentulous Scan")

    def clickEdentulousImpress(self):
        return self.getToolTipAndClickWhenVisible(locators.workflow_edentulous_impress,"Edentulous Scan-Impress")

    def clickPreparation(self):
        return self.getToolTipAndClickWhenVisible(locators.workflow_preparation,"Preparation Scan")
    
    def clickDenture(self):
        return self.getToolTipAndClickWhenVisible(locators.workflow_denture,"Denture Scan")
    
    def clickDentureMatching(self):
        return self.getToolTipAndClickWhenVisible(locators.workflow_denture_matching,"Denture Matching")
    
    
    '''
    Catalogs dictionary without common scan catalog
    '''
    def acqCatalogsDict(self):
        acqDict={'3':'Scanbody Lower','4':'Scanbody Upper','6':'Preparation Lower','7':'Preparation Upper',
              '8':'Edentulous Lower','9':'Edentulous Upper','130':'Emergence Profile Lower','131':'Emergence Profile Upper',
              '140':'Denture Lower','141':'Denture Upper'}
        return acqDict
    
    def isEnabledButton(self,locator):
        flag=False
        if object.exists(locator):
            obj=squish.waitForObjectExists(locator)
            flag=obj.enabled
        return flag
    def getStatusUpperJaw(self):
        return self.isEnabledButton(locators.leftBar_catalog_upper)
    def getStatusLowerJaw(self):
        return self.isEnabledButton(locators.leftBar_catalog_lower)
    
    