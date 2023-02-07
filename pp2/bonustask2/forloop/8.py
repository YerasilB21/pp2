#Сумма факториалов
def pactor(x):
    pac = 1
    for i in range(1, x+1):
        pac *= i
    return pac
n = int(input())
sum = 0
for i in range(1, n + 1):
    sum += pactor(i)
print(sum)
