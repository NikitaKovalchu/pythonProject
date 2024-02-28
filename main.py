a = input()
for b in range(len(a)):
    if b % 2 == 0:
        print(a[b].upper())
    else:
        print(a[b])

a = int(input('Введите число'))
if a < 1001:
    for i in range(a + 1):
        print(i)
else:
        print('Ошибка')


a = []
for b in range(1, 5+1):
    a.append(b)
a.reverse()
for c in a:
    print(c)


