import csv, re
from datetime import datetime, date

with open("Crimes.csv") as f:
  reader = csv.reader(f)
  stok = {}
  for row in reader:
    # if "Primary Type" in row:
    #   print(row)
    #
    pat = r"\d{4}"
    year = re.findall(pat, row[2])
    # print(year)
    for i in year:
      if int(i) == 2015:
        if row[5] in stok:
          stok[row[5]] += 1
        else:
          stok[row[5]] = 0
  print(stok)
  tab = []
  for k in stok:
    tab.append(stok[k])
  max = max(tab)
  print(tab)
  print(max)
  for k in stok:
    if stok[k] == max:
      print(k)
