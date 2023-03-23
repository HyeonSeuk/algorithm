n, k = map(int, input().split())
lst = []
cnt = 0 # 최소 동전 필요 개수
for i in range(n): 
    coin = int(input()) # 동전 종류들
    lst.append(coin) # 동전 종류들을 리스트에 더한다

for j in reversed(range(n)): # 동전의 종류 중 큰 값을 먼저 계산해야 최소 값이 나온다
    cnt += k//lst[j] # 돈과 동전의 종류의 계산 결과인 몫을 개수에 더한다
    k = k%lst[j] # 돈은 위에 계산 후 나머지 값으로 계속 이어간다.

print(cnt)