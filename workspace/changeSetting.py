import os
import shutil
try:
    import xml.etree.cElementTree as et
except ImportError:
    import xml.etree.ElementTree as et
from xml.dom import minidom

xmlFile = r'C:\ProgramData\DEXIS IS\ScanFlow\preference.xml'

def changeSetting(xmlfile,sectionname,tagname,attrdict):
    print("==== Change preference.xml setting ====")
    tree = et.parse(xmlfile)
    root = tree.getroot()
    flag=False
    for classChild in root:
        #print classChild.tag, ":", classChild.attrib
        if classChild.attrib=={'key': sectionname}:
            for child in classChild:
                if child.tag==tagname and child.attrib['key']==attrdict['key']:
                    child.attrib['value'] = attrdict['value']
                    print("update <%s key=%s,value=%s/> under %s"%(tagname,child.attrib['key'],child.attrib['value'],sectionname))
                    flag=True
            if not flag:
                elt = classChild.makeelement(tagname, attrdict)
                classChild.append(elt)
                print("add element <%s key=%s,value=%s/> under %s" % (tagname, attrdict['key'], attrdict['value'],sectionname))

    tree.write(xmlfile)
    #tree.write(xmlfile, encoding="utf-8", xml_declaration=True)



def delAllFiles(path):
    print("clean folder: [%s]"%(path))
    for file in os.listdir(path):
        #Delete all files
        if os.path.isfile(os.path.join(path, file)):
            os.unlink(os.path.join(path, file))
        #Delete all folders
        elif os.path.isdir(os.path.join(path, file)):
            shutil.rmtree(os.path.join(path, file))
			
#changeSetting("ENABLE_TT_LICENSE_CHECK", "false")
#changeSetting("ENABLE_DATA_RECOVERY", "false")
changeSetting(xmlFile,'CONFIG','option',{'value': 'false', 'key': 'ENABLE_SN_SCANNER_TYPE_CHECK'})
changeSetting(xmlFile,'CONFIG','option',{'value': 'false', 'key': 'ENABLE_TT_LICENSE_CHECK'})
#CSDATASERVICE_REGISTER_HOST is for CSDPP sn testing
#changeSetting(xmlFile,'CONFIG','option',{'value': 'csddsci.azurewebsites.net', 'key': 'CSDATASERVICE_REGISTER_HOST'})
changeSetting(xmlFile,'CONFIG','option',{'value': 'www.carestreamdental.com', 'key': 'CSCONNECT_AUTH_HOST'})
changeSetting(xmlFile,'GENERAL','option',{'value': '2', 'key': 'INSTALLATION_TYPE'})
changeSetting(xmlFile,'GENERAL','option',{'value': 'ENGLISH', 'key': 'SOFTWARE_LANGUAGE'})
changeSetting(xmlFile,'CONFIG','option',{'value': 'false', 'key': 'ENABLE_SOFTWARE_TOUR'})
delAllFiles(r'D:\data\Export')

