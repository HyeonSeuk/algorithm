# 1 먼저 약수 리스트를 만든다.
a = int(input())
lst = []
for i in range(2, a+1):
    if a % i == 0:
        lst.append(i)
# print(lst[0]%a) 2
# print(a//lst[0]) 36

while a != 1:
    for j in lst: # 리스트에 구했던 약수를 이용해서
        if a%j == 0:
            a = a//j # ex 36
            print(j) # 약수 값
            break   