import requests, re


def one_per(a, b):
  resA = requests.get(a)
  textA = resA.text
  pat = r'href="(.+?)"'
  rez = re.findall(pat, textA)
  # print(rez)

  for c in rez:
    if c == b:
      return 1

  return 0


# A = "https://stepic.org/media/attachments/lesson/24472/sample0.html"
# B = "https://stepic.org/media/attachments/lesson/24472/sample1.html"
A = input()
B = input()
resA = requests.get(A)
# resB = requests.get(b)
textA = resA.text
# print(textA)

pat = r'href="(.+?)"'
rez = re.findall(pat, textA)
# print(rez)
raspuns = "No"

for c in rez:
  if one_per(A, c) == 1 and one_per(c, B) == 1:
    raspuns = "Yes"
    break

print(raspuns)

# res = requests.get("https://yandex.ru/search/",
#                    params={
#                      "text": "Stepic",
#                      "test": "test1",
#                      "name": "name with space",
#                      "list": ["test1", "test2"]
#                    })
# print(res.status_code)
# print(res.headers)
# print(res.url)
