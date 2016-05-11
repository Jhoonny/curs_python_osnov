s = input()
t = input()

# s = "abababa"
# t = "aba"
# s = "aaaaa"
# t = "a"
i = 0
p = 0
for p in range(len(s)):
  f = s.find(t, p, p+len(t))
  if f != -1:
    i += 1

print(i)
