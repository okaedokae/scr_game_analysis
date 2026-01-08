import requests
#import matplotlib.pyplot as plt

year=2022

teamsdict = {
    2022 : {
        "maxpoints" : None,
        "rank1" : None,
    }, 
    2023 : {
        "maxpoints": None,  
        "rank1" : None,
    },
    2024 : {
        "maxpoints": None,
        "rank1" : None,
    },
    2025 : {
        "maxpoints": 300,
        "rank1" : None,
    }
}

headers = {
    'X-TBA-Auth-Key': "3AJcNjPY3385WzN6iFTPksA7zKrK44SWGCJJbgCwW4D7mZjBi31gFBhqCPK6aGGp",
}

while year < 2026:
    matchkeys = (requests.get(f'https://www.thebluealliance.com/api/v3/team/frc4613/event/{year}ausc/matches/keys',headers=headers)).json()
    matches = (requests.get(f'https://www.thebluealliance.com/api/v3/team/frc4613/event/{year}ausc/matches/simple',headers=headers)).json()
    print(year)
    for i in matches:
        if "frc4613" in matches[matches.index(i)]["alliances"]["red"]["team_keys"]:
            print(matchkeys[matches.index(i)], matches[matches.index(i)]["alliances"])
        else:
            print(matches[matches.index(i)]["alliances"])
    year += 1