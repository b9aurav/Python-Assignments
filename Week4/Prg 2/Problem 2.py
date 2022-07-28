import csv

def calculate_avg_cost(file, finish_point):
    finish_point = finish_point.upper()
    csvFile = csv.reader(file)
    total_cost = 0
    count = 0
    for index, line in enumerate(csvFile):
        if(index > 0 and line[10] == finish_point):
            total_cost += float(line[3])
            count += 1
    print('Total cost : ', total_cost)
    print('Average cost : ', total_cost / count)

finish_point = input('Enter finish point : ')

with open('Met_Office_2011_Air_Data.csv') as file:
    calculate_avg_cost(file, finish_point)