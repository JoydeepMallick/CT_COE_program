
n = int(input())
s = set(map(int, input().split()))

N = int(input())
for i in range(N):
    command = input().split()
    #print(command)
    if command[0] == 'pop':
        try:
            s.pop()
        except KeyError:
            pass
    elif command[0] == 'remove':
        try:
            s.remove(int(command[1]))
        except KeyError:
            pass
    else:
        s.discard(int(command[1]))

print(sum(s))
