def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        u = ""
        for ele in string[i:i+k]:
            if ele not in u:
                u += ele 
        print(u)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)