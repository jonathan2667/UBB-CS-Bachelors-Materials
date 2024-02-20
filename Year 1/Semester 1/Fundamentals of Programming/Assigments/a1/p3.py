from math import sqrt

def is_prime(x):
    if x == 2:
        return 1
    if x % 2 == 0:
        return 0
    if x == 1 or x == 0:
        return 0
    for i in range(3, int(sqrt(x)) + 1):
        if x % i == 0:
            return 0
    return 1

def algo(n, numero):
    d = 2
    while n > 1:
        if n % d == 0:
            while n % d == 0:
                n /= d
            for i in range(0, int(d)):
                print(int(d), end =" ")
        d = d + 1
        if n > 1 and d * d > n:
            d = n

def print_number():
    num = 2

    for i in range(1, 15):
        print("")
        if is_prime(i):
            print(i, end=" ")
            num = num - 1

        elif i == 1:
            print(i, end= " ")
            num = num - 1
        else :
            algo(i, num)

if __name__ == '__main__':
    print_number()
