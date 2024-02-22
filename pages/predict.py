import numpy as np
import pickle
import pandas as pd
import streamlit as st

html_temp = """
    <div style ="background-color:sky blue;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Smart Health</h1> 
    <h1 style ="color:black;text-align:center;">Hypertension Management </h1> 
    </div> 
    """
st.markdown(html_temp, unsafe_allow_html = True)
st.sidebar.markdown("# Predict ")

# load the prediction model
pickle_in = open("classifier1.pkl","rb")
classifier = pickle.load(pickle_in)

def welcome():
    return 'welcome All'

def predict_hypertension():

    gender = ('Male', 'Female')

    has_diabetes = ('No', 'Yes')

    has_heart_disease = ('No', 'Yes')
    
    smoking_status = ('unknown', 'never smoked', "formerly smoked", "smokes", "stopped smoking", "always smoking")

    diet = ('Healthy', 'Average', 'Unhealthy')

    # mapping gender
    g = {'Female' : 0, 'Male': 1}

    # mapping diabetes
    hd = {"No" : 0, "Yes" : 1}

    # mapping heart disease
    hhd = {"No" : 0, "Yes" : 1}

    # mapping smoking status
    ss = {'unknown' : 1, 'never smoked' : 2, "formerly smoked" : 3, "smokes" : 4, "stopped smoking" : 5, "always smoking" : 6}

    # mapping diet
    d = {'Healthy' : 1, 'Average' : 2, 'Unhealthy': 3}


    gender = st.selectbox(
    '**Gender**',
    (" ", 'Male', 'Female'))

    age = st.number_input('**Age**', placeholder = 'How old are you ?')

    has_diabetes = st.selectbox(
    '**Do you have diabetes ?**',
    (" ", 'No', 'Yes'))

    has_heart_disease = st.selectbox(
    '**Any History of Heart Disease**',
    (" ", 'No', 'Yes'))

    smoking_status = st.selectbox(
    '**Smoking Status**',
    (" ", 'unknown', 'never smoked', "formerly smoked", "smokes", "stopped smoking", "always smoking"))

    body_mass_index = st.number_input('**Body Mass Index**', step = 1.00)

    glycated_haemoglobin = st.number_input('**Glycated Haemoglobin**', step = 1.0)

    average_glucose_level = st.number_input('**Average Glucose Level**')

    stress_levels = st.slider('**Stress Levels**', min_value = 1, max_value = 10, step = 1)

    hours_of_sleep = st.number_input('**How Many Hours Do You Sleep**', step = 1)

    diet = st.selectbox(
    '**How would you consider your diet ?**',
    (" ", 'Healthy', 'Average', 'Unhealthy'))


    result = st.button('Predict')

    if result:
        vals = [gender, age, has_diabetes, has_heart_disease, smoking_status, body_mass_index, glycated_haemoglobin, average_glucose_level, stress_levels, hours_of_sleep, diet]
        col = ['gender', 'age', 'has_diabetes', 'has_heart_disease', 'smoking_status', 'body_mass_index', 'glycated_haemoglobin', 'average_glucose_level', 'stress_levels', 'hours_of_sleep', 'diet']
        testdf = pd.DataFrame([vals], columns = col)

        # encode test data 
        testdf['gender'] = testdf['gender'].map(g)
        testdf['has_diabetes'] = testdf['has_diabetes'].map(hd)
        testdf['has_heart_disease'] = testdf['has_heart_disease'].map(hhd)
        testdf['smoking_status'] = testdf['smoking_status'].map(ss)
        testdf['diet'] = testdf['diet'].map(d)

        # reindex

        testdf = testdf.reindex(columns = ['gender', 'age',
                                            'has_diabetes', 'has_heart_disease',
                                            'smoking_status', 'body_mass_index',
                                            'glycated_haemoglobin', 'average_glucose_level',
                                            'stress_levels', 'hours_of_sleep', 'diet'])
        

        response = classifier.predict(testdf) # predict hypertension

        if response == 1 :
            st.write('The chances of you having hypertension are quite high. Please visit the nearest healthcare provider')

        else:
            st.write('Chances of you having hypertension are low.')
    

if __name__=='__main__':
    predict_hypertension()















    
    
    

    

    

    


    

    

    

    

    

    
    

