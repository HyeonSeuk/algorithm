n = int(input())
s = 0
a = list(map(int, input().split()))
m = max(a)
for i in range(n):
    b = a[i]/m*100
    s += b
print(s/n) 