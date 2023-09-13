import streamlit as st
import pandas as pd
import  numpy as np
import pickle 
import sklearn

pickle_in = open('LogisticRegression.pkl','rb')
model = pickle.load(pickle_in)

st.title("Titanic Survival Prediction")

### inputting variables

P_class =st.number_input("P_class") 
Sex =st.number_input("Sex") 
Age =st.number_input("Age") 
SibSp =st.number_input("SibSp") 
Parch =st.number_input("Parch") 
Fare =st.number_input("Fare") 
Embarked =st.number_input("Embarked") 
submit = st.button("predict")
# Convert prediction to a human-readable response
if submit:
    prediction = model.predict([[P_class,Sex,Age,SibSp,Parch,Fare,Embarked]])
    if prediction == 0:
        st.write("Survived")
    else:
        st.write("Not Survived")
    




