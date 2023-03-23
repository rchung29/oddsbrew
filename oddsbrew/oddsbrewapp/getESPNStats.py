def getLast5(name, prop, proptype, allstats):
    games = allstats
    count = 0
    line = prop
    output = {
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
        'over': 0,
        'under': 0,
        'push': 0,
    }
    for months in games:
        if name == months['name']:
            if count == 5 and proptype == "Points":
                return [output['points'], output['over'], output['under'], output['push']]
            elif count == 5 and proptype == "Rebounds":
                return [output['rebounds'], output['over'], output['under'], output['push']]
            elif count == 5 and proptype == "Assists":
                return [output['assists'], output['over'], output['under'], output['push']]
            elif count == 5 and proptype == "3-PT Made":
                return [output['3pt'], output['over'], output['under'], output['push']]
            elif count == 5 and proptype == "Pts+Rebs+Asts":
                return [output['pts+rebs+asts'], output['over'], output['under'], output['push']]
            elif count == 5 and proptype == "Pts+Rebs":
                return [output['pts+rebs'], output['over'], output['under'], output['push']]
            elif count == 5 and proptype == "Pts+Asts":
                return [output['pts+asts'], output['over'], output['under'], output['push']]
            elif count == 5 and proptype == "Rebs+Asts":
                return [output['pts+rebs+asts'], output['over'], output['under'], output['push']]
            elif count == 5 and proptype == "Steals":
                return [output['pts+rebs'], output['over'], output['under'], output['push']]
            elif count == 5 and proptype == "Blocked Shots":
                return [output['pts+asts'], output['over'], output['under'], output['push']]
            output['points']+= float(months['points'])/5
            output['rebounds']+= float(months['rebounds'])/5
            output['assists']+= float(months['assists'])/5
            output['3pt']+= float(months['3pt'])/5
            output['steals']+= float(months['steals'])/5
            output['blocks']+= float(months['blocks'])/5
            output['pts+rebs+asts'] += float(months['points']+months['rebounds']+months['assists'])/5
            output['pts+rebs'] += float(months['points']+months['rebounds'])/5
            output['pts+asts'] += float(months['points']+months['assists'])/5
            output['rebs+asts'] += float(months['rebounds']+months['assists'])/5
            output['points'] = round(output['points'],1)
            output['rebounds'] = round(output['rebounds'], 1)
            output['assists'] = round(output['assists'], 1)
            output['steals'] = round(output['steals'], 1)
            output['blocks'] = round(output['blocks'], 1)
            output['pts+rebs+asts'] = round(output['pts+rebs+asts'], 1)
            output['pts+rebs'] = round(output['pts+rebs'], 1)
            output['pts+asts'] = round(output['pts+asts'], 1)
            output['rebs+asts'] = round(output['rebs+asts'], 1)
            output['3pt'] = round(output['3pt'], 1)
            if (proptype == "Points"):
                if months['points']>prop:
                    output['over']+=1
                if months['points']<prop:
                    output['under']+=1
                if months['points']==prop:
                    output['push']+=1
            elif (proptype == "Rebounds"):
                if months['rebounds']>prop:
                    output['over']+=1
                if months['rebounds']<prop:
                    output['under']+=1
                if months['rebounds']==prop:
                    output['push']+=1
            elif (proptype == "Assists"):
                if months['assists']>prop:
                    output['over']+=1
                if months['assists']<prop:
                    output['under']+=1
                if months['assists']==prop:
                    output['push']+=1
            elif (proptype == "3-PT Made"):
                if months['3pt']>prop:
                    output['over']+=1
                if months['3pt']<prop:
                    output['under']+=1
                if months['3pt']==prop:
                    output['push']+=1
            elif (proptype == "Pts+Rebs+Asts"):
                if months['points']+months['rebounds']+months['assists']>prop:
                    output['over']+=1
                if months['points']+months['rebounds']+months['assists']<prop:
                    output['under']+=1
                if months['points']+months['rebounds']+months['assists']==prop:
                    output['push']+=1
            elif (proptype == "Pts+Rebs"):
                if months['points']+months['rebounds']>prop:
                    output['over']+=1
                if months['points']+months['rebounds']<prop:
                    output['under']+=1
                if months['points']+months['rebounds']==prop:
                    output['push']+=1
            elif (proptype == "Pts+Asts"):
                if months['points']+months['assists']>prop:
                    output['over']+=1
                if months['points']+months['assists']<prop:
                    output['under']+=1
                if months['points']+months['assists']==prop:
                    output['push']+=1
            elif (proptype == "Rebs+Asts"):
                if months['rebounds']+months['assists']>prop:
                    output['over']+=1
                if months['rebounds']+months['assists']<prop:
                    output['under']+=1
                if months['rebounds']+months['assists']==prop:
                    output['push']+=1
            elif (proptype == "Blocked Shots"):
                if months['blocks']>prop:
                    output['over']+=1
                if months['blocks']<prop:
                    output['under']+=1
                if months['blocks']==prop:
                    output['push']+=1
            elif (proptype == "Steals"):
                if months['steals']>prop:
                    output['over']+=1
                if months['steals']<prop:
                    output['under']+=1
                if months['steals']==prop:
                    output['push']+=1
            count+=1

def getLast10(name, prop, proptype, allstats):
    games = allstats
    count = 0
    line = prop
    output = {
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
        'over': 0,
        'under': 0,
        'push': 0,
    }
    for months in games:
        if name == months['name']:
            if count == 10 and proptype == "Points":
                return [output['points'], output['over'], output['under'], output['push']]
            elif count == 10 and proptype == "Rebounds":
                return [output['rebounds'], output['over'], output['under'], output['push']]
            elif count == 10 and proptype == "Assists":
                return [output['assists'], output['over'], output['under'], output['push']]
            elif count == 10 and proptype == "3-PT Made":
                return [output['3pt'], output['over'], output['under'], output['push']]
            elif count == 10 and proptype == "Pts+Rebs+Asts":
                return [output['pts+rebs+asts'], output['over'], output['under'], output['push']]
            elif count == 10 and proptype == "Pts+Rebs":
                return [output['pts+rebs'], output['over'], output['under'], output['push']]
            elif count == 10 and proptype == "Pts+Asts":
                return [output['pts+asts'], output['over'], output['under'], output['push']]
            elif count == 10 and proptype == "Rebs+Asts":
                return [output['pts+rebs+asts'], output['over'], output['under'], output['push']]
            elif count == 10 and proptype == "Steals":
                return [output['pts+rebs'], output['over'], output['under'], output['push']]
            elif count == 10 and proptype == "Blocked Shots":
                return [output['pts+asts'], output['over'], output['under'], output['push']]
            output['points']+= float(months['points'])/10
            output['rebounds']+= float(months['rebounds'])/10
            output['assists']+= float(months['assists'])/10
            output['3pt']+= float(months['3pt'])/10
            output['steals']+= float(months['steals'])/10
            output['blocks']+= float(months['blocks'])/10
            output['pts+rebs+asts'] += float(months['points']+months['rebounds']+months['assists'])/10
            output['pts+rebs'] += float(months['points']+months['rebounds'])/10
            output['pts+asts'] += float(months['points']+months['assists'])/10
            output['rebs+asts'] += float(months['rebounds']+months['assists'])/10
            output['points'] = round(output['points'],1)
            output['rebounds'] = round(output['rebounds'], 1)
            output['assists'] = round(output['assists'], 1)
            output['steals'] = round(output['steals'], 1)
            output['blocks'] = round(output['blocks'], 1)
            output['pts+rebs+asts'] = round(output['pts+rebs+asts'], 1)
            output['pts+rebs'] = round(output['pts+rebs'], 1)
            output['pts+asts'] = round(output['pts+asts'], 1)
            output['rebs+asts'] = round(output['rebs+asts'], 1)
            output['3pt'] = round(output['3pt'], 1)
            if (proptype == "Points"):
                if months['points']>prop:
                    output['over']+=1
                if months['points']<prop:
                    output['under']+=1
                if months['points']==prop:
                    output['push']+=1
            elif (proptype == "Rebounds"):
                if months['rebounds']>prop:
                    output['over']+=1
                if months['rebounds']<prop:
                    output['under']+=1
                if months['rebounds']==prop:
                    output['push']+=1
            elif (proptype == "Assists"):
                if months['assists']>prop:
                    output['over']+=1
                if months['assists']<prop:
                    output['under']+=1
                if months['assists']==prop:
                    output['push']+=1
            elif (proptype == "3-PT Made"):
                if months['3pt']>prop:
                    output['over']+=1
                if months['3pt']<prop:
                    output['under']+=1
                if months['3pt']==prop:
                    output['push']+=1
            elif (proptype == "Pts+Rebs+Asts"):
                if months['points']+months['rebounds']+months['assists']>prop:
                    output['over']+=1
                if months['points']+months['rebounds']+months['assists']<prop:
                    output['under']+=1
                if months['points']+months['rebounds']+months['assists']==prop:
                    output['push']+=1
            elif (proptype == "Pts+Rebs"):
                if months['points']+months['rebounds']>prop:
                    output['over']+=1
                if months['points']+months['rebounds']<prop:
                    output['under']+=1
                if months['points']+months['rebounds']==prop:
                    output['push']+=1
            elif (proptype == "Pts+Asts"):
                if months['points']+months['assists']>prop:
                    output['over']+=1
                if months['points']+months['assists']<prop:
                    output['under']+=1
                if months['points']+months['assists']==prop:
                    output['push']+=1
            elif (proptype == "Rebs+Asts"):
                if months['rebounds']+months['assists']>prop:
                    output['over']+=1
                if months['rebounds']+months['assists']<prop:
                    output['under']+=1
                if months['rebounds']+months['assists']==prop:
                    output['push']+=1
            elif (proptype == "Blocked Shots"):
                if months['blocks']>prop:
                    output['over']+=1
                if months['blocks']<prop:
                    output['under']+=1
                if months['blocks']==prop:
                    output['push']+=1
            elif (proptype == "Steals"):
                if months['steals']>prop:
                    output['over']+=1
                if months['steals']<prop:
                    output['under']+=1
                if months['steals']==prop:
                    output['push']+=1
            count+=1