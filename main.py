from flask import Flask, request, render_template
from sklearn.metrics import r2_score
from werkzeug.utils import redirect
import prepareData
import logData


# Method that accepts inputs and returns a 1 or 0 for approved or not approved outcomes based on training model
def predict_outcome(credit, income, spouse_income, loan_amount, loan_term, property, education, dependents):
    predicted = prepareData.logistic_model.predict([[credit, income, spouse_income, loan_amount,
                                                     loan_term, property, education, dependents]])
    return predicted


app = Flask(__name__)

# Assigns the returned value from prepareData into the loan_data and accuracy_percent variables
# These variables are used later
loan_data, accuracy_percent = prepareData.loan_model_train()


# Main input form that is first shown
# Gathers all input information and used to make a prediction
# @ is a decorator - A way to wrap a function and modify the behavior
@app.route('/', methods=['GET', 'POST'])
def form_input():
    if request.method == "POST":
        # Logs information
        logData.write_file('New Input:')
        # Get inputs from HTML form and store in variables
        gender = str(request.form.get("gender"))
        # Cleaning data for predicting
        if gender == "":
            return render_template("error.html")
        elif gender == "Male":
            # Logs information
            logData.write_file('Gender:' + gender)
            gender = 1
        elif gender == "Female":
            # Logs information
            logData.write_file('Gender:' + gender)
            gender = 0
        else:
            # Logs information
            logData.write_file('Gender left blank - Reset Form')
            logData.new_line()
            return render_template("error.html")
        # Get inputs from HTML form and store in variables
        married = str(request.form.get("married"))
        # Cleaning data for predicting
        if married == "Yes":
            # Logs information
            logData.write_file('Married:' + married)
            married = 1
        elif married == "No":
            # Logs information
            logData.write_file('Married:' + married)
        else:
            # Logs information
            logData.write_file('Married left blank - Reset Form')
            logData.new_line()
            return render_template("error.html")
        # Get inputs from HTML form and store in variables
        dependents = str(request.form.get("dependents"))
        # Cleaning data for predicting
        if dependents == "0":
            # Logs information
            logData.write_file('Dependents:' + dependents)
            dependents = 0
        elif dependents == "1":
            # Logs information
            logData.write_file('Dependents:' + dependents)
            dependents = 1
        elif dependents == "2":
            # Logs information
            logData.write_file('Dependents:' + dependents)
            dependents = 2
        elif dependents == "3" or dependents == "3+":
            # Logs information
            logData.write_file('Dependents:' + dependents)
            dependents = 3
        else:
            # Logs information
            logData.write_file('Dependents left blank - Reset Form')
            logData.new_line()
            return render_template("error.html")
        # Get inputs from HTML form and store in variables
        edu = str(request.form.get("edu"))
        # Cleaning data for predicting
        if edu == "Graduate":
            # Logs information
            logData.write_file('Graduate:' + edu)
            edu = 1
        elif edu == "Not Graduate":
            # Logs information
            logData.write_file('Graduate:' + edu)
            edu = 0
        else:
            # Logs information
            logData.write_file('Graduate left blank - Reset Form')
            logData.new_line()
            return render_template("error.html")
        # Get inputs from HTML form and store in variables
        applicant_income = str(request.form.get("applicant_income"))
        if applicant_income == "":
            # Logs information
            logData.write_file('Applicant Income left blank - Reset Form')
            logData.new_line()
            return render_template("error.html")
        # Logs information
        logData.write_file('Applicant Income:' + applicant_income + 'K')
        # Get inputs from HTML form and store in variables
        applicant_income = float(applicant_income)
        # Get inputs from HTML form and store in variables
        spousal_income = str(request.form.get("spousal_income"))
        if spousal_income == "None":
            spousal_income = 0
        # Get inputs from HTML form and store in variables
        loan_amount = str(request.form.get("loan_amount"))
        # Get inputs from HTML form and store in variables
        spousal_income = float(spousal_income)
        if loan_amount == "":
            # Logs information
            logData.write_file('Loan Amount left blank - Reset Form')
            logData.new_line()
            return render_template("error.html")
        # Logs information
        logData.write_file('Loan Amount:' + loan_amount + 'K')
        loan_amount = float(loan_amount)
        # Clean data for predicting
        if 999 < loan_amount < 9999999:
            loan_amount /= 1000
        # Get inputs from HTML form and store in variables
        loan_term = str(request.form.get("loan_term"))
        if loan_term == "None" or loan_term == "":
            # Logs information
            logData.write_file('Loan Term left blank - Reset Form')
            logData.new_line()
            return render_template("error.html")
        loan_term = int(loan_term)
        loan_term *= 12
        # Logs information
        logData.write_file('Loan Term:' + str(loan_term))

        # Get inputs from HTML form and store in variables
        credit_history = str(request.form.get("credit_history"))
        # Cleaning data for predicting
        if credit_history == "Yes":
            # Logs information
            logData.write_file('Credit History Above Guideline:' + credit_history)
            credit_history = 1
        elif credit_history == "No":
            # Logs information
            logData.write_file('Credit History Above Guideline:' + credit_history)
            credit_history = 0
        else:
            # Logs information
            logData.write_file('Credit History left blank - Reset Form')
            logData.new_line()
            return render_template("error.html")
        # Get inputs from HTML form and store in variables
        property_area = str(request.form.get("property_area"))
        if property_area == "Semi-Urban":
            # Logs information
            logData.write_file('Property Area:' + property_area)
            property_area = 1
        elif property_area == "Urban":
            # Logs information
            logData.write_file('Property Area:' + property_area)
            property_area = 2
        elif property_area == "Rural":
            # Logs information
            logData.write_file('Property Area:' + property_area)
            property_area = 3
        else:
            # Logs information
            logData.write_file('Property Area left blank - Reset Form')
            logData.new_line()
            return render_template("error.html")
        # Get inputs from HTML form and store in variables
        occupation = str(request.form.get("occupation"))
        # Cleaning data for predicting
        if occupation == "Yes":
            # Logs information
            logData.write_file('Occupation:' + occupation)
            occupation = 1
        elif occupation == "No":
            # Logs information
            logData.write_file('Occupation:' + occupation)
            occupation = 0
        else:
            # Logs information
            logData.write_file('Occupation left blank - Reset Form')
            logData.new_line()
            return render_template("error.html")

        outcome = predict_outcome(credit_history, applicant_income, spousal_income, loan_amount, loan_term,
                                  property_area, edu, dependents)
        # Values using the data set average
        y_true = [1, 5109.0, 1629.20, 144.52, 342, 1, 1, 0]
        y_pred = [credit_history, applicant_income, spousal_income,
                  loan_amount, loan_term, property_area, edu, dependents]

        # R Squared scored used to shown deviation from average input
        r2_percent = r2_score(y_true, y_pred, sample_weight=None)
        r2_percent = ((str(r2_percent).split('.'))[1])
        # Splits variable into separate parts for passing into the browser
        r2_percent_whole = r2_percent[0:2]
        r2_percent_dec = r2_percent[2:6]

        str_outcome = str(outcome[0])
        number = str(accuracy_percent).split('.')
        # Splits variable into separate parts for passing into the browser
        accurate_whole = number[0]
        accurate_dec = number[1]

        # If outcome is NOT APPROVED
        if str_outcome == '0':
            # Writes to log
            logData.write_file('Outcome: NOT APPROVED')
            logData.new_line()
            link = '/ApprovalOutcome/Not Approved/' + str(accurate_whole) + '/' + str(accurate_dec) + '/' + \
                   str(r2_percent_whole) + '/' + str(r2_percent_dec)
            # Redirect to outcome page showing all information
            return redirect(link)
        # If outcome is APPROVED
        elif str_outcome == '1':
            # Writes to log
            logData.write_file('Outcome: APPROVED')
            logData.new_line()
            link = '/ApprovalOutcome/Approved/' + str(accurate_whole) + '/' + str(accurate_dec) + '/' + \
                   str(r2_percent_whole) + '/' + str(r2_percent_dec)
            # Redirect to outcome page showing all information
            return redirect(link)
        else:
            return render_template("approvalForm.html")
    return render_template("approvalForm.html")


# Used to show the approval outcome
# Accepts input to display percentages on browser for user
@app.route('/ApprovalOutcome/<outcome>/<whole>/<dec>/<r2whole>/<r2dec>')
def approval_outcome(outcome, whole, dec, r2whole, r2dec):
    if request.method == "GET":
        return render_template("approvalOutcome.html", outcome=outcome, whole=whole, dec=dec, r2whole=r2whole,
                               r2dec=r2dec)
    return render_template("approvalOutcome.html", outcome=outcome, whole=whole, dec=dec, r2whole=r2whole,
                           r2dec=r2dec)


# Used to show the dashboard
# Passes in the Visual value in dropdown box on form.
# Uses the value to show only the desired visual
@app.route('/dashboard/', methods=['GET', 'POST'])
def dashboard():
    visual = ""
    if request.method == "POST":
        print('POST')
        visual = str(request.form.get("visual"))
        return render_template("dashboard.html", visual=visual)
    return render_template("dashboard.html", visual=visual)


if __name__ == "__main__":
    app.run(debug=True)
