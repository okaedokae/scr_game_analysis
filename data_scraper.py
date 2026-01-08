import requests
#import matplotlib.pyplot as plt

year=2022

teamsdict = {
    2022 : {
        "maxpoints" : 189,
        "avgrank1" : None,
        "maxrank1": None,
        "ratequals": None,
    }, 
    2023 : {
        "maxpoints": 217,  
        "avgrank1" : None,
        "maxrank1": None,
        "ratequals": None,
    },
    2024 : {
        "maxpoints": 192,
        "avgrank1" : None,
        "maxrank1": None,
        "ratequals": None,
    },
    2025 : {
        "maxpoints": 301,
        "avgrank1" : None,
        "maxrank1": None,
        "ratequals": None,
    }
}

headers = {
    'X-TBA-Auth-Key': "3AJcNjPY3385WzN6iFTPksA7zKrK44SWGCJJbgCwW4D7mZjBi31gFBhqCPK6aGGp",
}

while year < 2026:
    wonmatches = 0
    qualscores = []
    playoffscores = []
    matches = (requests.get(f'https://www.thebluealliance.com/api/v3/team/frc4613/event/{year}ausc/matches/simple',headers=headers)).json()
    print(year)
    for i in matches:
        if "frc4613" in i["alliances"]["red"]["team_keys"]:
            if i["winning_alliance"] == "red":
                wonmatches += 1
            if i["comp_level"] == "qm":
                qualscores.append(i["alliances"]["red"]["score"])
            else:
                playoffscores.append(i["alliances"]["red"]["score"])
        else:
            if i["winning_alliance"] == "blue":
                wonmatches += 1
            if i["comp_level"] == "qm":
                qualscores.append(i["alliances"]["blue"]["score"])
            else:
                playoffscores.append(i["alliances"]["blue"]["score"])
    teamsdict[year]["ratequals"] = (wonmatches/len(matches))*100
    teamsdict[year]["avgrank1"] = (sum(qualscores)/len(qualscores))/teamsdict[year]["maxpoints"]
    teamsdict[year]["maxrank1"] = max(qualscores)/teamsdict[year]["maxpoints"]
    year += 1