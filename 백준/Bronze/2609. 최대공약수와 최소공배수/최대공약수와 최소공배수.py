a, b = map(int, input().split())
lst = []
for i in range(1, (a+b)):
    if (a%i, b%i) == (0, 0):
        lst.append(i)
print(max(lst))
print(a*b//max(lst))