import re
import sys

for line in sys.stdin:
    line = line.rstrip()
    # process line
    pat = r"\\"
    rez = re.findall(pat, line)
    if rez:
      print(line)