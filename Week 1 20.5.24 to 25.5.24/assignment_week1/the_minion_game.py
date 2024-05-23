def minion_game(string):
    vowels = ['A', 'E', 'I', 'O', 'U']
    kevin , stuart, n = 0, 0, len(string)
    for i in range(0,n) :
        if string[i] in vowels:
            kevin+= (n - i)
        else:
            stuart += (n-i)
    if(kevin == stuart):
        print("Draw")
    elif(kevin > stuart):
         print("Kevin", kevin)
    else:
         print("Stuart", stuart)
    
if __name__ == '__main__':
    s = input()
    minion_game(s)