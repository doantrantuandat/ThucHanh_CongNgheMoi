import numpy as np
import pandas as pd
def doc():
    print("Doan Tran Tuan Dat - 16035741 - DHKHMT12A")
def main():
    doc()
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
    