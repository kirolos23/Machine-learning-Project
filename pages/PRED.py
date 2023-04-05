from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
import numpy as np
import streamlit as st
import pandas as pd
import pickle as pickle
model = pickle.load(open('model.sav', 'rb'))


# reading data
df = pd.read_csv('heart_disease.csv')

def predict_heart(Gender_Male,age,currentSmoker,Cigeratte_per_day,BPMeds,prevalentHyp,diabetes,totchol,sysBP,diaBP,BMI,heartRate,glucose,prevalentStroke):
    input=np.array([[Gender_Male,age,currentSmoker,Cigeratte_per_day,BPMeds,prevalentHyp,diabetes,totchol,sysBP,diaBP,BMI,heartRate,glucose,prevalentStroke]]).astype(np.float64)
    prediction=model.predict(input)
    pred='{0:.{1}f}'.format(prediction[0][0], 2)
    return float(pred)

def main():
    st.title("Heart Stroke Prediction")


    Gender_Male= st.radio("Select Gender: ", ('Male', 'Female'))
    age = st.text_input("age","")
    currentSmoker = st.radio("currentSmoker",('Yes', 'No'))
    Cigeratte_per_day = st.text_input("Cigeratte_per_day","")
    BPMeds = st.radio("BPMeds",('Yes','No'))
    prevalentHyp= st.radio("prevalentHyp: ", ('Yes', 'No'))
    diabetes= st.radio("Diabetes: ", ('Yes', 'No'))
    totchol = st.text_input("cholestrol","")
    sysBP = st.text_input("systolic Blood Pressure","")
    diaBP = st.text_input("diastolic Blood Pressure","")
    BMI = st.text_input("Body Mass Isolation ","")
    heartRate = st.text_input("HeartRate","")
    glucose = st.text_input("Glucose","")
    prevalentStroke_yes= st.radio("prevalent stroke: ", ('Yes', 'No'))
    if currentSmoker=="Yes":
        currentSmoker=1 
    elif currentSmoker=="No":
        currentSmoker=0
    
    if BPMeds=="Yes":
        BPMeds=1
    elif BPMeds=="No":
        BPMeds=0
    
    if prevalentHyp=="Yes":
        prevalentHyp=1
    elif prevalentHyp=="No":
        prevalentHyp=0
 
    if diabetes=="Yes":
        diabetes=1
    elif diabetes=="No":
        diabetes=0
 
    if Gender_Male=="Female":
        Gender_Male=0
    elif Gender_Male=="Male":
          Gender_Male=1

    if prevalentStroke_yes=="Yes":
        prevalentStroke_yes=1
    elif prevalentStroke_yes=="No":
          prevalentStroke_yes=0

    if st.button("Predict"):
        output=predict_heart(Gender_Male,age,currentSmoker,Cigeratte_per_day,BPMeds,prevalentHyp,diabetes,totchol,sysBP,diaBP,BMI,heartRate,glucose,prevalentStroke_yes)
        st.success('Heart Stroke {}'.format(output))

        if output == 0:
            st.markdown('Heart Stroke',unsafe_allow_html=True)
        else:
            st.markdown('No heart stroke',unsafe_allow_html=True)

if __name__=='__main__':
    main()
















