a = int(input())
lst = set(map(int, input().split()))
b = int(input())
lit = list(map(int, input().split()))

for i in lit:
    if i in lst:
        print(1)
    else:
        print(0)