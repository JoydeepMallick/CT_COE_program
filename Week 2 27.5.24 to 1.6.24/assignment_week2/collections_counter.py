from collections import Counter

x = int(input())
shop_sizes = map(int, input().split())
shop_sizes = Counter(shop_sizes)

n = int(input())
amt = 0
while(n > 0):
    size, x =  map(int, input().split())
    if(shop_sizes[size] > 0):
        shop_sizes[size]-=1
        amt += x
    n -= 1
print(amt)
