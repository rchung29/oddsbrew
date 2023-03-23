import requests

def getESPNID():
    url = "https://sports.core.api.espn.com/v3/sports/basketball/nba/athletes?limit=20000"
    response = requests.get(url)
    response_json = response.json()
    output = []
    for row in response_json['items']:
        if id == "2991230":
            print(row['fullName'])
        push = {
            'name': row['fullName'],
            'id': row['id']
        }
        output.append(push)

    return output

def getAllStats(prizepicks):
    ids = getESPNID()
    aggregated = []
    for id in ids:
        playerID = id['id']
        if id['name'] in prizepicks:
            url = f"https://site.web.api.espn.com/apis/common/v3/sports/basketball/nba/athletes/{playerID}/gamelog"
            response = requests.get(url)
            if response.status_code == 500:
                aggregated.append({
                            'name': id['name'],
                            'points': 500,
                            'rebounds': 500,
                            'assists': 500,
                            '3pt': 500,
                            'pts+rebs+asts': 500,
                            'pts+rebs': 500,
                            'pts+asts': 500,
                            'rebs+asts': 500,
                            'steals': 500,
                            'blocks': 500,
                        })
            else:
                response_json = response.json()
                games = response_json['seasonTypes'][0]['categories']

                for months in games:
                    for events in months['events']:
                        output = {
                            'name': id['name'],
                            'points': 0,
                            'rebounds': 0,
                            'assists': 0,
                            '3pt': 0,
                            'pts+rebs+asts': 0,
                            'pts+rebs': 0,
                            'pts+asts': 0,
                            'rebs+asts': 0,
                            'steals': 0,
                            'blocks': 0,
                        }
                        output['points'] += float(events['stats'][13])
                        output['rebounds'] += float(events['stats'][7])
                        output['assists'] += float(events['stats'][8])
                        output['3pt'] += float(events['stats'][3].split('-')[0])
                        output['steals'] += float(events['stats'][10])
                        output['blocks'] += float(events['stats'][9])
                        output['pts+rebs+asts'] += float(events['stats'][13]) + float(events['stats'][7]) + float(events['stats'][8])
                        output['pts+rebs'] += float(events['stats'][13]) + float(events['stats'][7])
                        output['pts+asts'] += float(events['stats'][13]) + float(events['stats'][8])
                        output['rebs+asts'] += float(events['stats'][7]) + float(events['stats'][8])
                        aggregated.append(output)
        else:
            aggregated.append({
                'name': id['name'],
                'points': 500,
                'rebounds': 500,
                'assists': 500,
                '3pt': 500,
                'pts+rebs+asts': 500,
                'pts+rebs': 500,
                'pts+asts': 500,
                'rebs+asts': 500,
                'steals': 500,
                'blocks': 500,
            })
    return aggregated