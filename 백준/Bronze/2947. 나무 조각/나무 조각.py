a = list(map(int, input().split()))
numbers = [1, 2, 3, 4, 5]
while a != numbers:
    for i in range(4):
        if a[i] > a[i+1]:
            temp = a[i]
            a[i] = a[i+1]
            a[i+1] = temp
            print(*a)