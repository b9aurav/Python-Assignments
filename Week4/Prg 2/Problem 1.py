import csv

def Total_Cost(file):
    csvFile = csv.reader(file)
    sum = 0
    for index, line in enumerate(csvFile):
        if(index > 0):
            sum += float(line[3])
    print('Total Cost of All Flights is ',sum)

def remove_duplicates(originallist):
    list = [originallist[0]]
    for i in originallist:
        if i not in list:
            list.append(i)
    return list

def Cost_per_carrier(file):
    csvFile = csv.reader(file)
    records = ['FLYBE']
    for index, line in enumerate(csvFile):
        if(index > 0):
            records.append(line[11])
    cpc = remove_duplicates(records)

    sum = []

    for rec in cpc:
        ss = 0
        file.seek(0)
        for ind, line in enumerate(csvFile):
            if(ind > 0 and line[11] == rec):
                ss += float(line[3])
        cost = {
            'carrier' : rec,
            'cost' : ss
        }
        sum.append(cost)
    print(sorted(sum, key=lambda carrier: carrier['cost']))

     

with open('Met_Office_2011_Air_Data.csv') as file:
    Total_Cost(file)
    file.seek(0)
    Cost_per_carrier(file)