import sys
input = sys.stdin.readline

n = int(input())

arr = [0] * 10001

for _ in range(n):
    num = int(input())
    arr[num] += 1  # 해당 수의 등장 횟수 카운트

for i in range(10001):
    for _ in range(arr[i]): # 해당 수가 등장한 만큼 반복
        print(i)