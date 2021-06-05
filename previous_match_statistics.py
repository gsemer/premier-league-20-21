import pandas as pd
from IPython.display import display

data = pd.read_csv('datasets/train.csv')
test = pd.read_csv('datasets/test.csv')

input_1 = input('Home team: ')
input_2 = input('Away team: ')

home_team = data[data['HomeTeam'] == input_1]
away_team = data[data['AwayTeam'] == input_2]

home_list = []
away_list = []
for element in home_team['Id']:
    home_list.append(element)
for element in away_team['Id']:
    away_list.append(element)
home = home_team['HomeTeam'][home_list[0]-1]
away = away_team['AwayTeam'][away_list[0]-1]

display(home_team)
display(away_team)

home_total_games = len(home_team)
away_total_games = len(away_team)

print('\n')
display('FULL TIME')

home_win = home_team[home_team['FT'] == '1']
home_win_games = len(home_win)
home_draw = home_team[home_team['FT'] == 'X']
home_draw_games = len(home_draw)
home_lose = home_team[home_team['FT'] == '2']
home_lose_games = len(home_lose)
home_win_mean = round(home_win_games/home_total_games, 3) 
home_draw_mean = round(home_draw_games/home_total_games, 3)
home_lose_mean = round(home_lose_games/home_total_games, 3)
display("The average of {} wins (FT) is equal to {}".format(home, home_win_mean))
display("The average of {}'s draws (FT) is equal to {}".format(home, home_draw_mean))
display("The average of {} loses (FT) is equal to {}".format(home, home_lose_mean))

away_lose = away_team[away_team['FT'] == '1']
away_lose_games = len(away_lose)
away_draw = away_team[away_team['FT'] == 'X']
away_draw_games = len(away_draw)
away_win = away_team[away_team['FT'] == '2']
away_win_games = len(away_win)
away_win_mean = round(away_win_games/away_total_games, 3) 
away_draw_mean = round(away_draw_games/away_total_games, 3)
away_lose_mean = round(away_lose_games/away_total_games, 3)
display("The average of {} wins (FT) is equal to {}".format(away, away_win_mean))
display("The average of {}'s draws (FT) is equal to {}".format(away, away_draw_mean))
display("The average of {} loses (FT) is equal to {}".format(away, away_lose_mean))

print('\n')
display('HALF TIME')

home_win_half = home_team[home_team['HT'] == '1']
home_win_games_half = len(home_win_half)
home_draw_half = home_team[home_team['HT'] == 'X']
home_draw_games_half = len(home_draw_half)
home_lose_half = home_team[home_team['HT'] == '2']
home_lose_games_half = len(home_lose_half)
home_win_mean_half = round(home_win_games_half/home_total_games, 3) 
home_draw_mean_half = round(home_draw_games_half/home_total_games, 3)
home_lose_mean_half = round(home_lose_games_half/home_total_games, 3)
display("The average of {} wins (HT) is equal to {}".format(home, home_win_mean_half))
display("The average of {}'s draws (HT) is equal to {}".format(home, home_draw_mean_half))
display("The average of {} loses (HT) is equal to {}".format(home, home_lose_mean_half))

away_lose_half = away_team[away_team['HT'] == '1']
away_lose_games_half = len(away_lose_half)
away_draw_half = away_team[away_team['HT'] == 'X']
away_draw_games_half = len(away_draw_half)
away_win_half = away_team[away_team['HT'] == '2']
away_win_games_half = len(away_win_half)
away_win_mean_half = round(away_win_games_half/away_total_games, 3) 
away_draw_mean_half = round(away_draw_games_half/away_total_games, 3)
away_lose_mean_half = round(away_lose_games_half/away_total_games, 3)
display("The average of {} wins (HT) is equal to {}".format(away, away_win_mean_half))
display("The average of {}'s draws (HT) is equal to {}".format(away, away_draw_mean_half))
display("The average of {} loses (HT) is equal to {}".format(away, away_lose_mean_half))

print('\n')
display('TOTAL GOALS')

home_team_0_1 = home_team[home_team['TG'] == '0-1']
home_team_number_0_1 = len(home_team_0_1)
home_team_2_3 = home_team[home_team['TG'] == '2-3']
home_team_number_2_3 = len(home_team_2_3)
home_team_4_6 = home_team[home_team['TG'] == '4-6']
home_team_number_4_6 = len(home_team_4_6)
home_team_7 = home_team[home_team['TG'] == '7+']
home_team_number_7 = len(home_team_7)
home_0_1_mean = round(home_team_number_0_1/home_total_games, 3) 
home_2_3_mean = round(home_team_number_2_3/home_total_games, 3)
home_4_6_mean = round(home_team_number_4_6/home_total_games, 3)
home_7_mean = round(home_team_number_7/home_total_games, 3)
display('{} total goals 0-1: {}'.format(home, home_0_1_mean))
display('{} total goals 2-3: {}'.format(home, home_2_3_mean))
display('{} total goals 4-6: {}'.format(home, home_4_6_mean))
display('{} total goals 7+ : {}'.format(home, home_7_mean))

away_team_0_1 = away_team[away_team['TG'] == '0-1']
away_team_number_0_1 = len(away_team_0_1)
away_team_2_3 = away_team[away_team['TG'] == '2-3']
away_team_number_2_3 = len(away_team_2_3)
away_team_4_6 = away_team[away_team['TG'] == '4-6']
away_team_number_4_6 = len(away_team_4_6)
away_team_7 = away_team[away_team['TG'] == '7+']
away_team_number_7 = len(away_team_7)
away_0_1_mean = round(away_team_number_0_1/away_total_games, 3) 
away_2_3_mean = round(away_team_number_2_3/away_total_games, 3)
away_4_6_mean = round(away_team_number_4_6/away_total_games, 3)
away_7_mean = round(away_team_number_7/away_total_games, 3)
display('{} total goals 0-1: {}'.format(away, away_0_1_mean))
display('{} total goals 2-3: {}'.format(away, away_2_3_mean))
display('{} total goals 4-6: {}'.format(away, away_4_6_mean))
display('{} total goals 7+ : {}'.format(away, away_7_mean))

