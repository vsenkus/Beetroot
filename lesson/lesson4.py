import random


# Task 1
user_number = random.randint(1, 2)
while True:
    user_number = int(input('Вгадай число: '))
    if user_number == random.randint(1, 2):
        print('Ура ти виграв')
        break
    else:
        print('Ні')

# Task 2
user_name = input('Введіть ім’я:  ')
user_age = int(input('Введіть свій вік:  '))
print(f'Hello {user_name}, on your next birthday you’ll be {user_age + 1} years')

# Task 3
letters_2 = input('Введіть Привіт - ')
quantity_n = 5
i = 0
while i < quantity_n:
    print(random.choices(letters_2, k = 5))
    i += 1
    if i % quantity_n == 0:
        print('Дякую')

# Task 4
a = int(input('Введіть число a  '))
b = int(input('Введіть число b  '))
result = int(input('Який результат ділення a на b  '))

if result == round(a / b):
    print('Вірно')
else:
    print('Не вірно, спробуйте ще раз')
