import configparser

from utils import DateTimeUtil
from docs.Conf import BASE_DIR
def getConfig():
    # defined config file full path
    path=BASE_DIR+r'\shared\scripts\Resources\config.ini'
    config=configparser.ConfigParser()
    config.read(path)
    return config

def getScanFlowVersion():
    config=getConfig()
    return config['product']['ScanFlow_Version']

def getTestDataPool():
    config=getConfig()
    return config['test']['test_source_path']

def getScanFlowRoot():
    config=getConfig()
    return config['product']['ScanFlow_Root']

def getScanFlowLog():
    config=getConfig()
    log_path=config['product']['ScanFlow_Log_Path']
    log_name=config['product']['ScanFlow_Log_Name_ScanFlow_Format']
    log_name=log_name.replace('yyyymmdd',DateTimeUtil.get_dateYYYMMDD())
    return log_path+log_name

def getScanFlowLaunchStrByCmd():
    config=getConfig()
    return config['product']['ScanFlow_Launch_CmdLine']

def getTestLogFolder():
    config=getConfig()
    return config['test']['test_log_path']

def getTools_Import_Scanview():
    config=getConfig()
    return config['test']['tools_import_scanview']
def getTools_Scan_Scanview():
    config=getConfig()
    return config['test']['tools_scan_scanview']
def getTools_Import_Scanview_Impress():
    config=getConfig()
    return config['test']['tools_import_scanview_impress']
def getTools_Import_Refineview():
    config=getConfig()
    return config['test']['tools_import_refineview']
if __name__=='__main__':
    #print(str(sys.argv))
    #inputfile=r'C:\ProgramData\TW\AcqAltair\log\acqaltair_20220712.csv'
    inputfile=r'C:\ProgramData\DEXIS IS\ScanFlow\new2.xml'
    #main(inputfile)
    print(getTestLogFolder())
