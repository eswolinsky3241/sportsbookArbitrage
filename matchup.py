import requests
from bs4 import BeautifulSoup
import selenium
from selenium import webdriver


class Matchup:
    def __init__(self):
        self.teamA = ''
        self.teamB = ''
        self.oddsA = ''
        self.oddsB = ''
        self.type = ''

    def setTeamA(self, teamA):
        self.teamA = teamA

    def setTeamB(self, teamB):
        self.teamB = teamB

    def setOddsA(self, oddsA):
        self.oddsA = oddsA

    def setOddsB(self, oddsB):
        self.oddsB = oddsB


class Book:
    def __init__(self, url):
        self.url = url
        self.html = BeautifulSoup(requests.get(url).content, 'lxml')
        matchups = ''

    def getMatchups(self):

        if self.url.startswith('https://sportsbook.draftkings'):

            matchups = []

            # This will be used to assign teams as either A or B.
            # After the loop completes the team variable will be flipped

            matchupTeam = 1
            matchupInt = 0

            for table in self.html.find_all('tbody'):
                for row in table.find_all('tr'):
                    column = row.find_all(attrs={'class':"sportsbook-table__column-row"})
                    team = row.find(attrs={'class': 'event-cell__name'}).text
                    moneylineHTML = column[3].find(attrs={'class':'sportsbook-odds american default-color'})
                    if moneylineHTML is None:
                        moneyline = ''
                    else:
                        moneyline = moneylineHTML.text
                    if matchupTeam == 1:
                        newMatchup = Matchup()
                        newMatchup.setTeamA(team)
                        newMatchup.setOddsA(moneyline)
                        matchups.append(newMatchup)
                        # If matchupTeam = -1, the matchup already exists, and we just need to update it with Team B
                    else:
                        matchups[matchupInt].setTeamB(team)
                        matchups[matchupInt].setOddsB(moneyline)
                        matchupInt += 1
                    matchupTeam *= -1

            self.matchups = matchups

        elif self.url.startswith('https://sportsbook.fanduel'):
            matchups = []
            driver = webdriver.Chrome('/home/ethan/PycharmProjects/sportsbookArbitrage/chromedriver')
            driver.get(self.url)
            self.html = BeautifulSoup(driver.page_source,'html.parser')

            for event in self.html.find_all(attrs={'class': 'event'}):
                newMatchup = Matchup()
                teams = event.find_all(attrs={'class': 'name'})
                newMatchup.setTeamA(teams[0].text)
                newMatchup.setTeamB(teams[1].text)
                matchups.append(newMatchup)

            self.matchups = matchups
