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
from pages.ExportDialog import ExportDialog
class CommonRefinePage(BasePage):
    def __init__(self,logfolder):
        super().__init__(logfolder)
    '''
    @param flag: 1 means discard refine data
    '''        
    def clickScanButton(self,flag):
        test.log("click scan step button")
        squish.mouseClick(squish.waitForObject(locators.stepBar_scan))
        squish.snooze(2)
        if object.exists(locators.refineStep_discardDlg_discard) and flag==1:
            test.log("click Discard button on Discard Refine Data Dialog")
            squish.mouseClick(squish.waitForObject(locators.refineStep_discardDlg_discard))
            squish.snooze(1)
        else:
            test.log("click cancel button on Discard Refine Data Dialog")
            squish.mouseClick(squish.waitForObject(locators.base_notice_cancel))
            squish.snooze(1)


    '''

    '''
    def clickAdaptButton(self):
        test.log("click adapt step button")
        squish.mouseClick(squish.waitForObject(locators.stepBar_adapt))
        squish.snooze(2)
        return 0


    '''

    '''
    def clickExportButton(self):
        test.log("click export step button")
        squish.mouseClick(squish.waitForObject(locators.stepBar_export))
        squish.snooze(2)
        return ExportDialog(self.logfolder)
   
    '''
    def selectSaveTabOnExportDlg(self,path):
        exportWidget=squish.waitForObject(names.mainWindow_ExportWidget)
        parentOfbuttonlist0=getObjectByLayers(exportWidget,[0,0,0])
        btnlistObj=getChildObjByProperty(parentOfbuttonlist0, 'id','button_list')
        if not btnlistObj:
            parentOfbuttonlist0=getObjectByLayers(exportWidget,[0,0,0,0])
            btnlistObj=getChildObjByProperty(parentOfbuttonlist0, 'id','button_list')
        if btnlistObj:
            btnlistObj=getObjectByLayers(parentOfbuttonlist0,[0,0,3])#save button
        if not btnlistObj:
            return False
        squish.mouseClick(squish.waitForObject(btnlistObj))
        #getItemInExportButtonList(btnListObj,3)#kun add in 20210202 save
        squish.snooze(3)
    
        savePageObj=getObjectByLayers(parentOfbuttonlist0,[1,0,1,0,0,2])#id = save_page[1,0,0,1,2]
        txtExportPath=getObjectByLayers(savePageObj,[0,1,1,0])#id=txtExportPath
        targetDirectoryObj=squish.waitForObject(txtExportPath)#Kun add in 20210129 Export Dlg->Save 
        test.log(str(targetDirectoryObj.text).lower()) #debug...

        if(str(targetDirectoryObj.text).lower() != path.lower()):
            btnBrowseExportPath=getObjectByLayers(savePageObj,[0,1,1,1])#id=btnBrowseExportPath
            squish.mouseClick(squish.waitForObject(btnBrowseExportPath))
            squish.snooze(2)
            nativeType(path)
            squish.snooze(2)
            nativeType("<Return>")
            nativeType("<Return>")
        squish.snooze(2)
        checkOpenExportPathObj=getObjectByLayers(savePageObj,[0,1,2])#id=cbOpenExportPath
        squish.mouseClick(checkOpenExportPathObj, 47, 16, Qt.LeftButton)
        return True
    '''
    def isInRefineView(self):
        return self.getStatusScanStep()==False and self.getStatusRefineStep()==True


    def onlyHasCommonScanCatalog(self):
        flag=True
        for locator in [locators.workflow_implant_emergencyProfile,locators.workflow_implant_scanbody,locators.workflow_preparation,locators.workflow_edentulous,locators.workflow_extra]:
            if self.isVisibleInBasePage(locator):
                flag=False
                break
        return flag
    
    