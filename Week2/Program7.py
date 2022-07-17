def read_file_append(file):
    words = []
    for word in file:
        words.append(word)

    print('Append method : ')
    print(words)

def read_file_idiom(file):
    content = ''
    for word in file:
        content = content + " " + word

    print('\nIdiom method : ')
    print(content)

file = open('words.txt', 'r')
read_file_append(file)
file.seek(0)
read_file_idiom(file)