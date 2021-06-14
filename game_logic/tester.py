# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import DigiYo
import MatchMaker
import MatchAnalyzer
    
firstDigiYo = DigiYo.DigiYo('HiC', 6000, -1, -3, 'Leg Attack', 'Neutral', 'Top', 2)
secodDigiYo = DigiYo.DigiYo('Kick Out',6000, 0,0, 'Kick Out', 'Top', 'Neutral', -1)
thirdDigiYo = DigiYo.DigiYo('Single Leg', 6000, 0, -3, 'Leg Attack', 'Neutral', 'Top',2)
fourthDigiYo = DigiYo.DigiYo('Half Nelson', 6000, -1, 2, 'Turns', 'Top','Top-Nearfall', 4)

listOfDigiYo = [firstDigiYo, secodDigiYo, thirdDigiYo, fourthDigiYo]

maker = MatchMaker.MatchMaker()

for Digi in listOfDigiYo:
    maker.addMove(Digi)

analyzer = MatchAnalyzer.MatchAnalyzer(maker.getMoves(), 5000, 5, 1, 5, 6)

#print('Variance = 'analyzer.getVariance())

#analyzer.isCohesive()
#analyzer.isRare()
#analyzer.isComplete()

print('This match earned '+ str(analyzer.getStars()) + ' stars')




    


