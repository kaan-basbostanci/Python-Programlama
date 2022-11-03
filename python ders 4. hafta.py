import csv

with open('iris.data', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)
        print(row["species"]) 


        baslik = ["sicaklik","nem","basinc"]
        veri = [[30, 71.3, 10],[36.8, 50, 9]]
with open("sensor_veri.csv",
        "w", encoding=UTF8, newline='') as f:
        writer = csv.writer(f)
        writer = writerows(baslik)
