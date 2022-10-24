import os
import csv

directory = "data\\labels\\"
csvfile = "images\\locs.csv"

with open(csvfile) as csv_file:
    csv_reader = csv.reader(csv_file)
    rows = list(csv_reader)

with open("data\\checknum.txt","r") as f:
    rawdata = f.readlines()
    checknum_list = rawdata[0].split(",")

with open('data\\out.csv', 'w', encoding='UTF8', newline='') as csvf:
    writer = csv.writer(csvf)
    counter = 0
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if os.path.isfile(f):
            raw = filename[6:]
            raw = raw[:-4]
            if checknum_list[counter] == '1':
                print(raw)
                writer.writerow(rows[int(raw)])
                print(rows[int(raw)])
            counter += 1
