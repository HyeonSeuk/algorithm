a = list(input())
for _ in range(int(input())):
        b, c = map(int, input().split())
        a[b], a[c] = a[c], a[b]
print(''.join(a))