from itertools import permutations

n = int(input())
arr = list(map(int, input().split()))

# 모든 순열을 생성
all_permutations = permutations(arr)

total = 0
for p in all_permutations:
    temp_sum = 0
    for i in range(n-1):
        temp_sum += abs(p[i] - p[i+1])
    total = max(total, temp_sum) # 현재 순열의 합이 이전까지의 최대 값보다 크면, total 업데이트

print(total)