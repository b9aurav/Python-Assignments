def count_words(file):
    words = []
    for line in file.readlines():
        words.extend(line.split(' '))
    print(words)
    print('Words Count : ', len(words))

file = open('story.txt', 'r')
count_words(file)
file.close()