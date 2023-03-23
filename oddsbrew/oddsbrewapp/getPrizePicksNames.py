import requests
def get_player_names():
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
                alternate_name = matched_player['attributes']['name']
                team = matched_player['attributes']['team']
                player_name = matched_player['attributes']['name'].replace(" Jr.", "")
                if player_name.startswith("KJ "):
                    player_name = player_name.replace("KJ ", "Kenyon ", 1)
                if alternate_name == "KJ Martin Jr.":
                    alternate_name = "Kenyon Martin Jr."
                if alternate_name == "OG Anunoby":
                    alternate_name = "O.G. Anunoby"
                if alternate_name == "Fred VanVleet\t":
                    alternate_name = "Fred VanVleet"
                if alternate_name == "Nicolas Claxton":
                    alternate_name = "Nic Claxton"
                if alternate_name == "Marcus Morris":
                    alternate_name = "Marcus Morris Sr."
                output_data.append(alternate_name)
    unique_names = list(set(output_data))
    return unique_names