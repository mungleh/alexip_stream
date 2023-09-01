import streamlit as st
import pandas as pd
import requests
from PIL import Image
import os

# Fonction qui prend en entré le nom de la ville et va faire une requete a l'API
# pour aller chercher la reponse en json
def get_weather_data(city_name):

    # Récupérer la clé API à partir des variables d'environnement
    api_key = st.secrets["API_KEY"]

    # Requête à une API de météo (remplacez l'URL par l'API réelle que vous souhaitez utiliser)
    weather_url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"
    response = requests.get(weather_url)
    weather_data = response.json()

    if weather_data["cod"] == 200:

        # Affichage des données météo dans un carré avec bordure
        # Image météo
        icon_id = weather_data['weather'][0]['icon']
        icon_url = f"http://openweathermap.org/img/wn/{icon_id}.png"
        icon = Image.open(requests.get(icon_url, stream=True).raw)
        st.image(icon, caption='Weather Icon', width=100)

        st.markdown(
            f"""
            <div style='border: 6px solid #ccc; padding: 10px;'>
                <h2>Weather Data</h2>
                <p><strong>Ville:</strong> {weather_data['name']}</p>
                <p><strong>Pays:</strong> {weather_data['sys']['country']}</p>
                <p><strong>Description:</strong> {weather_data['weather'][0]['description']}</p>
                <p><strong>Température:</strong> {weather_data['main']['temp']} °C</p>
                <p><strong>Humidité:</strong> {weather_data['main']['humidity']} %</p>
                <p><strong>Pression:</strong> {weather_data['main']['pressure']} hPa</p>
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.write("Ville non trouvée. Veuillez entrer un nom de ville valide.")
