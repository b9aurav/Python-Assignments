def removeDuplicates(originallist):
    list = [originallist[0]]
    for i in originallist:
        if i not in list:
            list.append(i)
    print(list)

list = []
while True:
    value = input('Enter element value : ')
    if value == 'c':
        break
    list.append(int(value))

removeDuplicates(list)