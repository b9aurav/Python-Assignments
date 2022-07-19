import pickle

def add_record(code, name, salary):
    employee = {
        'code': code,
        'name': name,
        'salary': salary
    }
    file = open('employee.dat', 'ab')
    pickle.dump(employee, file)
    file.close()

def check_salary():
    file = open('employee.dat', 'rb')
    while True:
        try:
            employee = pickle.load(file)
            if int(employee['salary']) > 30000:
                print(employee)
        except:
            break
    file.close()
    
while True:
    print('[1]. Add Record')
    print('[2]. Less than 30000 Salary')
    print('[3]. Exit')
    c = int(input('Choose an option : '))
    if c == 1:
        code = input('Enter code : ')
        name = input('Enter Name : ')
        salary = int(input('Enter Salary : '))
        add_record(code, name, salary)
    elif c == 2:
        check_salary()
    elif c == 3:
        break
    else:
        print('Invalid Choice!')