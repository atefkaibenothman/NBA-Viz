import datetime

from data.database import Database
from utils import download_fantasy
from data.sql_cmds import (
    create_player_table,
    create_team_table,
    create_fantasy_table,
    create_gamestats_table,
    insert_player_table,
    insert_team_table,
    insert_fantasy_table,
    insert_gamestats_table
)
from utils.download import (
    download_all_players,
    download_player_game_log,
    download_common_player_info,
    download_all_teams,
    download_common_team_info,
    download_daily_schedule,
    download_daily_boxscore
)

# GLOBALS
SEASON = "2019-2020"
SEASON_TYPE = "Regular Season"
LEAGUE_ID = "00"
DATE_TODAY = str(
    int(str(datetime.datetime.today().date()).replace("-", "")) - 1)


def download_teams(db, extra=False):
    '''downloads team data from api (does not make a request to stats.nba.com)'''
    download_all_teams(db)  # download team data from api
    if (extra):
        download_common_team_info(db)  # download team details from api


def download_players(db, extra=False):
    '''downloads player data from api (does not make a requst to stats.nba.com)'''
    download_all_players(db)  # download player data from api
    if (extra):
        download_common_player_info(db)  # download player details from api


def download_today_schedule(db, date):
    '''downloads the schedule for the specified date from data.nba.com'''
    download_daily_schedule(db, date)  # downloads today's schedule


def download_today_boxscore(db, date):
    '''downloads the boxscore for individual players on a specified date from data.nba.com'''
    download_daily_boxscore(db, date)   # downloads


def download_fantasy_data(db):
    '''downloads player fantasy scores'''
    # download_fantasy.run(FANTASY_URL, db)
    pass


if __name__ == "__main__":
    db = Database()  # initialize database

    download_teams(db, extra=False)  # download all teams
    download_players(db, extra=False)  # download all players

    RESTART = str(input("do you want to restart? (y/n): "))
    UPDATE = str(input("do you want to update? (y/n): "))

    if (RESTART == "y"):
        print("restarting...")
        db.create_table("team", create_team_table)  # create table in database
        db.create_table("player", create_player_table)
        db.create_table("gamestats", create_gamestats_table)
        db.create_table("fantasy", create_fantasy_table)

        db.insert_into_table_team(insert_team_table)
        db.insert_into_table_player(insert_player_table)

    if (UPDATE == "y"):
        print("updating...")
        download_today_schedule(db, DATE_TODAY)
        download_today_boxscore(db, DATE_TODAY)
        # download_fantasy_data(db)

        db.insert_into_table_gamestats(insert_gamestats_table)
        # db.insert_into_table("fantasy", insert_fantasy_table)

    db.close_connection()
