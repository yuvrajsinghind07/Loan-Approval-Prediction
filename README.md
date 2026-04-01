#  Loan Default Prediction System
---

##  Project Overview
This project predicts whether a borrower will repay a loan or default using machine learning.  
The goal is to help in better loan approval decisions by analyzing financial and credit-related data.

---
##  Problem Statement
Build a machine learning model that can predict whether a customer will repay a loan or not based on financial and credit history.

---

##  Target Variable
**loan_paid_back** 
- 1 → Loan Repaid (Customer repay the loan)  
- 0 → Loan Default (Risky Customer)

---
## Dataset Features
- Demographic: age, gender, marital_status  
- Financial: annual_income, monthly_income, debt_to_income_ratio  
- Credit: credit_score, delinquency_history, public_records  
- Loan: loan_amount, interest_rate, loan_term, installment  
- Other: employment_status, loan_purpose, grade_subgrade

---
## Machine Learning Workflow
- Data cleaning and preprocessing  
- Exploratory Data Analysis (EDA)  
- Feature engineering  
- Handling imbalanced data using SMOTE  
- Model training and comparison  
- Hyperparameter tuning  
- Final pipeline (preprocessing + SMOTE + model)

---
## Model Performance
Final Model: Random Forest (Tuned)

- Training Accuracy: 91.1%  
- Testing Accuracy: 88.7%  
  
**Classification Report**

 Class 0 (Default):
- Precision: 0.89  
- Recall: 0.53  
- F1-score: 0.67  

 Class 1 (Repaid):
- Precision: 0.89  
- Recall: 0.98  
- F1-score: 0.94

**- Overall Accuracy: 88.7%**

---
## Key Insights
- Credit score and debt-to-income ratio are most important  
- High loan amount + low income = higher risk  
- Past delinquencies increase default probability

---
##  Tech Stack
- Python
- Pandas
- NumPy
- Seaborn
- Scikit-learn
- SMOTE
- Streamlit

---
## Run Locally
streamlit run app.py

---
## Live Demo Deployment(Streamlit app)
**Click here :**

---
##  Project Structure
```
loan-approval-prediction
├── dataset
│      └── loan_dataset.csv
├── notebooks  
│      └── Loan_prediction.ipynb  
├── deployment
│      └── loan_app.py
├── model
│      └── loan_approval_model.pkl
├── requirements.txt  
└── README.md  
```

---

## Financial Impact 
- Helps reduce loan default risk.
- Supports data-driven loan approval decisions.
- Improves overall financial decision-making.

---
## Author
Yuvraj Singh  
