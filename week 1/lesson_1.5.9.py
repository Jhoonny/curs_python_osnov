class Buffer:
  def __init__(self):
  # конструктор без аргументов
    self.bufer = []


  def add(self, *a):
  # добавить следующую часть последовательности
    fix = 5

    for val in a:
      self.bufer.append(val)

    lun = len(self.bufer) // fix
    self.bufer.reverse()
    if lun > 0:
      for j in range(lun):
        sum = 0
        count = 0
        for i in range(fix):
          i = self.bufer.pop()
          sum += i
        print(sum)
    self.bufer.reverse()

  def get_current_part(self):
  # вернуть сохраненные в текущий момент элементы последовательности в порядке, в котором они были
  # добавлены
    return self.bufer

buf = Buffer()
buf.add(1, 2, 3)
print(buf.get_current_part())
buf.add(4, 5, 6) # print(15) – вывод суммы первой пятерки элементов
print(buf.get_current_part()) # вернуть [6]
buf.add(7, 8, 9, 10) # print(40) – вывод суммы второй пятерки элементов
print(buf.get_current_part()) # вернуть []
buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1) # print(5), print(5) – вывод сумм третьей и четвертой пятерки
print(buf.get_current_part()) # вернуть [1]
