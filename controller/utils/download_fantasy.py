import requests
from bs4 import BeautifulSoup

from utils.response import Response

def run(url, db):
    r = get_response(url)
    s = get_soup(r)
    d = get_table_contents(s)

    r = Response(d, db)
    r.extract_fantasy_logs()

def get_response(url):
    response = requests.get(url)
    return response

def get_soup(resp):
    soup = BeautifulSoup(resp.text, "html.parser")
    return soup

def get_table_contents(soup):
    table = soup.find(class_="stat-table__body")
    count = 0
    content = []
    for row in table.find_all("tr"):
        columns = row.find_all("td")
        cols = [x.text.strip().strip() for x in columns]

        # game_info = cols[0].replace("\n", " ")
        # fanduel_points = cols[1]
        # player_cost = cols[2]
        # value = cols[3]
        # mins = cols[4]
        # pts = cols[5]
        # rebs = cols[6]
        # asts = cols[7]
        # stls = cols[8]
        # blks = cols[9]
        # turnovers = cols[10]

        content.append(cols)
    return content