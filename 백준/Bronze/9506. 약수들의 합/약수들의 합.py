while True:
    num = int(input())
    lst = []
    if num == -1:
        break
    for i in range(1, num):
        if num % i == 0:
            lst.append(i)
        if lst[-1] == num:
            lst.pop()

    if sum(lst) == num:
        print(num, " = ", " + ".join(str(j) for j in lst), sep="")
    else:
        print(f'{num} is NOT perfect.')