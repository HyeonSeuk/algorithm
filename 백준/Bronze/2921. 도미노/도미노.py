t = int(input())
cnt = 0
for n in range(1, t+1): # 1부터 t까지의 합을 구하기 위해서
    cnt += 1.5*n*(n+1) # 도미노 상단의 규칙은 2분의 n(n+1) 하단의 규칙은 n(n+1) 이므로 이 규칙을 합하면 1.5n(n+1)
print(int(cnt)) # cnt만 출력하면 ex 12.0 으로 나오므로 int로 변환해서 12 로 출력
