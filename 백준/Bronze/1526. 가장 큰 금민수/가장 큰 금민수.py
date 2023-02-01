n = int(input())
cnt = 0

for i in range(4,int(n)+1):
    s = str(i)
    a = s.count('4')+s.count('7')
    if a == len(s):
        cnt = i 

print(cnt)