n = int(input())
lst = []
for i in range(n):
    number = int(input())
    lst.append(number)

lst.sort()

for j in lst:
    print(j)