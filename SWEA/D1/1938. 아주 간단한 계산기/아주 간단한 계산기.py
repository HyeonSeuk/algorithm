a, b = list(map(int, input().split()))
calculator = [a+b, a-b, a*b, a//b]
for i in calculator:
    print(i)