T = int(input())

for t in range(1, T+1):
    a = list(map(int, input().split()))
    print(f'Case #{t}: {a[0]} + {a[1]} = {sum(a)}')