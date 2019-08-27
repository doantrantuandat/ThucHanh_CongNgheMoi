import numpy as np
def doc():
    print("Doan Tran Tuan Dat - 16035741 - DHKHMT12A")
def main():
    x = np.int(input('What is your favorite number?'))
    c = 0
    for i in range(1, x + 1):
        if x % i == 0:
            c = c + 1
    if c > 2:
        print(x, "has", c, "factors")
        print(x, "is not prime")
    else:
        print(x, "has", c, "factors")
        print(x, "is prime")
if __name__ == '__main__':
    main()

    