#pb 2

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#14, 10, 2
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


def print_number():
    num = int(input("Number?"))

    if (num % 2 == 1) :
        print("impossible ")
    else:
        for i in range (1, num):
            if is_prime(i) and is_prime(num-i):
                print(str(i) + " --- " + str(num-i))
                break


if __name__ == '__main__':
    print_number();


#mogovan jonathan
