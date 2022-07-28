import csv
data={}
with open('Met_Office_2011_Air_Data.csv','r') as file:
 csvFile = csv.reader(file)
 temp = [ data[i[11]].append(list(i)) if i[11] in data.keys() else data.update({i[11] : list(i)}) for i in csvFile ]
 print(data['FLYBE'])
print(type(data))




#import csv
#data={}
#with open('Met_Office_2011_Air_Data.csv','r') as file:
# csvFile = csv.DictReader(file)
# temp = [ data[i['Air Carrier']].append(list(i.values())) if i['Air Carrier'] in data.keys() else data.update({i['Air Carrier'] : list(i.values())}) for i in csvFile ]
# print(data['FLYBE'])