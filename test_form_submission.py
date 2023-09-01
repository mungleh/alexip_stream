
import streamlit as st
from unittest.mock import patch
import module_app
import pytest

def test_form_submission():
    # Simuler les interactions dans l'application Streamlit
    with patch("streamlit.button") as mocked_button, \
            patch("streamlit.text_input") as mocked_text_input:

        # Configurer les valeurs simulées pour le bouton et le champ de texte
        mocked_button.return_value = True
        mocked_text_input.return_value = "Lyon"  # Simuler un nom de ville entré

        # Appeler la fonction de votre application qui traite le formulaire
        result = module_app.process_form()

        # Vérifier les résultats
        assert result is True
        assert mocked_button.called
        assert mocked_text_input.called
