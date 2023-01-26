stack = []

for t in range(int(input())):
    a = int(input())
    
    if a == 0:
        stack.pop()
    else:
        stack.append(a)
print(sum(stack))