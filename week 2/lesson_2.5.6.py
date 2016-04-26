import operator as op

# op.itemgetter
# op.attrgetter

# import operator as op
# from functools import partial
#
# x = [
#   ("Guido", "van", "Rossum"),
#   ("Haskell", "Curry"),
#   ("John", "Backus")
#   ]
#
# sort_by_last = partial(list.sort, key=op.itemgetter(-1))
# print(x)
# sort_by_last(x)
# print(x)
#
#
# n, k = map(int, input().split())
# print(n+k)

def mod_checker(x, mod=0):
  chk = lambda y: y % x == mod
  return chk

mod_3 = mod_checker(3)

print(mod_3(3)) # True
print(mod_3(4)) # False

mod_3_1 = mod_checker(3, 1)
print(mod_3_1(4)) # True