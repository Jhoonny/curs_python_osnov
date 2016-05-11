import re
import sys

for line in sys.stdin:
    line = line.rstrip()
    # process line
    pat = r"human"
    rez = re.sub(pat, "computer", line)
    print(rez)

