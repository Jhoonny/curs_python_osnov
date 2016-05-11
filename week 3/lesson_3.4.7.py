import requests
import re

# texts = [
#   '<a href = "http://stepic.org/courses" >',
#   '<a href = "https://stepic.org" >',
#   '<a href = "http://neerc.ifmo.ru:1345" >',
#   '<a href = "ftp://mail.ru/distib" >',
#   '<a href = "ya.ru" >',
#   '<a href = "www.ya.ru" >',
#   '<a href = "../skip_relative_links" >',
#   '<link rel = "alternate" href = "http://static.feed.rbc.ru/rbc/internal/rss.rbc.ru/rbc.ru/mainnews.rss" >',
#   '<a class = "hello" href = "http://a.b.vc.ttepic.org/courses">'
# ]

# rezultatul
ras = []

# cerem pagina
link = input().strip()
req = requests.get(link)
text = req.text

# # link = "﻿http://pastebin.com/raw/hLx3HeZV\n"
# # link = "https://stepic.org/media/attachments/lesson/24472/sample0.html"
# # link = 'http://pastebin.com/raw/2mie4QYa﻿\n'

# print(req.status_code)
# print(text)

# for text in texts:
#     print(row)
# pat = r'href=".+?[/]{2}(.+?)[/].+"'

# pat = r'([https?|ftp]:\/\/)?([\da-z\.-]+\.[a-z\.]{2,6})([\/\w \.-]*)*\/?'

# pat = r'([https?|ftp]:\/\/)?([\da-z\.-]+\.[a-z\.]{2,6})([\/\w \.-]*)*\/?'
# pat = r'([https?|ftp]:\/\/)?([\a-z\.-]+\.[a-z\.]{2,6})([\/\w \.-]*)*\/?'
# pat = r'(<a href=)[.]?([https?|ftp]:\/\/)?([\da-z\.-]+\.[a-z\.]{2,6})([\/\w \.-]*)*\/?'
# pat = r'(?:<a .* href ?= ?)(?:\"|\')(?:http://|https://|ftp://|)([-_\.\w]*)'

# pat = r'(?:<a .* href ?= ?)(?:\"|\')(?:[\w]+://)*([-_\.\w]*)'
pat = r'href ?= ?"(?:\"|\')(?:[\w]+://)([\da-z\.-]+\.[a-z\.]{2,6})([\/\w \.-]*)*\/"'

rez = re.findall(pat, text)
print(rez)
# rez = re.match(pat, text)

# formam raspunsul
for r in rez:
  # print(r[1])
  ras.append(r[1])  # sortam raspunsul
ras = sorted(list(set(ras)))
for r in ras:
  print(r)
