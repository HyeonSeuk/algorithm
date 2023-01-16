score = int(input())
numbers = list(map(int, input().split()))
sum = 0
count = 0
for i in range(score):
    if numbers[i] == 1:
        count += 1
    else:
        count = 0
    sum += count
print(sum)