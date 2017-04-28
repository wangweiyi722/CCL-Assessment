

maxim = 0
trace = []
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

# Gets the total profit made off of this particular list of companies
def getProfit(compList):
    profit = 0
    for comp in compList:
        profit += comp.price
    return profit

# Finds the profit made by selling to a particular list of companies
def findProfit(compList):
    profit = 0
    for comp in compList:
        profit += comp.price
    return profit
    
# mergeSort algorithm for putting the items of the list in order by price/unit
def mergeSort(alist):
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]
        
        mergeSort(lefthalf)
        mergeSort(righthalf)
        
        i = 0
        j = 0
        k = 0
        
        while i<len(lefthalf) and j<len(righthalf):
            
            # Sort the companies based on the price per unit sold
            if lefthalf[i].unitPrice < righthalf[j].unitPrice:
                alist[k] = lefthalf[i]
                i += 1
            else:
                alist[k] = righthalf[j]
                j += 1
            k += 1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i += 1
            k += 1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j += 1
            k += 1
# Should output a list of companies
def maxProfit(compList,tracker, availUnits):
    # Base case occurs when available units is less than the number of units
    # requested by the next company in the list
    global maxim
    global trace
    print("-----------------------------------------")
    print("Company List: ")
    for comp in compList:
        print(comp)
        
    print()
    print("Tracker: ")
    for comp in tracker:
        print(comp)
        
    print()
    print("availUnits")
    print(availUnits)
    print()
    print("-------------------------------------------")
    if len(compList)==0:
        print("Reached end")
        if findProfit(tracker) > maxim:
            maxim = findProfit(tracker)
            trace = tracker[:]
            print ("proposed solution: ")
            for item in trace:
                print (item)
    elif availUnits < compList[-1].amount:
        print("Skipping")
        maxProfit(compList[:-1],tracker,availUnits)
        
    else:
        
        tracker.append(compList[-1])
        
        print("Going into max profit1")
        maxProfit(compList[:-1],tracker, availUnits-tracker[-1].amount)
        print("Going into max profit2")
        del tracker[-1]
        maxProfit(compList[:-1],tracker, availUnits)
        



# Returns the highest amount in the remaining company list
def compMaxAmt(compList):
    max = 0
    for comp in compList:
        if comp.amount > max:
            max = comp.amount
    
    return max

def main():
    in_file = open('counterexample.csv','r')
    header = in_file.readline()
    print(header)
    companyList = []
    for line in in_file:
        values = line.rstrip().split(sep = ',')
        tempCompany = Company(values[0], int(values[1]), int(values[2]))
        companyList.append(tempCompany)
    
    mergeSort(companyList)
    
    availUnits = int(input("Enter the number of units available for sale: "))
    idx = len(companyList)-1
    
    # tracker keeps track of the companies that should be bought from
    tracker = []
    
    # Simply choose the companies with the highest price/unit as long as this is true
    # Hopefully doing this will reduce the size of the problem fed into the recursive function
    # Worst case is that it won't change anything.
    unlSpend = True     
    
    while idx >= 0 and unlSpend and len(companyList) != 0:
        
        if companyList[idx].amount<=availUnits:
            
            temp = companyList[idx]
            del companyList[idx]
            
            if availUnits - temp.amount>=compMaxAmt(companyList):
                
                tracker.append(temp)
                availUnits -= temp.amount
                
            else:
                unlSpend = False
                companyList.append(temp)
            
            
            
        
        idx -= 1
    
    print("1")
    for comp in tracker:
        print (comp)
        
    print()        
    print("2")
    for comp in companyList:
        print(comp)
    
    print()
    print("3")
    
    maxProfit(companyList,tracker,availUnits)
    print("maxim: "+str(maxim))
    print()
    print("Companies to sell to:")
    for item in trace:
        print(item)

    
main()