n = int(input())
p = 1
lst = []
for i in range(1, n+1):
    p *= i

for j in str(p):
    lst.append(j)

cnt = 0
for k in lst:
    if k == '0':
        cnt += 1
    else:
        cnt = 0
print(cnt)