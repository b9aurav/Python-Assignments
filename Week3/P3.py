def count_lines(file):
    count = 0
    for line in file.readlines():
        if line.strip()[0] != 'T':
            count += 1
    return count

file = open('story.txt', 'r')
print('Line count : ', count_lines(file))
file.close()