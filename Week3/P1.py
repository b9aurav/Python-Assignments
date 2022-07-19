def add_student(name):
    file = open('students.txt', 'a')
    file.write(name)
    file.close()

def find_student(name):
    file = open('students.txt', 'r')
    index = 0
    for line in file.readlines():
        index += 1
        if line.strip() == name:
            file.close()
            return index
    
    file.close()
    return 'Student not found!'


add_student('Tushar')
add_student('\nHarsh')
add_student('\nGaurav')
add_student('\nJay')
add_student('\nHardip')
print('Student found at index ', find_student('Jay'))