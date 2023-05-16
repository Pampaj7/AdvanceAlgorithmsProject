import csv

with open("/Users/pampaj/Desktop/DataSet/dblp-all-csv/Prove/ProvaTabella.csv", 'rt') as f:
    data = csv.reader(f)
    line_count = 0
    for row in data:
        if line_count == 0:
            print("Nomi delle Colonne:")
            print(row)
            print('-' * 80)
            print('Dati:')
            line_count += 1
        else:
            print(row)


