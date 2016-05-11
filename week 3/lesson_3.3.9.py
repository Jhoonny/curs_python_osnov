import re
import sys

for line in sys.stdin:
    line = line.rstrip()
    # process line
    pat = r"z[a-zA-Z]{3}z"
    rez = re.findall(pat, line)
    if rez:
      print(line)