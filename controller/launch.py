import datetime
import requests
import json

from data.database import Database
from utils.download import (
    download_all_players,
    download_player_game_log,
    download_common_player_info,
    download_all_teams,
    download_common_team_info,
)
from utils import download_fantasy
from utils.response import Response

# GLOBALS
SEASON = "2019-2020"
SEASON_TYPE = "Regular Season"
LEAGUE_ID = "00"

SCHEDULE_URL = "http://data.nba.com/data/5s/json/cms/noseason/scoreboard/__date__/games.json"
BOXSCORE_URL = "http://data.nba.com/data/5s/json/cms/noseason/game/__date__/__gameId__/boxscore.json"
FANTASY_URL = "https://www.numberfire.com/nba/daily-fantasy/daily-basketball-projections"


# handles the intialization of the database and the creation of necessary tables
def setup_database(ct):
    # intialize empty database
    db = Database()

    if (ct):
        # create 'Team' table
        db.create_team_table()

        # create 'Player' table
        db.create_player_table()

        # create 'GameStats' table
        db.create_gamestats_table()

        # create 'Fantasy' table
        db.create_fantasy_table()

    return db


# retrieves the team info
def retrieve_teams(db):
    # retrieve teams
    download_all_teams(db)

    # retrieve team common info
    # download_common_team_info(db)

    # retrieves the active players


def retrieve_active_players(db):
    # retrieve active players
    download_all_players(database=db)

    # retrieve common player info
    # download_common_player_info(db)

    # retrieves the game stats for each player


def retrieve_player_game_logs(db, COUNT=10):
    # retrieve player game logs
    download_player_game_log(SEASON, SEASON_TYPE, database=db)


# retrieves the fantasy data
def retrieve_fantasy_data(db):
    download_fantasy.run(FANTASY_URL, db)


# inserts the data to the postgres database
def insert_to_database(db):
    # insert team data
    # db.insert_team_data()

    # # insert player data
    # db.insert_player_data()

    # # insert game logs
    db.insert_game_logs()

    # insert fantasy data
    # db.insert_fantasy_data()


# retrieves the games that occured on a specific date
def retrieve_game_schedule():
    base = str(datetime.datetime.today().date()).replace("-", "")
    base = str(int(base) - 1)
    url = SCHEDULE_URL.replace("__date__", base)
    response = requests.get(url).text
    d = json.loads(response)
    l = []
    for i in d["sports_content"]["games"]["game"]:
        l.append(i["id"])
    return l


# retrieves the box scores for each matchup that occured on a specific date
def retrieve_boxScore(schedule, db):
    base = str(datetime.datetime.today().date()).replace("-", "")
    base = str(int(base) - 1)
    for game_id in schedule:
        # print(player, " -> ", _player)
        url = BOXSCORE_URL.replace(
            "__date__", base).replace("__gameId__", game_id)
        resp = requests.get(url).text
        r = Response(resp, database=db)
        r.extract_boxScore()


if __name__ == "__main__":
    db = setup_database(ct=False)

    # Downloads NBA player data and stats
    retrieve_teams(db)
    retrieve_active_players(db)
    # retrieve_player_game_logs(db)

    s = retrieve_game_schedule()
    retrieve_boxScore(s, db)

    # Downloads NBA player fantasy data
    # retrieve_fantasy_data(db)

    # Inserts data
    insert_to_database(db)

    db.close_connection()
