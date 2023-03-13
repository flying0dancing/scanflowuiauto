#!/usr/bin/python
# -*- coding: UTF-8 -*-
import configparser
import os.path
import sys
def main(inputFile,sectionStr,keyStr,valueStr):
    if os.path.isfile(inputFile):
        config = configparser.RawConfigParser()
        config.optionxform=lambda optionstr:optionstr #reserve options' lower/upper cases
        config.read(inputFile)
        if config.has_section(sectionStr):
            for key, value in config[sectionStr].items():
                if key.lower() in  [keyStr]:
                    print("key %s, value %s"%(key,value))
                    config.set(sectionStr,key,valueStr)
                    config.write(open(inputFile,'w'))

if __name__=='__main__':
    print(str(sys.argv))
    inputFile=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+"\\suite_scanflow_auto\\shared\\scripts\\Resources\\config.ini"
    main(inputFile,'test','test_mode','release')