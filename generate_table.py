import pandas as pd
import sqlite3 as sql3
import os
from IPython.display import display


class PremierLeague:
    
    def __init__(self, data, teams):
        self.data = data 
        self.teams = teams
        self.calculateTotalPoints()
        self.calculateTotalGames() 
        self.calculateTotalWinsDrawsLoses()
        self.calculateTotalGoals()
        self.calculateTotalForm()
        self.sortDataFrame()
        self.fixDataFrameByDifferences()
        self.fixDataframeByGoals()
        self.createPremierLeagueTable()
        self.showPromotion()
        self.showRelegation()
        self.showMessageRules()
        self.showChampion()
        self.createCSV()
        self.createDatabase()
            
    def calculateTotalPoints(self):
        # Initialize a list that will keep the points of each team
        self.total_points = []
        for team in self.teams:
            # The concat of following dataframes is a dataframe of every game of each team
            home = self.data[self.data['HomeTeam'] == team]
            away = self.data[self.data['AwayTeam'] == team]
            # Find wins
            home_win = home[home['FT'] == '1']
            away_win = away[away['FT'] == '2']
            # Find draws
            home_draw = home[home['FT'] == 'X']
            away_draw = away[away['FT'] == 'X']
            # Find loses
            home_lose = home[home['FT'] == '2']
            away_lose = away[away['FT'] == '1']
            # Initialize the points of each team
            team_points = 0
            # Calculate total points of each team
            for win in range(len(home_win)):
                team_points += 3
            for win in range(len(away_win)):
                team_points += 3
            for draw in range(len(home_draw)):
                team_points += 1
            for draw in range(len(away_draw)):
                team_points += 1
            for lose in range(len(home_lose)):
                team_points += 0
            for lose in range(len(away_lose)):
                team_points += 0
            # Store the calculated points in the list
            self.total_points.append(team_points)
        
    def calculateTotalGames(self):
        # Initialize a list that will keep the number of games of each team
        self.total_games = []
        for team in self.teams:
            # The concat of following dataframes is a dataframe of every game of each team
            home = self.data[self.data['HomeTeam'] == team]
            away = self.data[self.data['AwayTeam'] == team]
            # Calculate total games of each team     
            team_games = len(home)+len(away)
            # Store the calculated games in the list 
            self.total_games.append(team_games)
            
    def calculateTotalWinsDrawsLoses(self):
        # Initialize a list tha t will keep the number of wins of each team
        # Initialize a list tha t will keep the number of draws of each team
        # Initialize a list tha t will keep the number of loses of each team
        self.total_wins = []
        self.total_draws = []
        self.total_loses = []
        for team in self.teams:
            # The concat of following dataframes is a dataframe of every game of each team
            home = self.data[self.data['HomeTeam'] == team]
            away = self.data[self.data['AwayTeam'] == team]
            # Find wins
            home_win = home[home['FT'] == '1']
            away_win = away[away['FT'] == '2']
            # Find draws
            home_draw = home[home['FT'] == 'X']
            away_draw = away[away['FT'] == 'X']
            # Find loses
            home_lose = home[home['FT'] == '2']
            away_lose = away[away['FT'] == '1']
            # Initialize number of wins
            # Initialize number of draws
            # Initialize number of loses
            wins = 0
            draws = 0
            loses = 0
            # Calculate total wins of each team
            # Calculate total draws of each team
            # Calculate total loses of each team
            for win in range(len(home_win)):
                wins += 1
            for win in range(len(away_win)):
                wins += 1
            for draw in range(len(home_draw)):
                draws += 1
            for draw in range(len(away_draw)):
                draws += 1
            for lose in range(len(home_lose)):
                loses += 1
            for lose in range(len(away_lose)):
                loses += 1
            # Store the calculated wins in the list
            # Store the calculated draws in the list
            # Store the calculated loses in the list
            self.total_wins.append(wins)
            self.total_draws.append(draws)
            self.total_loses.append(loses)
            
    def calculateTotalGoals(self):
        # Initialize a list tha t will keep the number of goals of each team
        self.total_goals = [] 
        for team in self.teams:
            # The concat of following dataframes is a dataframe of every game of each team
            home = self.data[self.data['HomeTeam'] == team]
            away = self.data[self.data['AwayTeam'] == team]
            # Initialize number of goals
            # Initialize number of conceded goals
            goals = 0
            goals_conceded = 0
            # Calculate goals 
            for goal in home['HG']:
                goals += goal 
            for goal in away['AG']:
                goals += goal
            # Calculate conceded goals
            for goal in home['AG']:
                goals_conceded += goal 
            for goal in away['HG']:
                goals_conceded += goal
            # Store the calculated goals and conceded goals
            table = '{}:{}'.format(str(goals), str(goals_conceded))
            self.total_goals.append(table)
                                    
    def calculateTotalForm(self):
        # Initialize a list that will keep the results of five last games of every team 
        self.total_forms = []
        for team in self.teams:
            temporary = []
            index = len(self.data)-1
            while index >= 0:
                if (self.data['HomeTeam'][index] == team) or (self.data['AwayTeam'][index] == team):
                    if self.data['HomeTeam'][index] == team:
                        if self.data['FT'][index] == '1':
                            temporary.append('W')
                        if self.data['FT'][index] == 'X':
                            temporary.append('D')
                        if self.data['FT'][index] == '2':
                            temporary.append('L')
                    if self.data['AwayTeam'][index] == team:
                        if self.data['FT'][index] == '1':
                            temporary.append('L')
                        if self.data['FT'][index] == 'X':
                            temporary.append('D')
                        if self.data['FT'][index] == '2':
                            temporary.append('W')
                if len(temporary) == 5:
                    temporary = ' '.join(temporary)
                    self.total_forms.append(temporary)
                    break
                index -= 1
            
    def sortDataFrame(self):
        # Sort the list which contains total points in descending order by using selection sort algorithm 
        # Make necessary changes on the other lists while algorithm is still in process
        for i in range(len(self.total_points)-1):
            maximum = i
            for j in range(i+1, len(self.total_points), 1):
                if self.total_points[maximum] < self.total_points[j]:
                    maximum = j
            self.teams[maximum], self.teams[i] = self.teams[i], self.teams[maximum]
            self.total_points[maximum], self.total_points[i] = self.total_points[i], self.total_points[maximum]
            self.total_games[maximum], self.total_games[i] = self.total_games[i], self.total_games[maximum]
            self.total_wins[maximum], self.total_wins[i] = self.total_wins[i], self.total_wins[maximum]
            self.total_draws[maximum], self.total_draws[i] = self.total_draws[i], self.total_draws[maximum]
            self.total_loses[maximum], self.total_loses[i] = self.total_loses[i], self.total_loses[maximum]
            self.total_goals[maximum], self.total_goals[i] = self.total_goals[i], self.total_goals[maximum]
            self.total_forms[maximum], self.total_forms[i] = self.total_forms[i], self.total_forms[maximum]
        
    def fixDataFrameByDifferences(self):
        # Initialize a list that will keep the score differences
        self.differences = []
        for table in self.total_goals:
            i = 0
            while table[i] != ':':
                i += 1
            # Calculate score difference of each team 
            difference = int(table[:i]) - int(table[i+1:])
            # Store calculated differences
            self.differences.append(difference) 
        # If any clubs finish with the same number of points, their position in the Premier League table is determined by goal difference
        i = 0
        while i <= len(self.total_points)-1:
            j = i+1
            if j == len(self.total_points):
                break
            if self.total_points[j] != self.total_points[i]:
                i += 1
            else:
                while self.total_points[j] == self.total_points[j-1]:
                    j += 1 
                    if j == len(self.total_points):
                        break
                while i<=j-2:
                    maximum = i
                    index = i+1
                    while index<=j-1:
                        if self.differences[maximum] < self.differences[index]:
                            maximum = index
                        index += 1
                    self.differences[maximum], self.differences[i] = self.differences[i], self.differences[maximum] 
                    self.teams[maximum], self.teams[i] = self.teams[i], self.teams[maximum]
                    self.total_points[maximum], self.total_points[i] = self.total_points[i],  self.total_points[maximum]
                    self.total_games[maximum], self.total_games[i] = self.total_games[i], self.total_games[maximum]
                    self.total_wins[maximum], self.total_wins[i] = self.total_wins[i], self.total_wins[maximum]
                    self.total_draws[maximum], self.total_draws[i] = self.total_draws[i], self.total_draws[maximum]
                    self.total_loses[maximum], self.total_loses[i] = self.total_loses[i], self.total_loses[maximum]
                    self.total_goals[maximum], self.total_goals[i] = self.total_goals[i], self.total_goals[maximum]
                    self.total_forms[maximum], self.total_forms[i] = self.total_forms[i], self.total_forms[maximum]
                    i += 1 
            i = j
            
    def fixDataframeByGoals(self):
        # Initialize a list that will keep the score differences
        goals = []
        for table in self.total_goals:
            i = 0
            while table[i] != ':':
                i += 1
            # Calculate goals of each team 
            goal = int(table[:i]) 
            # Store calculated goals
            goals.append(goal) 
        # If two or more teams share same points and same goal difference, then team with more goals takes the lead in scoreboard
        i = 0
        while i<=len(self.total_points)-1:
            j = i+1
            if j == len(self.total_points):
                break
            if self.total_points[j] != self.total_points[i]:
                i += 1
            else:
                while self.total_points[j] == self.total_points[j-1]:
                    j += 1
                while i <= j-1:
                    k = i+1
                    if self.differences[k] != self.differences[i]:
                        i += 1
                    else:
                        while self.differences[k] == self.differences[k-1]:
                            k += 1
                            if k == j:
                                break
                        while i <= k-2:
                            maximum = i
                            index = i+1
                            while index <= k-1:
                                if goals[maximum] <= goals[index]:
                                    maximum = index
                                index += 1
                            goals[maximum], goals[i] = goals[i], goals[maximum]
                            self.differences[maximum], self.differences[i] = self.differences[i], self.differences[maximum] 
                            self.teams[maximum], self.teams[i] = self.teams[i], self.teams[maximum]
                            self.total_points[maximum], self.total_points[i] = self.total_points[i],  self.total_points[maximum]
                            self.total_games[maximum], self.total_games[i] = self.total_games[i], self.total_games[maximum]
                            self.total_wins[maximum], self.total_wins[i] = self.total_wins[i], self.total_wins[maximum]
                            self.total_draws[maximum], self.total_draws[i] = self.total_draws[i], self.total_draws[maximum]
                            self.total_loses[maximum], self.total_loses[i] = self.total_loses[i], self.total_loses[maximum]
                            self.total_goals[maximum], self.total_goals[i] = self.total_goals[i], self.total_goals[maximum]
                            self.total_forms[maximum], self.total_forms[i] = self.total_forms[i], self.total_forms[maximum]
                            i += 1
            i = j
        
    def createPremierLeagueTable(self):
        label = []
        for i in range(len(self.teams)):
            label.append(str(i+1)+'.')
        dictionary = {'Team': self.teams, 'MP': self.total_games, 'W': self.total_wins, 'D': self.total_draws, 
                      'L': self.total_loses, 'Goals': self.total_goals, 'Pts': self.total_points, 'Forms': self.total_forms}
        self.df = pd.DataFrame(dictionary, index=label)
        display(self.df)
        
    def showPromotion(self):
        print('\n')
        print('Champions League : {}'.format(self.teams[0]))
        print('                   {}'.format(self.teams[1]))
        print('                   {}'.format(self.teams[2]))
        print('                   {}'.format(self.teams[3]))   
        print('\n')
        print('Europa League    : {}'.format(self.teams[4]))             
    
    def showRelegation(self):
        print('\n')
        print('Championship     : {}'.format(self.teams[-3]))
        print('                   {}'.format(self.teams[-2]))
        print('                   {}'.format(self.teams[-1]))
        
    def showMessageRules(self):
        print('\n')
        print('*If teams finish on equal points at the end of the season, score difference will be the tie-breaker.')
    
    def showChampion(self):
        matches_completed = 0
        for i in range(len(self.total_games)):
            if self.total_games[i] == 2*len(self.teams)-2:
                matches_completed += 1
        if matches_completed == len(self.total_games):    
            print('\n')
            print('{} is the champion of premier league in season 2020-2021.'.format(self.teams[0]))
        else:
            print('\n')
            print('{} is in the first position in premier league table so far.'.format(self.teams[0]))
    
    def createCSV(self):
        question = input('Do you want to create a file that will contain the table for english premier league? ')
        if (question == 'Y') or (question == 'y') or (question == 'Yes') or (question == 'yes'):
            try:
                self.df.to_csv('premier league table/premierLeagueTable.csv', header=True, index=0)
            except FileNotFoundError as e:
                print(e)
        else:
            return
        
    def createDatabase(self):
        question= input('Do you want to create a database for premier league matches? ')
        if (question == 'Y') or (question == 'y') or (question == 'Yes') or (question == 'yes'):
            try:
                # Connect
                connection = sql3.connect('database/premierLeagueDb.db')
                # Create db from csv
                self.data.to_sql('PremierLeague', connection, if_exists='replace', index=False)
            except FileNotFoundError as e:
                print(e)
        else:
            return 
            

if __name__ == '__main__':
   if os.path.isfile('datasets/train.csv'):
        dataframe = pd.read_csv('datasets/train.csv')
        teams = ['Liverpool', 'Manchester City', 'Manchester United', 'Everton', 'Tottenham Hotspur', 
                 'Leicester City', 'Fulham', 'Southampton', 'Wolves', 'Leeds United', 'Chelsea', 'Arsenal', 
                 'Burnley', 'Aston Villa', 'West Ham', 'West Bromwich Albion', 'Sheffield United', 
                 'Crystal Palace', 'Brighton and Hove Albion', 'Newcastle United']
        PremierLeague(dataframe, teams)
   else:
        print('Put folder datasets and file GenerateTable.py in the same folder')

