import time

append_time = 0.0
idiom_time = 0.0

def read_file_append(file):
    append_time = time.time()
    words = []
    for word in file:
        words.append(word)

    print('Append method : ')
    print(words)
    print('Execution time : ', (time.time() - append_time) * 1000, 'ms')

def read_file_idiom(file):
    idiom_time = time.time()
    content = ''
    for word in file:
        content = content + " " + word

    print('\nIdiom method : ')
    print(content)
    print('Execution time : ', (time.time() - idiom_time) * 1000, 'ms')

file = open('words.txt', 'r')
read_file_append(file)
file.seek(0)
read_file_idiom(file)