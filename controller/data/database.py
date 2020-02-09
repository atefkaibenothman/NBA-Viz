import psycopg2

from data.player import Player
from data.team import Team


class Database:
    # initializes an empty dictionary to start
    def __init__(self):
        self.db_player = dict()
        self.db_team = dict()
        self.con = self.connect_to_db()
        self.curr = self.con.cursor()
        self.daily_schedule = []

    # returns the number of players in the database
    def __len__(self):
        return len(self.db_player)

    def __iter__(self):
        return self.db_player.__iter__()

    # prints player info and stats (id -> full_name)
    def list_all_players(self):
        print("\nLISTING ALL PLAYERS IN DATABASE")
        print("===============================")
        for player_id, _player in self.db_player.items():
            # FINISH THIS
            _player.get_player_stats()

    # adds a player to the database if they haven't been added before
    def add_player(self, player_id, full_name, first_name, last_name, is_active):
        if player_id not in self.db_player:
            self.db_player[player_id] = Player(
                player_id, full_name, first_name, last_name, is_active
            )
        else:
            print(f"{player_id} is already in the database!")

    # adds a team to the database
    def add_team(self, team_id, full_name, abbr, nick_name, city):
        if team_id not in self.db_team:
            self.db_team[team_id] = Team(
                team_id, full_name, abbr, nick_name, city)
        else:
            print(f"{team_id} is already in the database!")

    # adds a game log to the Player class
    def add_game_log(self, player_id, player_game_log):
        self.db_player[player_id].add_game_log_entry(player_game_log)

    # adds common info to Player class
    def add_player_common_info(self, player_id, info):
        self.db_player[player_id].add_common_info(info)

    # adds common info to Team class
    def add_team_common_info(self, team_id, info):
        self.db_team[team_id].add_common_info(info)

    # adds fantasy logs to Player class
    def add_fantasy_logs(self, first_name, last_name, fantasy_log):
        for player_id, _player in self.db_player.items():
            if (first_name in _player.first_name and last_name in _player.last_name):
                self.db_player[player_id].add_fantasy_entry(fantasy_log)

    # adds box score data to Player class
    def add_boxScore(self, first, last, player_id, date, game_id, matchup, data):
        try:
            self.db_player[int(player_id)].add_boxScoreEntry(
                date, game_id, matchup, data)
            # print(self.db_player[int(player_id)])
        except KeyError:
            # print(f"{first} {last} ({player_id}) does not exist in the database")
            pass

    # connect to the db
    def connect_to_db(self):
        h = "localhost"
        db = "nba_db"
        usr = "kai"
        pw = "123"
        prt = 5432
        con = psycopg2.connect(host=h, database=db,
                               user=usr, password=pw, port=prt,)
        print(f" --> connected to database: '{db}' <-- ")
        return con

    # close connection to db
    def close_connection(self):
        self.con.close()
        print(f" --> closed connection to database <-- ")

    # drop table
    def drop_table(self, table_name):
        command = f"DROP TABLE IF EXISTS {table_name} CASCADE;"
        self.curr.execute(command)
        self.con.commit()
        print(f" --> dropping table: '{table_name}' <-- ")

    # create table
    def create_table(self, table_name, sql_cmd):
        self.drop_table(table_name)
        self.curr.execute(sql_cmd)
        self.con.commit()
        print(f" --> created table: '{table_name}' <-- ")

    # insert into table TEAM
    def insert_into_table_team(self, sql_cmd):
        self.curr.execute(sql_cmd, (0, "#", "#", "#",
                                    "#", "#", "#", "#", "#", "#"))
        self.con.commit()

        for team_id, _team in self.db_team.items():
            self.curr.execute(
                sql_cmd,
                (
                    team_id,
                    _team.nick_name,
                    _team.abbr,
                    _team.city,
                    _team.team_code,
                    _team.conference,
                    _team.division,
                    _team.wins,
                    _team.loses,
                    _team.pct,
                )
            )
        self.con.commit()
        print("inserted data into table: Team")

    # insert into table PLAYER
    def insert_into_table_player(self, sql_cmd):
        for player_id, _player in self.db_player.items():
            self.curr.execute(
                sql_cmd,
                (
                    player_id,
                    _player.last_name,
                    _player.first_name,
                    _player.position,
                    _player.jersey,
                    _player.team_id,
                    _player.team_abbreviation,
                    _player.is_active,
                )
            )
        self.con.commit()
        print("inserted data into table: Player")

    # insert into table GameStats
    def insert_into_table_gamestats(self, sql_cmd):
        for player_id, _player in self.db_player.items():
            if len(_player.game_log) != 0:
                for game_id, _game in _player.game_log.items():
                    # print(len(_player.game_log))
                    self.curr.execute(
                        sql_cmd,
                        (
                            player_id,
                            game_id,
                            _game["game_date"],
                            _game["matchup"],
                            _game["win_lose"],
                            _game["min_played"],
                            _game["fgm"],
                            _game["fga"],
                            _game["fg_pct"],
                            _game["fg3m"],
                            _game["fg3a"],
                            _game["fg3_pct"],
                            _game["ftm"],
                            _game["fta"],
                            _game["ft_pct"],
                            _game["oreb"],
                            _game["dreb"],
                            _game["tot_reb"],
                            _game["ast"],
                            _game["stl"],
                            _game["blk"],
                            _game["tov"],
                            _game["pf"],
                            _game["pts"],
                            _game["plus_minus"],
                        )
                    )
        self.con.commit()
        print("inserted game logs into table: GameStats")

    # insert into table Fantasy
    def insert_into_table_fantasy(self, sql_cmd):
        for player_id, _player in self.db_player.items():
            if (len(_player.fantasy_log) != 0):
                for game_id, _game in _player.fantasy_log.items():
                    self.curr.execute(
                        sql_cmd,
                        (
                            player_id,
                            _player.first_name,
                            _player.last_name,
                            _game["opponent"],
                            _game["fantasy_points"],
                            _game["cost"],
                            _game["value"],
                            _game["min"],
                            _game["pts"],
                            _game["rebs"],
                            _game["asts"],
                            _game["stls"],
                            _game["blks"],
                            _game["tos"],
                        )
                    )
        self.con.commit()
        print("inserted fantasy logs into table: Fantasy")
