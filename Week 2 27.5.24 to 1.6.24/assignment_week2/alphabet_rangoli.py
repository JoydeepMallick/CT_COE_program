def print_rangoli(size):
    rows = 2*size -1
    cols = 2*(rows)-1
    start = 97 + size - 1
    for i in range(rows):
        if(i < size):
            mid = start - i
        else:
            mid = start - (rows - i - 1)
        left = "".join([chr(c) for c  in range(start, mid-1, -1)]) 
        right = left[::-1][1:]
        #print(left, right)
        s = "-".join(left + right)
        
        s = s.center(cols, "-")
        print(s)
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)