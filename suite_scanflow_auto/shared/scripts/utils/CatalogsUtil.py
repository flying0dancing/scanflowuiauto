# -*- coding: utf-8 -*-
from utils import ZipUtil, DateTimeUtil
import test

acqDict={'3':'Scanbody Lower','4':'Scanbody Upper','6':'Preparation Lower','7':'Preparation Upper',
              '8':'Edentulous Lower','9':'Edentulous Upper','130':'Emergence Profile Lower','131':'Emergence Profile Upper',
              '140':'Denture Lower','141':'Denture Upper'} #not include common for judged flag=notonlycommon or not.

'''
def acqCatalogsDict():
        acqDict={'3':'Scanbody Lower','4':'Scanbody Upper','6':'Preparation Lower','7':'Preparation Upper',
              '8':'Edentulous Lower','9':'Edentulous Upper','130':'Emergence Profile Lower','131':'Emergence Profile Upper',
              '140':'Denture Lower','141':'Denture Upper'}
        return acqDict
'''
class AcqCatalogs():
    #__acqIdentifiers
    __file_name=''
    __pass_30days=False
    __common_upper=False
    __common_lower=False
    __common_bite=False
    __scanbody_upper=False
    __scanbody_lower=False
    __emergenceProfile_upper=False
    __emergenceProfile_lower=False
    __preparation_lower=False
    __preparation_upper=False
    __edentulous_lower=False
    __edentulous_upper=False
    __denture_lower=False
    __denture_upper=False
    __extra=False
    __shade=False
    
    
    __scanRefList=[]
    __refineRefList=[]
    
    def __init__(self,zipFile):
        acqIdentifiers=ZipUtil.getInitialRefsFromZipFile(zipFile)
        
        if '0' in acqIdentifiers:
            self.set_common_lower(True)
        if '1' in acqIdentifiers:
            self.set_common_upper(True)
        if '3' in acqIdentifiers:
            self.set_scanbody_lower(True)
        if '4' in acqIdentifiers:
            self.set_scanbody_upper(True)
        if '130' in acqIdentifiers:
            self.set_emergenceProfile_lower(True)
        if '131' in acqIdentifiers:
            self.set_emergenceProfile_upper(True)
        if '6' in acqIdentifiers:
            self.set_preparation_lower(True)
        if '7' in acqIdentifiers:
            self.set_preparation_upper(True)
        if '8' in acqIdentifiers:
            self.set_edentulous_lower(True)
        if '9' in acqIdentifiers:
            self.set_edentulous_upper(True)
        if '140' in acqIdentifiers:
            self.set_denture_lower(True)
        if '141' in acqIdentifiers:
            self.set_denture_upper(True)
        if '200' in acqIdentifiers or '201' in acqIdentifiers or '202' in acqIdentifiers:
            self.set_extra(True)
        if 'shade' in acqIdentifiers:
            self.set_shade(True)
        self.set_file_name(zipFile)
        self.set_common_bite(acqIdentifiers)
        self.set_pass_30days(zipFile)
        self.set_RefList(acqIdentifiers)
        
    def set_file_name(self,file_name):
        self.__file_name=file_name
    def get_file_name(self):
        return self.__file_name
        
    def set_common_lower(self,flag):
        self.__common_lower=flag
    def get_common_lower(self):
        return self.__common_lower
    def set_common_upper(self,flag):
        self.__common_upper=flag
    def get_common_upper(self):
        return self.__common_upper
            
    def set_scanbody_lower(self,flag):
        self.__scanbody_lower=flag
    def get_scanbody_lower(self):
        return self.__scanbody_lower
    def set_scanbody_upper(self,flag):
        self.__scanbody_upper=flag
    def get_scanbody_upper(self):
        return self.__scanbody_upper
    
    def set_emergenceProfile_lower(self,flag):
        self.__emergenceProfile_lower=flag
    def get_emergenceProfile_lower(self):
        return self.__emergenceProfile_lower
    def set_emergenceProfile_upper(self,flag):
        self.__emergenceProfile_upper=flag
    def get_emergenceProfile_upper(self):
        return self.__emergenceProfile_upper
    
    def set_preparation_lower(self,flag):
        self.__preparation_lower=flag
    def get_preparation_lower(self):
        return self.__preparation_lower
    def set_preparation_upper(self,flag):
        self.__preparation_upper=flag
    def get_preparation_upper(self):
        return self.__preparation_upper
    
    def set_edentulous_lower(self,flag):
        self.__edentulous_lower=flag
    def get_edentulous_lower(self):
        return self.__edentulous_lower
    def set_edentulous_upper(self,flag):
        self.__edentulous_upper=flag
    def get_edentulous_upper(self):
        return self.__edentulous_upper
    
    def set_denture_lower(self,flag):
        self.__denture_lower=flag
    def get_denture_lower(self):
        return self.__denture_lower
    def set_denture_upper(self,flag):
        self.__denture_upper=flag
    def get_denture_upper(self):
        return self.__denture_upper
    def set_extra(self,flag):
        self.__extra=flag
    def get_extra(self):
        return self.__extra
    
    def set_shade(self,flag):
        self.__shade=flag
    def get_shade(self):
        return self.__shade
    
    
    
    def containsDenture(self):
        return self.get_denture_upper() or self.get_denture_lower() or self.get_edentulous_lower() or self.get_edentulous_upper()
    
    def containsPreparation(self):
        return self.get_preparation_lower() or self.get_preparation_upper()
    
    def containsImplant(self):
        return self.get_scanbody_lower() or self.get_scanbody_upper() or self.get_emergenceProfile_lower() or self.get_emergenceProfile_upper()
    def containsOtherWorkflows(self):
        return self.containsDenture() or self.containsImplant() or self.containsPreparation()
    def isNotOnlyCommon(self):
        return self.containsDenture() or self.containsImplant() or self.containsPreparation() or self.get_extra()
    
    def set_pass_30days(self,fname):
        self.__pass_30days=False
        diffdays=DateTimeUtil.getDiffDays(fname)
        if diffdays>30:
            self.__pass_30days=True
        
    def get_pass_30days(self):
        return self.__pass_30days
    
    def get_scanRef(self):
        refStr=','.join(self.__scanRefList)
        test.log(str(refStr)) 
        return refStr
    
    def get_refineRef(self):
        refStr=','.join(self.__refineRefList)
        test.log(str(refStr)) 
        return refStr
    def set_common_bite(self,acqIdentifiers):
        self.__common_bite=False
        if 'bite' in acqIdentifiers:
            self.__common_bite=True
        else:
            bite_codelist=['11','12','13','14','15','16','100','101','102','103','104','105','106','107','108','109','110','111','112','113','114','115','116','117','118','119',
                       '120','121','122','123']
            for bite_code in bite_codelist:
                if bite_code in acqIdentifiers:
                    self.__common_bite=True
                    break
    def get_common_bite(self):
        return self.__common_bite
   
    def set_RefList(self,acqIdentifiers):
        #self.__scanRefList.append('data')
        if '0' in acqIdentifiers:
            if '1' in acqIdentifiers:
                if self.get_common_bite():
                    self.__scanRefList.append('fullarch')
                    self.__refineRefList.append('fullarch')
                else:
                    self.__scanRefList.append('fullarchwithoutbite')
                    self.__refineRefList.append('fullarchwithoutbite')
            else:
                self.__scanRefList.append('onlylower')
                self.__refineRefList.append('onlylower')
        else:
            if '1' in acqIdentifiers:
                self.__scanRefList.append('onlyupper')
                self.__refineRefList.append('onlyupper')
            #else:
                #self.__scanRefList.remove('data')
                #self.__scanRefList.append('nodata')
            #common doesn't contains data, maybe only edentulous
    
        if self.get_common_bite():
            self.__scanRefList.append('bite')
            self.__refineRefList.append('bite')
        else:
            if 'fullarchwithoutbite' in self.__scanRefList:
                pass
            else:
                self.__scanRefList.append('nobite')
                self.__refineRefList.append('nobite')
                
        if self.get_shade():
            self.__refineRefList.append('shade')
        else:
            self.__refineRefList.append('noshade')
            
        if self.isNotOnlyCommon():
            self.__refineRefList.append('notonlycommon')
        else:
            self.__refineRefList.append('onlycommon')
            
    def get_scanRefList(self):
        return self.__scanRefList
    
    def get_refineRefList(self):
        return self.__refineRefList
    
   


