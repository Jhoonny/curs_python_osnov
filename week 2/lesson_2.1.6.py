#  Verificare claselor mostenite la errori
#  vers 0.0.1

n = int(input())  # numarul de clase
d = {}

for i in range(n):
  ask = input().split(' ')
  if ask[0] not in d:
    d[ask[0]] = []
  if len(ask) > 1:
    for s in ask[2:]:
      if s not in d:
        d[s] = []
      if d[ask[0]] != s and s not in d[ask[0]]:
        d[ask[0]].append(s)
# print(d)

# # de reinoit dic
for i in range(len(d)//2):
  for k in d:
    temp = []
    for v in d[k]:
      if (v in d):
        for x in d[v]:
          if x not in d[k]:
            d[k].append(x)

# print(d)

m = int(input())
res = []
for i in range(m):
  zap = input()
  res.append(zap)

for i in range(1, len(res)):
  for j in range(i):
    if res[i] in d:
      if res[j] in d[res[i]]:
        print(res[i])
        break

