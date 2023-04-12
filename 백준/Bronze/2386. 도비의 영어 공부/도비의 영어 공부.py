while True :
  a = input()
  if a == '#' :
    break
  n = a[0]
  lst = a[2::]
  cnt = lst.count(n) + lst.count(n.upper())
  print(n, cnt)