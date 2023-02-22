n = int(input())
total = 1000 - n
coin = [500, 100, 50, 10, 5, 1]
cnt = 0
for i in coin:
    cnt += total//i
    total %= i
print(cnt)