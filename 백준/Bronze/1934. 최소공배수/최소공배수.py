import math
for i in range(int(input())):
    a, b = map(int, input().split())
    lcm = (a * b) // math.gcd(a, b)
    print(lcm)