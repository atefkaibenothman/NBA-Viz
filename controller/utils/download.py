import requests
import json

from utils.response import Response

from nba_api.stats.static import players, teams
from nba_api.stats.endpoints import PlayerGameLog, commonplayerinfo, teaminfocommon

# URLS
SCHEDULE_URL = "http://data.nba.com/data/5s/json/cms/noseason/scoreboard/__date__/games.json"
BOXSCORE_URL = "http://data.nba.com/data/5s/json/cms/noseason/game/__date__/__gameId__/boxscore.json"
FANTASY_URL = "https://www.numberfire.com/nba/daily-fantasy/daily-basketball-projections"


# download all player basic info
# https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/static/players.md
def download_all_players(database=None):
    # call nba_api and get all the players
    all_players = players.get_players()

    # initialize response with the specified database
    r = Response(all_players, database=database)

    # extract the response for only active players
    r.extract_active_players()


# download all team basic info
# https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/static/teams.md
def download_all_teams(database=None):
    # call nba_api and get all the teams
    all_teams = teams.get_teams()

    # intilialize respoinse with the specified database
    r = Response(all_teams, database=database)

    # extract the team data
    r.extract_teams()


# download player game log
# https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/endpoints/playergamelog.md
def download_player_game_log(SEASON, SEASON_TYPE, database=None):
    for player_id in database:
        # call nba_api and get player game info
        pgl = PlayerGameLog(player_id).get_normalized_dict()

        # initialize response with the specified database
        r = Response(pgl, database=database)

        # extract the response for player game log
        r.extract_player_game_log(player_id)


# download common player info
# https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/endpoints/commonplayerinfo.md
def download_common_player_info(database=None):
    for player_id in database:
        # call nba_api and get common player info
        cpi = commonplayerinfo.CommonPlayerInfo(
            player_id).get_normalized_dict()

        # initialize response with the specified database
        r = Response(cpi, database=database)

        # extract the response for player common info
        r.extract_player_common_info(player_id)


# download common team info
# https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/endpoints/commonplayerinfo.md
def download_common_team_info(database=None):
    for team_id, _team in database.db_team.items():
        # call nba_api and get common team info
        tci = teaminfocommon.TeamInfoCommon(team_id).get_normalized_dict()

        # initialize response with the specified database
        r = Response(tci, database=database)

        # extract the response for team common info
        r.extract_team_common_info(team_id)


# download daily game schedule
# https://github.com/kashav/nba.js/blob/master/docs/api/DATA.md
def download_daily_schedule(db, date):
    url = SCHEDULE_URL.replace("__date__", date)
    response = requests.get(url).text
    d = json.loads(response)
    game_ids = []
    for i in d["sports_content"]["games"]["game"]:
        game_ids.append(i["id"])
    db.daily_schedule = game_ids


# download boxscore results for individual players
# https://github.com/kashav/nba.js/blob/master/docs/api/DATA.md
def download_daily_boxscore(db, date):
    for game_id in db.daily_schedule:
        url = BOXSCORE_URL.replace(
            "__date__", date).replace("__gameId__", game_id)
        resp = requests.get(url).text
        r = Response(resp, database=db)
        r.extract_boxScore()
