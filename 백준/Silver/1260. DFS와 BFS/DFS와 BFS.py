def dfs(start):
    g_dfs.append(start) # 방문 노드 추가
    visited[start] = 1 # 방문 표시
    
    for k in graph[start]:
        if not visited[k]: # 방문하지 않은 경우
               dfs(k) # 방문을 해라

def bfs(c):
    q = []  # 필요한 q, v[], 변수 생성 v[]의 경우 아래 생성 이미 했으므로 생략
    q.append(c) # Q에 초기 데이터(들) 삽입
    g_bfs.append(c) # c는 초기 데이터
    visited[c] = 1
    
    while q:
        c = q.pop(0)
        for l in graph[c]:
            if not visited[l]: # 방문하지 않은 경우 큐를 삽입
                q.append(l)
                g_bfs.append(l)
                visited[l] = 1

n, m, v = map(int, input().split()) # n : 정점, m: 간선 v: 시작
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a) # 양방향

# 오름차순 정렬
for i in range(1, n+1):
    graph[i].sort()

visited = [0] * (n+1)
g_dfs = []
dfs(v)

visited = [0] * (n+1)
g_bfs = []
bfs(v)

print(*g_dfs)
print(*g_bfs)