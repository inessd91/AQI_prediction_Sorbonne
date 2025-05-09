import streamlit as st
import pandas as pd
import joblib

# chargement de modele
model = joblib.load('modele_aqi.pkl')

# catégorisation de l’AQI
def categorize_aqi_india(aqi):

    if 0 <= aqi <= 50:
        return "Good 🟢" 
    elif 51 <= aqi <= 100:
        return "Satisfactory 🟡" 
    elif 101 <= aqi <= 200:
        return "Moderately polluted 🟠" 
    elif 201 <= aqi <= 300:
        return "Poor 🔴" 
    elif 301 <= aqi <= 400:
        return "Very Poor 🟣" 
    elif 401 <= aqi <= 500:
        return "Severe ⚫" 
    else:
        return "Beyond Index ❌"  # aqi<0 ou aqi>500 hors de l'echelle définie par l'autorité indienne (0 à 500) 
    

# Design Streamlit/ Titre de la page 

#st.title("Prédiction de l'AQI en Inde")
#st.write("Entrez les valeurs moyennes des polluants pour prédire l'indice de qualité de l'air.")
st.set_page_config(page_title="AQI India Predictor", page_icon="🌀", layout="centered")
st.markdown("## 🌀 Air Quality Index (AQI) Prediction in India")
st.markdown("Enter the average pollutant values to estimate the air quality according to the Indian national AQI standard 🇮🇳.")

st.markdown("---")


# Interface utilisateur
st.markdown("### 📥 Input Pollutant Levels")
col1, col2 = st.columns(2)
with col1:
    pm25 = st.number_input("💨PM2.5 (µg/m³)", min_value=0.0, max_value=1000.0)
    pm10 = st.number_input("💨PM10 (µg/m³)", min_value=0.0, max_value=1000.0)
with col2:
    no2 = st.number_input("💨NO2 (µg/m³)", min_value=0.0, max_value=500.0)
    so2 = st.number_input("💨SO2 (µg/m³)", min_value=0.0, max_value=500.0)

# Prédiction sur bouton
if st.button("🔍 Predict AQI"):
    prediction = model.predict([[pm25, pm10, no2, so2]])[0]
    category = categorize_aqi_india(prediction)

    st.write(f" 📊 Predicted AQI : {prediction:.2f}")
    st.write(f"🧪Air Quality: {category}")