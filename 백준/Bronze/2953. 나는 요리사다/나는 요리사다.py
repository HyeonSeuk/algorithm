lst = []
for i in range(5):
    a = list(map(int, input().split()))
    lst.append(sum(a))
rank = lst.index(max(lst))+1
score = max(lst)
print(f'{rank} {score}')