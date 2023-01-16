n = 0
for i in range(5):
    numbers = int(input())
    if numbers < 40:
        numbers = 40
    n += numbers
print(n//5)