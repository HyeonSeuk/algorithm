import sys
input = sys.stdin.readline
result = list()
n = int(input())
for _ in range(n):
    result.append(int(input()))
result.sort(reverse=True)

for i in result:
    print(i)