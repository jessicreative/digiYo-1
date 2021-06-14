# -*- coding: utf-8 -*-
"""
Spyder Editor
This is a temporary script file.
"""

import random

    
def createPack(packSize: int,LegendLimit: float, RareLimit: float,UncommonLimit):
    LEGEND_LIMIT = LegendLimit
    RARE_LIMIT = RareLimit
    UNCOMMON_LIMIT = UncommonLimit
    
    PACK_SIZE = packSize

    common = 0 
    uncommon = 0
    rare = 0
    legendary = 0

    for x in range (0,PACK_SIZE):
        x = random.random() *1000
        
        #'pack = []'''
    
        if (x > LEGEND_LIMIT):
            legendary += 1   #replace with pack.append(getLegendary())
        
        #elif (x > VRARE_LIMIT):
        #    very_rare += 1   #replace with pack.append(getVRare())'''
        
        elif (x > RARE_LIMIT):
            rare += 1      #replace with pack.append(getRare())'''
        
        elif (x > UNCOMMON_LIMIT):
            uncommon += 1  #replace with pack.append(getUncommon()) '''
        
        else:
            common += 1    #replace with pack.append(getCommon())'''
        
        pack = [common, uncommon, rare, legendary]   #Cards will already be appended'''
        
    #print(pack)  #instead would be return pack'''
    return pack
    
    
def createBronze():
    createPack(5,997.5,950,600)  #returns the basic pack''
    return createPack(5,997.5,950,600)
    
def createSilver():
      #returns intermediate pack'''
    return createPack(5,975,850,500)
    
def createGold():
       #returns advanced pack'''
    return createPack(5, 950,800,450)

def createStarter():
    createPack(10, 1001,1001,1001)
    return
    
    
    
def getCommon():
    # Return card at random from common card library
    return
    
def getUncommon():
    # Return card at random from uncommon card library'''
    return
def getRare():
    # Return card at random from rare card library'''
    return
    
    
def getLegendary():
    # Return card at random from legendary card library'''
    return

def sampleBronze():
    pack = [0,0,0,0]
    for x in range (10001):
        p1 = createBronze()
        for i in range (0, 4):
            
            pack[i] = p1[i]+pack[i]
    pack = [pack[0]/10000.0, pack[1]/10000.0, pack[2]/10000.0, pack[3]/10000.0]
    return pack

def sampleSilver():
    pack = [0,0,0,0]
    for x in range (10001):
        p1 = createSilver()
        for i in range (0, 4):
            pack[i] = p1[i] + pack[i]
            
    pack = [pack[0]/10000.0, pack[1]/10000.0, pack[2]/10000.0, pack[3]/10000.0]
    return pack

def sampleGold():
    pack = [0,0,0,0]
    for x in range (10001):
        p1 = createGold()
        for i in range (0, 4):
            pack[i] = p1[i] + pack[i]
            
    pack = [pack[0]/10000.0, pack[1]/10000.0, pack[2]/10000.0, pack[3]/10000.0]
    return pack 
