

def create(namespace, parent):
  global space
  if namespace not in space:
    space[namespace] = {}
    space[namespace]['parent'] = parent
    space[namespace]['name'] = namespace
    space[namespace]['var'] = []
  else:
    space[namespace]['parent'] = parent


def add(namespace, var):
  global space
  if namespace not in space:
    space[namespace] = {}
    space[namespace]['name'] = namespace
    space[namespace]['var'] = [var]
  else:
    space[namespace]['var'].append(var)

def get (namespace, var):
  global space
  if namespace in space:
    if var in space[namespace]['var']:
      # print('1 ',str(space[namespace]['name']))
      return str(space[namespace]['name'])
    else:
      # new_name = space[namespace]['parent']
      new_name = space[namespace].get('parent', None)
      if new_name and new_name in space:
        name = get(new_name, var)
        # print('2 ',name)
        return name
      else:
        return None
  else:
    return None


space = {}

n = int(input())
if n > 100 or n < 1:
  exit(1)

for i in range(n):
  fun, sp, var = input().lower().split(' ')

  if fun == "create":
    create(sp, var)
  elif fun == "add":
    add(sp, var)
  elif fun == "get":
    print(get(sp, var))
  else:
    print("Unknow function")

  # print(space)
