n = int(input())
a = map(int, input().split())
cnt = 0
for i in a:
    count = 0
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                count += 1
        if count == 0:
            cnt += 1
print(cnt)