import requests
from bs4 import BeautifulSoup

class Matchup:
    def __init__(self):
        self.teamA = ''
        self.teamB = ''

    def setTeamA(self, teamA):
        self.teamA = teamA

    def setTeamB(self, teamB):
        self.teamB = teamB

    def getTeamA(self):
        return self.teamA

    def getTeamB(self):
        return self.teamB

class Book:
    def __init__(self, url):
        self.url = url
        self.html = BeautifulSoup(requests.get(url).content, 'lxml')
        self.matchups = ''


    def getMatchups(self):
        matchups = []

        # This will be used to assign teams as either A or B. After the loop completes the team variable will be flipped
        matchupTeam = 1
        matchupInt = 0

        for books in self.html.find_all(attrs={'class': 'sportsbook-table__body'}):
            for row in books.find_all(attrs={'class': 'event-cell__team-info'}):
                team = (row.find(attrs={'class': 'event-cell__name'}).text)
                if matchupTeam == 1:
                    newMatchup = Matchup()
                    newMatchup.setTeamA(team)
                    matchups.append(newMatchup)
                    ## If matchupTeam = -1, the matchup already exists, and we just need to update it with Team B
                else:
                    matchups[matchupInt].setTeamB(team)
                    matchupInt += 1
                matchupTeam *= -1

        self.matchups = matchups



