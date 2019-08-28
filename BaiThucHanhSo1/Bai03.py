def showName():
    print("Nguyen Vu Khanh Huy - 16025591 - DHKHMT12A")
    print("_____________________________________________")
def main():
    showName()
    num = int(input('What is your favorite number?'))
    inc =0
    for i in range(1, num + 1):
        if num % i == 0:
            inc = inc + 1
    if inc > 2:
        print(num, "has", inc, "factors")
        print(num, "is not prime")
    else:
        print(num, "has", inc, "factors")
        print(num, "is prime")
if __name__ == '__main__':
    main()

    