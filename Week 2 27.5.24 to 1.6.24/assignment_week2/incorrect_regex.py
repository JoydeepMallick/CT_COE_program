import re
for _ in range(int(input())):
    s = input()
    try:
        re.compile(r'{}'.format(s))
        print(True)
    except re.error:
        print(False)
