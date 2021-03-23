# matchup.py
# This module contains classes for collecting and organizing betting information from platforms

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from main import convertOdds


class Matchup:
    def __init__(self):
        self.teamA = ''
        self.teamB = ''
        self.oddsA = ''
        self.oddsB = ''
        self.type = ''
        self.category = ''

    def setTeamA(self, teamA):
        self.teamA = teamA

    def setTeamB(self, teamB):
        self.teamB = teamB

    def setOddsA(self, oddsA):
        self.oddsA = oddsA

    def setOddsB(self, oddsB):
        self.oddsB = oddsB

    def setCategory(self, category):
        self.category = category


class Book:
    def __init__(self, name, category, url):
        self.name = name
        self.url = url
        self.category = category
        self.html = BeautifulSoup(requests.get(url).content, 'lxml')
        self.matchups = ''

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
                        newMatchup.setOddsA(convertOdds(moneyline))
                        newMatchup.setCategory(self.category)
                        matchups.append(newMatchup)
                        # If matchupTeam = -1, the matchup already exists, and we just need to update it with Team B
                    else:
                        matchups[matchupInt].setTeamB(team)
                        matchups[matchupInt].setOddsB(convertOdds(moneyline))
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
                for price in event.find_all(attrs = {'class':'market money'}):
                    moneylines = price.find_all(attrs={'class':'selectionprice'})
                newMatchup.setTeamA(teams[0].text)
                newMatchup.setTeamB(teams[1].text)
                newMatchup.setOddsA(convertOdds(moneylines[0].text))
                newMatchup.setOddsB(convertOdds(moneylines[1].text))
                newMatchup.setCategory(self.category)
                matchups.append(newMatchup)

            self.matchups = matchups
