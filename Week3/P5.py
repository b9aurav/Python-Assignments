def check_char(file):
    upper_count = 0
    for line in file.readlines():
        for char in line:
            if char.isupper():
                upper_count += 1
    print('Upper case character count : ', upper_count)

file = open('story.txt', 'r')
check_char(file)
file.close()