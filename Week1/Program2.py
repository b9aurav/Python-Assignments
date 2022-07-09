def feetToInch(feet):
    return float(feet * 12)

def inchToFeet(inch):
    return float(inch / 12)

n = float(input('Enter value : '))
print('\n|-----OPTIONS-----|')
print('|[1].Feet to Inch.|')
print('|[2].Inch to Feet.|')
print('|-----------------|\n')
choice = int(input('Choose an option : '))

if choice == 1:
    print('Inches : ', feetToInch(n))
elif choice == 2:
    print('Feets : ', inchToFeet(n))
else:
    print('Invalid choice!')