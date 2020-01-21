class Team:
    def __init__(self, id, full_name, abbr, nick_name, city):
        self.id = id
        self.full_name = full_name
        self.abbr = abbr
        self.nick_name = nick_name
        self.city = city
        self.conference = None
        self.division = None
        self.team_code = None
        self.wins = None
        self.loses = None
        self.pct = None

    def add_common_info(self, info):
        self.conference = info["TEAM_CONFERENCE"]
        self.division = info["TEAM_DIVISION"]
        self.team_code = info["TEAM_CODE"]
        self.wins = info["W"]
        self.loses = info["L"]
        self.pct = info["PCT"]
