import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

st.markdown("<h1 style='text-align: left; color: black;'>Smart Health Dashboard</h1>", unsafe_allow_html=True)

st.sidebar.markdown("## Filter")
gender_filter = st.sidebar.selectbox("Gender", ["All", "Male", "Female"])
diet_filter = st.sidebar.selectbox("Diet", ["All", 'Healthy', 'Average', 'Unhealthy'])


st.subheader("Data Evaluation")

col1, col2 = st.columns(2)
with col1:
    st.metric(
        "Average Sleep Hours",
        value = '7 Hours')
with col2:
    st.metric(
        "Average Age",
        value = '42 Years')
    

st.subheader("Exploratory Data Analysis")

df = pd.read_csv('clean_data2.csv')

if gender_filter != "All":
    df = df[df['gender'] == gender_filter]

if diet_filter != "All":
    df = df[df['diet'] == diet_filter]

col1, col2 = st.columns(2)

with col1:
    sns.countplot(data = df, x='has_diabetes', hue='has_hypertension', palette='dark:#5A9_r')
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot()
    
with col2:
    
    sns.countplot(data = df, x='has_heart_disease', hue='has_hypertension', palette='dark:#5A9_r')
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot()
    


