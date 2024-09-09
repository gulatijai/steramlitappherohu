

import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved model

diabetes_model= pickle.load(open('trained_model_diabetes.sav', 'rb'))

heart_disease_model= pickle.load(open('heart_disease_model.sav', 'rb'))

parkinsons_model= pickle.load(open('parkinsons_model.sav','rb'))

# sidebar for navigation

with st.sidebar:
    
    selected= option_menu('Multiple Disease Prediction System',
                          ['Diabetes Prediction',
                           'Heart Disease Prediction',
                           'Parkinson Prediction'], 
                          icons= ['activity', 'heart', 'person'],  # icons are added from the name from icon bootstrap website
                          default_index= 1)


# Diabetes Prediction page

if (selected== 'Diabetes Prediction'):
    
    st.title('Diabetes Prediction')
    
    # getting the input the data
    
    # columns for input data
    col1, col2, col3= st.columns(3)
    
    with col1:
        Pregnancies= st.text_input('Number of pregnancies')
    
    with col2:
        Glucose= st.text_input('Glucose level')
    
    with col3:    
        BloodPressure= st.text_input('BP level')
    
    with col1:
        SkinThickness= st.text_input('Skin thickness value')
    
    with col2:
        Insulin= st.text_input('Insulin level')
    
    with col3:
        BMI= st.text_input('BMI Number')
    
    with col1:
        DiabetesPedigreeFunction= st.text_input('Diabetes Pedigree Function')
    
    with col2:
        Age= st.text_input('Age of the person')
    
    # code for prediction
    diab_daignosis= ''
    
    # creating button for the prediction
    if st.button('Diabetes Test Results'):
        
        diab_prediction= diabetes_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
        
        if (diab_prediction[0]==1):
            diab_daignosis= 'The preson is diabetic'
            
        else:
            diab_daignosis= 'The preson is not diabetic'
            
        st.success(diab_daignosis)
        
        

# Heart Disease 
if (selected== 'Heart Disease Prediction'):
    
    st.title('Heart Disease Prediction using ML')
    
    # columns for input data
    col1, col2, col3, col4= st.columns(4)
    
    with col1:
        age= st.text_input('Age of the person')
    
    with col2:
        sex= st.text_input('Sex')
    
    with col3:
        cp= st.text_input('Chest pain types')
    
    with col4:
        trestbps= st.text_input('Resting BP')
    
    with col1:
        chol= st.text_input('Serum Cholestrol level mg/dl')
    
    with col2:
        fbs= st.text_input('Fasting Blood sugar')
    
    with col3:
        restecg= st.text_input('Electric Cardiograohic results')
    
    with col4:
        thalach= st.text_input('Maximum Heart rate achieved')
    
    with col1:
        exang= st.text_input('Exercise induced Agina')
    
    with col2:
        oldpeak= st.text_input('Old peak- ST depression by exercise relative to rest')
    
    with col3:
        slope= st.text_input('The slope of the peak exercise')
    
    with col4:
        ca= st.text_input('Number of major vessels(0-3) coloured by fluroscopy')
    
    with col1:
        thal= st.text_input('thal:0- normal, 1- fixed defect, 2- reversabe defect')
    
    # code for prediction
    Heart_disease_daignosis= ''

    # creating button for the prediction
    if st.button('Heart Test Results'):
    
        heart_disease_prediction= heart_disease_model.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang, oldpeak, slope, ca, thal]])
    
        if (heart_disease_prediction[0]==1):
            Heart_disease_daignosis= 'The person has heart disease'
        
        else:
            Heart_disease_daignosis= 'The person has not heart disease'
        
        st.success(Heart_disease_daignosis)
    
    
# Parkinson
if (selected== 'Parkinson Prediction'):
    
    st.title('Parkinson Prediction using ML')
    
   # columns for input data
    col1, col2, col3, col4, col5 = st.columns(5)
   
    with col1:
       fo= st.text_input('MDVP:Fo(Hz)')
   
    with col2:
       fhi= st.text_input('MDVP:Fhi(Hz)')
    
    with col3:
        flo= st.text_input('MDVP:Flo(Hz)')
    
    with col4:
        Jitter_percent= st.text_input('MDVP:Jitter(%)')
    
    with col5:
        Jitter_Abs= st.text_input(' MDVP:Jitter(Abs)')
    
    with col1:
        RAP= st.text_input('MDVP:RAP')
    
    with col2:
        PPQ= st.text_input('MDVP:PPQ')
    
    with col3:
        Jitter_DDP= st.text_input('Jitter:DDP')
    
    with col4:
        Shimmer= st.text_input(' MDVP:Shimmer')
    
    with col5:
        Shimmer_DB= st.text_input('MDVP:Shimmer(dB)')
    
    with col1:
        APQ3=st.text_input('Shimmer:APQ3')
    
    with col2:
        APQ5=st.text_input('Shimmer:APQ5')
    
    with col3:
        APQ= st.text_input('MDVP:APQ')
    
    with col4:
        DDA= st.text_input('Shimmer:DDA')
    
    with col5:
        NHR= st.text_input('NHR')
    
    with col1:
        HNR=st.text_input('HNR')
    
    with col2:
        RPDE=st.text_input('RPDE')
    
    with col3:
        DFA=st.text_input('DFA')

    with col4:
        spread1=st.text_input('Spread 1')

    with col5:
        spread2=st.text_input('Spread 2')
    
    with col1:
        D2=st.text_input('D2')
    
    with col2:
        PPE=st.text_input('PPE')
    
    
    # code for prediction
    parkisnson_daignosis= ''

    # creating button for the prediction
    if st.button('Parkinson Results'):
    
        parkinson_prediction= parkinsons_model.predict([[fo,fhi, flo, Jitter_percent,Jitter_Abs,RAP, PPQ, Jitter_DDP,Shimmer,
                                                         Shimmer_DB,APQ3,APQ5,APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE ]])
    
        if (parkinson_prediction[0]==1):
            parkisnson_daignosis= 'The person has parkinson'
        
        else:
            parkisnson_daignosis= 'The person has not parkinson'
        
        st.success(parkisnson_daignosis)
    
    
    
    
    

