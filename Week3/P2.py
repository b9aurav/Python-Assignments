def read_file(file):
    for line in file.readlines():
        print(line.strip())

file = open('poem.txt', 'r')
read_file(file)
file.close()