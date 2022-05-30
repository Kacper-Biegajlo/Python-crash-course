import json

from plotly.graph_objs import Scattergeo, Layout 
from plotly import offline

filename = 'data/MODIS_C6_1_Global_7d.csv'
with open(filename) as f:
    all_eq_data = json.load(f)

title = all_eq_data['metadata']['title']    
all_eq_dicts = all_eq_data['features']

mags, lons, lats, hover_texts = [], [], [], []
for eq_dict in all_eq_dicts:
    mags.append(eq_dict['properties']['mag'])
    lons.append(eq_dict['geometry']['coordinates'][0])
    lats.append(eq_dict['geometry']['coordinates'][1])
    hover_texts.append(eq_dict['properties']['title'])


# Map the earthquakes.
data = [{
       'type': 'scattergeo',
       'lon': lons,
       'lat': lats,
       'text': hover_texts,
       'marker': {
           'size': [4*mag for mag in mags],
           'color': mags,
           'colorscale': 'Viridis',
           'reversescale': True,
           'colorbar': {'title': 'Magnitude'},
}, }]
my_layout = Layout(title=title)  

fig = {'data': data, 'layout': my_layout} 
offline.plot(fig, filename='global_earthquakes.html')   
