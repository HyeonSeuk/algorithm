n = int(input())
road = list(map(int, input().split()))
h = 0
lst = []
for i in range(n-1):
    if road[i] < road[i+1]:
        h += (road[i+1] - road[i])
        lst.append(h)
    else:
        h = 0
        lst.append(h)

print(max(lst))