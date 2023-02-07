#Количество нулей
n = int(input())
d = 0
for i in range(n):
    number = int(input())
    if number == 0:
        d += 1
print(d)