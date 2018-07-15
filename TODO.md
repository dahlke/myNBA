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

# Find popular graphs and reproduce them for practice

# https://www.reddit.com/r/dataisbeautiful/comments/7ajydl/every_final_score_that_has_occurred_in_the_nba_oc/
# https://www.reddit.com/r/dataisbeautiful/comments/8wsjap/he_who_must_not_be_named_how_nba_fans_in/

