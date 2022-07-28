import csv
import os




def sort(sub_li): 
    # reverse = None (Sorts in Ascending order) 
    # key is set to sort using second element of 
    # sublist lambda has been used 
    sub_li.sort(key = lambda x: x[11],reverse=True) 
    return sub_li 

list2=[]
with open('Met_Office_2011_Air_Data.csv') as file:
     
     csvFile = csv.reader(file)
     #for i in csvFile:
     #    print(i)
     sum=0
     for i,val in enumerate(csvFile):
         if i>0:
             list1 = val
             sum += float(list1[1])
             list2.append(val)
     print("sum of prices",sum)
     print("csvFile is an object of type",type(csvFile))
     print("list2 is an object of type",type(list2))
     #print(list2[0])
     #print((sort(list2))[:10])

     carrierset= set(row[11] for row in list2)
     print(carrierset)
     
     filtered = list(filter( lambda x: x if x[11]=='FLYBE' else None,list2))
     print(len(filtered))
     print(list2)
     #print(filtered[-20:-1])
     sumcount=0
     for i,val in enumerate(filtered):
         sumcount += 1
         #print(sumcount)

     #print(sumcount)

     if os.path.exists('output'):
        if os.path.join('output/','single.csv'):
                with open(r'output/single.csv', 'w', newline='') as f:
                    writer = csv.writer(f)
                    singlelist = list(filter( lambda x: x if x[5]=='Single' else None,list2))
                    writer.writerows(singlelist)
        if os.path.join('output/','return.csv'):
                with open(r'output/return.csv', 'w', newline='') as f:
                    writer = csv.writer(f)
                    returnlist = list(filter( lambda x: x if x[5]=='Return' else None,list2))
                    writer.writerows(returnlist)
                
                            
