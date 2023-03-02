cnt = 0
a, b = map(int, input().split())
for i in range(1, a+1):
    cnt += str(i).count(str(b))
print(cnt)