import sys  # sys 모듈을 가져옵니다. (표준 입력을 위해 사용됩니다.)

# 체스판의 크기 n과 해답 수를 저장할 cnt를 초기화합니다.
n, cnt = int(sys.stdin.readline()), 0  

# a: 각 열에 퀸이 배치되었는지 확인합니다.
# b와 c: 대각선에 퀸이 배치되었는지 확인합니다.
# b는 / 모양의 대각선, c는 \ 모양의 대각선을 나타냅니다.
a, b, c = [False]*n, [False]*(2*n-1), [False]*(2*n-1)

# i번째 행에 대해 퀸의 위치를 결정하는 함수입니다.
def solve_dfs(i):  
    global cnt  # cnt는 전역 변수로서 함수 내에서 값을 변경할 수 있게 합니다.
    
    # 모든 행에 퀸이 배치되면 해답 수를 증가시킵니다.
    if i == n:  
        cnt += 1
        return
    
    # i번째 행의 각 열에 대해 퀸을 배치하는 것을 시도합니다.
    for j in range(n):
        # 현재 위치에 퀸을 배치할 수 있는지 체크합니다.
        if (not a[j] and not b[i+j] and not c[i-j+n-1]) :
            
            # 현재 위치에 퀸을 배치합니다.
            a[j] = b[i+j] = c[i-j+n-1] = True
            
            # 다음 행에 대해 퀸의 위치를 결정합니다.
            solve_dfs(i+1)
            
            # 백트래킹: 현재 위치의 퀸을 제거하고 다음 열에 퀸을 배치하는 것을 시도합니다.
            a[j] = b[i+j] = c[i-j+n-1] = False

# 첫 번째 행부터 시작하여 DFS를 실행합니다.
solve_dfs(0)

# 해답 수를 출력합니다.
print(cnt)