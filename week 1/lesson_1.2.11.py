

objects = [1,2,3,True, [12], "as", 2,3,1]

### in test
ans = 0
a = []

for obj in objects:
  if id(obj) not in a:
    a.append(id(obj))

print(len(a))

