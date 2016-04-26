import os.path
import shutil

print(os.getcwd())
# print(os.listdir())
# print(os.path.exists("in.txt"))
# print(os.path.abspath("in.txt"))
# print(os.path.exists("in2.txt"))

res = []
for home, dirs, files in os.walk("main"):
  # for dir in dirs:
  #   for file in files:
  #     if file.endswith(".py"):
  #       r = os.path.join(home, dir)
  #       if r not in res:
  #         res.append(r)
  for file in files:
    if file.endswith(".py"):
      r = str(home)
      if r not in res:
        res.append(r)

res.sort()
# print(res)

out_file = "out_les_2.4.6.txt"
with open(out_file, "w") as f:
  for line in res:
    # line.replace('\\', '/')
    l = line + "\n"
    f.writelines(l)
