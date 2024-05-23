# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

n = int(input())
lst = input().split()
k = int(input())

nCk = len(list(combinations(lst, k)))
lst_withouta = [ele for ele in lst if ele != 'a']
combwitha = nCk - len(list(combinations(lst_withouta, k)))
ans = combwitha/nCk

print(f"{ans:.4f}")
