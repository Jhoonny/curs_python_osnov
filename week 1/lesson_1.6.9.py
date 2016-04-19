import time

class Loggable:
  def log(self, msg):
    print(str(time.ctime()) + ": " + str(msg))


#######  paste in test ###

class LoggableList(list, Loggable):

  def append(self, obj):
    super(LoggableList, self).append(obj)
    self.log(obj)

### ---------------

def test():
  l = LoggableList([1,2,3,4])
  print(l)
  l.append(5)
  print(l)

test()