# create PLAYER table
create_player_table = """
            CREATE TABLE IF NOT EXISTS Player (
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

# create TEAM table
create_team_table = """
        CREATE TABLE IF NOT EXISTS Team (
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

# create FANTASY table
create_fantasy_table = """
        CREATE TABLE IF NOT EXISTS Fantasy (
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

# create GAMESTATS table
create_gamestats_table = """
        CREATE TABLE IF NOT EXISTS GameStats (
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
        );
    """

# inserts into TEAM table
insert_team_table = """
        INSERT INTO Team (team_id, team_name, team_abr, team_city, team_code, team_conference, team_division, team_wins, team_loses, team_wlpct)
        VALUES (%s, %s, %s ,%s, %s, %s, %s, %s, %s, %s);
    """

# inserts into Player table
insert_player_table = """
        INSERT INTO Player (player_id, lname, fname, position, jersey, team_id, team_abr, is_active)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
    """

# inserts into FANTASY table
insert_fantasy_table = """
        INSERT INTO Fantasy (player_id, fname, lname, matchup, points, cost, value, mins, pts, rebs, asts, stls, blks, tos)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
    """

# inserts into GAMESTATS table
insert_gamestats_table = """
        INSERT INTO gamestats (player_id, game_id, game_date, matchup, winlose, mp, fgm, fga, fg_pct, fg3m, fg3a, fg3_pct, ftm, fta, ft_pct, oreb, dreb, tot_reb, ast, stl, blk, tov, pf, pts, plus_minus)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
    """
