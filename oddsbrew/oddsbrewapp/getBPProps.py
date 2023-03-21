import requests
import json
from .getBPSchedule import getGameIds


#gary-trent-jr
#kenyon-martin-jr
#kevin-porter-jr

def getBPProps():
    eventid = getGameIds()
    formatted_name = ""
    # if name == "deaaron-fox":
    #     formatted_name = "DE'AARON FOX"
    # elif name == "dennis-smith-jr":
    #     formatted_name = "DENNIS SMITH"
    # elif name == "kevin-porter-jr":
    #     formatted_name = "KEVIN PORTER"
    # elif name == "kenyon-martin-jr":
    #     formatted_name = "KENYON MARTIN"
    # elif name == "gary-trent-jr":
    #     formatted_name = "GARY TRENT"
    # elif name == "alperen-sengun-c":
    #     formatted_name = "ALPEREN SENGUN"
    # elif name == "pj-washington":
    #     formatted_name = "P.J. WASHINGTON"
    # elif name == "cameron-johnson-g":
    #     formatted_name = "CAMERON JOHNSON"
    # elif name == "deandre-hunter":
    #     formatted_name = "DE'ANDRE HUNTER"
    # else:
    #     split = name.split('-')
    #     formatted_name = ' '.join([name.upper() for name in split])
    # formatted_name = ' '.join([name.capitalize() for name in name.split('-')])
    url = f"https://api.bettingpros.com/v3/offers?sport=NBA&market_id=156:157:151:162:147:160:152:335:336:337:338&event_id={eventid}&location=NJ&live=true"
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US,en;q=0.9",
        "dnt": "1",
        "origin": "https://www.bettingpros.com",
        # "referer": "https://www.bettingpros.com/nba/odds/player-props/desmond-bane/?date=2023-03-15",
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
    response_json = response.json()
    # print(response)
    output = []
    for row in response_json["offers"]:
        name = row["participants"][0]["player"]["slug"]
        formatted_name = ""
        if name == "deaaron-fox":
            formatted_name = "DE'AARON FOX"
        elif name == "dennis-smith-jr":
            formatted_name = "DENNIS SMITH"
        elif name == "kevin-porter-jr":
            formatted_name = "KEVIN PORTER"
        elif name == "kenyon-martin-jr":
            formatted_name = "KENYON MARTIN"
        elif name == "gary-trent-jr":
            formatted_name = "GARY TRENT"
        elif name == "alperen-sengun-c":
            formatted_name = "ALPEREN SENGUN"
        elif name == "pj-washington":
            formatted_name = "P.J. WASHINGTON"
        elif name == "cameron-johnson-g":
            formatted_name = "CAMERON JOHNSON"
        elif name == "deandre-hunter":
            formatted_name = "DE'ANDRE HUNTER"
        elif name == "shai-gilgeous-alexander":
            formatted_name = "SHAI GILGEOUS-ALEXANDER"
        elif name == "trey-murphy":
            formatted_name = "TREY MURPHY III"
        else:
            parts = name.split("-")
            capitalized_parts = [part.upper() for part in parts]
            formatted_name = " ".join(capitalized_parts)
        dfOver = None
        dfLine = None
        dfUnder = None
        fdOver = None
        fdLine = None
        fdUnder = None
        mgmOver = None
        mgmLine = None
        mgmUnder = None
        if row["market_id"] == 160:
            propType = "Steals"
            for entries in row["selections"]:
                ou = entries["selection"]
                for props in entries["books"]:
                    if props["id"] == 12 and ou == "over":
                        dfOver = props["lines"][0]["cost"]
                        dfLine = props["lines"][0]["line"]
                    elif props["id"] == 13 and ou == "over":
                        mgmOver = props["lines"][0]["cost"]
                        mgmLine = props["lines"][0]["line"]
                    elif props["id"] == 19 and ou == "over":
                        fdOver = props["lines"][0]["cost"]
                        fdLine = props["lines"][0]["line"]
                    elif props["id"] == 12 and ou == "under":
                        dfUnder = props["lines"][0]["cost"]
                        dfLine = props["lines"][0]["line"]
                    elif props["id"] == 13 and ou == "under":
                        mgmUnder = props["lines"][0]["cost"]
                        mgmLine = props["lines"][0]["line"]
                    elif props["id"] == 19 and ou == "under":
                        fdUnder = props["lines"][0]["cost"]
                        fdLine = props["lines"][0]["line"]
            output.append({'name': formatted_name,'propType':propType,'Draft Kings Line':dfLine,'Draft Kings Over':dfOver,'Draft Kings Under':dfUnder,'Fanduel Line':fdLine,'Fanduel Over':fdOver,'Fanduel Under':fdUnder,'MGM Line':mgmLine,'MGM Over':mgmOver,'MGM Under':mgmUnder})
        elif row["market_id"] == 337:
            propType = "Rebs+Asts"
            for entries in row["selections"]:
                ou = entries["selection"]
                for props in entries["books"]:
                    if props["id"] == 12 and ou == "over":
                        dfOver = props["lines"][0]["cost"]
                        dfLine = props["lines"][0]["line"]
                    elif props["id"] == 13 and ou == "over":
                        mgmOver = props["lines"][0]["cost"]
                        mgmLine = props["lines"][0]["line"]
                    elif props["id"] == 19 and ou == "over":
                        fdOver = props["lines"][0]["cost"]
                        fdLine = props["lines"][0]["line"]
                    elif props["id"] == 12 and ou == "under":
                        dfUnder = props["lines"][0]["cost"]
                        dfLine = props["lines"][0]["line"]
                    elif props["id"] == 13 and ou == "under":
                        mgmUnder = props["lines"][0]["cost"]
                        mgmLine = props["lines"][0]["line"]
                    elif props["id"] == 19 and ou == "under":
                        fdUnder = props["lines"][0]["cost"]
                        fdLine = props["lines"][0]["line"]
            output.append({'name': formatted_name,'propType':propType,'Draft Kings Line':dfLine,'Draft Kings Over':dfOver,'Draft Kings Under':dfUnder,'Fanduel Line':fdLine,'Fanduel Over':fdOver,'Fanduel Under':fdUnder,'MGM Line':mgmLine,'MGM Over':mgmOver,'MGM Under':mgmUnder})
        elif row["market_id"] == 157:
            propType = "Rebounds"
            for entries in row["selections"]:
                ou = entries["selection"]
                for props in entries["books"]:
                    if props["id"] == 12 and ou == "over":
                        dfOver = props["lines"][0]["cost"]
                        dfLine = props["lines"][0]["line"]
                    elif props["id"] == 13 and ou == "over":
                        mgmOver = props["lines"][0]["cost"]
                        mgmLine = props["lines"][0]["line"]
                    elif props["id"] == 19 and ou == "over":
                        fdOver = props["lines"][0]["cost"]
                        fdLine = props["lines"][0]["line"]
                    elif props["id"] == 12 and ou == "under":
                        dfUnder = props["lines"][0]["cost"]
                        dfLine = props["lines"][0]["line"]
                    elif props["id"] == 13 and ou == "under":
                        mgmUnder = props["lines"][0]["cost"]
                        mgmLine = props["lines"][0]["line"]
                    elif props["id"] == 19 and ou == "under":
                        fdUnder = props["lines"][0]["cost"]
                        fdLine = props["lines"][0]["line"]
            output.append({'name': formatted_name,'propType':propType,'Draft Kings Line':dfLine,'Draft Kings Over':dfOver,'Draft Kings Under':dfUnder,'Fanduel Line':fdLine,'Fanduel Over':fdOver,'Fanduel Under':fdUnder,'MGM Line':mgmLine,'MGM Over':mgmOver,'MGM Under':mgmUnder})
        elif row["market_id"] == 152:
            propType = "Blocks"
            for entries in row["selections"]:
                ou = entries["selection"]
                for props in entries["books"]:
                    if props["id"] == 12 and ou == "over":
                        dfOver = props["lines"][0]["cost"]
                        dfLine = props["lines"][0]["line"]
                    elif props["id"] == 13 and ou == "over":
                        mgmOver = props["lines"][0]["cost"]
                        mgmLine = props["lines"][0]["line"]
                    elif props["id"] == 19 and ou == "over":
                        fdOver = props["lines"][0]["cost"]
                        fdLine = props["lines"][0]["line"]
                    elif props["id"] == 12 and ou == "under":
                        dfUnder = props["lines"][0]["cost"]
                        dfLine = props["lines"][0]["line"]
                    elif props["id"] == 13 and ou == "under":
                        mgmUnder = props["lines"][0]["cost"]
                        mgmLine = props["lines"][0]["line"]
                    elif props["id"] == 19 and ou == "under":
                        fdUnder = props["lines"][0]["cost"]
                        fdLine = props["lines"][0]["line"]
            output.append({'name': formatted_name,'propType':propType,'Draft Kings Line':dfLine,'Draft Kings Over':dfOver,'Draft Kings Under':dfUnder,'Fanduel Line':fdLine,'Fanduel Over':fdOver,'Fanduel Under':fdUnder,'MGM Line':mgmLine,'MGM Over':mgmOver,'MGM Under':mgmUnder})
        elif row["market_id"] == 336:
            propType = "Pts+Rebs"
            for entries in row["selections"]:
                ou = entries["selection"]
                for props in entries["books"]:
                    if props["id"] == 12 and ou == "over":
                        dfOver = props["lines"][0]["cost"]
                        dfLine = props["lines"][0]["line"]
                    elif props["id"] == 13 and ou == "over":
                        mgmOver = props["lines"][0]["cost"]
                        mgmLine = props["lines"][0]["line"]
                    elif props["id"] == 19 and ou == "over":
                        fdOver = props["lines"][0]["cost"]
                        fdLine = props["lines"][0]["line"]
                    elif props["id"] == 12 and ou == "under":
                        dfUnder = props["lines"][0]["cost"]
                        dfLine = props["lines"][0]["line"]
                    elif props["id"] == 13 and ou == "under":
                        mgmUnder = props["lines"][0]["cost"]
                        mgmLine = props["lines"][0]["line"]
                    elif props["id"] == 19 and ou == "under":
                        fdUnder = props["lines"][0]["cost"]
                        fdLine = props["lines"][0]["line"]
            output.append({'name': formatted_name,'propType':propType,'Draft Kings Line':dfLine,'Draft Kings Over':dfOver,'Draft Kings Under':dfUnder,'Fanduel Line':fdLine,'Fanduel Over':fdOver,'Fanduel Under':fdUnder,'MGM Line':mgmLine,'MGM Over':mgmOver,'MGM Under':mgmUnder})
        elif row["market_id"] == 162:
            propType = "3-PT Made"
            for entries in row["selections"]:
                ou = entries["selection"]
                for props in entries["books"]:
                    if props["id"] == 12 and ou == "over":
                        dfOver = props["lines"][0]["cost"]
                        dfLine = props["lines"][0]["line"]
                    elif props["id"] == 13 and ou == "over":
                        mgmOver = props["lines"][0]["cost"]
                        mgmLine = props["lines"][0]["line"]
                    elif props["id"] == 19 and ou == "over":
                        fdOver = props["lines"][0]["cost"]
                        fdLine = props["lines"][0]["line"]
                    elif props["id"] == 12 and ou == "under":
                        dfUnder = props["lines"][0]["cost"]
                        dfLine = props["lines"][0]["line"]
                    elif props["id"] == 13 and ou == "under":
                        mgmUnder = props["lines"][0]["cost"]
                        mgmLine = props["lines"][0]["line"]
                    elif props["id"] == 19 and ou == "under":
                        fdUnder = props["lines"][0]["cost"]
                        fdLine = props["lines"][0]["line"]
            output.append({'name': formatted_name,'propType':propType,'Draft Kings Line':dfLine,'Draft Kings Over':dfOver,'Draft Kings Under':dfUnder,'Fanduel Line':fdLine,'Fanduel Over':fdOver,'Fanduel Under':fdUnder,'MGM Line':mgmLine,'MGM Over':mgmOver,'MGM Under':mgmUnder})
        elif row["market_id"] == 338:
            propType = "Pts+Rebs+Asts"
            for entries in row["selections"]:
                ou = entries["selection"]
                for props in entries["books"]:
                    if props["id"] == 12 and ou == "over":
                        dfOver = props["lines"][0]["cost"]
                        dfLine = props["lines"][0]["line"]
                    elif props["id"] == 13 and ou == "over":
                        mgmOver = props["lines"][0]["cost"]
                        mgmLine = props["lines"][0]["line"]
                    elif props["id"] == 19 and ou == "over":
                        fdOver = props["lines"][0]["cost"]
                        fdLine = props["lines"][0]["line"]
                    elif props["id"] == 12 and ou == "under":
                        dfUnder = props["lines"][0]["cost"]
                        dfLine = props["lines"][0]["line"]
                    elif props["id"] == 13 and ou == "under":
                        mgmUnder = props["lines"][0]["cost"]
                        mgmLine = props["lines"][0]["line"]
                    elif props["id"] == 19 and ou == "under":
                        fdUnder = props["lines"][0]["cost"]
                        fdLine = props["lines"][0]["line"]
            output.append({'name': formatted_name,'propType':propType,'Draft Kings Line':dfLine,'Draft Kings Over':dfOver,'Draft Kings Under':dfUnder,'Fanduel Line':fdLine,'Fanduel Over':fdOver,'Fanduel Under':fdUnder,'MGM Line':mgmLine,'MGM Over':mgmOver,'MGM Under':mgmUnder})
        elif row["market_id"] == 335:
            propType = "Pts+Asts"
            for entries in row["selections"]:
                ou = entries["selection"]
                for props in entries["books"]:
                    if props["id"] == 12 and ou == "over":
                        dfOver = props["lines"][0]["cost"]
                        dfLine = props["lines"][0]["line"]
                    elif props["id"] == 13 and ou == "over":
                        mgmOver = props["lines"][0]["cost"]
                        mgmLine = props["lines"][0]["line"]
                    elif props["id"] == 19 and ou == "over":
                        fdOver = props["lines"][0]["cost"]
                        fdLine = props["lines"][0]["line"]
                    elif props["id"] == 12 and ou == "under":
                        dfUnder = props["lines"][0]["cost"]
                        dfLine = props["lines"][0]["line"]
                    elif props["id"] == 13 and ou == "under":
                        mgmUnder = props["lines"][0]["cost"]
                        mgmLine = props["lines"][0]["line"]
                    elif props["id"] == 19 and ou == "under":
                        fdUnder = props["lines"][0]["cost"]
                        fdLine = props["lines"][0]["line"]
            output.append({'name': formatted_name,'propType':propType,'Draft Kings Line':dfLine,'Draft Kings Over':dfOver,'Draft Kings Under':dfUnder,'Fanduel Line':fdLine,'Fanduel Over':fdOver,'Fanduel Under':fdUnder,'MGM Line':mgmLine,'MGM Over':mgmOver,'MGM Under':mgmUnder})
        elif row["market_id"] == 156:
            propType = "Points"
            for entries in row["selections"]:
                ou = entries["selection"]
                for props in entries["books"]:
                    if props["id"] == 12 and ou == "over":
                        dfOver = props["lines"][0]["cost"]
                        dfLine = props["lines"][0]["line"]
                    elif props["id"] == 13 and ou == "over":
                        mgmOver = props["lines"][0]["cost"]
                        mgmLine = props["lines"][0]["line"]
                    elif props["id"] == 19 and ou == "over":
                        fdOver = props["lines"][0]["cost"]
                        fdLine = props["lines"][0]["line"]
                    elif props["id"] == 12 and ou == "under":
                        dfUnder = props["lines"][0]["cost"]
                        dfLine = props["lines"][0]["line"]
                    elif props["id"] == 13 and ou == "under":
                        mgmUnder = props["lines"][0]["cost"]
                        mgmLine = props["lines"][0]["line"]
                    elif props["id"] == 19 and ou == "under":
                        fdUnder = props["lines"][0]["cost"]
                        fdLine = props["lines"][0]["line"]
            output.append({'name': formatted_name,'propType':propType,'Draft Kings Line':dfLine,'Draft Kings Over':dfOver,'Draft Kings Under':dfUnder,'Fanduel Line':fdLine,'Fanduel Over':fdOver,'Fanduel Under':fdUnder,'MGM Line':mgmLine,'MGM Over':mgmOver,'MGM Under':mgmUnder})
        elif row["market_id"] == 151:
            propType = "Assists"
            for entries in row["selections"]:
                ou = entries["selection"]
                for props in entries["books"]:
                    if props["id"] == 12 and ou == "over":
                        dfOver = props["lines"][0]["cost"]
                        dfLine = props["lines"][0]["line"]
                    elif props["id"] == 13 and ou == "over":
                        mgmOver = props["lines"][0]["cost"]
                        mgmLine = props["lines"][0]["line"]
                    elif props["id"] == 19 and ou == "over":
                        fdOver = props["lines"][0]["cost"]
                        fdLine = props["lines"][0]["line"]
                    elif props["id"] == 12 and ou == "under":
                        dfUnder = props["lines"][0]["cost"]
                        dfLine = props["lines"][0]["line"]
                    elif props["id"] == 13 and ou == "under":
                        mgmUnder = props["lines"][0]["cost"]
                        mgmLine = props["lines"][0]["line"]
                    elif props["id"] == 19 and ou == "under":
                        fdUnder = props["lines"][0]["cost"]
                        fdLine = props["lines"][0]["line"]
            output.append({'name': formatted_name,'propType':propType,'Draft Kings Line':dfLine,'Draft Kings Over':dfOver,'Draft Kings Under':dfUnder,'Fanduel Line':fdLine,'Fanduel Over':fdOver,'Fanduel Under':fdUnder,'MGM Line':mgmLine,'MGM Over':mgmOver,'MGM Under':mgmUnder})
    return output