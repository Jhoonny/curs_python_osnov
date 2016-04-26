# import datetime
from datetime import date, timedelta

a, l, z = input().strip().split(' ')
days = int(input().strip())
days = timedelta(days=days)
a, l, z = int(a), int(l), int(z)

try:
    date(a,l,z)
except ValueError as e:
  print(e)
else:
  d = date(a,l,z)
  rez = d + days
  print(rez.strftime("%Y %-m %-d"))
