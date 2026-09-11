import string

def print_rangoli(size):
    alpha = string.ascii_lowercase
    
    for i in range(size-1, -size, -1):
        row = "-".join(alpha[size-1:abs(i):-1] + alpha[abs(i):size])
        print(row.center(4*size-3, "-"))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
