T = int(input())
for t in range(1, T+1):
    n = int(input())
    print("#{}{}".format(t, (" 1/"+str(n))*n))