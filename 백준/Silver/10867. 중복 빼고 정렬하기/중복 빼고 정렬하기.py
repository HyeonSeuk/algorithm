n = int(input())
a = list(map(int, input().split()))
a = list(set(a))
a.sort()
for i in a:
    print(i, end=' ')