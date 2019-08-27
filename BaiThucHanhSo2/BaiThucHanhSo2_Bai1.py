import numpy as np
import math as mt
def doc():
    print("Doan Tran Tuan Dat - 16035741 - DHKHMT12A")
def main():
    doc()
    sum = 0
    arr = []
    x = input('Credit Carad Number need to check: ')
    for i in range(0,len(x)):
        arr.append(int(x[i]))
    for i in range(0,len(x)):
        if i % 2 == 0:
            tam = int(arr[i]) * 2
            if tam >= 10:
                #print(tam)
                sum = sum + ((tam % 10) + int(tam / 10))
            else:
                sum = sum + tam
        else:
            sum = sum + int(arr[i])
    if sum % 10 == 0:
        print(sum, "is divisible by 10, therefore this card number is valid.")
    else:
        print(sum, "is not divisible by 10, therefore this card number is invalid.")
if __name__ == '__main__':
    main()
    