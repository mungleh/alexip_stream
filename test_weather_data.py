from unittest.mock import patch
from module_app import get_weather_data   # Remplacez par le chemin vers votre code

def test_weather_data():
    # Exemple de réponse réelle de l'API pour la ville de Lyon
    lyon_response = {
        "name": "Lyon",
        "sys": {"country": "FR"},
        # ... autres données réelles
    }

    # Utilisez 'patch' comme context manager avec 'start' et 'stop'
    with patch("requests.get") as mocked_get:
        # Configurez la valeur renvoyée par 'json()' pour l'objet simulé
        mocked_get.return_value.json.return_value = lyon_response

        # Appelez votre fonction avec les données simulées
        weather_data = get_weather_data("Lyon")

        # Assertions sur les données renvoyées
        assert weather_data["name"] == "Lyon"
        assert weather_data["sys"]["country"] == "FR"
        # ... vérification d'autres données renvoyées
