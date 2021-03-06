# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 12:07:36 2021

@author: jenny
"""
import DigiYoMove

class MatchMaker(object):
    

    
    def __init__(self, reward = 0, reqStart = 'null', reqEnd = 'null'):
        self.start_str = reqStart
        self.end_str = reqEnd
        self.listOfMoves = [] #would it be better to make a linked list? Might help for addMove/delMove 
        self.reward_int = reward 
        

        
    def addMove(self, move: DigiYoMove):
        if len(self.listOfMoves) == 0:
            if (self.start_str == 'null'):
                self.listOfMoves.append(move)
            elif (self.start_str == self.listOfMoves[0].getStart()):
                self.listOfMoves.append(move)
            
            else:
                print("Move must start in the correct position to be added 1")
        
        else:
            
            if (self.listOfMoves[-1].getEnd() == move.getStart() ):
                
                self.listOfMoves.append(move)
                
            else:
                print("Move must start in the correct position to be added 2")
        #self.listOfMoves.append(move)
        
    def delMove(self, moveIndex: int):
        
        self.listOfMoves = self.listOfMoves[:moveIndex]
        
        #delete the moves at and after the given index
        
    def getEnd(self):
        
        return self.listOfMoves[-1].getEnd()
    
    def getStart(self):
        
        return self.listOfMoves[0].getStart()
        
        
    def getMoves(self):
        
        tupOfMoves = tuple(self.listOfMoves)
        return tupOfMoves
    
    def getReward(self):
        return self.reward_int
    
    
    
