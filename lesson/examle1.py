def hello_n(name: str, n: int):
    for i in range(n):
        print('привіт', name)

hello_n('Вася', 2)

t = ('q','w','e')
print(*t)
for x in t:
    print(x)

x = 178 / 3
x %= 5
print(x)

print(178 % 3)