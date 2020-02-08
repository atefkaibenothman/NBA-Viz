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
            print(f"{first} {last} ({player_id}) does not exist in the database")

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

    # create PLAYER table
    def create_player_table(self):
        table_name = "Player"
        self.drop_table(table_name)

        command = f"""
            CREATE TABLE IF NOT EXISTS {table_name} (
                player_id INT PRIMARY KEY,
                lname TEXT,
                fname TEXT,
                position TEXT,
                jersey TEXT,
                team_id INT REFERENCES team (team_id),
                team_abr TEXT,
                is_active BOOLEAN
            );
        """

        self.curr.execute(command)
        self.con.commit()
        print(f" --> created table: '{table_name}' <-- ")

    # create TEAM table
    def create_team_table(self):
        table_name = "Team"
        self.drop_table(table_name)

        command = f"""
            CREATE TABLE IF NOT EXISTS {table_name} (
                team_id INT PRIMARY KEY,
                team_name TEXT,
                team_abr TEXT,
                team_city TEXT,
                team_code TEXT,
                team_conference TEXT,
                team_division TEXT,
                team_wins TEXT,
                team_loses TEXT,
                team_wlpct TEXT
            );
        """

        self.curr.execute(command)
        self.con.commit()
        print(f" --> created table: '{table_name}' <-- ")

    # create FANTASY table
    def create_fantasy_table(self):
        table_name = "Fantasy"
        self.drop_table(table_name)

        command = f"""
            CREATE TABLE IF NOT EXISTS {table_name} (
                player_id INT PRIMARY KEY,
                fname TEXT,
                lname TEXT,
                matchup TEXT,
                points TEXT,
                cost TEXT,
                value TEXT,
                mins TEXT,
                pts TEXT,
                rebs TEXT,
                asts TEXT,
                stls TEXT,
                blks TEXT,
                tos TEXT
            );
        """

        self.curr.execute(command)
        self.con.commit()
        print(f" --> created table: '{table_name}' <-- ")

    # insert fantasy data to database
    def insert_fantasy_data(self):
        for player_id, _player in self.db_player.items():
            if len(_player.fantasy_log) != 0:
                for game_id, _game in _player.fantasy_log.items():
                    # print(player_id, _player)
                    command = """
                        INSERT INTO Fantasy (player_id, fname, lname, matchup, points, cost, value, mins, pts, rebs, asts, stls, blks, tos)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
                    """

                    self.curr.execute(
                        command,
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
                        ),
                    )
                self.con.commit()
                print("inserted data into table")

    # create GameStats table
    def create_gamestats_table(self):
        table_name = "GameStats"
        self.drop_table(table_name)

        command = f"""
            CREATE TABLE IF NOT EXISTS {table_name} (
                player_id INT REFERENCES player (player_id),
                game_id INT,
                game_date TEXT,
                matchup TEXT,
                winlose TEXT,
                mp INT,
                fgm INT,
                fga INT,
                fg_pct NUMERIC,
                fg3m INT,
                fg3a INT,
                fg3_pct NUMERIC,
                ftm INT,
                fta INT,
                ft_pct NUMERIC,
                oreb INT,
                dreb INT,
                tot_reb INT,
                ast INT,
                stl INT,
                blk INT,
                tov INT,
                pf INT,
                pts INT,
                plus_minus INT,
                primary key (player_id, game_id)
            )
        """

        self.curr.execute(command)
        self.con.commit()
        print(f" --> created table: '{table_name}' <-- ")

    # insert player id's and names to database
    def insert_player_data(self):
        for player_id, _player in self.db_player.items():
            # print(player_id, _player)
            command = """
                INSERT INTO Player (player_id, lname, fname, position, jersey, team_id, team_abr, is_active)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
            """

            self.curr.execute(
                command,
                (
                    player_id,
                    _player.last_name,
                    _player.first_name,
                    _player.position,
                    _player.jersey,
                    _player.team_id,
                    _player.team_abbreviation,
                    _player.is_active,
                ),
            )
        self.con.commit()
        print("inserted data into table")

    # insert team data to database
    def insert_team_data(self):
        self.curr.execute(
            "INSERT INTO Team (team_id, team_name, team_abr, team_city, team_code, team_conference, team_division, team_wins, team_loses, team_wlpct) VALUES (%s, %s, %s ,%s, %s, %s, %s, %s, %s, %s);",
            (0, "#", "#", "#", "#", "#", "#", "#", "#", "#"),
        )
        self.con.commit()

        for team_id, _team in self.db_team.items():
            command = """
                INSERT INTO Team (team_id, team_name, team_abr, team_city, team_code, team_conference, team_division, team_wins, team_loses, team_wlpct)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
            """

            self.curr.execute(
                command,
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
                ),
            )
        self.con.commit()
        print("inserted data into team table")

    # insert game logs to database
    def insert_game_logs(self):
        for player_id, _player in self.db_player.items():
            if len(_player.game_log) != 0:
                for game_id, _game in _player.game_log.items():
                    game_date = _game["game_date"]
                    min_played = _game["min_played"]
                    matchup = _game["matchup"]
                    winlose = _game["win_lose"]
                    fgm = _game["fgm"]
                    fga = _game["fga"]
                    fg_pct = _game["fg_pct"]
                    fg3m = _game["fg3m"]
                    fg3a = _game["fg3a"]
                    fg3_pct = _game["fg3_pct"]
                    ftm = _game["ftm"]
                    fta = _game["fta"]
                    ft_pct = _game["ft_pct"]
                    oreb = _game["oreb"]
                    dreb = _game["dreb"]
                    tot_reb = _game["tot_reb"]
                    ast = _game["ast"]
                    stl = _game["stl"]
                    blk = _game["blk"]
                    tov = _game["tov"]
                    pf = _game["pf"]
                    pts = _game["pts"]
                    plus_minus = _game["plus_minus"]

                    command = f"""
                        INSERT INTO gamestats (player_id, game_id, game_date, matchup, winlose, mp, fgm, fga, fg_pct, fg3m, fg3a, fg3_pct, ftm, fta, ft_pct, oreb, dreb, tot_reb, ast, stl, blk, tov, pf, pts, plus_minus)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
                    """

                    self.curr.execute(
                        command,
                        (
                            player_id,
                            game_id,
                            game_date,
                            matchup,
                            winlose,
                            min_played,
                            fgm,
                            fga,
                            fg_pct,
                            fg3m,
                            fg3a,
                            fg3_pct,
                            ftm,
                            fta,
                            ft_pct,
                            oreb,
                            dreb,
                            tot_reb,
                            ast,
                            stl,
                            blk,
                            tov,
                            pf,
                            pts,
                            plus_minus,
                        ),
                    )

        self.con.commit()
        print("inserted game logs to database")
