# arbitrage.py
# This module is used to match games from Draftkings and Fanduel

class Arb:
    def __init__(self, bookA, bookB):
        self.bookA = bookA
        self.bookB = bookB
        self.matchupPairs = []
        self.partialPairs = []

    def pairMatchups(self):
        matchupPairs = []
        partialPairs = []

        for a in self.bookA.matchups:
            for b in self.bookB.matchups:
                if (a.teamA == b.teamA and a.teamB == b.teamB) or (a.teamA == b.teamB and a.teamB == b.teamA):
                    matchupPairs.append((a, b))
                # only one team matches
                elif (a.teamA == b.teamA) or (a.teamB == b.teamB) or (a.teamA == b.teamB) or (a.teamB == b.teamA):
                    partialPairs.append((a, b))

        self.matchupPairs = matchupPairs
        self.partialPairs = partialPairs

        # I f a partial match is found, confirm with user whether they are the same game
        if len(partialPairs) >= 1:
            print(str(len(partialPairs)), ' partial matchup(s) found:\n')
            for i in partialPairs:
                print('Matchup1: ')
                print(i[0].teamA, ' vs. ', i[0].teamB,'\n')
                print('Matchup2:')
                print(i[1].teamA, ' vs. ', i[1].teamB)
                print('Are these games the same?(y/n)')
                user_input = input()
                if user_input.upper() == 'Y':
                    self.matchupPairs.append(i)

