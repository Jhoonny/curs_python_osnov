import itertools


def primes():
  i = 1
  while True:
    i += 1
    p = 0
    for k in range(2, i):
      if i % k != 0:
        p += 1
    p = p - i + 2

    if p == 0:
      yield i

# test

print(list(itertools.takewhile(lambda x : x <= 31, primes())))
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
