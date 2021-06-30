import DigiYoMove
import MatchMaker
import MatchAnalyzer
import DigiYoTrain
import DigiYoArticle
import DigiYoUser

    
firstDigiYo = DigiYoMove.DigiYoMove('HiC', 'Common', -1, -3, 'Leg Attack', 'Neutral', 'Top', 2,'A solid, fundamental leg attack. This head outside single leg variation isn\'t flashy, but it\'ll get the job done.')
secodDigiYo = DigiYoMove.DigiYoMove('Kick Out','Common', 0,0, 'Kick Out', 'Top', 'Neutral', -1)
thirdDigiYo = DigiYoMove.DigiYoMove('Single Leg', 'Common', 0, -3, 'Leg Attack', 'Neutral', 'Top',2)
fourthDigiYo = DigiYoMove.DigiYoMove('Half Nelson', 'Common', -1, 2, 'Turns', 'Top','Top-Nearfall', 4)

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



firstTraining = DigiYoTrain.DigiYoTrain('Sprawls','Common', 'Warm Up', False )
firstAttire = DigiYoArticle.DigiYoArticle('Singlet', 'Common', 'Clothing','Singlet' )

user = DigiYoUser.DigiYoUser('Andy')
for Digi in listOfDigiYo:
    user.addCards(Digi) 
    
user.addCards(firstTraining)
user.addCards(firstAttire)

user.addStars(analyzer)





    


