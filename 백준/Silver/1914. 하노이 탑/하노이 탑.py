def move(no: int, x: int, y: int) -> None:
    if no > 1:
        move(no - 1, x, 6 - x - y)
    if n <= 20:
        print(f'{x} {y}')
    if no > 1:
        move(no - 1, 6 - x - y, y)

n = int(input())
print(2**n - 1)
if n <= 20:
    move(n, 1, 3)