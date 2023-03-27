
def isDigit(string):
    temp = True
    for i in string:
        if i.isdigit():
            continue
        else:
            temp = False
            return temp
    return temp

def calculateCreditModifier(ID):
   if (ID % 4 == 0):
      creditModifier = "debt"
   elif (ID % 3 == 0):
      creditModifier = 100
   elif (ID % 5 == 0):
      creditModifier = 300
   else:
      creditModifier = 1000
   return creditModifier
    
def BestDeal(creditModifier, loanAmount, loanPeriod):
    if creditModifier == "debt":
        return -1, -1
    minLoanAmount = 2000
    maxLoanAmount = 10000
    minLoanPeriod = 12
    maxLoanPeriod = 60
    amountDifference = 5
    periodDifference = 1
    creditScore = (creditModifier * loanPeriod) / loanAmount
    while creditScore < 1:
        while loanAmount > minLoanAmount:
            loanAmount -= amountDifference
            creditScore = (creditModifier * loanPeriod) / loanAmount
            if creditScore >= 1:
                return loanAmount, loanPeriod
        loanAmount += amountDifference
        while loanPeriod < maxLoanPeriod:
            loanPeriod += periodDifference
            creditScore = (creditModifier * loanPeriod) / loanAmount
            if creditScore >= 1:
                return loanAmount, loanPeriod
        return 0,0
    while creditScore >= 1:
        while loanAmount <= maxLoanAmount:
            loanAmount += amountDifference
            creditScore = (creditModifier * loanPeriod) / loanAmount
            if creditScore < 1:
                loanAmount -= amountDifference
                return loanAmount, loanPeriod
            if loanAmount > maxLoanAmount:
                loanAmount -= amountDifference
                return loanAmount, loanPeriod
        while loanPeriod >= minLoanPeriod:
            loanPeriod -= periodDifference
            creditScore = (creditModifier * loanPeriod) / loanAmount
            if creditScore < 1 or loanPeriod <  minLoanPeriod:
                loanPeriod += periodDifference
                return loanAmount, loanPeriod
        return 0,0