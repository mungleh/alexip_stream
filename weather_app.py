import streamlit as st
import numpy as np
import pandas as pd
import module_app
from PIL import Image
import requests
import folium
from geopy.geocoders import Nominatim
from streamlit_folium import folium_static

st.set_page_config(
    page_title="Main page",
    layout="wide"
)

st.markdown("""
        <style>
               .block-container {
                    padding-top: 0.5rem;
                    padding-bottom: 0rem;
                    padding-left: 6rem;
                    padding-right: 6rem;
                }
        </style>
        """, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;'>WEATHER</h1>", unsafe_allow_html=True)

    # Titre de l'application

# # Sidebar
# st.sidebar.header("Map")
# Diviser la page en deux colonnes
col1, col2 = st.columns(2)

# Colonne de gauche pour les données météo
with col1:
    # Entrée de la ville
    city_name = st.text_input("Please Enter name of city")

    # Bouton pour envoyer la demande
    if st.button("Send"):
        # if city_name:
        module_app.get_weather_data(city_name)

    else:
        st.write("Entrez le nom d'une ville pour afficher les données météo.")


# Colonne de droite pour la carte
with col2:
    st.write("## Carte")
    if city_name:
        # Obtenir les coordonnées de la ville à partir de son nom
        geolocalisation = Nominatim(user_agent="city_locator")
        localisation = geolocalisation.geocode(city_name)

        if localisation:

            st.write(f"localisation de **{city_name}**:")
            #st.write(f"Latitude: {localisation.latitude}, Longitude: {localisation.longitude}")

            carte = folium.Map(location=[localisation.latitude, localisation.longitude], zoom_start=10)
            folium.Marker([localisation.latitude, localisation.longitude], popup=city_name).add_to(carte)

            # Afficher la carte
            folium_static(carte)
        else:
            st.write("Impossible de trouver la ville.")
