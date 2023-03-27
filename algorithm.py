
# isDigit function checks if the string is a number
def isDigit(string):
    temp = True
    for i in string:
        if i.isdigit():
            continue
        else:
            temp = False
            return temp
    return temp

# calculateCreditModifier function calculates the credit modifier based on the ID
# The credit modifier is used to calculate the credit score, which is used to determine the best deal
# The function is hard coded as requested, since I don't have access to the external registries
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

# BestDeal function calculates the best deal based on the credit modifier, loan amount and loan period
def BestDeal(creditModifier, loanAmount, loanPeriod):
    # if the credit modifier is "debt", the user is not eligible for a loan because of debt
    if creditModifier == "debt":
        return -1, -1
    # defining some variables for cleaner code
    # amountDifference and periodDifference are used to increase/decrease the loan amount and loan period 
    # can be changed if needed to get a more/less accurate result
    minLoanAmount = 2000
    maxLoanAmount = 10000
    minLoanPeriod = 12
    maxLoanPeriod = 60
    amountDifference = 5
    periodDifference = 1
    creditScore = (creditModifier * loanPeriod) / loanAmount
    # first instance when the credit score is less than 1
    while creditScore < 1:
        # firstly trying to get the highest possible loan amount within the period
        while loanAmount > minLoanAmount:
            loanAmount -= amountDifference
            creditScore = (creditModifier * loanPeriod) / loanAmount
            if creditScore >= 1:
                return loanAmount, loanPeriod
        loanAmount += amountDifference
        # increasing the loan period to get on score >= 1
        while loanPeriod < maxLoanPeriod:
            loanPeriod += periodDifference
            creditScore = (creditModifier * loanPeriod) / loanAmount
            if creditScore >= 1:
                return loanAmount, loanPeriod
        return 0,0
    # second instance when the credit score is greater or equal than 1
    while creditScore >= 1:
        # maximizing the loan amount within the period 
        while loanAmount <= maxLoanAmount:
            loanAmount += amountDifference
            creditScore = (creditModifier * loanPeriod) / loanAmount
            if creditScore < 1:
                loanAmount -= amountDifference
                return loanAmount, loanPeriod
            if loanAmount > maxLoanAmount:
                loanAmount -= amountDifference
                return loanAmount, loanPeriod
        # decreasing the loan period to get creditScore as close as possible to 1
        while loanPeriod >= minLoanPeriod:
            loanPeriod -= periodDifference
            creditScore = (creditModifier * loanPeriod) / loanAmount
            if creditScore < 1 or loanPeriod <  minLoanPeriod:
                loanPeriod += periodDifference
                return loanAmount, loanPeriod
        # if best loan amount and loan period are not found, the user is not eligible for a loan
        return 0,0
