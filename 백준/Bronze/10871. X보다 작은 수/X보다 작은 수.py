a, b = list(map(int, input().split()))
numbers = list(map(int, input().split()))

for i in numbers:
    if b > i:
        print(i, end=' ')