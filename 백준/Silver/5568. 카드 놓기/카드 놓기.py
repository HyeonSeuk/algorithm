import sys
from itertools import permutations
input = sys.stdin.readline

n = int(input())
k = int(input())

lst = []

for _ in range(n):
    card_num = input().strip()
    lst.append(card_num)
    
result = set()

for i in permutations(lst, k):
    result.add(''.join(i))
    
print(len(result))