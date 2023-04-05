import streamlit as st
import pandas as pd
import numpy as np




st.title('Heart Failure prediction')
st.header("Dataset")
df = pd.read_csv("heart_disease.csv")
df

st.header("This dataset include")
st.header("Gender")
st.header("Age")
st.header("education status")
st.header("current smoker")
st.header("cigarette per day")
st.header("BP meds : High blood Pressure")
st.header("prevelant stroke")
st.header("prevelantHyp : Prelevant hypertension")
st.header("Diabetes")
st.header("Totchol: Cholestrol")
st.header("sysBP : Systolic Blood Pressure")
st.header("diaBP: Diastolic Blood pressure")
st.header("BMI : Body Mass Isolation")
st.header("HeartRate")
st.header("Glucose")
st.header("HeartStroke")
