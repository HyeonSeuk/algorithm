s = int(input())
cnt = 0
for i in range(int(input())):
    a, b = map(int, input().split())
    cnt += a*b
if s == cnt:
    print('Yes')
else:
    print('No')