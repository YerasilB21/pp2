#Ряд - 2
a = int(input())
b = int(input())
if a < b:
    for i in range(a, b + 1):
        print(i, end = " ")
elif a > b:
    for i in range(a, b - 1, -1):
        print(i, end = " ")
elif a == b:
    print(a)