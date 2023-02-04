a, b, c = map(int, input().split())
if b >= c:   # 가변비용이 수입보다 많아지면 손익분기점이 존재하지 않게 된다.
    print(-1)
else:
    print(a//(c-b)+1)