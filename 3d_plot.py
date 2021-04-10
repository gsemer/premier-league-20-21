from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt 
import pandas as pd

# Plot the performance of a team depending on the field

df = pd.read_csv('datasets/train.csv')
input_team = input('Team: ') 

full_time = []
plays = []
matches = 0
for i in range(len(df.values)):
    if df['HomeTeam'].iloc[i] == input_team or df['AwayTeam'].iloc[i] == input_team:
        matches = matches + 1
        if df['HomeTeam'].iloc[i] == input_team:
            # win in home
            if df['FT'].iloc[i] == '1':
                full_time.append(2)
                plays.append(1)
            # draw in home
            if df['FT'].iloc[i] == 'X':
                full_time.append(1)
                plays.append(1)
            # lose in home
            if df['FT'].iloc[i] == '2':
                full_time.append(0)
                plays.append(1)
        if df['AwayTeam'].iloc[i] == input_team:
            # lose in away 
            if df['FT'].iloc[i] == '1':
                full_time.append(0)
                plays.append(0)
            # draw in away
            if df['FT'].iloc[i] == 'X':
                full_time.append(1)
                plays.append(0)
            # win in away
            if df['FT'].iloc[i] == '2':
                full_time.append(2)
                plays.append(0)

total_matches = []
for i in range(matches):
    total_matches.append(i+1)

# Initialize the 3-dimension schema
fig = plt.figure()
ax = Axes3D(fig)

# Show the name of the team at the top left corner
ax.text2D(0.05, 0.95, '{}'.format(input_team), transform=ax.transAxes)

# Make the plot in the schema
ax.scatter(full_time, total_matches, plays, marker='o', color='red')
ax.plot(full_time, total_matches, plays)

# X-axis:
    # 0 stands for lose
    # 1 stands for draw
    # 2 stands for win
# Y-axis: 
    # each coordinate represents the number of match
# Z-axis:
    # 0 stands for away game
    # 1 stands for home game
ax.set_xlabel('result')
ax.set_ylabel('match')
ax.set_zlabel('plays')

# Show the final 3-dimension schema
plt.show()

