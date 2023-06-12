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
    if config['test']['test_mode']=='debug':
        tmp=config['test.debug']['test_source_path']
    else:
        tmp=config['test.release']['test_source_path']
    return tmp

def getTestConfigPool():
    config=getConfig()
    if config['test']['test_mode']=='debug':
        tmp=config['test.debug']['test_config_path']
    else:
        tmp=config['test.release']['test_config_path']
    return tmp

def getTestLogFolder():
    config=getConfig()
    if config['test']['test_mode']=='debug':
        tmp=config['test.debug']['test_log_path']
    else:
        tmp=config['test.release']['test_log_path']
    return tmp

def getTestMode():
    config=getConfig()
    return config['test']['test_mode']

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

def getScanFlowTempFolder():
    config=getConfig()
    return config['product']['ScanFlow_Temp_folder']

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

def getTestConfig(testName,suffix):
    tconfig=''
    config=getConfig()
    if config['test']['test_mode']=='debug':
        tconfig='inputdata.tsv'
    else:
        tconfig=config['test.release']['test_config_path']+testName+suffix
    return tconfig
if __name__=='__main__':
    #print(str(sys.argv))
    #inputfile=r'C:\ProgramData\TW\AcqAltair\log\acqaltair_20220712.csv'
    inputfile=r'C:\ProgramData\DEXIS IS\ScanFlow\new2.xml'
    #main(inputfile)
    print(getTestLogFolder())
