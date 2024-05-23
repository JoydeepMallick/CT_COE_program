def print_formatted(number):
    width = len(bin(number)[2:])
    
    for n in range(1, number+1):
        oct_val = oct(n)[2:]
        hex_val = hex(n)[2:].upper()
        bin_val = bin(n)[2:]
        print(f'{n:>{width}} {oct_val:>{width}} {hex_val:>{width}} {bin_val:>{width}}')

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)