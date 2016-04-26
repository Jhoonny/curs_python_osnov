
class NonPositiveError(Exception):
  pass


class PositiveList(list):

  def append(self, x):

    if x <= 0:
      raise NonPositiveError
    else:
      super(PositiveList, self).append(x)



l = PositiveList()
l.append(5)
l.append(-1)
l.append(0)
l.append(10)
l.append(-10)
l.append(2)
print(l)

l2 = list()
l2.append(5)
l2.append(-1)
l2.append(0)
l2.append(10)
l2.append(-10)
l2.append(2)
print(l2)



