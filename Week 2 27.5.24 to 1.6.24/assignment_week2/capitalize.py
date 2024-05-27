#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    spaces = []
    for i in range(0, len(s)):
        if(s[i] == ' '):
            if(i == 0):
                 spaces.append(1)
            elif(i > 0 and s[i-1] == ' ' ):
                spaces[-1] += 1
            else:
                spaces.append(1)
    space_at_ind0 = False
    if(s[0] == ' '):
         space_at_ind0 = True
                
    lst = s.split()
    lst = [name.capitalize() for name in lst]
    news = ""
    start = 0
    if space_at_ind0:
        news += " "*spaces[start]
        start += 1
    #print(space_at_ind0, start, spaces)
    for name in lst:
        news += name
        if(start  < len(spaces)):
            news += " "*spaces[start]
            start+=1
        
    return news

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
