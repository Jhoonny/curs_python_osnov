def closest_mod_5(x):

  while 1:

    if x % 5 == 0:
      break
    else:
      x += 1

  return x

print(closest_mod_5(5))