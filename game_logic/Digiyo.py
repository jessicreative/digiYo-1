# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 16:31:14 2021

@author: jenny
"""

class DigiYo(object):
    '''interactive NFT Class'''
    
    #Include a start and end state for each move?
    #printRun = number of move in circulation
    #can switch printRun with proportionInEcosystem or something of the like
    
    
    
    def __init__(self,moveName,printRun,space,funk, moveType, startState, endState, points,cardID=0):
        self.move_name_str = moveName
        self.move_printRun_int = printRun
        self.move_funk_float = funk
        self.move_space_float = space
        self.move_ID_int = cardID
        self.moveType_str = moveType
        self.startState_str = startState
        self.endState_str = endState
        self.points_int = points
        
        
    
    def getRarity(self): #Disregard this function, rarity will just be a string given when we instantiate a DigiYo object
                            
        
        run = self.move_printRun_int
        
        if (run <= 25):                     
            return 'LEGENDARY'
        #elif (run <= 500):
        #    return 'VERY RARE'
        elif (run <= 500):
            return 'RARE'
        elif (run <= 4000):
            return 'UNCOMMON'
        else:
            return 'COMMON'               
        
        
        
    
    def getRarityColor(self):
        
        rarity = self.getRarity()
        
        ListOfRarities = ['COMMON','UNCOMMON','RARE','VERY RARE','LEGENDARY']
        ListOfColors = ['Gray', 'Black', 'Bronze', 'Silver', 'Gold']
        c = 0
        
        for element in ListOfRarities:
            if (rarity == element):
                return ListOfColors[c]
            else:
                c += 1
                
        return 'Invalid Rarity'
        
        
    
    
    def getArchetypeColor(self):
        archetype = self.getArchetype()
        
        ListOfArchetypes = ['Scrambler','Wild Card','Upper Body','Bruiser','Fundamentalist',\
                            'Quick and Fundamental','Quick and Outside', 'Slick']
        ListOfColors = ['Maroon','Red','Orange','Yellow','Green','Sky BLue','BLue','Purple']
        c = 0
        
        for element in ListOfArchetypes:
            if (archetype == element):
                return ListOfColors[c]
            else:
                c += 1
        return 'Invalid Archetype'
            
           
    
    def getArchetype(self):
        
        y = self.move_funk_float
        x = self.move_space_float
        
        if ((x == 0) and (y == 0)):
            return 'Neutral'
        
        elif ((x >= 0) and (y >= 0)):
            if (y >= (2*x)):
                return 'Scrambler'
            elif (y >= (.5*x)):
                return 'Wildcard'
            else:
                return 'Upper Body'
            
        elif ((x >= 0) and (y <= 0)):
            if (y <= (-2*x)):
                return 'Fundamentalist'
            elif (y <= (-.5*x)):
                return 'Bruiser'
            else:
                return 'Upper Body'
        
        elif ((x <= 0) and (y >= 0)):
            if (y >= (-2*x)):
                return 'Scrambler'
            elif (y >= (-.5*x)):
                return 'Slick'
            else:
                return 'Quick and Explosive'
            
        else: #(x<= 0) and (y<= 0)
            if (y >= (.5*x)):
                return 'Quick and Explosive'
            elif (y >= (2*x)):
                return 'Quick and Fundamental'
            else:
                return 'Fundamentalist'
            
    
    def getSpace(self):
        
        return self.move_space_float
    
    def getFunk(self):
        
        return self.move_funk_float
    
    def getType(self):
        
        return self.moveType_str
    
    def getStart(self):
        
        return self.startState_str
    
    def getEnd(self):
        
        return self.endState_str
    
    def getPoints(self):
        return self.points_int
    
    def getName(self):
        return self.move_name_str
    
            
        

    
    
    
