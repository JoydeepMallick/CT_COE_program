from itertools import groupby
s = input()
for digit, group in groupby(s):
  print(f"({len(''.join(group))}, {digit})", end = " ")
