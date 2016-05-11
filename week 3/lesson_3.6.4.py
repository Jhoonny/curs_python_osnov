import requests
import json
import re

client_id = 'abe925a5848fc53113e5'
client_secret = '96ca7298fabe759a0adf34b886f3f2b5'

# инициируем запрос на получение токена
r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })

# разбираем ответ сервера
j = json.loads(r.text)
# достаем токен
token = j["token"]

# создаем заголовок, содержащий наш токен
headers = {"X-Xapp-Token": token}


fin = 'dataset_24476_4.txt'
fou = 'lesson_3.6.4.txt'
tab = []
with open(fin, 'r') as f:
  for row in f:
    data = row.strip()
    # data = '4d8b92b34eb68a1b2c0003f4'
    # инициируем запрос с заголовком
    api_ulr = "https://api.artsy.net/api/artists/"
    auth = data
    api_ulr += data
    r = requests.get(api_ulr, headers=headers)
    # разбираем ответ сервера
    j = json.loads(r.text)

    # print(j['sortable_name'],'-',j['birthday'])
    str = '' + j['birthday'] + ' ' + j['sortable_name']
    tab.append(str)
print(sorted(tab))
pat = r'\d{4} '
ras = []
for t in sorted(tab):
  r = re.sub(pat, "", t)
  ras.append(r)
# print(ras)

with open(fou, "w", encoding="UTF-8") as out:
  for r in ras:
   out.write(r+"\n")