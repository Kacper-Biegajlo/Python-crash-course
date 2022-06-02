import requests

from plotly.graph_objs import Bar
from plotly import offline

url = 'http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/\
    ?key=XXXXXXXXXXXXXXXX&steamid=76561198010625224&format=json'
# For security reasons I removed my SteamAPI key but there should be a screen
#   shot of program working in this folder

# Also to use program for other accounts please change SteamID 

r = requests.get(url)
print(f"Status code: {r.status_code}")

all_eq_data = r.json()

all_eq_dicts = all_eq_data['response']['games']

appids, playtimes, links = [], [], []
for eq_dict in all_eq_dicts:
    playtime = eq_dict['playtime_forever']
    if playtime > 1440:
        appids.append(str(eq_dict['appid']))
        appid = eq_dict['appid']
        playtimes.append((eq_dict['playtime_forever']/1440))
        url = f"https://store.steampowered.com/agecheck/app/{appid}"
        link = f"<a href='{url}'>{appid}</a>"
        links.append(link)

# Make visualization. 
data = [{
       'type': 'bar',
       'x': links,
       'y': playtimes,
       'hovertext': links,
       'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1, 'color': 'rgb(25, 25, 25)'}
       },
        'opacity': 0.6,
}]
my_layout = {
       'title': 'My top played games on steam - in days',
       'titlefont': {'size': 28},
       'xaxis': {
        'categoryorder':'total descending',
        'title': 'Games IDs',
        'titlefont': {'size': 20},
        'tickfont': {'size': 15},
    },
        'yaxis': {
        'title': 'Days played',
        'titlefont': {'size': 20},
        'tickfont': {'size': 15},
    },
}
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='python_repos.html')