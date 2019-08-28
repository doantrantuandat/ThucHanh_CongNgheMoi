def showName():
    print("Nguyen Vu Khanh Huy - 16025591 - DHKHMT12A")
    print("_____________________________________________")
def main():
    showName()
    sum = 0
    arr = []
    x = input('Credit Card Number need to check: ')
    if(len(x)!=16):
        print("Length of credit card must equal 16")
    elif(x[0]!='4'):
        print(x[0])
        print("Credit card always begin with number 4")
    else:
        for i in range(0,len(x)):
            digit = int(x[i])
            if i % 2 == 0:
                digit = digit * 2
                if digit >= 10:
                    #print(tam)
                    sum = sum + (digit % 10) + (digit // 10)
                else:
                    sum = sum + digit
            else:
                sum = sum + digit
        if sum % 10 == 0:
            print(sum, "is divisible by 10, therefore this card number is valid.")
        else:
            print(sum, "is not divisible by 10, therefore this card number is invalid.")
if __name__ == '__main__':
    main()
    