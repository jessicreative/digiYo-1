# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 13:32:09 2021

@author: jenny
"""
import math 

class MatchAnalyzer(object):
    
    def __init__(self, tupOfMoves , rarityLimit, varianceLimit, minMoves, maxMoves, pointDiff, moveType = ''): 
        
        #we can add whatever other criteria we see fit depending on the prompt
        #such as a required move type, minimal rarity, specific move archetype, etc.
        
        self.moves_tup = tupOfMoves
        self.rarity_limit = rarityLimit
        self.variance_limit = varianceLimit
        self.minMoves_int = minMoves
        self.maxMoves_int = maxMoves
        self.pointDiff_int = pointDiff
        
        
    def getVariance(self):
        '''X is space, Y is funk'''
        moves = self.moves_tup
        
        listOfCoordinates = []
        
        for move in moves:
            
            listOfCoordinates.append((move.getSpace(), move.getFunk()))
            
        x = 0
        y = 0
        #find mean            
        for tup in listOfCoordinates:
            x += tup[0]
            y += tup[1]
        z = len(listOfCoordinates)
        mean = (x/z, y/z)
            
        #find variance
            #-sum the distances
        dist = 0
        for coordinate in listOfCoordinates:
            dist += math.sqrt((coordinate[0]-mean[0])**2 + (coordinate[1]-mean[1])**2)
     
        #-divide by length of list-1
        variance = dist/(z-1)
      
        return variance
      

    def isCohesive(self): #isCohesive
        
        if (self.getVariance() < self.variance_limit):
            return True
        else:
            return False
        
    
    def getAvgRarity(self):
        moves = self.moves_tup
        
        rareScore = 0
        
        #rarities = ['COMMON','UNCOMMON','RARE','VERY RARE','LEGENDARY']
        rarities = ['COMMON','UNCOMMON','RARE','LEGENDARY']
        #scores = [50, 150, 375, 650, 1000]
        scores = [50, 150, 375, 1000]
        
        i  = 0
        
        for move in moves:
            rarity = move.getRarity()
            
            for level in rarities:
                
                if rarity == level:
                    rareScore += scores[i]
                    break
                
                else:
                    i += 1
        
        avgRarity = rareScore/len(moves)
        
        return avgRarity
            
        
    def isRare(self): #isRare
        
        rareLimit = self.rarity_limit
        
        if self.getAvgRarity() > rareLimit:
            return True
        else:
            return False
        
    
    def getPoints(self):
        points = 0
        for move in self.moves_tup:
            points += move.getPoints()
            
        return points
    
    

    def isComplete(self):
    
        if len(self.moves_tup) >= self.minMoves_int and len(self.moves_tup) <= self.maxMoves_int :
            
            if self.getPoints() >= self.pointDiff_int:
                
                return True
            
        return False
    
    def getStars(self):
        
        stars = 0
        
        if self.isComplete():
            stars += 1
        else:
            return 0
        
        if self.isRare():
            stars+=1
        
        if self.isCohesive():
            stars += 1
        
        return stars
            
            
            
        
        
