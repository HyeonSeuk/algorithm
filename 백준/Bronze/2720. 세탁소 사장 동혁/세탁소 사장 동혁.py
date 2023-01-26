money = [25, 10, 5, 1]
for t in range(int(input())):
    person = int(input())
    lst = []
    for i in money:
        lst.append(person // i)
        person = person % i
    print(*lst)