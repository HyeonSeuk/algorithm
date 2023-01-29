a = int(input())
n = 0
for i in range(1, a+1):
    if i < 100:
        n += 1
    else:
        s = list(map(int, str(i)))
        if s[1] - s[0] == s[2] - s[1]:
            n += 1
print(n)