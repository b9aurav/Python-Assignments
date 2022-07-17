def find_palindrome(list):
    palindrome_list = []
    for word in list:
        word_stack = []
        for char in word:
            word_stack.insert(0, char)
        reverse_word = ''.join(word_stack)
        if word == reverse_word:
            palindrome_list.append(word)
    
    print(palindrome_list)

list = ['madam', 'apple', 'deer', 'wow', 'peep', 'fear', 'dad']
find_palindrome(list)