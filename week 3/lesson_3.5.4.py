import json
data = json.loads(input())
# val = r'[{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]'
# data = json.loads(val)
# print(data)

dic = {}
for k in data:
  dic[k['name']] = k['parents']

# print(dic)
# # de reinoit dic
for i in range(len(dic)//2):
  for k in dic:
    temp = []
    for v in dic[k]:
      if (v in dic):
        for x in dic[v]:
          if x not in dic[k]:
            dic[k].append(x)

# print(dic)
# dic now
ras = {}
for k in dic:
  ras[k] = 1

for k in dic:
  for v in dic:
    if k in dic[v]:
      ras[k] += 1
R = []
for k in ras:
  s = str(k) + ' : ' + str(ras[k])
  R.append(s)
R = sorted(R)
for r in R:
  print(r)


# stud1 = {
#   'first_name': 'Greg',
#   'last_name': 'Dan',
#   'score': [70,80,90],
#   'description': 'Good job',
#   'certificate': True
# }
# stud2 = {
#   'first_name': 'Alo',
#   'last_name': 'Man',
#   'score': [70,50,90],
#   'description': 'Good job',
#   'certificate': True
# }
#
# data = [stud1, stud2]
# res = json.dumps(data,indent=4, sort_keys=True)
# print(res)
#
# # with open("students.json", "w") as f:
# #   json.dump(data, f, indent=4, sort_keys=True)