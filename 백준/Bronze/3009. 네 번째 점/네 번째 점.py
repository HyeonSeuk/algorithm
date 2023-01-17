a, b = list(map(int, input().split()))
c, d = list(map(int, input().split()))
e, f = list(map(int, input().split()))

if a == c:
    x = e
elif c == e:
    x = a
else:
    x = c

if b == d:
    y = f
elif d == f:
    y = b
else:
    y = d

print(f'{x} {y}')