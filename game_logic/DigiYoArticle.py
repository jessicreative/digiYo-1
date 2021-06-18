# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 14:39:12 2021

@author: jenny
"""
class DigiYoArticle(object):
    '''interactive NFT Class'''
    
    
    
    def __init__(self,articleName,rarity,attireType, clothingSubtype = '', description:str = '',cardID=0):
        self.article_name_str = articleName
        self.article_rarity = rarity #is it a thing?
        self.move_ID_int = cardID
        self.attireType_str = attireType
        self.clothingSub_str = clothingSubtype
        self.description_str = description
        
        
    
    def getRarity(self):                          
        
        
        return self.article_rarity 
        
        
    
    def getRarityColor(self):
        
        rarity = self.getRarity()
        
        ListOfRarities = ['COMMON','UNCOMMON','RARE','LEGENDARY']
        ListOfColors = ['Gray', 'Bronze', 'Silver', 'Gold']
        c = 0
        
        for element in ListOfRarities:
            if (rarity == element):
                return ListOfColors[c]
            else:
                c += 1
                
        return 'Invalid Rarity'
        
    def getType(self):
        #Clothing or accessory
        
        return self.attireType_str
    
    def hasSubType(self):
        if (self.clothingSub_str == ''):
            return False
        else:
            return True
        
    def getSubType(self):
        if self.hasSubType():
            return self.clothingSub_str
        else:
            return 'No Subtype'
    
    def getTypeColor(self):
        trainType = self.getType()
        ListOfTypes = ['Clothing', 'Accessory']
        ListOfColors = ['Blue', 'Yellow']
        c = 0
        
        for element in ListOfTypes:
            if (trainType == element):
                return ListOfColors[c]
            else:
                c += 1
                
        return 'Invalid Type'
        
    
    
    def getName(self):
        return self.article_name_str
    
    
    def getDescription(self):
        return self.description_str