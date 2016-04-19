# Emulare mostenire clase
# version 0.2

n = int(input())  # numarul de clase

d = {}

for i in range(n):
  ask = input().lower().split(' ')
  if ask[0] not in d:
    d[ask[0]] = []
  if len(ask) > 1:
    for s in ask[2:]:
      if s not in d:
        d[s] = []
      if d[ask[0]] != s and s not in d[ask[0]]:
        d[ask[0]].append(s)
# print(d)

# de reinoit dic

for i in range(len(d)//2):
  for k in d:
    temp = []
    for v in d[k]:
      if (v in d):
        for x in d[v]:
          if x not in d[k]:
            d[k].append(x)

# for k in d:
#   print(k, " : ", d[k])

#  verificarea dic

q = int(input())  # numarul de cereri
# ras = []
for i in range(q):
  res = 0

  b, a = input().lower().split()
  if a == b:
    res = 1
  elif (a in d) and (b in d[a]):
    res = 1
  if res:
    # ras.append("Yes")
    print("Yes")
  else:
    # ras.append("No")
    print("No")

# for r in ras:
#   print(r)
# print "Yes" if class 1  < class 2 else "No"

