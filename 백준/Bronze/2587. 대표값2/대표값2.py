lst = []
for i in range(5):
    a = int(input())
    lst.append(a)
lst.sort()
print(int(sum(lst)//len(lst)))
print(lst[2])