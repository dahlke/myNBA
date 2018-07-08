TODO:
    - logging for each argument differentiated, and levels
    - Clean up the APIs and make them classes

IDEAS:
    - Top 10 rivalries / teams that have played each other the most times
    - Of them, who has the biggest point differential?
    - Over time how did those point differentials cross over as one team got better?
    - Teams with the biggest point differentials against each other
    - Teams with the biggest point differentials at home or away against each other
    - Players with the biggest point differentials against each other



Download Logic:

Get all teams (stats-teamYears):
    Download common team info (stats-teamInfoCommon)

Get all current players:
    Download common player info (stats-playerInfo)


Start in the modern NBA era (60s on), get all games for each day:
    Get game header and line score (stats.scoreboard)
    Get game box score (stats.boxscore)
    Get player performance
    Get coaches
    Get refs (stats-boxScoreSummary)

# Get the date
# Get every game played that day
# Get the results of each game
# Get the teams in each game
# Get the players in each game
# Get the box scores of each game

# Find popular graphs and reproduce them for practice
