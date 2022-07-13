def is_sorted(list):
    min = list[0]

    for i in range(0, len(list)):
        if list[i] < min:
            return False
        min = list[i]
        
    return True

list = []
while True:
    value = input('Enter element value : ')
    if value == 'c':
        break
    list.append(int(value))

if is_sorted(list):
    print('List is sorted.')
else:
    print('List is not sorted!')