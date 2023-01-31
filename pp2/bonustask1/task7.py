#Парты
x = int(input())
y = int(input())
z = int(input())
a = x // 2
b = x % 2
c = y // 2
d = y % 2
e = z // 2
f = z % 2
if b > 0:
    a = a + 1
if d > 0:
    c = c + 1
if f > 0:
    e = e + 1
print(a + c + e)