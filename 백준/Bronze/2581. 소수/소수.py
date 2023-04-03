a = int(input())
b = int(input())
lst = []
for i in range(a, b+1):
    lst.append(i)

new_lst = []
for j in lst:
    if j in [2, 3, 5, 7]:
        new_lst.append(j)
    elif j > 1 and all(j % i != 0 for i in range(2, int(j**0.5)+1)):
        new_lst.append(j)

if not new_lst:
    print(-1)
else:
    print(sum(new_lst))
    print(min(new_lst))