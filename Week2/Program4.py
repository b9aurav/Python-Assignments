def is_anagram(word1, word2):
    if len(word1) != len(word2):
        return False

    for char in word1:
        if char not in word2:
            return False

    return True
            
        
word1 = str(input('Enter 1st word : '))
word2 = str(input('Enter 2nd word : '))

if is_anagram(word1, word2):
    print('Anagram!')
else:
    print('Not anagram!')
