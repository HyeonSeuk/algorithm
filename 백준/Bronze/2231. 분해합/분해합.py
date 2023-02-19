a = int(input())

for i in range(1, a+1):
    b = sum(map(int, str(i)))
    b_sum = i + b
    
    if a == b_sum:
        print(i)
        break
    if i == a:
        print(0)