def average(array):
    st = set(array)
    avg = sum(st)/len(st)
    avg_for = f"{avg :.3f}"
    #print(avg_for)
    return avg_for

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)