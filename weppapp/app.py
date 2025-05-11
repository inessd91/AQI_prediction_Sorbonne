import streamlit as st
import joblib
import numpy as np

# Charger le modèle sauvegardé
model = joblib.load('C:/Users/BOUQALLABA-TOUMMINI/Desktop/Projects DU Data Analytics/projet-intro-python/projet-intro-python/prediction_python/weppapp/linear_model_aqi.pkl')

# Fonction de catégorisation AQI
def categorize_aqi_india(aqi):
    if 0 <= aqi <= 50:
        return "Good"
    elif 51 <= aqi <= 100:
        return "Satisfactory"
    elif 101 <= aqi <= 200:
        return "Moderately polluted"
    elif 201 <= aqi <= 300:
        return "Poor"
    elif 301 <= aqi <= 400:
        return "Very Poor"
    elif 401 <= aqi <= 500:
        return "Severe"
    else:
        return "Beyond Index"

# Titre
st.title("🌍 Prédiction de la qualité de l'air (AQI)")

st.markdown("Réglez les curseurs pour simuler les niveaux de polluants dans l'air :")

# Curseurs pour chaque polluant
pm25 = st.slider("PM2.5 (µg/m³)", 0.0, 500.0, 50.0)
pm10 = st.slider("PM10 (µg/m³)", 0.0, 500.0, 50.0)
no2 = st.slider("NO2 (µg/m³)", 0.0, 200.0, 30.0)
nh3 = st.slider("NH3 (µg/m³)", 0.0, 200.0, 20.0)
so2 = st.slider("SO2 (µg/m³)", 0.0, 200.0, 20.0)
co = st.slider("CO (mg/m³)", 0.0, 10.0, 1.0)
ozone = st.slider("OZONE (µg/m³)", 0.0, 300.0, 30.0)

# Prédiction
if st.button("🔍 Prédire l'AQI"):
    features = np.array([[pm25, pm10, no2, nh3, so2, co, ozone]])
    prediction = model.predict(features)[0]
    category = categorize_aqi_india(prediction)

    st.success(f"🌫️ AQI estimé : {prediction:.2f}")
    st.info(f"📊 Catégorie : {category}")

    # Suggestions si l'air n'est pas "Good"
    if prediction > 50:
        ratio = 50 / prediction
        st.warning("🎯 Pour atteindre une qualité d'air de catégorie 'Good' (AQI ≤ 50), essayez de viser :")

        st.markdown(f"- PM2.5 : **{pm25 * ratio:.2f} µg/m³**")
        st.markdown(f"- PM10  : **{pm10 * ratio:.2f} µg/m³**")
        st.markdown(f"- NO2   : **{no2 * ratio:.2f} µg/m³**")
        st.markdown(f"- NH3   : **{nh3 * ratio:.2f} µg/m³**")
        st.markdown(f"- SO2   : **{so2 * ratio:.2f} µg/m³**")
        st.markdown(f"- CO    : **{co * ratio:.2f} mg/m³**")
        st.markdown(f"- OZONE : **{ozone * ratio:.2f} µg/m³**")

