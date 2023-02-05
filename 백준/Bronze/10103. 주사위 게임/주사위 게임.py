x = 100
y = 100
for i in range(int(input())):
    a, b = map(int, input().split())
    if a > b:
        y -= a
    elif a < b:
        x -= b
    elif a == b:
        pass
print(x)
print(y) 