T = int(input())
for _ in range(T):
    n = int(input())
    numbers = list(map(int, input().split()))
    print(min(numbers), max(numbers))