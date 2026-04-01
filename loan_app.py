import streamlit as st
import joblib
import pandas as pd

model = joblib.load("loan_approval_model.pkl")

st.title("Loan Approval Prediction")

st.write("Enter Borrower details")

# Inputs
age = st.number_input("Age")

gender = st.selectbox("Gender", ["Male", "Female","Other"])

marital_status = st.selectbox("Marital Status", ["Single", "Married","Divorced" ,"Widowed"])

education_level = st.selectbox("Education", ["Bachelor's", "High School" ,"Master's","PhD","Other"])

annual_income = st.number_input("Annual Income")

monthly_income = st.number_input("Monthly Income")

employment_status = st.selectbox("Employment", ["Employed", "Unemployed" ,"Self-employed","Student","Retired"])

debt_to_income_ratio = st.number_input("Debt to Income Ratio")

credit_score = st.number_input("Credit Score")

loan_amount = st.number_input("Loan Amount")

loan_purpose = st.selectbox("Loan Purpose", ["Car", "Home", "Education","Business","Medical","Vacation","Debt consolidation","Other"])

interest_rate = st.number_input("Interest Rate")

loan_term = st.number_input("Loan Term")

installment = st.number_input("Installment")

grade_subgrade = st.selectbox("Grade", ["A1","A2","A3","B1","B2","B3","C1","C2","C3","D1","D2","D3","E1","E2","E3"])

num_of_open_accounts = st.number_input("Open Accounts")

total_credit_limit = st.number_input("Total Credit Limit")

current_balance = st.number_input("Current Balance")

delinquency_history = st.number_input("Delinquency History")

public_records = st.number_input("Public Records")

num_of_delinquencies = st.number_input("Number of Delinquencies")

if st.button("Predict"):
    data = pd.DataFrame({
        "age":[age],
        "gender":[gender],
        "marital_status":[marital_status],
        "education_level":[education_level],
        "annual_income":[annual_income],
        "monthly_income":[monthly_income],
        "employment_status":[employment_status],
        "debt_to_income_ratio":[debt_to_income_ratio],
        "credit_score":[credit_score],
        "loan_amount":[loan_amount],
        "loan_purpose":[loan_purpose],
        "interest_rate":[interest_rate],
        "loan_term":[loan_term],
        "installment":[installment],
        "grade_subgrade":[grade_subgrade],
        "num_of_open_accounts":[num_of_open_accounts],
        "total_credit_limit":[total_credit_limit],
        "current_balance":[current_balance],
        "delinquency_history":[delinquency_history],
        "public_records":[public_records],
        "num_of_delinquencies":[num_of_delinquencies]
    })

    result = model.predict(data)

    if result[0] == 1:
        st.success("Loan Will be Paid Back")
    else:
        st.error("Loan Risk")