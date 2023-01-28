a = int(input())
b = list(map(int, input().split()))
c = int(input())

for i in range(a):
    v = b.count(c)
print(v)