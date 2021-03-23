# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from matchup import Book, Matchup
from arbitrage import Arb


def convertOdds(odds):
    if int(odds) >= 0:
        return (int(odds) / 100) + 1
    else:
        return (100 / -int(odds)) + 1

def getWagerValue(matchupPair):

    if ((convertOdds(matchupPair[0].oddsA) > convertOdds(matchupPair[1].oddsA) and
            convertOdds(matchupPair[1].oddsB) > convertOdds(matchupPair[0].oddsB)) or
            (convertOdds(matchupPair[0].oddsB) > convertOdds(matchupPair[1].oddsB) and
                convertOdds(matchupPair[1].oddsA) > convertOdds(matchupPair[0].oddsA))):
        return 'True'
    else:
        return 'False'



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # create sportsbook objects

    # College Basketball
    fd_cbb = Book('Fanduel', 'College Basketball', 'https://sportsbook.fanduel.com/sports/navigation/11086.3/11087.3')
    dk_cbb = Book('Draftkings', 'College Basketball', 'https://sportsbook.draftkings.com/leagues/basketball/3230960?category=game-lines&subcategory=game')

    # NHL
    fd_nhl = Book('Fanduel', 'NHL', 'https://sportsbook.fanduel.com/sports/navigation/1550.1/10329.3')
    dk_nhl = Book('Draftkings', 'NHL', 'https://sportsbook.fanduel.com/sports/navigation/1550.1/10329.3')


    # get Matchups
    fd_nhl.getMatchups()
    dk_nhl.getMatchups()
    arb = Arb(fd_nhl, dk_nhl)
    arb.pairMatchups()

    for i in arb.matchupPairs:
        print(i[0].teamA, i[0].oddsA, i[0].teamB, i[0].oddsB, i[1].teamA, i[1].oddsA, i[1].teamB, i[1].oddsB)

