phone = input('Enter phone number : ')
if len(phone) == 12:
    digitCount = 0
    isValid = False
    for digit in phone:
        if (digitCount == 3 or digitCount == 7):
            if digit == '-':
                isValid = True
            else:
                isValid = False
                break
        elif digit.isdigit():
            isValid = True
        else:
            isValid = False
            break
        digitCount = digitCount + 1

if isValid:
    print('Valid format.')
else:
    print('Invalid format!')