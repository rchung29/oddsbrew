import requests
import json

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
