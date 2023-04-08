a, b = input().split()
b = int(b)
cnt = 0

for i, c in enumerate(a[::-1]):
    num = int(c, b) if c.isdigit() else ord(c) - 55
    cnt += num * (b ** i)

print(cnt)