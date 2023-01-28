numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

lst =[]
for i in range(28):
    lst.append(int(input()))
    lst.sort()
set1 = set(numbers)
set2 = set(lst)
x = (set1 - set2)
print(min(x))
print(max(x))