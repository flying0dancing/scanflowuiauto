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
    def __init__(self,logfolder):
        self.logfolder=logfolder
    
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
        squish.snooze(15)

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
    
    def visibleEmergencyProfile(self):
        return self.isVisibleInBasePage(locators.workflow_implant_emergenceProfile)
    
    def visibleEmergencyProfileImpress(self):
        return self.isVisibleInBasePage(locators.workflow_implant_emergenceProfile_impress)
    
    def visibleScanbody(self):
        return self.isVisibleInBasePage(locators.workflow_implant_scanbody)
    
    def visibleImplantMatching(self):
        return self.isVisibleInBasePage(locators.workflow_implant_matching)
    
    def visibleEdentulousImpress(self):
        return self.isVisibleInBasePage(locators.workflow_edentulous_impression)
    
    def visibleEdentulous(self):
        return self.isVisibleInBasePage(locators.workflow_edentulous)
    
    def visibleDenture(self):
        return self.isVisibleInBasePage(locators.workflow_denture)
    
    def visibleDentureMatching(self):
        return self.isVisibleInBasePage(locators.workflow_denture_matching)
    
    def visiblePreparation(self):
        return self.isVisibleInBasePage(locators.workflow_preparation)
    
    def visiblePreparationImpress(self):
        return self.isVisibleInBasePage(locators.workflow_preparation_impress)
    
    def visibleExtra(self):
        return self.isVisibleInBasePage(locators.workflow_extra)

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
                squish.snooze(1)
                self._select_a_way_for_EmergencyProfile(2)
                self._select_a_way_for_scanbody(2)
                self._select_a_way_for_denture(2)
                self.waitingProgress(10)
                flag=True
        return flag
    
    def _select_a_way_for_scanbody(self,optionFlag):
        flag=False
        squish.snooze(1)
        if object.exists(locators.workflow_copyDlg_scanbody_title):
            test.log("Scanbody Scan copy Dialog")
            if optionFlag==0:#copy from common scan
                prop_value=squish.waitForObjectExists(locators.workflow_copyDlg_scanbody_copyfrom_common).enabled
                if prop_value==True:
                    test.log("select copy from common scan")
                    squish.mouseClick(squish.waitForObject(locators.workflow_copyDlg_scanbody_copyfrom_common))
            if optionFlag==1:#copy from EmergenceProfile scan
                prop_value=squish.waitForObjectExists(locators.workflow_copyDlg_scanbody_copyfrom_emergenceProfile).enabled
                if prop_value==True:
                    test.log("select copy from EmergenceProfile scan")
                    squish.mouseClick(squish.waitForObject(locators.workflow_copyDlg_scanbody_copyfrom_emergenceProfile))
                else:
                    prop_value=squish.waitForObjectExists(locators.workflow_copyDlg_scanbody_copyfrom_common).enabled
                    if prop_value==True:
                        test.log("EmergenceProfile might empty cannot copy from it, select copy from common scan")
                        squish.mouseClick(squish.waitForObject(locators.workflow_copyDlg_scanbody_copyfrom_common))
                
            if optionFlag==2:#new scan
                prop_value=squish.waitForObjectExists(locators.workflow_copyDlg_emergenceProfile_new_scan).enabled
                if prop_value==True:
                    test.log("select start new scan")
                    squish.mouseClick(squish.waitForObject(locators.workflow_copyDlg_emergenceProfile_new_scan))
            squish.snooze(1)
            squish.saveDesktopScreenshot(self.logfolder+"_ScanbodyScanCopyDialog.png")        
            test.log("click OK on Scanbody Scan copy Dialog")        
            squish.mouseClick(squish.waitForObject(locators.workflow_copyDlg_scanbody_ok))
            self.waitingProgress(10)  
            flag=True
        return flag
    
    def _select_a_way_for_EmergencyProfile(self,optionFlag):
        flag=False
        squish.snooze(1)
        if object.exists(locators.workflow_copyDlg_emergenceProfile_title):
            test.log("EmergencyProfile Scan copy Dialog")  
            if optionFlag==0:#copy from common scan
                prop_value=squish.waitForObjectExists(locators.workflow_copyDlg_emergenceProfile_copyfrom_common).enabled
                if prop_value==True:
                    test.log("select copy from common scan")
                    squish.mouseClick(squish.waitForObject(locators.workflow_copyDlg_emergenceProfile_copyfrom_common))
            if optionFlag==2:#new scan
                prop_value=squish.waitForObjectExists(locators.workflow_copyDlg_emergenceProfile_new_scan).enabled
                if prop_value==True:
                    test.log("select start new scan")
                    squish.mouseClick(squish.waitForObject(locators.workflow_copyDlg_emergenceProfile_new_scan))
            squish.snooze(1)
            squish.saveDesktopScreenshot(self.logfolder+"_EmergencyProfileScanCopyDialog.png")        
            test.log("click OK on EmergencyProfile Scan copy Dialog")        
            squish.mouseClick(squish.waitForObject(locators.workflow_copyDlg_emergenceProfile_ok))
            self.waitingProgress(10)
            flag=True
        return flag
    
    def _select_a_way_for_denture(self,optionFlag):
        flag=False
        squish.snooze(1)
        if object.exists(locators.workflow_copyDlg_denture_title):
            test.log("Denture Scan copy Dialog")   
            if optionFlag==0:#copy from common scan
                prop_value=squish.waitForObjectExists(locators.workflow_copyDlg_denture_copyfrom_common).enabled
                if prop_value==True:
                    test.log("select copy from common scan")
                    squish.mouseClick(squish.waitForObject(locators.workflow_copyDlg_denture_copyfrom_common))
            if optionFlag==1:#copy from edentulous scan
                #TODO
                pass
            if optionFlag==2:#new scan
                prop_value=squish.waitForObjectExists(locators.workflow_copyDlg_denture_new_scan).enabled
                if prop_value==True:
                    test.log("select start new scan")
                    squish.mouseClick(squish.waitForObject(locators.workflow_copyDlg_denture_new_scan))
            squish.saveDesktopScreenshot(self.logfolder+"_DentureScanCopyDialog.png")        
            test.log("click OK on Denture Scan copy Dialog")        
            squish.mouseClick(squish.waitForObject(locators.workflow_copyDlg_denture_ok))
               
            self.waitingProgress(10)
            squish.snooze(5)
            flag=True

        return flag
    
    
    def clickCommonScan(self):
        return self.getToolTipAndClickWhenVisible(locators.workflow_common,"Common Scan")

    def clickCommonImpress(self):
        return self.getToolTipAndClickWhenVisible(locators.workflow_common_impress,"Common Scan-Impress")

    def clickEmergencyProfile(self):
        return self.getToolTipAndClickWhenVisible(locators.workflow_implant_emergenceProfile,"Emergence Profile Scan")

    def clickEmergencyProfileImpress(self):
        return self.getToolTipAndClickWhenVisible(locators.workflow_implant_emergenceProfile_impress,"Emergence Profile Scan-Impress")
    
    def clickImplantMatching(self):
        return self.getToolTipAndClickWhenVisible(locators.workflow_implant_emergenceProfile_impress,"Implant Matching")
    
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
    
    @staticmethod
    def acqCatalogsDict():
        acqDict={'3':'Scanbody Lower','4':'Scanbody Upper','6':'Preparation Lower','7':'Preparation Upper',
              '8':'Edentulous Lower','9':'Edentulous Upper','130':'Emergence Profile Lower','131':'Emergence Profile Upper',
              '140':'Denture Lower','141':'Denture Upper'}
        return acqDict
    '''
    
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
    
    