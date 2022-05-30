import csv

filename = 'data/MODIS_C6_1_Global_7d.csv'  
with open(filename) as f:
    reader = csv.reader(f) 
    header_row = next(reader) 
    print(header_row)