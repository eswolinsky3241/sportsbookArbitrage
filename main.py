# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from matchup import Book, Matchup
from arbitrage import Arb


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # create sportsbook objects
    fd = Book('https://sportsbook.fanduel.com/sports/navigation/11086.3/11087.3')
    dk = Book('https://sportsbook.draftkings.com/leagues/basketball/3230960?category=game-lines&subcategory=game')
    # get Matchups
    fd.getMatchups()
    dk.getMatchups()
    arb = Arb(fd, dk)
    arb.pairMatchups()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
