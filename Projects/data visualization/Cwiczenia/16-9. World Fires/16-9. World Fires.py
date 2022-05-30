import csv
from datetime import datetime

from plotly.graph_objs import Scattergeo, Layout 
from plotly import offline

num_rows = 10_000

filename = 'data/MODIS_C6_1_Global_7d.csv'  
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader) 
   
    # Get dates, and high and low temperatures from this file.
    dates, bris = [], []
    lats, lons = [], []
    hover_texts = []
    row_num = 0
    for row in reader:
        date = datetime.strptime(row[5], '%Y-%m-%d')
        bri = float(row[2])
        label = f"{date.strftime('%m/%d/%y')} - {bri}"

        dates.append(date)
        bris.append(bri)
        lats.append(row[0])
        lons.append(row[1])
        hover_texts.append(label)

        row_num += 1
        if row_num == num_rows:
            break

# Map the earthquakes.
data = [{
       'type': 'scattergeo',
       'lon': lons,
       'lat': lats,
       'text': hover_texts,
       'marker': {
           'size': [bri/30 for bri in bris],
           'color': bris,
           'colorscale': 'YlOrRd',
           'reversescale': True,
           'colorbar': {'title': 'Brightness'},
}, }]

my_layout = Layout(title='Global Fire Activity')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_fires.html')