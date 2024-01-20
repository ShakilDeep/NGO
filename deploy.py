import streamlit as st
import pandas as pd
import pickle


def user_input_features():
    Loan_cycle = st.sidebar.number_input('Loan_cycle')
    Disburse_amount = st.sidebar.number_input('Disburse_amount')
    Present_loan_amount = st.sidebar.number_input('Present_loan_amount')
    Saving_balance = st.sidebar.number_input('Saving_balance')
    Day_expire = st.sidebar.number_input('Day_expire')
    Loan_disburse_date = st.sidebar.date_input('Loan_disburse_date', value=pd.to_datetime('01/01/2011'))
    Date_last_installment = st.sidebar.date_input('Date_last_installment', value=pd.to_datetime('01/01/2011'))
    data = {'Loan_cycle': Loan_cycle,
            'Disburse_amount': Disburse_amount,
            'Present_loan_amount': Present_loan_amount,
            'Saving_balance': Saving_balance,
            'Day_expire': Day_expire,
            'Last_transaction_Year': Loan_disburse_date.year,
            'Last_transaction_Month': Loan_disburse_date.month,
            'Last_transaction_Day': Loan_disburse_date.day,
            'Date_last_installment_Year': Date_last_installment.year,
            'Date_last_installment_Month': Date_last_installment.month,
            'Date_last_installment_Day': Date_last_installment.day}
    features = pd.DataFrame(data, index=[0])
    return features


st.write("# Loan Defaulter Prediction App")
df = user_input_features()

model = pickle.load(open('ngo.pkl', 'rb'))

if st.button('Submit'):
    prediction = model.predict(df)
    if prediction[0] == 1:
        st.write("The member is predicted to be a defaulter.")
    else:
        st.write("The member is predicted not to be a defaulter.")

