def sort(list):
    length = len(list)
    for elementIndex1 in range(0, length - 1):
        for elementIndex2 in range(0, length - elementIndex1 - 1):
            if list[elementIndex2] > list[elementIndex2 + 1]:
                temp = list[elementIndex2]
                list[elementIndex2] = list[elementIndex2 + 1]
                list[elementIndex2 + 1] = temp

    print(list)

list = [70,60,50,40,30]
sort(list)