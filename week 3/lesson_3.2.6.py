
# s = input().strip()
# a = input().strip()
# b = input().strip()

s = "ababa"
a = "a"
b = "b"
i = 0
r = ""
while 1:
  if b.find(a) != -1 and s.find(a) != -1:
    r = "Impossible"

    break
  if s.find(a) != -1:
    s2 = s.replace(a, b)
    i += 1
    if s != s2:
      s = s2
    else:
      r = "Impossible"
      break
  else:
    break
if r:
  print(r)
else:
  print(i)
