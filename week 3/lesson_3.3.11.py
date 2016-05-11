import re
import sys

for line in sys.stdin:
    line = line.rstrip()
    # process line
    pat = r"\b(\w+)\1\b"
    rez = re.findall(pat, line)
    # print(rez)
    if rez:
      print(line)
