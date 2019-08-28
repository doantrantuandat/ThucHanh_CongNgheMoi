import numpy as np
import math as mt
def showName():
    print("Nguyen Vu Khanh Huy - 16025591 - DHKHMT12A")
    print("_____________________________________________")
def main():
    showName()
    print("\n")
    file = open("hour.txt")
    for line in file:
        name, id, mon, tue, wed, thu, fri = line.split()
        h = float(mon) + float(tue) + float(wed) + float(thu) + float(fri)
        print("Name: %s, ID: %s, worked: %.1f hours (%.1f h/day)" % (id,name,h,h/5))

if __name__ == '__main__':
    main()
    