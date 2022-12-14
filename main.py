import pickle
import streamlit as st


breast_cancer_model = pickle.load(open('breast_cancer_model.sav', 'rb'))

#Judul Web
st.title('Data Mining Prediksi Pasien Kanker Payudara')



col1, col2 = st.columns(2)

with col1 :
    meanradius = st.text_input('input_meanradius', 0, 500)
with col1 :
    mean_texture = st.text_input('input_mean_texture', 0, 500)
with col1 :
    mean_perimeter = st.text_input('input_mean_perimeter', 0, 500)
with col2 :
    mean_area = st.text_input('input_mean_area', 0, 500)
with col2 :
    mean_smoothness =st.text_input('input_mean_smoothness', 0 , 500)
    
    #code untuk prediksi
cancer_diagnosis = ''

if st.button('Prediksi Kanker'):
    cancer_prediction = breast_cancer_model.predict([[meanradius, mean_texture, mean_perimeter, mean_area, mean_smoothness ]])
    
    if(cancer_prediction[0] == 1):
        cancer_diagnosis = 'Pasien mengalami kanker'
    else:
        cancer_diagnosis = 'Pasien tidak mengalami kanker'
    
    st.success(cancer_diagnosis, icon="✅")
  

    