# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 12:27:11 2021

@author: jenny
"""
class DigiYoUser(object):
    
    def __init__(self, username = 'user'):
        self.username_string = username
        self.moveLibrary_DigiList = list()
        self.totalStars_int = 0
        
    
    
    def addStars(self, MatchAnalyzer):
        self.totalStars_int += MatchAnalyzer.getStars()
        return        
        
    def addCards(self, DigiYoMove):
        self.moveLibrary_DigiList.append(DigiYoMove)
        return
    
    def addCards(self, DigiYoTrain):
        self.moveLibrary_DigiList.append(DigiYoTrain)
        return
    
    def addCards(self, DigiYoArticle):
        self.moveLibrary_DigiList.append(DigiYoArticle)
        return
    
    def giveCards(self, DigiYoMove):
        i = self.moveLibrary_DigiList.index(DigiYoMove)
        return self.moveLibrary_DigiList.pop(i)#index of card user is giving
    
    def giveCards(self, DigiYoTrain):
        i = self.moveLibrary_DigiList.index(DigiYoTrain)
        return self.moveLibrary_DigiList.pop(i)#index of card user is giving
    
    def giveCards(self, DigiYoArticle):
        i = self.moveLibrary_DigiList.index(DigiYoArticle)
        return self.moveLibrary_DigiList.pop(i)#index of card user is giving
    
    def getUsername(self):
        return self.username_string
    
    def getStars(self):
        return self.totalStars_int
    
    def getCards(self):
        return self.moveLibrary_DigiList
    
    