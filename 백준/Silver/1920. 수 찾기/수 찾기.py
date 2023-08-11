a = int(input())
lst = set(map(int, input().split())) #list --> O(n), set --> O(1) 시간 복잡도가 줄어든다?
b = int(input())
lit = list(map(int, input().split()))

for i in lit:
    if i in lst:
        print(1)
    else:
        print(0)
