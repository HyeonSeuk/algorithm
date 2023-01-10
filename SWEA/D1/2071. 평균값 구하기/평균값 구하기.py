T = int(input())
for t in range(1, T+1):
    a = list(map(int, input().split()))
    average = round(sum(a)/10)
    print(f"#{t} {average}")