class MoneyBox:
  def __init__(self, capacity):
  # конструктор с аргументом – вместимость копилки
    self.money = 0
    self.capacity = capacity

  def can_add(self, v):
  # True, если можно добавить v монет, False иначе
    if self.money + v <= self.capacity:
      return True
    return False

  def add(self, v):
  # положить v монет в копилку
    if self.can_add(v):
      self.money += v

m = MoneyBox(10)
m.add(5)
print(m.money)
m.add(10)
print(m.money)
print(m.can_add(2))
print(m.can_add(10))
m.add(2)
print(m.money)

m2 = MoneyBox(100)
print(m2.money)
print(m2.capacity)
m2.add(100)
print(m2.money)
