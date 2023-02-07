n = int(input())
lst = []
for t in range(n):
    lst.append(list(map(int, input().split())))
    
for i in range(n):
    rank = 1 # 1등은 정해져 있으니 더하는 방식으로 가기 위해
    for j in range(n):
        if (lst[i][0] < lst[j][0]) and (lst[i][1] < lst[j][1]):
            rank += 1
    print(rank, end=' ')