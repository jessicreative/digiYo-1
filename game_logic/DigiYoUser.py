class DigiYoUser(object):
    
    def __init__(self, username = 'user'):
        self.username_string = username
        self.moveLibrary_DigiList = list()
        self.totalStars_int = 0
        self.balance_int = 0  #refers to in-game currency
        
        
   # def completedMatch(self, MatchAnalyzer, MatchMaker):
    #    self.addBalance(MatchMaker.getReward())
     #   self.addStars(MatchAnalyzer.getStars())
        
      #  return
    
    
    
    #adjusment methods
    def addBalance(self, credit):
        self.balance_int += credit
        return
    
    def decBalance(self, debt):
        self.balance_int -= debt
        return
    
    def addStars(self, stars):
        self.totalStars_int += stars
        return        
        
    
    
     #add functions for all types of DigiYo Cards when purchasing packs, and cards
     #from the market and auctionhouse
    def addCards(self, DigiYoMove):
        self.moveLibrary_DigiList.append(DigiYoMove)
        return
    
    def addCards(self, DigiYoTrain):
        self.moveLibrary_DigiList.append(DigiYoTrain)
        return
    
    def addCards(self, DigiYoArticle):
        self.moveLibrary_DigiList.append(DigiYoArticle)
        return
    
    
    
    #pop functions for all types of DigiYo Cards when selling packs, whether in the 
    #auction house or back to us
    def giveCards(self, DigiYoMove):
        i = self.moveLibrary_DigiList.index(DigiYoMove)
        return self.moveLibrary_DigiList.pop(i)#index of card user is giving
    
    def giveCards(self, DigiYoTrain):
        i = self.moveLibrary_DigiList.index(DigiYoTrain)
        return self.moveLibrary_DigiList.pop(i)#index of card user is giving
    
    def giveCards(self, DigiYoArticle):
        i = self.moveLibrary_DigiList.index(DigiYoArticle)
        return self.moveLibrary_DigiList.pop(i)#index of card user is giving
    
    
    #get functions to retrieve variavbles
    def getUsername(self):
        return self.username_string
    
    def getStars(self):
        return self.totalStars_int
    
    def getCards(self):
        return self.moveLibrary_DigiList
    
    def getBalance(self):
        return self.balance_int
    
    
