from oddsbrewapp.getBPProps import getBPProps
from oddsbrewapp.PrizePicks import get_player_data

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
                    "last5avg": csv_prop['last5avg'],
                    "last5over": csv_prop['last5over'],
                    "last5under": csv_prop['last5under'],
                    "last5push": csv_prop['last5push'],
                    "last10avg": csv_prop['last10avg'],
                    "last10over": csv_prop['last10over'],
                    "last10under": csv_prop['last10under'],
                    "last10push": csv_prop['last10push'],
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
                    if prop[f'{book}over'] <= -138 or prop[f'{book}under'] <= -138:
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
    print(best_props)
    print(final_props)
    return best_props, final_props
