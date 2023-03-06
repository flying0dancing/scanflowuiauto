# -*- coding: utf-8 -*-

from xml.etree import ElementTree as et

import names
import subprocess
import os
import time
import shutil
from remotesystem import RemoteSystem
#from pyautogui import screenshotUtil

# Switch tooth number standard
def switchToothNumberSTD(standard):
    xmlFile = "C:\\ProgramData\\TW\\AcqAltair\\preference.xml"
    tree = et.parse(xmlFile)
    
    for node in tree.find('class'):
        if node.attrib['key'] == "TOOTH_NUMBERING_SYSTEM":
            if standard == 'American':
                node.attrib['value'] = '1'
                test.verify(node.attrib['value'] == '1')
                test.log("Set tooth number to American standard.")
            elif standard == 'European':
                node.attrib['value'] = '0'
                test.verify(node.attrib['value'] == '0')
                test.log("Set tooth number to European standard.")
    tree.write(xmlFile)
    snooze(1)


#Replace preference.xml file in remote computer. Call this function only when you need distributed test
def replacePreferenceFile():
    try:
        remotesys = RemoteSystem()
        test.verify(remotesys.deleteFile("C://ProgramData//TW//AcqAltair//preference.xml"))
        test.verify(remotesys.exists("C://ProgramData//TW//AcqAltair//preference.xml") == False)
        test.verify(remotesys.upload("C://ProgramData//TW//AcqAltair//preference.xml", "C://ProgramData//TW//AcqAltair//preference.xml"))
        test.verify(remotesys.exists("C://ProgramData//TW//AcqAltair//preference.xml"))
        snooze(2)
    except Exception as e:
        test.fail("RemoteSystem error", str(e))

def testInitial():
    pass

#Delete all files under a assigned path
def delFiles(path, type):
    for folderName, subfolders, filenames in os.walk(path):
        for filename in filenames:
            if filename.endswith(type):
                test.log("%s" % os.path.join(folderName,filename))
                os.unlink(os.path.join(folderName,filename))
                test.verify(os.path.exists(os.path.join(folderName,filename)) == False, "The file '%s' should be deleted." % filename)        
    #Delete all folders and files under path
    #shutil.rmtree(path)



# Read all available cszx files under a directory
def readFiles(dataPath):
    dataFiles = []
    for r, d, f in os.walk(dataPath):
        for file in f:
            if ".cszx" in file:
                dataFiles.append(os.path.join(r,file))
    test.log("Return a list of all cszx files in a directory")
    return dataFiles

        
def testVerifyIt(objlist,propName,propExpectation,message):
    flag=False
    for tobj in objlist:
        if isinstance(tobj,dict):
            if object.exists(tobj):
                try:
                    obj=waitForObject(tobj)
                    flag=propsExists(obj,propName,propExpectation)
                    if flag:
                        test.verify(propExpectation == propExpectation, message)
                        break
                    else:
                        continue
                except LookupError:
                    pass
        else:
            flag=propsExists(tobj,propName,propExpectation)
            if flag:
                test.verify(propExpectation == propExpectation, message)
                break
            else:
                continue
    if not flag:
        test.fail(message)
        #test.verify('' == propExpectation, message)
 
"""
def testverifyItAttr(tobj,tattr,texpectation,tmessage):
    flag=propsExists(obj,tattr,texpectation)
    if flag:
        test.verify(texpectation == texpectation, tmessage)
    else:
        test.verify(False == texpectation, tmessage)
"""    
    
def objectExist(objlist):
    existObj=None
    for obj in objlist:
        if object.exists(obj):
            existObj=obj
            break
    return existObj
"""
def getItemInExportButtonList(listViewObj,selectIndex):
    #listViewObj=objectExist(listViewObjlist)
    #test.log(str(listViewObj))
    listView=waitForObject(listViewObj)
    titemObj = object.children(listView)
    test.log(str(titemObj))
    titems= object.children(titemObj[0])
    index=-1
    for titem in titems:
        index+=1
        if(index==selectIndex):
            mouseClick(waitForObject(titem))
            break
 """    
    
def getObjectByLayers(parentObj,layerList):
    #parentO=waitForObject(parentObj)
    parentO=parentObj
    childO=None
    if not layerList:
        return childO
    for i in layerList:
        childrenO=object.children(parentO)
        #test.log("children:"+str(len(childrenO)))
        #test.log("i:"+str(i))
        if i>=len(childrenO):
            childO=None
            break
        else:
            childO=object.children(parentO)[i]
        parentO=childO
    #printProps(childO)
    return childO

    
def getChildObjByProperty(parentObj,propName,propValue):
    parentO=parentObj
    childO=None
    if not propName:
        return childO
    childrenO=object.children(parentO)
    
    for childO in childrenO:
        flag=propsExists(childO,propName,propValue)
        if flag:
            break
    if not flag:
        childO=None
    return childO

def printProps(obj):
    #objO=waitForObject(obj)
    if not obj:
        return
    objO=obj
    propsO=object.properties(objO)
    for name,value in propsO.iteritems():
        test.log("%s = %s" % (name, value))
        
def propsExists(obj,propName,propValue):
    flag=False
    if not obj:
        return flag
    objO=obj
    propsO=object.properties(objO)
    if propName in propsO:
        #test.log("............................find prop "+propName)
        if propsO[propName]==propValue:
            flag=True
            #test.log("............................getIt %s = %s" % (propName, propsO[propName]))
    return flag

# find item by id, type...using parent object
def getObject(parentObjList,propName,propValue,resultList):
    parentObject=None
    if parentObjList:
        for parentObj in parentObjList:
            objList=None
            try:
                parentObject=waitForObject(parentObj)
                objList=object.children(parentObject)
                for tobj in objList:
                    tprops=object.properties(tobj)
                    test.log("props::::::"+str(tprops))
                    if(propName in tprops):
                        test.log("............................find prop")
                        if(tprops[propName]==propValue):
                            test.log("getIt.... %s = %s" % (propName, tprops[propName]))
                            resultList.append(tobj)
                            test.log("result list len:"+str(len(resultList)))
                            test.log("get"+str(tobj))
                        break
                    if len(resultList)!=0:
                        break
            except LookupError:
                test.log("cannot waitforObject")
            if len(resultList)==0:
                getObject(objList,propName,propValue,resultList)
                
    

                
        
#Check buttons after user clicks scan label in home page
def scanViewButtonsCheck():
    #clickButton(waitForObject(names.btn_box_OK_QPushButton))
    snooze(5)
    if object.exists(names.btn_not_show_again_QPushButton):
        clickButton(names.btn_not_show_again_QPushButton)
        clickButton(names.btn_ok_QPushButton)
        snooze(2)
    if object.exists(names.continue_without_signing_in_Text):
        mouseClick(waitForObject(names.continue_without_signing_in_Text))
        snooze(2)
    recoverDataDlg()
    mouseClick(waitForObject(names.scan_StyleLabel))
    snooze(5)
    test.verify(waitForObject(names.toolbar_btn_cut_GroupButton).visible == True, "Cut button should be visible.")
    test.verify(waitForObject(names.toolbar_btn_scan_area).visible == True, "Scan area button should be visible.")
    #testVerifyVisible([names.scrollArea_toolbar_btn_scan_area_csStateButton,names.toolbar_btn_scan_area], True, "Scan area button should be visible.")
    
    #test.verify(waitForObject(names.toolbar_btn_intraoral).visible == True, "Intraoral button should be visible.")
    test.verify(waitForObject(names.toolbar_btn_lock).visible == True, "Lock button should be visible.")
    test.verify(waitForObject(names.toolbar_btn_freeze).visible == True, "Freeze button should be visible.")
    test.verify(waitForObject(names.toolbar_btn_scan_history).visible == True, "Scan history button should be visible.")
    test.verify(waitForObject(names.toolbar_btn_delete_all).visible == True, "Delete button should be visible.")
    #test.verify(waitForObject(names.toolbar_btn_measurement).Visible == True, "Measurement button should be disabled")
    #mouseClick(waitForImage("..\\..\\..\\images\\scrollUpButton.png"))
    #test.verify(waitForObject(names.toolbar_btn_parallelism_check).enabled == False, "Parallelism button should be disabled")
    test.verify(waitForObject(names.catalog_bar_btn_upper).checked == True, "Upper jaw should be selected.")
    test.verify(waitForObject(names.catalog_bar_btn_lower).checked == False, "Lower jaw shouldn't be selected.")
    #test.verify(waitForObject(names.workflow_bar_btn_common).checked == True, "Common scan should be selected.") #kun mark it as comment at 20210201
    buttonsObj=waitForObject(names.catalogBar_buttons_RowLayout) #"id": "buttons" 
    btnCommon=getObjectByLayers(buttonsObj,[0])
    testVerifyIt([btnCommon],'checked',True,"Common scan should be selected.")#kun add common scan at 20210204
    #testVerifyIt([names.workflow_bar_btn_common,names.workflow_bar_btn_common1],'checked',True,"Common scan should be selected.")#kun add common scan at 20210201
    #test.verify(waitForObject(names.workflow_bar_btn_cut_hole).visible == False, "Cut hole button should be hidden before adding.")
    btnimplant=getChildObjByProperty(buttonsObj,'objectName','workflow_bar.btn_implant')
    testVerifyIt([btnimplant],'visible',False,"Implant button should be hidden before adding.")#kun add common scan at 20210204
    btnpreparation=getChildObjByProperty(buttonsObj,'objectName','workflow_bar.btn_preparation')
    testVerifyIt([btnpreparation],'visible',False,"Post scan button should be hidden before adding.")#kun add common scan at 20210204
    #test.verify(object.exists(names.workflow_bar_btn_implant) == False, "Implant button should be hidden before adding.")
    
    btnImpression=getChildObjByProperty(buttonsObj,'objectName','workflow_bar.btn_common_impression')
    testVerifyIt([btnImpression],'visible',False,"Common Impression button should be hidden before adding.")#kun add common scan at 20210204
    
    btnImpression=getChildObjByProperty(buttonsObj,'objectName','workflow_bar.btn_edentulous_impression')
    if btnImpression:
        testVerifyIt([btnImpression],'visible',False,"Edentulous Impression button should be hidden before adding.")#kun add common scan at 20210204
    
    btnImpression=getChildObjByProperty(buttonsObj,'objectName','workflow_bar.btn_implant_impression')
    testVerifyIt([btnImpression],'visible',False,"Implant Impression button should be hidden before adding.")#kun add common scan at 20210204
    
    btnImpression=getChildObjByProperty(buttonsObj,'objectName','workflow_bar.btn_preparation_impression')
    testVerifyIt([btnImpression],'visible',False,"Preparation Impression button should be hidden before adding.")#kun add common scan at 20210204
    
    #test.verify(object.exists(names.workflow_bar_btn_impression) == False, "Impression button should be hidden before adding.")
    #test.verify(object.exists(names.workflow_bar_btn_postscan) == False, "Post scan button should be hidden before adding.")
    test.log("Verify buttons in scan view page")
    snooze(2)
    
 

# Import data, make sure the scanner isn't plugged in
def importData(filename, type, flag):
    #clickButton(waitForObject(names.btn_box_OK_QPushButton))    
    snooze(5)

    recoverDataDlg()

    if object.exists(names.continue_without_signing_in_Text):
        mouseClick(waitForObject(names.continue_without_signing_in_Text))
        snooze(2)

        mouseClick(waitForObject(names.o_Image_2), 30, 32, Qt.LeftButton)
        mouseClick(waitForObject(names.o_Image_2), 25, 16, Qt.LeftButton)
        mouseClick(waitForObject(names.exit_Exit_Text))

    mouseClick(waitForObject(names.import_StyleLabel))
    snooze(2)
    nativeType(filename)
    snooze(2)
    nativeType("<Return>")
    nativeType("<Return>")
    if "shade" == flag:
        try:
            clickButton(waitForObject(names.btn_box_OK_QPushButton, 600000))
            snooze(2)
        except LookupError:
            test.log("The ok doesn't show up.")
    elif "normal" == flag:
        snooze(2)
        while object.exists(names.import_Scan_Data_StyleLabel):
            snooze(3)
            
    test.log("Import data with name: %s" % filename)
    #checkButtonState(type)
    snooze(2)
    
#Check buttons with different types
def checkButtonState(type):
    snooze(1)
    buttonsObj=waitForObject(names.catalogBar_buttons_RowLayout) #"id": "buttons"   
    btnpreparation=getChildObjByProperty(buttonsObj,'objectName','workflow_bar.btn_preparation')   
    if type == "orth":
        #test.verify(waitForObject(names.scrollArea_toolbar_btn_cut_GroupButton).visible == True, "Cut button should be visible.")#kun marked at 20210201
        testVerifyIt([names.toolbar_btn_cut_GroupButton,names.scrollArea_toolbar_btn_cut_GroupButton], 'visible',True, "Cut button should be visible.")#kun add at 20210201
        test.verify(waitForObject(names.toolbar_btn_scan_area).visible == True, "Scan area button should be visible.")
        test.verify(waitForObject(names.toolbar_btn_intraoral).visible == True, "Intraoral button should be visible.")
        test.verify(waitForObject(names.toolbar_btn_lock).visible == True, "Lock button should be visible.")
        test.verify(waitForObject(names.toolbar_btn_freeze).visible == True, "Freeze button should be visible.")
        test.verify(waitForObject(names.toolbar_btn_scan_history).visible == True, "Scan history button should be visible.")
        test.verify(waitForObject(names.toolbar_btn_delete_all).visible == True, "Delete button should be visible.")
        # test.verify(waitForObject(names.toolbar_btn_measurement).visible == True, "Measurement button should be visible.")
#       if object.exists("..\\..\\..\\images\\scrollUpButton.png"):
#            mouseClick(waitForImage("..\\..\\..\\images\\scrollUpButton.png"))
        snooze(2)
        test.verify(waitForObject(names.toolbar_btn_parallelism_check).visible == True, "Parallelism button should be visible.")
        #test.verify(waitForObject(names.workflow_bar_btn_common).checked == True, "Common scan should be selected.")
        test.log("Verify buttons for Orth data.")
    elif type == "restore":
        #test.verify(waitForObject(names.workflow_bar_btn_common).checked == False, "Common scan should be deselected.")
        #test.verify(waitForObject(names.scrollArea_toolbar_btn_cut_GroupButton).visible == True, "Cut button should be visible.")#kun marked at 20210201
        testVerifyIt([names.toolbar_btn_cut_GroupButton,names.scrollArea_toolbar_btn_cut_GroupButton], 'visible',True, "Cut button should be visible.")#kun add at 20210201
        test.verify(waitForObject(names.toolbar_btn_freeze).visible == True, "Freeze button should be visible.")
        test.verify(waitForObject(names.toolbar_btn_scan_history).visible == True, "Scan history button should be visible.")
        test.verify(waitForObject(names.toolbar_btn_delete_all).visible == True, "Delete button should be visible.")
        
        
        if btnpreparation:
            #test.verify(waitForObject(names.workflow_bar_btn_common).checked == True, "Common scan should be selected.")
            #test.verify(waitForObject(names.workflow_bar_btn_postscan).checked == False, "The post scan button should be deselected.")
            test.verify(waitForObject(names.toolbar_btn_intraoral).visible == True, "Intraoral button should be visible.")
            test.verify(waitForObject(names.toolbar_btn_lock).visible == True, "Lock button should be visible.")
            #test.verify(waitForObject(names.toolbar_btn_measurement).visible == True, "Measurement button should be visible.")
            test.verify(waitForObject(names.toolbar_btn_parallelism_check).visible == True, "Parallelism button should be visible.")
            test.log("Verify buttons for postscan data.")
        else:
            #test.verify(waitForObject(names.workflow_bar_btn_impression).checked == False, "The impression button should be selected.")
            #test.verify(waitForObject(names.workflow_bar_btn_common).checked == True, "Common scan should be selected.")
            btnCommon=getObjectByLayers(buttonsObj,[0])
            testVerifyIt([btnCommon],'checked',True,"Common scan should be selected.")
            #testVerifyIt([names.workflow_bar_btn_common,names.workflow_bar_btn_common1],'checked',True,"Common scan should be selected.")#kun add at 20210201
            test.log("Verify buttons for impression data.")
    elif type == "implant":
        snooze(2)
        btnimplant=getChildObjByProperty(buttonsObj,'objectName','workflow_bar.btn_implant')
        mouseClick(btnimplant,26, 24, Qt.LeftButton)
        #mouseClick(waitForObject(objectExist([names.workflow_bar_btn_implant,names.workflow_bar_btn_implant1]), 94506), 26, 24, Qt.LeftButton) #Kun comment it at 20200204
        
        snooze(2)
        clickButton(waitForObject(objectExist([names.workspace_Next_csButton,names.workspace_Next_csButton1])))
        snooze(2)
        #test.verify(waitForObject(names.scrollArea_toolbar_btn_cut_GroupButton).visible == True, "Cut button should be visible.")
        testVerifyIt([names.toolbar_btn_cut_GroupButton,names.scrollArea_toolbar_btn_cut_GroupButton], 'visible',True, "Cut button should be visible.")#kun add at 20210201
        test.verify(waitForObject(names.toolbar_btn_freeze).visible == True, "Freeze button should be visible.")
        test.verify(waitForObject(names.toolbar_btn_scanbody_area).visible == True, "Scanbody area button should be visible")
        test.verify(waitForObject(names.toolbar_btn_scan_history).visible == True, "Scan history button should be visible.")
        test.verify(waitForObject(names.toolbar_btn_parallelism_check).visible == True, "Parallelism button should be visible.")
        #test.verify(waitForObject(names.workflow_bar_btn_common).checked == False, "Common scan should be deselected.")
        #test.verify(waitForObject(names.workflow_bar_btn_cut_hole).checked == False, "Cut hole button shouldn't be selected.")
        #test.verify(waitForObject(names.workflow_bar_btn_implant).checked == True, "Implant button should be selected.")
        test.log("Verify buttons for implant data.") 
    
# Perform free cut on upper jaw
def cutOnUpperJaw():
    pointTopLeft = UiTypes.ScreenPoint(337, 450)
    pointTopRight = UiTypes.ScreenPoint(1747, 450)
    pointBottomRight = UiTypes.ScreenPoint(1747, 480)
    pointBottomLeft = UiTypes.ScreenPoint(337, 480)

    mouseClick(waitForObject(names.catalog_bar_btn_upper), 56, 25, Qt.NoModifier, Qt.LeftButton)
    snooze(2)
    #mouseClick(waitForImage("..\\..\\..\\images\\cutButton.png"))
    mouseClick(waitForObject(names.scrollArea_toolbar_btn_cut_GroupButton), 36, 42, Qt.NoModifier, Qt.LeftButton)
    
    snooze(2)
    
    mouseClick(pointTopLeft, Qt.NoModifier, Qt.LeftButton)
    snooze(1)
    mouseClick(pointTopRight, Qt.NoModifier, Qt.LeftButton)
    snooze(1)
    mouseClick(pointBottomRight, Qt.NoModifier, Qt.LeftButton)
    snooze(1)
    doubleClick(pointBottomLeft, Qt.NoModifier, Qt.LeftButton)
    snooze(5)
    mouseClick(waitForImage("..\\..\\..\\images\\restoreButton.png"))
    snooze(2)
    mouseClick(waitForImage("..\\..\\..\\images\\backButton.png"))
    snooze(2)
    test.log("Cut and restore on upper jaw.")


# Perform free cut on lower jaw
def cutOnLowerJaw():
    pointTopLeft = UiTypes.ScreenPoint(337, 450)
    pointTopRight = UiTypes.ScreenPoint(1747, 450)
    pointBottomRight = UiTypes.ScreenPoint(1747, 480)
    pointBottomLeft = UiTypes.ScreenPoint(337, 480)
    
    mouseClick(waitForObject(names.catalog_bar_btn_lower), 50, 41, Qt.NoModifier, Qt.LeftButton)
    snooze(2)
    mouseClick(waitForObject(names.scrollArea_toolbar_btn_cut_GroupButton), 36, 42, Qt.NoModifier, Qt.LeftButton)
    snooze(2)
    
    mouseClick(pointTopLeft, Qt.NoModifier, Qt.LeftButton)
    snooze(1)
    mouseClick(pointTopRight, Qt.NoModifier, Qt.LeftButton)
    snooze(1)
    mouseClick(pointBottomRight, Qt.NoModifier, Qt.LeftButton)
    snooze(1)
    doubleClick(pointBottomLeft, Qt.NoModifier, Qt.LeftButton)
    snooze(5)
    mouseClick(waitForImage("..\\..\\..\\images\\restoreButton.png"))
    snooze(2)
    mouseClick(waitForImage("..\\..\\..\\images\\backButton.png"))
    snooze(2)
    test.log("Cut and restore on lower jaw.")


# Refinement without shade matching
def refineMesh(resolution):
    mouseClick(waitForObject(names.mainWindow_csStateButton_2))#Kun add at 20210129 check button
    #mouseClick(waitForImage("..\\..\\..\\images\\checkButton.png"))#Kun mark it as comment at 20210129
    
    snooze(2)
    
    if object.exists(names.btn_box_Yes_QPushButton):
        clickButton(names.btn_box_Yes_QPushButton)
        snooze(2)
        
    if object.exists(names.btn_box_Yes_QPushButton):
        clickButton(names.btn_box_Yes_QPushButton)
        snooze(2)
    
    # Refine with different resolutions
    if "high" == resolution:
        clickButton(waitForObject(names.refine_view_resolution_frame_button_resolution_high_csButton))
    elif "standard" == resolution:
        clickButton(waitForObject(names.refine_view_resolution_frame_button_resolution_standard_csButton))
    elif "low" == resolution:
        clickButton(waitForObject(names.refine_view_resolution_frame_button_resolution_low_csButton))
        
    clickButton(waitForObject(names.refine_view_button_frame_button_refine_DelayButton))
    snooze(4)
    #Wait until refinement is done
    while object.exists(names.progress_view_button_cancel_progress):
        snooze(10)
        test.log("Wait for another 10s.")
    snooze(4)
    #test.compare(waitForObjectExists(names.scrollArea_toolbar_btn_cut_GroupButton).visible, True)
    testVerifyIt([names.toolbar_btn_cut_GroupButton,names.scrollArea_toolbar_btn_cut_GroupButton], 'visible',True, "Cut button should be visible.")#kun add at 20210201
        
    test.compare(waitForObjectExists(names.toolbar_btn_scan_area).visible, True)
    test.compare(waitForObjectExists(names.toolbar_btn_intraoral).visible, True)
    snooze(2)
    test.log("Perform refinement.")

    
#Check buttons after refinement
def checkAfterRefine(type):
    snooze(2)
    try:
        buttonsObj=waitForObject(names.catalogBar_buttons_RowLayout) #"id": "buttons" 
        btnpreparation=getChildObjByProperty(buttonsObj,'objectName','workflow_bar.btn_preparation')
        #test.verify(waitForObject(names.scrollArea_toolbar_btn_cut_GroupButton).visible == True, "Cut button should be visible.")
        testVerifyIt([names.toolbar_btn_cut_GroupButton,names.scrollArea_toolbar_btn_cut_GroupButton], 'visible',True, "Cut button should be visible.")#kun add at 20210201
        test.verify(waitForObject(names.toolbar_btn_scan_area).visible == True, "Scan area button should be visible.")
        test.verify(waitForObject(names.toolbar_btn_intraoral).visible == True, "Intraoral button should be visible.")
        test.verify(waitForObject(names.toolbar_btn_quadrant_snapshot).visible == True, "Quadrant button should be visible.")
        test.verify(waitForObject(names.toolbar_btn_transparency).visible == True, "Transparency button should be visible.")
        test.verify(waitForObject(names.toolbar_btn_measurement).visible == True, "Measurement button should be visible.")
        test.verify(waitForObject(names.toolbar_btn_orientation_adjustment).visible == True, "Orientation button should be visible.")
        test.verify(waitForObject(names.toolbar_btn_occlusion_pressure).visible == True, "Occlusion pressure button should be visible.")
        
        #test.verify(waitForObject(names.workflow_bar_btn_common).checked == True, "Common scan should be selected.")
        btnCommon=getObjectByLayers(buttonsObj,[0])
        testVerifyIt([btnCommon],'checked',True,"Common scan should be selected.")
        #testVerifyIt([names.workflow_bar_btn_common,names.workflow_bar_btn_common1],'checked',True,"Common scan should be selected.")#kun add common scan at 20210201
    
        if type == "orth":
            #mouseClick(waitForImage("..\\..\\..\\images\\scrollUpButton.png"))
            snooze(2)
            #test.verify(waitForObject(names.toolbar_btn_margin_line).visible == True, "Margin line button should be visible.")
            testVerifyIt([names.toolbar_btn_margin_line],'visible',True,"Margin line button should be visible.")#kun add common scan at 20210201
            test.verify(waitForObject(names.toolbar_btn_undercut).visible == True, "Under cut button should be visible.")
            test.verify(waitForObject(names.toolbar_btn_parallelism_check).visible == True, "Parallelism button should be visible.")
            test.log("Verify buttons after refinement for Orth data.")
        elif type == "restore":
            if propsExists(btnpreparation,'visible',True):
                testVerifyIt([btnpreparation],'checked',False,"The post scan button should be visible and unchecked.")#kun add common scan at 20210204
                #test.verify(waitForObject(names.workflow_bar_btn_postscan).checked == False, "The post scan button should be visible and unchecked.")
                mouseClick(btnpreparation, 36, 42, Qt.NoModifier, Qt.LeftButton)
                #mouseClick(names.workflow_bar_btn_postscan, 36, 42, Qt.NoModifier, Qt.LeftButton)
                #mouseClick(waitForImage("..\\..\\..\\images\\scrollUpButton.png"))
                snooze(2)
                test.verify(waitForObject(names.toolbar_btn_preparation_check).visible == True, "Preparation button should be visible.")
                #testVerifyIt([names.toolbar_btn_margin_line,names.toolbar_btn_margin_line1],'visible',True,"Margin line button should be visible.")#kun add common scan at 20210201
                test.verify(waitForObject(names.toolbar_btn_undercut).visible == True, "Under cut button should be visible.")
                test.verify(waitForObject(names.toolbar_btn_parallelism_check).visible == True, "Parallelism button should be visible.")
                test.verify(waitForObject(names.toolbar_btn_dual_view).visible == True, "Dual view button should be visible.")
                test.log("Verify buttons for postscan data.")
            else:
                #mouseClick(waitForImage("..\\..\\..\\images\\scrollUpButton.png"))
                snooze(2)
                #testVerifyIt([names.toolbar_btn_margin_line,names.toolbar_btn_margin_line1],'visible',True,"Margin line button should be visible.")#kun add common scan at 20210201
                test.verify(waitForObject(names.toolbar_btn_undercut).visible == True, "Under cut button should be visible.")
                test.verify(waitForObject(names.toolbar_btn_parallelism_check).visible == True, "Parallelism button should be visible.")
                test.log("Verify buttons for impression data.")
        elif type == "implant": 
            #mouseClick(waitForImage("..\\..\\..\\images\\scrollUpButton.png"))
            snooze(2)
            #test.verify(waitForObject(names.toolbar_btn_margin_line).visible == True, "Margin line button should be visible.")
            test.verify(waitForObject(names.toolbar_btn_undercut).visible == True, "Under cut button should be visible.")
            test.verify(waitForObject(names.toolbar_btn_parallelism_check).visible == True, "Parallelism button should be visible.")
            #test.verify(waitForObject(names.workflow_bar_btn_implant).visible == True, "Implant button should be visible after refinement.")       
            #test.verify(waitForObject(names.workflow_bar_btn_implant).checked == False, "Implant button should be shown and unchecked.")
            btnimplant=getChildObjByProperty(buttonsObj,'objectName','workflow_bar.btn_implant')
            testVerifyIt([btnimplant], 'visible', True, "Implant button should be visible after refinement.")#kun add common scan at 20210201
            testVerifyIt([btnimplant], 'checked', False, "Implant button should be shown and unchecked.")#kun add common scan at 20210201
            test.log("Verify buttons for implant data.")
    except LookupError as e:
        test.log("Fail to find object: %s" % str(e))

        
#Refinement with shade matching info
def refineMeshWithShade(resolution):
    mouseClick(waitForImage("..\\..\\..\\images\\checkButton.png"))
    snooze(2)
    
    if object.exists(names.btn_box_Yes_QPushButton):
        clickButton(names.btn_box_Yes_QPushButton)
        snooze(2)
        
    if object.exists(names.btn_box_Yes_QPushButton):
        clickButton(names.btn_box_Yes_QPushButton)
        snooze(2)
    
    # Refine with different resolutions
    if "High" == resolution:
        clickButton(waitForObject(names.refine_view_resolution_frame_button_resolution_high_csButton))
    elif "Standard" == resolution:
        clickButton(waitForObject(names.refine_view_resolution_frame_button_resolution_standard_csButton))
    elif "Low" == resolution:
        clickButton(waitForObject(names.refine_view_resolution_frame_button_resolution_low_csButton))
        
    clickButton(waitForObject(names.refine_view_button_frame_button_refine_DelayButton))
    
    try:
        mouseClick(waitForImage("..\\..\\..\\images\\backButton.png", {"timeout":600000}))
        snooze(2)
    except LookupError:
        test.log("The wait time isn't long enough")
    test.compare(waitForObjectExists(names.scrollArea_toolbar_btn_cut_GroupButton).visible, True)
    test.compare(waitForObject(names.toolbar_btn_scan_area).visible, True)
    test.compare(waitForObject(names.toolbar_btn_intraoral).visible, True)
    snooze(2)
    test.log("Perform refinement with shade matching")

# Draw margin line automatically, this step starts after user enters to restoration tool. x,y represent the drawing position
def autoMarginLineUpper(x, y, person):
    if not object.exists(names.toolbar_btn_restoration):
        mouseClick(waitForImage("..\\..\\..\\images\\scrollUpButton.png"))
        snooze(1)
    mouseClick(waitForObject(names.toolbar_btn_restoration), 36, 42, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.toolbar_btn_margin_line), 36, 42, Qt.NoModifier, Qt.LeftButton)
    # When two catalogs are checked, then uncheck lower jaw catalog
    if waitForObject(names.catalog_bar_btn_upper).checked:
        mouseClick(waitForObject(names.catalog_bar_btn_upper), 50, 41, Qt.NoModifier, Qt.LeftButton)
        mouseClick(waitForObject(names.catalog_bar_btn_upper), 50, 41, Qt.NoModifier, Qt.LeftButton)
    #else:
        #mouseClick(waitForObject(names.catalog_bar_btn_upper), 50, 41, Qt.NoModifier, Qt.LeftButton)
    #Click auto margin line button
    clickButton(waitForObject(names.toolbar_auto_margin_line))
    
    #Check whether the person is adult or child
    if "Adult" == person:
        ##Select a tooth number on upper jaw for adult
        clickButton(waitForObject(names.workspace_18_QPushButton ))
        test.log("Draw margin line on upper jaw automatically for adult")
    elif "Child" == person:
        #Switch to children tooth number showing
        mouseClick(waitForImage("..\\..\\..\\images\\adultToChild.png"))
        #Select a tooth number on upper jaw for child
        clickButton(waitForObject(names.workspace_55_QPushButton ))
        test.log("Draw margin line on upper jaw automatically for child")
    
    #Click on the specific position
    position = UiTypes.ScreenPoint(x, y)
    mouseClick(position, Qt.NoModifier, Qt.LeftButton)
    #Go back to restoration tool mode
    mouseClick(waitForImage("..\\..\\..\\images\\backButton.png"))
    test.verify(waitForObject(names.toolbar_btn_margin_line).visible == True)
    mouseClick(waitForImage("..\\..\\..\\images\\backButton.png"))
    snooze(2)
    
    
#Draw margin line on lower jaw
def autoMarginLineLower(x, y, person):
    if not object.exists(names.toolbar_btn_restoration):
        mouseClick(waitForImage("..\\..\\..\\images\\scrollUpButton.png"))
        snooze(1)
    #Click restoration tool button
    mouseClick(waitForObject(names.toolbar_btn_restoration), 36, 42, Qt.NoModifier, Qt.LeftButton)
    #Click margin line button
    mouseClick(waitForObject(names.toolbar_btn_margin_line), 36, 42, Qt.NoModifier, Qt.LeftButton)
    # Select lower jaw 
    mouseClick(waitForObject(names.catalog_bar_btn_lower), 50, 41, Qt.NoModifier, Qt.LeftButton)
    #Click auto margin line button
    clickButton(waitForObject(names.toolbar_auto_margin_line))
    
    if "Adult" == person:
        #Select a tooth number for adult
        clickButton(waitForObject(names.workspace_48_QPushButton ))
        snooze(1)
        test.log("Draw margin line on lower jaw automatically for adult")
    elif "Child" == person:
        #Switch to children tooth number showing
        if not object.exists(names.workspace_85_QPushButton):
            mouseClick(waitForImage("..\\..\\..\\images\\adultToChild.png"))
        #Select a tooth number on lower jaw
        clickButton(waitForObject(names.workspace_85_QPushButton))
        snooze(1)
        test.log("Draw margin line on lower jaw automatically for child")
        
    #Click on the specific position
    position = UiTypes.ScreenPoint(x, y)
    mouseClick(position, Qt.NoModifier, Qt.LeftButton)
    #Go back to restoration tool mode
    mouseClick(waitForImage("..\\..\\..\\images\\backButton.png"))
    test.verify(waitForObject(names.toolbar_btn_margin_line).visible == True)
    mouseClick(waitForImage("..\\..\\..\\images\\backButton.png"))
    snooze(2)
    

def manualMarginLineUpper(person):
    if not object.exists(names.toolbar_btn_restoration):
        mouseClick(waitForImage("..\\..\\..\\images\\scrollUpButton.png"))
    mouseClick(waitForObject(names.toolbar_btn_restoration), 36, 42, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.toolbar_btn_margin_line), 36, 42, Qt.NoModifier, Qt.LeftButton)
    # When two catalogs are checked, then uncheck lower jaw catalog
    if waitForObject(names.catalog_bar_btn_upper).checked:
        mouseClick(waitForObject(names.catalog_bar_btn_upper), 50, 41, Qt.NoModifier, Qt.LeftButton)
        mouseClick(waitForObject(names.catalog_bar_btn_upper), 50, 41, Qt.NoModifier, Qt.LeftButton)
    
    clickButton(waitForObject(names.toolbar_manual_margin_line))
    
    #Check whether the person is adult or child
    if "Adult" == person:
        clickButton(waitForObject(names.workspace_18_QPushButton ))
        test.log("Draw margin line on upper jaw manually for adult")
    elif "Child" == person:
        #Switch to children tooth number showing
        mouseClick(waitForImage("..\\..\\..\\images\\adultToChild.png"))
        #Select a tooth number on upper jaw
        clickButton(waitForObject(names.workspace_55_QPushButton ))
        test.log("Draw margin line on upper jaw manually for child")
    
    #Hard code positions for manual margin line drawing
    mouseClick(UiTypes.ScreenPoint(702, 511), Qt.NoModifier, Qt.LeftButton)
    mouseClick(UiTypes.ScreenPoint(740, 437), Qt.NoModifier, Qt.LeftButton)
    mouseClick(UiTypes.ScreenPoint(842, 429), Qt.NoModifier, Qt.LeftButton)
    mouseClick(UiTypes.ScreenPoint(938, 465), Qt.NoModifier, Qt.LeftButton)
    mouseClick(UiTypes.ScreenPoint(954, 593), Qt.NoModifier, Qt.LeftButton)
    mouseClick(UiTypes.ScreenPoint(934, 655), Qt.NoModifier, Qt.LeftButton)
    mouseClick(UiTypes.ScreenPoint(864, 679), Qt.NoModifier, Qt.LeftButton)
    mouseClick(UiTypes.ScreenPoint(764, 675), Qt.NoModifier, Qt.LeftButton)
    mouseClick(UiTypes.ScreenPoint(704, 629), Qt.NoModifier, Qt.LeftButton)
    mouseClick(UiTypes.ScreenPoint(698, 553), Qt.NoModifier, Qt.LeftButton)
    doubleClick(UiTypes.ScreenPoint(702, 511), Qt.NoModifier, Qt.LeftButton)
    
    #Go back to restoration tool mode
    mouseClick(waitForImage("..\\..\\..\\images\\backButton.png"))
    test.verify(waitForObject(names.toolbar_btn_margin_line).visible == True)
    mouseClick(waitForImage("..\\..\\..\\images\\backButton.png"))
    snooze(2)
    

#Draw margin line on lower jaw
def manualMarginLineLower(person):
    if not object.exists(names.toolbar_btn_restoration):
        mouseClick(waitForImage("..\\..\\..\\images\\scrollUpButton.png"))
    mouseClick(waitForObject(names.toolbar_btn_restoration), 36, 42, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.toolbar_btn_margin_line), 36, 42, Qt.NoModifier, Qt.LeftButton)
    
    mouseClick(waitForObject(names.catalog_bar_btn_lower), 50, 41, Qt.NoModifier, Qt.LeftButton)
    #Click auto margin line button
    clickButton(waitForObject(names.toolbar_manual_margin_line))
    
    if "Adult" == person:
        #Select a tooth number for adult
        clickButton(waitForObject(names.workspace_48_QPushButton ))
        test.log("Draw margin line on lower jaw manually for adult")
    elif "Child" == person:
        #Switch to children tooth number showing
        if not object.exists(names.workspace_85_QPushButton):
            mouseClick(waitForImage("..\\..\\..\\images\\adultToChild.png"))
        #Select a tooth number on lower jaw for child
        clickButton(waitForObject(names.workspace_85_QPushButton))
        test.log("Draw margin line on lower jaw manually for child")
    
    #Hard code positions for manual margin line drawing
    mouseClick(UiTypes.ScreenPoint(724, 562), Qt.NoModifier, Qt.LeftButton)
    mouseClick(UiTypes.ScreenPoint(739, 498), Qt.NoModifier, Qt.LeftButton)
    mouseClick(UiTypes.ScreenPoint(782, 503), Qt.NoModifier, Qt.LeftButton)
    mouseClick(UiTypes.ScreenPoint(806, 521), Qt.NoModifier, Qt.LeftButton)
    mouseClick(UiTypes.ScreenPoint(827, 566), Qt.NoModifier, Qt.LeftButton)
    mouseClick(UiTypes.ScreenPoint(823, 622), Qt.NoModifier, Qt.LeftButton)
    mouseClick(UiTypes.ScreenPoint(783, 643), Qt.NoModifier, Qt.LeftButton)
    mouseClick(UiTypes.ScreenPoint(740, 639), Qt.NoModifier, Qt.LeftButton)
    mouseClick(UiTypes.ScreenPoint(715, 615), Qt.NoModifier, Qt.LeftButton)
    mouseClick(UiTypes.ScreenPoint(710, 563), Qt.NoModifier, Qt.LeftButton)
    doubleClick(UiTypes.ScreenPoint(724, 562), Qt.NoModifier, Qt.LeftButton)
    
    #Go back to restoration tool mode
    mouseClick(waitForImage("..\\..\\..\\images\\backButton.png"))
    test.verify(waitForObject(names.toolbar_btn_margin_line).visible == True)
    mouseClick(waitForImage("..\\..\\..\\images\\backButton.png"))
    #test.log("Draw a margin line on lower jaw successfully")
    snooze(2)
    

#Export to DCM
def exportToDCM():
    mouseClick(waitForImage("..\\..\\..\\images\\exportButton.png"))
    snooze(1)
    mouseClick(waitForImage("..\\..\\..\\images\\saveButton.png"))
    snooze(1)
    mouseClick(waitForObject(names.save_StyleButton), 70, 17, Qt.LeftButton)
    snooze(1)
    test.log("Export data to DCM.")


#Deprecated
#Set a directory to save PLY or STL file
def setDirectory(directory):
    snooze(3)
    mouseClick(waitForImage("D:\\Eva\\acq_dallas_automation_test\\images\\exportButton.png"))
    snooze(1)
    mouseClick(waitForImage("D:\\Eva\\acq_dallas_automation_test\\images\\saveButton.png"))
    snooze(1)
    #Click browser button to define a directory
    mouseClick(waitForObject(names.btnBrowseExportPath_StyleButton), 31, 37, Qt.LeftButton)
    snooze(2)
    nativeType(directory)
    snooze(2)
    nativeType("<Return>")
    snooze(2)
    nativeType("<Return>")
    snooze(4)
    mouseClick(waitForImage("D:\\Eva\\acq_dallas_automation_test\\images\\sendToButton.png"))
    snooze(2)
    mouseClick(waitForImage("D:\\Eva\\acq_dallas_automation_test\\images\\checkButton2.png"))
    snooze(2)

def countFolder(path):
    """
    folders = []
    for folder in os.listdir(path):
        if os.path.isdir(os.path.join(path,folder)):
            folders.append(os.path.join(path,folder))
    return len(folders)
    """
    folderCount=0
    for folder in os.listdir(path):
        if os.path.isdir(os.path.join(path,folder)):
            folderCount=folderCount+1
    return folderCount
    
    
def clickExport():
    mouseClick(waitForObject(names.mainWindow_csStateButton))#kun add in 20210128 export
    #mouseClick(waitForImage("D:\\Eva\\acq_dallas_automation_test\\images\\exportButton.png"))#Kun mark it as comment at 20210128
    snooze(3)
    
def selectSaveTabOnExportDlg(path):
    exportWidget=waitForObject(names.mainWindow_ExportWidget)
    parentOfbuttonlist0=getObjectByLayers(exportWidget,[0,0,0])
    btnlistObj=getChildObjByProperty(parentOfbuttonlist0, 'id','button_list')
    if not btnlistObj:
        parentOfbuttonlist0=getObjectByLayers(exportWidget,[0,0,0,0])
        btnlistObj=getChildObjByProperty(parentOfbuttonlist0, 'id','button_list')
    if btnlistObj:
        btnlistObj=getObjectByLayers(parentOfbuttonlist0,[0,0,3])#save button
    if not btnlistObj:
        return False
    mouseClick(waitForObject(btnlistObj))
    #getItemInExportButtonList(btnListObj,3)#kun add in 20210202 save
    #mouseClick(findImage("D:\\Eva\\acq_dallas_automation_test\\images\\saveButton.png"))#Kun mark it as comment at 20210128
    snooze(3)
    
    savePageObj=getObjectByLayers(parentOfbuttonlist0,[1,0,1,0,0,2])#id = save_page
    txtExportPath=getObjectByLayers(savePageObj,[0,1,1,0])#id=txtExportPath
    targetDirectoryObj=waitForObject(txtExportPath)#Kun add in 20210129 Export Dlg->Save 
    test.log(str(targetDirectoryObj.text).lower()) #debug...

    if(str(targetDirectoryObj.text).lower() != path.lower()):
        btnBrowseExportPath=getObjectByLayers(savePageObj,[0,1,1,1])#id=btnBrowseExportPath
        mouseClick(waitForObject(btnBrowseExportPath))
        snooze(2)
        nativeType(path)
        snooze(2)
        nativeType("<Return>")
        nativeType("<Return>")
    snooze(2)
    checkOpenExportPathObj=getObjectByLayers(savePageObj,[0,1,2])#id=cbOpenExportPath
    mouseClick(checkOpenExportPathObj, 47, 16, Qt.LeftButton)
    return True

#Export to stl or ply format
def exportFile(format, type, path):
    """
    mouseClick(waitForObject(names.mainWindow_csStateButton))#kun add in 20210128 export
    #mouseClick(waitForImage("D:\\Eva\\acq_dallas_automation_test\\images\\exportButton.png"))#Kun mark it as comment at 20210128
    snooze(3)
    
    mouseClick(waitForObject(names.button_list_Item_4))#kun add in 20210128 save
    #mouseClick(findImage("D:\\Eva\\acq_dallas_automation_test\\images\\saveButton.png"))#Kun mark it as comment at 20210128
    snooze(2) 
    """  
    
    
    exportWidget=waitForObject(names.mainWindow_ExportWidget)
    
    parentOfbuttonlist0=getObjectByLayers(exportWidget,[0,0,0])
    flag=propsExists(object.children(parentOfbuttonlist0)[0], 'id','button_list')
    if not flag:
        parentOfbuttonlist0=getObjectByLayers(exportWidget,[0,0,0,0])
    
    savePageObj=getObjectByLayers(parentOfbuttonlist0,[1,0,1,0,0,2])#id = save_page
    
    #Export format drop down list
    #mouseClick(waitForObject(names.cbExportFormat_StyleComboBox), 381, 28, Qt.LeftButton)
    #mouseClick(waitForObject(names.content_page_Rectangle))#kun add in 20210128 dropDownArraowButton

    #mouseClick(findImage("D:\\Eva\\acq_dallas_automation_test\\images\\dropDownIcon.png"))#Kun mark it as comment at 20210128
    #mouseClick(waitForObject(names.o_Image), 15, 7, Qt.LeftButton)
    cbexportFormatObj=getObjectByLayers(savePageObj,[0,2,1])# exportFormat Rectangle
    exportFormatTxtObj=getObjectByLayers(cbexportFormatObj,[2])
    exportFormatTxt=str(exportFormatTxtObj.text)
    test.log("before select format["+format+"], display format:"+exportFormatTxt)
    
    arrowDownBtn=getObjectByLayers(cbexportFormatObj,[0])
    
    snooze(2)
    if "PLY" == format:
        if "STL" in exportFormatTxt:
            mouseClick(arrowDownBtn, 15, 7, Qt.LeftButton)
            mouseClick(arrowDownBtn, 15, 7, Qt.LeftButton)
            snooze(1)
            nativeMouseClick(262, 42, MouseButton.LeftButton)
            pass
        #mouseClick(waitForObject(names.o_ItemDelegate), 262, 42, Qt.LeftButton)
    elif "STL" == format:
        if "PLY" in exportFormatTxt:

            mouseClick(waitForObject(names.content_page_Image), 10, 9, Qt.LeftButton)
            mouseClick(waitForObject(names.o_ItemDelegate_4), 365, 21, Qt.LeftButton)
            
            #mouseClick(arrowDownBtn, 15, 7, Qt.LeftButton)
            snooze(1)
            nativeMouseClick(285, 34, MouseButton.LeftButton)
            pass
        #mouseClick(waitForOcrText("STL (Stereolithography File Format)"))
        #mouseClick(waitForObject(names.o_ItemDelegate_2), 285, 34, Qt.LeftButton)
    #snooze(2)
    exportFormatTxt=str(exportFormatTxtObj.text)
    test.log("after select format["+format+"], display format:"+exportFormatTxt)
    #ClinicalIndication drop down list
    #mouseClick(waitForObject(names.cbExportClinicalIndication_StyleComboBox), 451, 41, Qt.LeftButton)
    snooze(2)
    radioButtonObj=getObjectByLayers(savePageObj,[0,3,1])
    if "orth" == type:
        #mouseClick(waitForImage("D:\\Eva\\acq_dallas_automation_test\\images\\OrthType.png")) 
        orthodonticsRadioButton=getObjectByLayers(radioButtonObj,[0])
        mouseClick(orthodonticsRadioButton)
        #mouseClick(waitForObject(names.content_page_Orthodontics_StyleRadioButton), 90, 24, Qt.LeftButton)
    elif "restore" == type:
        #mouseClick(waitForImage("D:\\Eva\\acq_dallas_automation_test\\images\\RestoreType.png")) 
        estorationRadioButton=getObjectByLayers(radioButtonObj,[1])
        mouseClick(estorationRadioButton)
        #mouseClick(waitForObject(names.content_page_Restoration_StyleRadioButton), 78, 21, Qt.LeftButton)
    elif "implant" == type:
        implantRadioButton=getObjectByLayers(radioButtonObj,[2])
        mouseClick(implantRadioButton)
        #mouseClick(waitForObject(names.content_page_Implant_StyleRadioButton), 70, 21, Qt.LeftButton)
    snooze(2)
    currApp=currentApplicationContext()
    previousFolders = countFolder(path)
    setApplicationContext(currApp)
    savebtn=getObjectByLayers(parentOfbuttonlist0,[1,0,2,4])# save button
    mouseClick(savebtn)#kun add in 20210128 click save button
    #mouseClick(waitForObject(names.save_StyleButton), 70, 17, Qt.LeftButton)#Kun mark it as comment at 20210128
    snooze(10)
    currApp=currentApplicationContext()
    laterFolder = countFolder(path)
    setApplicationContext(currApp)
    
    snooze(2)
    test.verify(laterFolder == previousFolders + 1, "The folder count should be added 1.")
    test.log("laterFolder:"+str(laterFolder)+"  previousFolders:"+str(previousFolders))
    while object.exists(names.processing_please_wait_StyleLabel):
        snooze(5)
    
    #btnListObjList=[]
    #getObject(names.mainWindow_ExportWidget,'id','button_list',btnListObjList)
    #getItemInExportButtonList(btnListObjList[0],0)#kun add in 20210201
    #snooze(1)
    #mouseClick(waitForImage("D:\\Eva\\acq_dallas_automation_test\\images\\sendToButton.png"))#Kun mark it as comment at 20210128
    
    
    #mouseClick(waitForImage(r"D:\Eva\acq_dallas_automation_test\images\checkButton2.png"))#Kun mark it as comment at 20210128



"""Export STL or PLY files"""
def export_STL_PLY(type, path):
    clickExport()
    flag=selectSaveTabOnExportDlg(path)
    if flag:
        #Export to STL format
        exportFile("STL", type, path)
    
        #Export to PLY format
        exportFile("PLY", type, path)
        test.log("finished export STL PLY files, checked in folder: "+path)
        exportWidget=waitForObject(names.mainWindow_ExportWidget)
        parentOfbuttonlist0=getObjectByLayers(exportWidget,[0,0,0])
        flag1=propsExists(object.children(parentOfbuttonlist0)[0], 'id','button_list')
        if not flag1:
            parentOfbuttonlist0=getObjectByLayers(exportWidget,[0,0,0,0])

        cancelbtn=getObjectByLayers(parentOfbuttonlist0,[1,0,2,1])# cancel button
        mouseClick(cancelbtn)
    else:
        test.log("this scanflow doesn't contains function which save file to local.")
    
    
    snooze(2)

#Open with 3rd party software
def openWithMeshViewer():
    mouseClick(waitForImage("..\\..\\..\\images\\exportButton.png"))
    snooze(1)
    mouseClick(waitForImage("..\\..\\..\\images\\openWithButton.png"))
    snooze(1)
    mouseClick(waitForObject(names.cS_MeshViewer_StyleLabel))
    snooze(1)
    #Click Clinical Indication drop down list
    mouseClick(waitForObject(names.o_Image_3), 12, 3, Qt.LeftButton)
    snooze(1)
    #Select Restoration option
    mouseClick(waitForObject(names.o_ItemDelegate_2), 183, 46, Qt.LeftButton)
    snooze(1)
    mouseClick(waitForObject(names.open_StyleButton), 132, 52, Qt.LeftButton)
    snooze(15)
    #Take a screenshot
    now = time.strftime("%y-%m-%d_%H-%M-%S", time.localtime())
    imageName = now + "_screenshot.png"
    screenshotPath = "D:\\Eva\\TestSuites\\screenshots"
    screenshotUtil.screenshot(os.path.join(screenshotPath, imageName))
    snooze(5)
    test.verify(os.path.isfile(os.path.join(screenshotPath, imageName)) == True, "Screenshot is saved.")
    os.system("taskkill /f /im CSMeshViewer.exe")
    snooze(2)
    

#Cut file of any type from source directory to dest directory
def moveFile(source, dest, type):
    for filename in os.listdir(source):
        if filename.endswith(type):
            shutil.move(os.path.join(source,filename),dest)
            test.verify(os.path.isfile(os.path.join(source,filename)) == False, "The '%s' file should be moved." % os.path.join(source,filename))

#Export to CSZ
def exportToCSZ(path, name):
    menuButtonObj=None
    if object.exists(names.mainWindow_button_menu_csButton):
        menuButtonObj=waitForObject(names.mainWindow_button_menu_csButton)
    else:
        root_TitleBar=waitForObject(names.root_TitleBar)
        menuButtonObj=getObjectByLayers(root_TitleBar,[3,3,0,0])  #scanflow version 1.0.3.1000
        if not menuButtonObj:
            menuButtonObj=getObjectByLayers(root_TitleBar,[2,2,0,0]) #scanflow version 1.0.3.600
        
    mouseClick(menuButtonObj, 31, 10, Qt.NoModifier, Qt.LeftButton)
    #clickButton(waitForObject(objectExist([names.menuButton_StyleButton,names.mainWindow_button_menu_csButton]))) #kun comment at 20210204
    snooze(2)
   
    mouseClick(waitForObject(names.mainMenu_Export_Raw_Data_csButton), 88, 29, Qt.NoModifier, Qt.LeftButton)
   
    snooze(3)
    
    filename = path + "\\" + name
    test.log("Saved CSZ name: %s" % filename)
    nativeType(filename)
    snooze(2)
    nativeType("<Return>")
    snooze(2)
    while object.exists(names.animateRect_Rectangle):
        snooze(10)
        test.log("Waiting for exporting...")
    #Check whether the file exported successfully
    snooze(2)
    fileCheck = os.path.isfile(filename)
    if fileCheck:
        test.passes("Export to CSZ file successfully.")
    else:
        test.fail("No CSZ file found")
    snooze(2)
    
    
    
#Check whether user need to switch to common scan
def restoreCheckBeforeCut():
    snooze(2)
    buttonsObj=waitForObject(names.catalogBar_buttons_RowLayout) #"id": "buttons" 
    btnCommon=getObjectByLayers(buttonsObj,[0])
    #if (waitForObject(names.workflow_bar_btn_common).checked == False):
    if propsExists(btnCommon,'checked',False):
        #mouseClick(waitForObject(names.workflow_bar_btn_common),32, 23, Qt.NoModifier, Qt.LeftButton)
        mouseClick(btnCommon,32, 23, Qt.NoModifier, Qt.LeftButton)
        snooze(2)
    
    if object.exists(names.btn_box_Yes_QPushButton):
        clickButton(names.btn_box_Yes_QPushButton)
        snooze(3)
      

#Post scan check before refinement
def postscanCheck():
    snooze(2)
    buttonsObj=waitForObject(names.catalogBar_buttons_RowLayout) #"id": "buttons" 
    btnpreparation=getChildObjByProperty(buttonsObj,'objectName','workflow_bar.btn_preparation')
    #if (object.exists(names.workflow_bar_btn_postscan)):
    if btnpreparation:
        mouseClick(waitForObject(btnpreparation),46, 35, Qt.NoModifier, Qt.LeftButton)
        #mouseClick(waitForObject(names.workflow_bar_btn_postscan),46, 35, Qt.NoModifier, Qt.LeftButton)
        while(object.exists(names.mainWindow_BusyDialog)):
            continue
        snooze(3)
        cutOnUpperJaw()
        cutOnLowerJaw()
    test.log("Perform cut and restore if post scan is available")

#Kill ACQ software
def killApp():
    subprocess.call([r'C:\auto_click_run\kill_io_3d_acq.exe.bat'])
    snooze(2)
    test.log("Kill ACQ application")
    


def recoverDataDlg():
    if not object.exists(names.o_MessageDialog):
        return
    msgDlg=waitForObject(names.o_MessageDialog)
    msgContent=getObjectByLayers(msgDlg,[0,0,0,0,1])
    msgTitle=getObjectByLayers(msgContent,[1])
    if(str(msgTitle.text) == 'Recover Data'):
        msgCancelBtn=getObjectByLayers(msgContent,[4,0,0])
        mouseClick(msgCancelBtn) 
        snooze(3)
        
def userLogin(user, password):
    if object.exists(names.sign_In_StyleButton):
        loginObj=waitForObject(names.userLoginPart_UserLoginPart) #"objectName": "userLoginPart"
        btnClear=getObjectByLayers(loginObj,[0,2]) # clear user
        if propsExists(btnClear,'enabled',True):
            mouseClick(btnClear)
            snooze(1)
        type(getObjectByLayers(loginObj,[0]), user)
        btnClear=getObjectByLayers(loginObj,[1,2]) # clear password
        if propsExists(btnClear,'enabled',True):
            snooze(1)
            mouseClick(btnClear)
        type(getObjectByLayers(loginObj,[1]), password)
        
        mouseClick(waitForObject(names.sign_In_StyleButton)) #click Sign In
        snooze(2)   
def closeApplication():
    test.log("close application")
    mouseClick(waitForObject(names.closeButton_StyleButton))

    
    mouseClick(waitForObject(names.exit_Exit_Text))
    #Wait until save data is done
    
    snooze(25)
    pass




