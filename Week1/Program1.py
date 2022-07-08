n = int(input('Enter a number : '))
for y in range(1, 11):
    for x in range(1, n + 1):
        print(x*y, end="\t")
    print()