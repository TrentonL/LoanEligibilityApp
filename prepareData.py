from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
import pandas as pd
from models import create_scatter, create_loggrid, create_heatmap

# Creates a logistic regression object and sets default values
# Solver and Max_Iter needed to prevent warning of convergence
logistic_model = LogisticRegression(solver='lbfgs', max_iter=200)


def loan_model_train():
    loan_data = pd.read_csv('Loan_Train.csv')
    # Cleaning up data from data set before training the model

    # Drops the Loan_ID column which will not be used in the training set
    loan_data.drop('Loan_ID', inplace=True, axis=1)

    # Fills in any empty values in the Credit_History column and LoanAmount column
    # Empty Credit History values are filled in with the outcome that occurs the most in the dataset
    # Empty LoanAmount values are filled in with the average value of all the non-null LoanAmount values
    loan_data['Credit_History'].fillna(loan_data['Credit_History'].mode(), inplace=True)
    loan_data['LoanAmount'].fillna(loan_data['LoanAmount'].mean(), inplace=True)
    loan_data['Loan_Amount_Term'].fillna(loan_data['Loan_Amount_Term'].mode(), inplace=True)

    # Changing Boolean Values to 0 and 1
    loan_data.Loan_Status = loan_data.Loan_Status.replace({"Y": 1, "N": 0})
    loan_data.Gender = loan_data.Gender.replace({"Male": 1, "Female": 0})
    loan_data.Married = loan_data.Married.replace({"Yes": 1, "No": 0})
    loan_data.Self_Employed = loan_data.Self_Employed.replace({"Yes": 1, "No": 0})

    loan_data['Gender'].fillna(loan_data['Gender'].mode()[0], inplace=True)
    loan_data['Dependents'].fillna(loan_data['Dependents'].mode()[0], inplace=True)
    loan_data['Married'].fillna(loan_data['Married'].mode()[0], inplace=True)
    loan_data['Credit_History'].fillna(loan_data['Credit_History'].mean(), inplace=True)
    loan_data['Loan_Amount_Term'].fillna(loan_data['Loan_Amount_Term'].mean(), inplace=True)

    # Changing multiple value options using the labelEncoder
    features = ['Education', 'Dependents', 'Property_Area']
    label_encoder = LabelEncoder()
    for column in features:
        loan_data[column] = label_encoder.fit_transform(loan_data[column])

    # Setting the training features
    trained_features = ['Credit_History', 'ApplicantIncome', 'CoapplicantIncome', 'LoanAmount', 'Loan_Amount_Term',
                        'Property_Area', 'Education', 'Dependents']

    # Creating and setting the training sets
    # X will contain the values without the outcome
    # y will contain the outcome based on the X's values
    x = loan_data[trained_features].values
    y = loan_data['Loan_Status'].values

    # Fitting the model for future predictions
    logistic_model.fit(x, y)

    # Calculates the training model accuracy score
    score = logistic_model.score(x, y)
    score = score * 100
    create_scatter(loan_data)
    create_heatmap(loan_data)
    create_loggrid(loan_data)

    # returns the loan_data array and the training model percent
    return loan_data, score
