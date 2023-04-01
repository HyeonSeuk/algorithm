n, m = map(int, input().split())
lst = list(range(1, n+1))
for i in range(m):
    a, b, c = map(int, input().split())
    lst = lst[:a-1] + lst[c-1:b] + lst[a-1:c-1] + lst[b:]
print(*lst)