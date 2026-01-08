import requests
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as MaxNLocator

year=2022

teamsdict = {
    2022 : {
        "maxpoints" : 189,
        "avgrank1" : None,
        "maxrank1": None,
        "avgplay": None,
        "maxplay" : None,
        "ratequals": None,
    }, 
    2023 : {
        "maxpoints": 217,  
        "avgrank1" : None,
        "maxrank1": None,
        "avgplay": None,
        "maxplay" : None,
        "ratequals": None,
    },
    2024 : {
        "maxpoints": 192,
        "avgrank1" : None,
        "maxrank1": None,
        "avgplay": None,
        "maxplay" : None,
        "ratequals": None,
    },
    2025 : {
        "maxpoints": 301,
        "avgrank1" : None,
        "maxrank1": None,
        "avgplay": None,
        "maxplay" : None,
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
    teamsdict[year]["avgrank1"] = (sum(qualscores)/len(qualscores))/teamsdict[year]["maxpoints"]*100
    teamsdict[year]["maxrank1"] = max(qualscores)/teamsdict[year]["maxpoints"]*100
    teamsdict[year]["avgplay"] = (sum(playoffscores)/len(playoffscores))/teamsdict[year]["maxpoints"]*100
    teamsdict[year]["maxplay"] = max(playoffscores)/teamsdict[year]["maxpoints"]*100
    year += 1
print(teamsdict)
fig, ax = plt.subplots()
ax.plot(np.array((2022,2023,2024,2025)),np.array((teamsdict[2022]["maxplay"],teamsdict[2023]["maxplay"],teamsdict[2024]["maxplay"],teamsdict[2025]["maxplay"])), color="blue", label="Maximum % in Playoffs")
ax.plot(np.array((2022,2023,2024,2025)),np.array((teamsdict[2022]["avgplay"],teamsdict[2023]["avgplay"],teamsdict[2024]["avgplay"],teamsdict[2025]["avgplay"])), color="red", label="Average % in Playoffs")
ax.plot(np.array((2022,2023,2024,2025)),np.array((teamsdict[2022]["maxrank1"],teamsdict[2023]["maxrank1"],teamsdict[2024]["maxrank1"],teamsdict[2025]["maxrank1"])), color="green", label="Maximum % in Qualifications")
ax.plot(np.array((2022,2023,2024,2025)),np.array((teamsdict[2022]["avgrank1"],teamsdict[2023]["avgrank1"],teamsdict[2024]["avgrank1"],teamsdict[2025]["avgrank1"])), color="yellow", label="Average % in Qualifications")
ax.set_xticks(range(2022,2026))
plt.legend()
plt.show()