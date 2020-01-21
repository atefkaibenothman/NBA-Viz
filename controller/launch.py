from data.database import Database
from utils.download import (
    download_all_players,
    download_player_game_log,
    download_common_player_info,
    download_all_teams,
    download_common_team_info,
)

# GLOBALS
SEASON = "2019-2020"
SEASON_TYPE = "Regular Season"
LEAGUE_ID = "00"


# handles the intialization of the database and the creation of necessary tables
def setup_database():
    # intialize empty database
    db = Database()

    # create 'Team' table
    db.create_team_table()

    # create 'Player' table
    # db.create_player_table()

    # create 'GameStats' table
    # db.create_gamestats_table()

    return db


# retrieves the team info
def retrieve_teams(db):
    # retrieve teams
    download_all_teams(db)

    # retrieve team common info
    download_common_team_info(db)

    # insert team data in postgres database
    db.insert_team_data()


# retrieves the active players and inserts them into the database
def retrieve_active_players(db):
    # retrieve active players
    download_all_players(database=db)

    # retrieve common player info
    download_common_player_info(db)

    # insert player data into postgres database
    db.insert_player_data()


# retrieves the game stats for each player
def retrieve_player_game_logs(db, COUNT=10):
    # retrieve player game logs
    download_player_game_log(SEASON, SEASON_TYPE, database=db)

    # insert game logs into postgres database
    db.insert_game_logs()


if __name__ == "__main__":
    db = setup_database()
    retrieve_teams(db)
    # retrieve_active_players(db)
    # retrieve_player_game_logs(db)
    db.close_connection()
