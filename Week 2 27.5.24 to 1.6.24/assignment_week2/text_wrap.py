import textwrap

def wrap(string, max_width):
    wrappedstring = ""
    for i in range(len(string)):
        if(i>0 and i%max_width == 0):
            wrappedstring += "\n" + string[i]
        else:
            wrappedstring += string[i]
    return wrappedstring

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)