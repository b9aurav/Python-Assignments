lines = []
print('START TYPING:')
while True:
    line = input()
    if line:
        lines.append(line)
        lines.append(' ')
    else:
        break

text = ''.join(lines)

print('------------------------TEXT------------------------')
print(text)

print('\n------------------------INFO------------------------')
print('No. of characters : ', len(text))
print('No. of words      : ', len(text.split(' '))-1)

alphanumeric = 1
for char in text:
    if char.isalpha():
        alphanumeric = alphanumeric + 1
print('% of alphanumeric : ', (alphanumeric * 100) / len(text))