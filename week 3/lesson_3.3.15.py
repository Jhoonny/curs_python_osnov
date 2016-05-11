import re
import sys

for line in sys.stdin:
    line = line.rstrip()
    # process line
    pat = r"(\w)(\1+)"
    # print(re.findall(pat, line))

    rez = re.sub(pat, r"\0\1", line)
    # rez = re.sub(pat, r"\0\1", line, flags=re.IGNORECASE)
    correct_rez = re.sub(r'[^\x20-\x7e]', '', rez)
    print(correct_rez)
