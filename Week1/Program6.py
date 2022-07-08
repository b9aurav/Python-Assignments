def sort(list):
    length = len(list)
    for elementIndex1 in range(0, length):
        for elementIndex2 in range(elementIndex1, length):
            if list[elementIndex1] > list[elementIndex2]:
                temp = list[elementIndex1]
                list[elementIndex1] = list[elementIndex2]
                list[elementIndex2] = temp

    print(list)

list = [70,60,50,40,30]
sort(list)