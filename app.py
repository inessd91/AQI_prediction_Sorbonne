import streamlit as st
import pandas as pd
import joblib

# 12. chargement de modele dans l'application
model = joblib.load('modele_aqi.pkl')

# 13. Création de l’interface utilisateur avec Streamlit

# a. Catégorisation de l’AQI
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
    
# b. Conseils de santé
def get_health_advice_en(aqi):
    if 0 <= aqi <= 50:
        return "🌿 Air quality is good. No precautions needed."
    elif 51 <= aqi <= 100:
        return "🙂 Acceptable air quality, but sensitive individuals may feel mild effects."
    elif 101 <= aqi <= 200:
        return "⚠️ Limit prolonged outdoor activity if you have respiratory issues."
    elif 201 <= aqi <= 300:
        return "😷 People with lung or heart disease should avoid outdoor exertion."
    elif 301 <= aqi <= 400:
        return "🚫 Everyone should reduce physical activity outdoors."
    elif 401 <= aqi <= 500:
        return "🛑 Health alert: Avoid outdoor activities and stay indoors."
    else:
        return "❓ Invalid AQI value."


# c. Design Streamlit/ Titre de la page 
#st.title("Prédiction de l'AQI en Inde")
st.set_page_config(page_title="AQI India Predictor", page_icon="🌀", layout="centered")
st.markdown("## 🌀 Air Quality Index (AQI) Prediction in India")
st.markdown("Enter the average pollutant values to estimate the air quality according to the Indian national AQI standard 🇮🇳.")

st.markdown("---")

# d. Interface utilisateur
st.markdown("### 📥 Input Pollutant Levels")
# Curseurs pour chaque polluant
pm25 = st.slider("PM2.5 (µg/m³)", 0.0, 500.0, 50.0) #max value est défini en fonction des valeurs maximales du dataset (df.describe) et de celles recommandées pour chaque polluant.
pm10 = st.slider("PM10 (µg/m³)", 0.0, 500.0, 50.0)
no2 = st.slider("NO2 (µg/m³)", 0.0, 500.0, 30.0)
nh3 = st.slider("NH3 (µg/m³)", 0.0, 500.0, 20.0)
so2 = st.slider("SO2 (µg/m³)", 0.0, 500.0, 20.0)
co = st.slider("CO (mg/m³)", 0.0, 500.0, 1.0)
ozone = st.slider("OZONE (µg/m³)", 0.0, 500.0, 30.0)

# e. Prédiction sur bouton
st.markdown("### 🔍 AQI Prediction")
st.write("Click on the button to predict the AQI based on pollutant levels.")
if st.button("Predict AQI"):
    input_data = [[pm25, pm10, no2, nh3, so2, co, ozone]]
    prediction = model.predict(input_data)[0]
    category = categorize_aqi_india(prediction)
    st.info(get_health_advice_en(prediction))

    st.write(f" 📊 Predicted AQI : {prediction:.2f}")
    st.write(f"🧪Air Quality: {category}")


# f. Ajout d'informations pour l'utilisateur
## explication sur l'AQI : What is AQI?
st.markdown("##### ℹ️ Understanding the Air Quality Index (AQI)")
with st.expander("What is AQI?"):
    st.markdown("""
The **Air Quality Index (AQI)** is a numerical scale used to communicate the level of air pollution in a specific area.  
It is calculated based on the concentrations of key air pollutants such as: **PM2.5, PM10, NO₂, SO₂, CO, and O₃**.

Here's how to understand the AQI values:
*AQI values are based on India's National Air Quality Standards.*
                
- 🟢 **0–50** : Good – air quality is considered satisfactory.  
- 🟡 **51–100** : Satisfactory – may affect very sensitive individuals.  
- 🟠 **101–200** : Moderate – sensitive people should reduce long outdoor activities.  
- 🔴 **201–300** : Poor – may cause health effects for everyone.  
- 🟣 **301–400** : Very Poor – serious health impact after prolonged exposure.  
- ⚫ **401–500** : Severe – hazardous for all, avoid outdoor activity.
""")

#14. déploiement web :
# lancer le WebApp avec streamlit : 
# dans le terminal: streamlit run app.py