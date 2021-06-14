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
        
    print(pack)  #instead would be return pack'''
    return
    
    
def createBronze():
    createPack(5,997.5,950,600)  #returns the basic pack''
    return
    
def createSilver():
    createPack(5,992.5,900,500)  #returns intermediate pack'''
    return
    
def createGold():
    createPack(5, 985,850,450)   #returns advanced pack'''
    return

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
    
    
