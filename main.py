# sportsbookArbitrage
# Compare sports matchups in Draftkings and Fanduel to find guaranteed profit opportunities.

from matchup import Book, Matchup
from arbitrage import Arb

if __name__ == '__main__':
    # create sportsbook objects
    fd = Book('https://sportsbook.fanduel.com/sports/navigation/11086.3/11087.3')
    dk = Book('https://sportsbook.draftkings.com/leagues/basketball/3230960?category=game-lines&subcategory=game')
    # get Matchups
    fd.getMatchups()
    dk.getMatchups()
    # find matchup pairs
    arb = Arb(fd, dk)
    arb.pairMatchups()

