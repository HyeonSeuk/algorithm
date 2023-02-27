n,m = map(int, input().split())
nn = set()
mm = set()

for _ in range(n):
    word = input()
    nn.add(word)

for _ in range(m):
    word = input()
    mm.add(word)

result = sorted(list(nn & mm)) # 교집합

print(len(result), *result, sep= '\n') # 시간초과 방지를 위해 한줄로