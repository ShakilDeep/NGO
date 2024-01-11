import pickle
import pandas as pd
import streamlit as st

# Load the model from the file
with open('model/regressor_model.pkl', 'rb') as file:
    model = pickle.load(file)
# Assuming that 'data' is a pandas DataFrame containing your input data
data = pd.DataFrame({
    'zone_name': ['zone1'],
    'area_name': ['area1'],
    'branch_name': ['branch1'],
    'branch_code': [123],
    'Samity': ['samity1'],
    'branc_code': [123],
    'Member_code': [123],
    'Member_name': ['member1'],
    'Spouse_name': ['spouse1'],
    'Mobile_no': ['1234567890'],
    'Component_name': ['component1'],
    'Loan_code': [123],
    'Loan_cycle': [1],
    'Loan_disburse_date': ['2022-01-01'],
    'Disburse_amount': [1000],
    'Last_transaction_date': ['2022-01-02'],
    'Date_last_installment': ['2022-01-03'],
    'Present_loan_amount': [500],
    'Due_amount': [200],
    'Saving_balance': [300],
    'Member': [1],
    'Organization': ['org1'],
    'Day_expire': [30]
})

# Make a prediction
prediction = model.predict(data)

st.write(prediction)
