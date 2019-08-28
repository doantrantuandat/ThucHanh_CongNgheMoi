import numpy as np
import pandas as pd
def showName():
    print("Nguyen Vu Khanh Huy - 16025591 - DHKHMT12A")
    print("_____________________________________________")
def main():
    showName()
    pay = float(input('How much do you want to pay for each textbook?'))
    cost = float(input('How much did the average textbook actually cost?'))
    number = float(input('How many books did you buy?'))
    overpriced = cost - pay
    ratio = (overpriced/pay) * 100
    ripped = number * overpriced
    print("Each book is overpriced by" , overpriced ,"$", "(", round(ratio),"%", ")")
    print("You got ripped off by $", ripped, "total")
if __name__ == "__main__":
    main()
    