
in_file = "dataset_24465_4.txt"
# in_file = "in.txt"
out_file = "out.txt"
tab = []
with open(in_file, "r") as inf, open(out_file, "w") as outf:
  for line in inf:
    l = line.strip()
    tab.append(l)

  tab.reverse()
  print(tab)

  for line in tab:
    line = line + "\n"
    outf.writelines(line)


