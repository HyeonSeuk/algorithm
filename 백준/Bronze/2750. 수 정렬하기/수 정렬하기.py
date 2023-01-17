n = int(input())
list = []
for i in range(n):
    number = int(input())
    list.append(number)
    list.sort()
for j in range(len(list)):
    print(list[j])