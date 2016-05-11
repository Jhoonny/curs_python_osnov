import re
import sys

for line in sys.stdin:
    line = line.rstrip()
    # process line
    pat = r"\ba+\b"
    # print(re.findall(pat, line))
    rez = re.sub(pat, "argh", line, count=1, flags=re.IGNORECASE)
    print(rez)
