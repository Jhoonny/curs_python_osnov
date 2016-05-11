import re
import sys

for line in sys.stdin:
    line = line.rstrip()
    # process line
    pat = r"cat"
    rez = re.findall(pat, line)
    if len(rez) > 1:
      print(line)


# re.match()
# re.search()
# re.findall()
# re.sub()
#
# """
# [] - multime
# * - mai multe
# {can} - cantitatea necesara
#
# \d
# \D
# \w
# \W
#
# + - povtor
# ? - nejadnii
#
# | - sau
# () - grupup fix
#
# \1 - grupa 1
#
# """
#
# pattern = r"a[\w.]c"
# string = "abc, a.c, aac, a-c, aBc, azc"
# all_inclusions = re.findall(pattern, string)
# print(all_inclusions)
#
# fixed_types = re.sub(pattern, "abc", string)
# print(fixed_types)
#
# p2 = r"a[ab]+?a"
# print(re.match(p2, string="abaaba"))
# print(re.findall(p2, string="abaaba"))
