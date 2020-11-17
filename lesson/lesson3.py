# Task 1
s = 'helloworld'
print(s[:2], s[-2:])
print(len('helloworld'))

a = 'my'
print(a * 2)
if a == 'x':
    print('ok')
else:
    print(' ')

# Task 2
phone_number = '0985070966'
print(len(phone_number))
if phone_number.isnumeric():
    print('Ok')
else:
    print('No')

# Task 3
s = 'anton'
d = (input('Введіть ім’я: '))
if s == d.lower():
    print('Ok')
else:
    print('No')
