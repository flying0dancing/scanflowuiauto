# -*- coding: utf-8 -*-
import object
import test
import squish
import locators
class LeftBarTool():
    
    def verifyLeftTool(self,locatorName,verifiedDict={'toolTip':'toolTip','premium':'False','checked':'False','enabled':'False','visible':'False'}):
        modulename='locators'
        objOrigin=getattr(globals()[modulename],locatorName,'ObjectNotExists')
        logstr=''
        flag=True
        if object.exists(objOrigin):
            obj=squish.waitForObjectExists(objOrigin)
            #obj=objOrigin
            for key in verifiedDict.keys():
                realValue=self.getPropValue(obj, key)
                expectedValue=verifiedDict[key]
                if realValue.lower()==expectedValue.lower():
                    pass
                else:
                    logstr=logstr+key+'[real:'+realValue+', expected:'+expectedValue+']; '
                    flag=False
            if flag:
                logstr=locatorName+' {'+self.getProps2String(obj)+'}'
            else:
                logstr=locatorName+' '+logstr
        else:
            logstr=locatorName+' does not exist'
            flag=False
        return (flag, logstr)            

    
    def verifyIt(self,locatorName):
        if object.exists(locatorName):
            obj=squish.waitForObjectExists(locatorName)
            self.getProps2String(obj)
        else:
            test.log("locatorName %s does not exist" %(locatorName.decode()))

    def getPropValue(self,obj,propName):
        if not obj:
            return 'ObjectNotExists'
        objO=obj
        result='PropertyNotExists'
        propsO=object.properties(objO)
        if propName in propsO.keys():
            result=str(propsO[propName])
        return result
        
    def getProps2String(self,obj,propsList=['visible','enabled','checked','premium','toolTip']):
        #objO=squish.waitForObject(obj)
        if not obj:
            return
        objO=obj
        propsO=object.properties(objO)
        result=''
        for key in propsList:
            if key in propsO.keys():
                result=key+":"+str(propsO[key])+", "+result
        result=result[:-2] #remove last ", "
        #test.log(result)
        return result    



    