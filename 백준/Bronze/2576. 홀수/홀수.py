lst = []
for i in range(7):
    a = int(input())
    if a % 2 == 1:
        lst.append(a)
if lst == []:
    print(-1)
else:
    print(sum(lst))
    print(min(lst))