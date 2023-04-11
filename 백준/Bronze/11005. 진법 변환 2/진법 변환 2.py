a, b = map(int, input().split())
alpha = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
result = ''
while a > 0:
    result = alpha[a % b] + result
    a //= b
print(result)