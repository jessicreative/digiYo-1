# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 11:23:28 2021

@author: jenny
"""

class DigiYoTrain(object):
    '''interactive NFT Class'''
    
    
    
    def __init__(self,moveName,rarity,trainingType, partner: bool , description:str = '',cardID=0):
        self.move_name_str = moveName
        self.move_rarity = rarity
        self.move_ID_int = cardID
        self.trainingType_str = trainingType
        self.partner_bool = partner
        self.description_str = description
        
        
    
    def getRarity(self):                          
        
        
        return self.move_rarity 
        
        
    
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
        #Warm Up, Strength, or Cardio
        
        return self.trainingType_str
    
    def getTypeColor(self):
        trainType = self.getType()
        ListOfTypes = ['Warm Up', 'Strength', 'Cardio']
        ListOfColors = ['Red - Orange', 'Black', 'White']
        c = 0
        
        for element in ListOfTypes:
            if (trainType == element):
                return ListOfColors[c]
            else:
                c += 1
                
        return 'Invalid Type'
        
    
    
    def getName(self):
        return self.move_name_str
    
    def needPartner(self):
        return self.partner_bool
    
    def getDescription(self):
        return self.description_str