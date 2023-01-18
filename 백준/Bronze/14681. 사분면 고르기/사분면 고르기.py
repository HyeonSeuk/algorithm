a = int(input())
b = int(input())

if a >= 1 and b >= 1:
    print(1)
elif a <= -1 and b >= 1 :
    print(2)
elif a <= -1 and b <= -1:
    print(3)
elif a >= 1 and b <= -1:
    print(4)