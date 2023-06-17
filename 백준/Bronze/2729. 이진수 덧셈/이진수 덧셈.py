n = int(input())
for _ in range(n):
    a, b = input().split()
    x = int(a, 2)
    y = int(b, 2)
    c = x + y
    print(bin(c)[2:])