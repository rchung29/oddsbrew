import requests
from .getBPProps import getBPProps

def format_name(name):
    if name == "TREY MURPHY III":
        return "trey-murphy"
    first, last = name.split(" ")
    if name == "DE'AARON FOX":
        return "deaaron-fox"
    elif name == "DENNIS SMITH":
        return "dennis-smith-jr"
    elif name == "KEVIN PORTER":
        return "kevin-porter-jr"
    elif name == "KENYON MARTIN":
        return "kenyon-martin-jr"
    elif name == "GARY TRENT":
        return "gary-trent-jr"
    elif name == "ALPEREN SENGUN":
        return "alperen-sengun-c"
    elif name == "P.J. WASHINGTON":
        return "pj-washington"
    elif name == "CAMERON JOHNSON":
        return "cameron-johnson-g"
    elif name == "DE'ANDRE HUNTER":
        return "deandre-hunter"
    return f"{first.lower()}-{last.lower()}"

def get_player_data():
    pp_props_url = 'https://api.prizepicks.com/projections?league_id=7&per_page=250&single_stat=true'
    headers = {
        'Connection': 'keep-alive',
        'Accept': 'application/json; charset=UTF-8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
        'Access-Control-Allow-Credentials': 'true',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Referer': 'https://app.prizepicks.com/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9'
    }

    with requests.Session() as session:
        session.headers.update(headers)
        response = session.get(url=pp_props_url)
    response_json = response.json()

    # Extract data and included objects
    data = response_json['data']
    included = response_json['included']

    # Create a dictionary to store new_player objects
    new_players = {}

    for entry in included:
        if entry['type'] == 'new_player':
            new_players[entry['id']] = entry

    # Loop through the data to find projections and match them to new_players
    output_data = []

    for entry in data:
        if entry['type'] == 'projection':
            player_id = entry['relationships']['new_player']['data']['id']
            if player_id in new_players:
                matched_player = new_players[player_id]
                team = matched_player['attributes']['team']
                player_name = matched_player['attributes']['name'].replace(" Jr.", "")
                if player_name.startswith("KJ "):
                    player_name = player_name.replace("KJ ", "Kenyon ", 1)
                output_data.append({
                    'name': player_name.upper(),
                    'line_score': entry['attributes']['line_score'],
                    'stat_type': entry['attributes']['stat_type'],
                    'team': team
                })

    return output_data

def getGameIds():
    url = "https://api.bettingpros.com/v3/events?sport=NBA&date=2023-03-21"
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US,en;q=0.9",
        "dnt": "1",
        "origin": "https://www.bettingpros.com",
        "referer": "https://www.bettingpros.com/nba/odds/player-props/giannis-antetokounmpo/",
        "sec-ch-ua": '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": "Android",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36",
        "x-api-key": "CHi8Hy5CEE4khd46XNYL23dCFX96oUdw6qOt1Dnh",
    }

    response = requests.get(url, headers=headers)
    data = response.json()

    event_ids = [str(event["id"]) for event in data["events"]]
    event_ids_string = ":".join(event_ids)

    return event_ids_string

def compare_props(csv_props, bp_props):
    result = []
    for csv_prop in csv_props:
        for bp_prop in bp_props:
            if (csv_prop["stat_type"] == bp_prop["propType"] and csv_prop["name"] == bp_prop["name"]):
                prop = {
                    "name": bp_prop["name"],
                    "propType": bp_prop["propType"],
                    "PPLine": csv_prop["line_score"],  # Add PrizePicks Line
                    "dkline": bp_prop["Draft Kings Line"],
                    "dkover": bp_prop["Draft Kings Over"],
                    "dkunder": bp_prop["Draft Kings Under"],
                    "fdline": bp_prop["Fanduel Line"],
                    "fdover": bp_prop["Fanduel Over"],
                    "fdunder": bp_prop["Fanduel Under"],
                    "mgmline": bp_prop["MGM Line"],
                    "mgmover": bp_prop["MGM Over"],
                    "mgmunder": bp_prop["MGM Under"],
                }
                result.append(prop)

    return result

def find_best_props_v2(final_props):
    best_props = []

    for prop in final_props:
        ppline = float(prop['PPLine'])  # Convert PrizePicks Line to float
        dkline = prop['dkline']
        fdline = prop['fdline']
        csline = prop['mgmline']
        lines = [dkline, fdline, csline]

        available_books = [book for book in ['dk', 'fd', 'mgm']
                           if prop[f'{book}line'] is not None]

        if len(available_books) > 0:
            for book in available_books:
                if prop[f'{book}line'] == ppline:
                    if prop[f'{book}over'] <= -140 or prop[f'{book}under'] <= -140:
                        best_props.append(prop)
                        break
                elif prop[f'{book}line'] < ppline and prop[f'{book}under'] <= -125:
                    best_props.append(prop)
                elif prop[f'{book}line'] > ppline and prop[f'{book}over'] <= -125:
                    best_props.append(prop)

    return best_props

def main():
    csv_props = get_player_data()  # Use get_player_data instead of read_output_csv
    final_props = []
    bp_props = getBPProps()
    for prop in csv_props:
        common_props = compare_props([prop], bp_props)
        final_props.extend(common_props)
    # df = pd.DataFrame(final_props)
    # df.to_csv('output_picks.csv', index=False)
    best_props = find_best_props_v2(final_props)
    # df2 = pd.DataFrame(best_props)
    # df2.to_csv('good_picks.csv', index=False)
    # for prop in best_props:
    #     print(prop)
    # print(final_props)
    return best_props

# if __name__ == "__main__":
#     main()
