# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 18:18:46 2023

@author: Sarah Ahmed
"""

import numpy as np
import pickle
import streamlit as st

loaded_model = pickle.load(open('cancer_section_model.sav', 'rb'))


# creating a function for Prediction

def cancer_prediction(input_data):
    

    # converting data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # array reshaping as predicting for single instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return 'low chance of cancer'
    else:
      return 'high chance of cancer'
  
    
  
def main():
    

    st.title('Welcome to MediHelp cancer stage prediction ')
    
    
    Age = st.slider('enter age',0,100)
    Gender = st.slider('your gender',0,2)
    GeneticRisk = st.slider('genetic risk',0,7)
    chronicLungDisease = st.slider('chronic lung stage',0,7)
    Obesity = st.slider('obesity',0,9)
    PassiveSmoker = st.slider('passive smoker',0,11)
    ChestPain = st.slider('chest pain',0,10)
    CoughingofBlood = st.slider('coughing of blood',0,9)
    Fatigue = st.slider('fatigue',0,10)
    WeightLoss= st.slider('weight loss',0,11)
    DryCough = st.slider('weight loss',0,9)


    diagnosis = ''
    
    # prediction button
    
    if st.button('cancer Test Result'):
        diagnosis = cancer_prediction([Age,Gender,GeneticRisk,chronicLungDisease,Obesity,PassiveSmoker,ChestPain,CoughingofBlood,Fatigue,WeightLoss,DryCough])        
        
    st.success(diagnosis)
       
    
    
if __name__ == '__main__':
    main()