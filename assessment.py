# Make a company class to take in name,amount and price
class Company:
    
    def __init__(self, name, amount,price):
        self.name = name
        self.amount = amount
        self.price = price
        self.unitPrice = price/amount

    # Mainly for debugging purposes
    def __str__(self):
        
        return ("Name: " + self.name + ", " + "Units: " + str(self.amount) + ", " + "Price: " + str(self.price))



def main():
    in_file = open('pricedata.csv','r')
    header = in_file.readline()
    print(header)
    companyList = []
    for line in in_file:
        values = line.rstrip().split(sep = ',')
        tempCompany = Company(values[0], int(values[1]), int(values[2]))
        companyList.append(tempCompany)


    
main()