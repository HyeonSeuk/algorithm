n, m = map(int, input().split())

balls = list(range(1, n+1))

for i in range(m):
    a, b = map(int, input().split())
    balls[a-1], balls[b-1] = balls[b-1], balls[a-1]

print(*balls)