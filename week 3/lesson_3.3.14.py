import re
import sys

for line in sys.stdin:
    line = line.rstrip()
    # process line
    pat = r"\b(\w)(\w)(\w*)\b"
    # print(re.findall(pat, line))

    rez = re.sub(pat, r"\2\1\3", line)
    print(rez)
