import os
import csv

air_data = []

if not os.path.exists('output'):
    os.mkdir('output')

singlecsv_dir = os.path.join('output','single.csv')
returncsv_dir = os.path.join('output','return.csv')

def fetch_data(file):
    air_data.clear()
    csvFile = csv.reader(file)
    for index, line in enumerate(csvFile):
        air_data.append(list(line))

def create_singlecsv(singlecsv_dir):
    with open(singlecsv_dir, 'w') as singlecsv_file:
        writer = csv.writer(singlecsv_file)
        single_list = list(filter(lambda column: column if column[5] == 'Single' or column[5] == 'Ticket Single or Return' else None, air_data))
        for row in single_list:
            for element in row:
                if element == 'Single' or element == 'Ticket Single or Return':
                    row.remove(element)
        writer.writerows(single_list)

def create_returncsv(returncsv_dir):
    with open(returncsv_dir, 'w') as returncsv_dir:
        writer = csv.writer(returncsv_dir)
        return_list = list(filter(lambda column: column if column[5] == 'Return' or column[5] == 'Ticket Single or Return' else None, air_data))
        for row in return_list:
            for element in row:
                if element == 'Return' or element == 'Ticket Single or Return':
                    row.remove(element)
        writer.writerows(return_list)

with open('Met_Office_2011_Air_Data.csv', 'r') as file:
    fetch_data(file)
    create_singlecsv(singlecsv_dir)
    file.seek(0)
    fetch_data(file)
    create_returncsv(returncsv_dir)