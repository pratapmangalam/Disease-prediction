import os
import pickle # pre trained model loading
import streamlit as st #web app
from streamlit_option_menu  import option_menu

st.set_page_config(page_title='Prediction of Disease Outbreaks',
                   layout='wide',
                   page_icon='👨‍⚕️')
diabetes_model = pickle.load(open("diabetes_model.sav",'rb'))
heart_disease_model = pickle.load(open("heart_model.sav",'rb'))
parkinsons_model = pickle.load(open("parkinsons.sav",'rb'))

with st.sidebar:
    selected = option_menu("Prediction of disease outbreak system",['Diabetes Prediction','Heart Disease Prediction','Parkinsons Prediction'],
                           menu_icon = 'hospital-fill',icons =['activity','heart','person'],default_index=0 )

if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction using Machine Learning')
    col1,col2,col3 = st.columns(3)
    with col1:
        Pregnancies = st.text_input('No. of pregnancies')
    with col2:
        Glucose = st.text_input('Glucose level')
    with col3:
        Bloodpressure = st.text_input('Blood pressure value')
    with col1:
        Skinthickness = st.text_input('Skin Thickness value')
    with col2:
        Insulin = st.text_input('Insulin level')
    with col3:
        BMI = st.text_input('BMI value')
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    with col2:
        Age = st.text_input('Age')

    diabetes_diagnosis = ''
    if st.button('Diabetes Test Result'):
        user_input=[Pregnancies, Glucose, Bloodpressure, Skinthickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
        user_input=[float(x) for x in user_input]
        diabetes_prediction=diabetes_model.predict([user_input])
        if diabetes_prediction[0] == 1:
            diabetes_diagnosis = "The person is diabetic"
        else:
            diabetes_diagnosis = "The person is not diabetic"
    st.success(diabetes_diagnosis)
    

if selected == 'Heart Disease Prediction':
    st.title("Heart disease prediction using ML")
    col1,col2,col3 = st.columns(3)
    with col1:
        age = st.text_input("Age")
    with col2:
        sex = st.text_input("Sex (0 = Female, 1 = Male)")
    with col3:
        ca = st.text_input("Number of Major Vessels (0-3)")
    with col1:
        trestbps = st.text_input("Resting Blood Pressure (mm Hg)")
    with col2:
        chol = st.text_input("Serum Cholesterol (mg/dL)")
    with col3:
        fbs = st.text_input("Fasting Blood Sugar > 120 mg/dL (0 = No, 1 = Yes)")
    with col1:
        thalach = st.text_input("Maximum Heart Rate Achieved")
    with col2:
        exang = st.text_input("Exercise-Induced Angina (0 = No, 1 = Yes)")
    with col3:
        oldpeak = st.text_input("ST Depression (oldpeak)")
    with col1:
        cp = st.text_input("Chest Pain Type ( 1 = Typical Angina,  2 = Atypical Angina,       3 = Non-anginal, 4 = Asymptomatic)")
    with col2:
        restecg = st.text_input("Resting ECG  (  0 = Normal,   1 = ST-T wave abnormality,   2 = Left ventricular hypertrophy)")
    with col3:
        thal = st.text_input("Thalassemia (1 = Normal, 2 = Fixed Defect, 3 = Reversible Defect)")
    with col1:
        slope = st.text_input("Slope of Peak Exercise (0 = Up, 1 = Flat, 2 = Down)")


    


    heart_diagnosis = ''
    if st.button('Heart Disease Test Result'):
        user_input=[age,sex,cp,trestbps,chol,fbs,thalach,exang,restecg,oldpeak,slope,ca,thal]
        user_input=[float(x) for x in user_input]
        heart_disease_prediction=heart_disease_model.predict([user_input])
        if heart_disease_prediction[0] == 1:
            heart_diagnosis = "The person has heart disease."
        else:
            heart_diagnosis = "The person does not have any heart disease."
    st.success(heart_diagnosis)


if selected == 'Parkinsons Prediction':
    st.title("Parkinsons prediction using ML")
    col1,col2,col3=st.columns(3)
    with col1:
        Fo = st.text_input("MDVP:Fo(Hz)")
    with col2:
        Fhi = st.text_input("MDVP:Fhi(Hz)")
    with col3:
        Flo = st.text_input("MDVP:Flo(Hz)")
    with col1:
        Jitter = st.text_input("MDVP:Jitter(%)")
    with col2:
        jittera = st.text_input("MDVP:Jitter(Abs)")
    with col3:
        RAP = st.text_input("MDVP:RAP")
    with col1:
        PPQ = st.text_input("MDVP:PPQ")
    with col2:
        Jitterd = st.text_input("Jitter:DDP")
    with col3:
        shimmer = st.text_input("MDVP:Shimmer")
    with col1:
        shimmerd = st.text_input("MDVP:Shimmer(dB)")
    with col2:
        shimmera = st.text_input("Shimmer:APQ3")
    with col3:
        shimmerap = st.text_input("Shimmer:APQ5")
    with col1:
        APQ = st.text_input("MDVP:APQ")
    with col2:
        shimmerdd = st.text_input("Shimmer:DDA")
    with col3:
        NHR = st.text_input("NHR")
    with col1:
        HNR = st.text_input("HNR")
    with col2:
        RPDE = st.text_input("RPDE")
    with col3:
        DFA = st.text_input("DFA")
    with col1:
        spread1 =st.text_input("Spread1")
    with col2:
         spread2 =st.text_input("Spread2")
    with col3:
        D2 = st.text_input("D2")
    with col1:
        PPE = st.text_input("PPE")
    
    parkinsons_diagnosis = ''
    if st.button("Parkinsons Test Result"):
        user_input=[Fo,Fhi,Flo,Jitter,jittera,RAP,PPQ,Jitterd,shimmer,shimmerd,shimmera,shimmerap,APQ,shimmerdd,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]
        user_input=[float(x) for x in user_input]
        parkinsons_prediction=parkinsons_model.predict([user_input])
        if parkinsons_prediction[0]==1:
            parkinsons_diagnosis = "The person has Parkinson's disease."
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease."
        st.success(parkinsons_diagnosis)