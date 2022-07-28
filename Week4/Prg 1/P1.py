from Shape import Circle
from Shape import Square

while True:
    print('[1] Circle')
    print('[2] Square')
    print('[3] Exit')
    ch = int(input('Enter Choice -> '))
    if(ch == 1):
        radius = float(input('Enter radius : '))
        print('Area of a circle is ', Circle.Area(radius))
        print('Volume of a circle is ', Circle.Volume(radius))
    elif(ch == 2):
        length = float(input('Enter length : '))
        print('Area of a square is ', Square.Area(length))
        print('Volume of a square is ', Square.Volume(length))
    elif(ch == 3):
        break
    else:
        print('Invalid Choice!')