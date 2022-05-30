# Version with automatic indexing


import csv
from datetime import datetime

from matplotlib import pyplot as plt

def get_weather_data(filename):
    """Get the highs and lows from a data file."""
    place_name = ''
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        date_index = header_row.index('DATE')
        high_index = header_row.index('TMAX')
        low_index = header_row.index('TMIN')
        name_index = header_row.index('NAME')

        # Get dates, and high and low temperatures from this file.
        for row in reader:
            if not place_name:
                place_name = row[name_index]
            current_date = datetime.strptime(row[date_index], '%Y-%m-%d')
            try:
                high = int(row[high_index])
                low = int(row[low_index])
            except ValueError:
                print(f"Missing data for {current_date}")
            else:
                dates.append(current_date)
                highs.append(high)
                lows.append(low)


# Get temperatures and dates from Sitka
dates, highs, lows = [], [], []
get_weather_data(filename = 'data/sitka_weather_2018_simple.csv')

# Plot data for Sitka
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Get temperatures and dats from Death Valley.
dates, highs, lows = [], [], []
get_weather_data(filename = 'data/death_valley_2018_simple.csv')

# Plot data for Death Valley
ax.plot(dates, highs, c='red', alpha=0.2)
ax.plot(dates, lows, c='blue', alpha=0.2)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.05)

# Format plot.
title = "Daily high and low temperatures - 2018\nDeath Valley and Sitka"
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16) 
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()