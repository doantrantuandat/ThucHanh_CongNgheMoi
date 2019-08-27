import numpy as np
import math as mt
def doc():
    print("Doan Tran Tuan Dat - 16035741 - DHKHMT12A")
def main():
    print("\n")
    doc()
    file = open("hour.txt")
    for line in file:
        name, id, mon, tue, wed, thu, fri = line.split()
        h = float(mon) + float(tue) + float(wed) + float(thu) + float(fri)
        print("Name: %s, ID: %s, worked: %.1f hours (%.1f h/day)" % (id,name,h,h/5))

if __name__ == '__main__':
    main()
    