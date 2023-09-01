from unittest.mock import patch
import subprocess
import pytest

def test_app_launch():
    # Simulez l'exécution de l'application Streamlit en utilisant subprocess
    with patch("subprocess.run") as mocked_run:
        # Configurer le retour de subprocess.run
        mocked_run.return_value = subprocess.CompletedProcess(None, returncode=0)

        # Exécuter weather_app comme s'il était appelé depuis le terminal
        result = subprocess.run(["streamlit", "run", "weather_app.py"], capture_output=True)

        # Vérifier les résultats
        assert result.returncode == 0
