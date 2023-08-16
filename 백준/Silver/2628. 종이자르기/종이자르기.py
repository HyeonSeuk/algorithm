n, m = map(int, input().split())

x = [0, n]  
y = [0, m]

for _ in range(int(input())):
    t, a = map(int, input().split())
    if t == 0:  # 가로 점선
        y.append(a)
    elif t == 1:  # 세로 점선
        x.append(a)

x.sort()
y.sort()

# 최대 간격을 저장
max_x = max_y = 0

# x 리스트를 순회하며 가장 긴 간격을 찾는다.
for i in range(len(x)-1):
    if max_x < x[i+1]-x[i]:
        max_x = x[i+1]-x[i]

# y 리스트를 순회하며 가장 긴 간격을 찾는다.
for i in range(len(y)-1):
    if max_y < y[i+1]-y[i]:
        max_y = y[i+1]-y[i]

print(max_x*max_y)