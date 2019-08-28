def showName():
    print("Nguyen Vu Khanh Huy - 16025591 - DHKHMT12A")
    print("_____________________________________________")
def total_payment(loan,n,c):
    payment = loan * ((c * mt.pow((1 + c),n)) / (mt.pow((1 + c),n) - 1))
    return payment
def main():
    showName()
    print("This program computes monthly loan payments.")
    
    loan = np.int(input('Loan amount?'))
    number_of_year = np.int(input('Number of years?'))
    interrest_rate = np.float(input('Interest rate?'))

    number_rent = number_of_year * 12
    interrest_calculate = (interrest_rate / 12.0) / 100.0
    print("Your payment is $", round(total_payment(loan, number_rent, interrest_calculate),2))

if __name__ == '__main__':
    main()
    