import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns


# Creates the .png of historical data
# This scatter plot shows a relation between the application income
# and the loan amount requested from an applicant
def create_scatter(loan_data):
    plt.figure(figsize=(18, 6))
    plt.title("Relation Between Application Income vs Loan Amount ")

    plt.grid()
    plt.scatter(loan_data['ApplicantIncome'], loan_data['LoanAmount'], c='k', marker='x')
    plt.xlabel("Applicant Income")
    plt.ylabel("Loan Amount")

    plt.savefig('./static/scatterplot.png')
    return 0


# Creates the .png of historical data
# This heat map shows a relation between each of the form inputs that
# are used when predicting the outcome
def create_heatmap(loan_data):
    plt.figure(figsize=(12, 14))
    sns.heatmap(loan_data.corr(), cmap='coolwarm', annot=True, fmt='.1f', linewidths=.1)
    plt.savefig('./static/heatmap.png')
    return 0


# Creates the .png of historical data
# Shows a bar graph of the average income and
# loan amount
def create_loggrid(loan_data):
    plt.subplot(1, 1, 1)
    plt.grid()
    plt.hist(np.log(loan_data['LoanAmount']))
    plt.title("Average Loan Application Amount - Loan Amount by Monthly Income (In Thousands)")
    plt.savefig('./static/loanappamount.png')
    return 0
