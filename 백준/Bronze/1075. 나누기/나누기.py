n = int(input())
f = int(input())
a = n // 100
b = a * 100

while b % f != 0:
    b += 1
print(str(b)[-2:])