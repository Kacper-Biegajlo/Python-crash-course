import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'data/sitka_weather_2018_simple.csv'  
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader) 
   
    # Get dates,and PRCPs from this file.
    dates, PRCPs = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            PRCP = float(row[3])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            PRCPs.append(PRCP)
        

# Plot the PRCPS.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, PRCPs, c='blue')

# Format plot.
title = "Daily PRCP - 2018\nSitka"
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Rainfall (in)", fontsize=16) 
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()