#!/usr/bin/python
# -*- coding: UTF-8 -*-
import locators

def main():
    verifyCatalogSwitch()
    print(getattr(globals()['locators'],'leftBar_catalog_switch'))


def verifyCatalogSwitch():
    print(locators.leftBar_catalog_switch)
    print(locators.leftBar_tool_freeze)

if __name__=='__main__':
    #inputfile=r'C:\ProgramData\TW\AcqAltair\log\acqaltair_20220712.csv'
    inputfile=r'\\10.196.98.73\Test\Quality\Test_Obj_ScanFlow\Precision\Precision_Result_Ver1.0.8.302.d145\Offline_Processing_Speed\3600\ScanFlow_20230109.csv'
    main()
    #calcTimeDiff('2021-05-21T15:25:30', '2021-05-21T15:27:21')