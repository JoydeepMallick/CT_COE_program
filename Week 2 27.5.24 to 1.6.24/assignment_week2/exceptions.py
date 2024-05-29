t= int(input())

while(t > 0):
    a, b =  input().split()
    try:
        print(int(a)//int(b))
    except ValueError as e:
        print("Error Code:", e)
    except ZeroDivisionError as e:
        print("Error Code:", e)
    t-=1
