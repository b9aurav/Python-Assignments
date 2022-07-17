import random

ist = [0] * 365
list = []
count = 0

def has_duplicate(list):
    for element in list:
        if ist[element] == 1:
            global count;
            count += 1
        else:
            ist[element] += 1

for i in range(0, 23):
    list.append(random.randint(1, 31))

has_duplicate(list)
print(count/23)