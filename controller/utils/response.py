from data.database import Database

# goes through the response from nba_api and extracts the relevant info


class Response:
    def __init__(self, resp, database=None):
        self.resp = resp
        self.db = database

    # extract only active player info
    def extract_active_players(self):
        print("extracting active player templates...")
        for player in self.resp:
            if player["is_active"]:
                id = player["id"]
                full_name = player["full_name"]
                first_name = player["first_name"]
                last_name = player["last_name"]
                is_active = player["is_active"]

                self.db.add_player(id, full_name, first_name,
                                   last_name, is_active)

    # extract team info
    def extract_teams(self):
        print("extracting team templates...")
        for team in self.resp:
            id = team["id"]
            full_name = team["full_name"]
            abbr = team["abbreviation"]
            nick_name = team["nickname"]
            city = team["city"]
            state = team["state"]
            year_founded = team["year_founded"]

            self.db.add_team(id, full_name, abbr, nick_name, city)

    # extract game log for players
    def extract_player_game_log(self, player_id):
        print(f"extracting player game logs for {player_id}...")
        for game in self.resp["PlayerGameLog"]:
            player_id = game["Player_ID"]  # player ID
            if self.db != None:
                self.db.add_game_log(player_id, self.resp["PlayerGameLog"])
            else:
                print("database not specified... cannot add game log!")

    # extract common player info for players (team_id, position, etc.)
    def extract_player_common_info(self, player_id):
        print(f"extracting common player info for {player_id}...")
        for info in self.resp["CommonPlayerInfo"]:
            if self.db != None:
                # print("info: ", info)
                self.db.add_player_common_info(player_id, info)
            else:
                print("database not specified... cannot add common player info!")

    # extract common team info for teams (conference, division, win/loses, etc.)
    def extract_team_common_info(self, team_id):
        print(f"extracting common team info for {team_id}...")
        for info in self.resp["TeamInfoCommon"]:
            if self.db != None:
                # print("info: ", info)
                self.db.add_team_common_info(team_id, info)
            else:
                print("database not specified... cannot add common team info!")


    def extract_fantasy_logs(self):
        for i in self.resp:
            info = i[0]
            info = info.split()
            data = info + i[1:]
            first_name = info[2]
            last_name = info[3]
            self.db.add_fantasy_logs(first_name, last_name, data)