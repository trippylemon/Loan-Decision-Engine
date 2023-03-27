from flask import Flask, render_template, url_for, request, redirect, flash
from algorithm import BestDeal, calculateCreditModifier, isDigit
app = Flask(__name__)
app.secret_key = 'some_secret_key'

@app.route('/', methods=['GET','POST'])
def index():
   if request.method == 'POST':
      personalID = request.form['personal-code']
      loanAmount = request.form['loan-amount']
      loanPeriod = request.form['loan-period']
      isnumber = False
      if (isDigit(personalID) and isDigit(loanAmount) and isDigit(loanPeriod)):
         isnumber = True
      if isnumber:
         creditModifier = calculateCreditModifier(int(personalID))
         bestLoanAmount, bestLoanPeriod = BestDeal(creditModifier, int(loanAmount), int(loanPeriod))
         if (bestLoanAmount == 0 and bestLoanPeriod == 0):
            flash("You are not eligible for a loan")
         elif (bestLoanAmount == -1 and bestLoanPeriod == -1):
            flash("You have a debt, you are not eligible for a loan")
         else:
            flash(f"Your are eligible for {int(bestLoanAmount)} for {int(bestLoanPeriod)} months")
      else:
         flash("Please enter only numbers")
      return redirect("/")
   else:
      return render_template('index.html')

if __name__ == "__main__":
   app.run(debug=True)