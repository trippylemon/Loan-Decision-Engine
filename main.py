from flask import Flask, render_template, url_for, request, redirect, flash
from algorithm import BestDeal, calculateCreditModifier, isDigit
# Create the app
app = Flask(__name__)
app.secret_key = 'some_secret_key'
# Index route
@app.route('/', methods=['GET','POST'])
def index():
   # If the request is POST, the user has submitted the form
   if request.method == 'POST':
      # Get the data from the form
      personalID = request.form['personal-code']
      loanAmount = request.form['loan-amount']
      loanPeriod = request.form['loan-period']
      # Check if the data is valid
      isNumber = False
      if (isDigit(personalID) and isDigit(loanAmount) and isDigit(loanPeriod)):
         isNumber = True
      if isNumber:
         creditModifier = calculateCreditModifier(int(personalID))
         bestLoanAmount, bestLoanPeriod = BestDeal(creditModifier, int(loanAmount), int(loanPeriod))
         # Display the result
         # If the user is not eligible for a loan, corresponding message will be displayed
         if (bestLoanAmount == 0 and bestLoanPeriod == 0):
            flash("You are not eligible for a loan")
         # If the user is not eligible for a loan because of debt, corresponding message will be displayed 
         elif (bestLoanAmount == -1 and bestLoanPeriod == -1):
            flash("You have a debt, you are not eligible for a loan")
         # If the user is eligible for a loan, the bestLoanAmount and bestLoanPeriod will be displayed on web page
         else:
            flash(f"Your are eligible for {int(bestLoanAmount)} for {int(bestLoanPeriod)} months")
      # error handling if user enters non-numeric values
      else:
         flash("Please enter only numbers")
      # redirecting to the same page after the run is completed
      return redirect("/")
   # If the request is GET, the user has not submitted the form
   else:
      return render_template('index.html')
   
# Run the app
if __name__ == "__main__":
   app.run(debug=True)
