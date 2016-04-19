class ExtendedStack(list):

  # операция сложения
  def sum(self):
    # if len(self) > 2:
      self.append(self.pop() + self.pop())

  # операция вычитания
  def sub(self):
    # if len(self) > 2:
      self.append(self.pop() - self.pop())

  # операция умножения
  def mul(self):
    # if len(self) > 2:
      self.append(self.pop() * self.pop())

  # операция целочисленного деления
  def div(self):
    # if len(self) > 2:
      self.append(self.pop() // self.pop())



### TEST ###

s = ExtendedStack()

for i in range(10):
  s.append(1)

print(s)

s.sum()
print(s)
s.sub()
print(s)
s.mul()
print(s)
s.div()
print(s)


def test():
  ex_stack = ExtendedStack([1, 2, 3, 4, -3, 3, 5, 10])
  ex_stack.div()
  assert ex_stack.pop() == 2
  ex_stack.sub()
  assert ex_stack.pop() == 6
  ex_stack.sum()
  assert ex_stack.pop() == 7
  ex_stack.mul()
  assert ex_stack.pop() == 2
  assert len(ex_stack) == 0

test()