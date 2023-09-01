import unittest
from unittest.mock import patch
from io import BytesIO
from PIL import Image
from module_app import get_weather_data

#
class TestWeatherApp(unittest.TestCase):
    @patch('your_module.st.image')
    @patch('your_module.st.markdown')
    @patch('your_module.requests.get')
    def test_get_weather_data(self, mock_requests_get, mock_markdown, mock_image):
        # Mock the response from the API
        mock_response = mock_requests_get.return_value
        mock_response.json.return_value = {
            "cod": 200,
            "name": "Paris",
            "sys": {"country": "FR"},
            "weather": [{"description": "Clear", "icon": "01d"}],
            "main": {"temp": 20, "humidity": 50, "pressure": 1010}
        }
        
        # Mock the image
        mock_icon = Image.new("RGB", (100, 100))
        mock_response_image = BytesIO()
        mock_icon.save(mock_response_image, format="PNG")
        mock_icon_url = f"http://openweathermap.org/img/wn/01d.png"
        mock_requests_get.return_value.raw = mock_response_image
        mock_response_image.seek(0)

        # Call the function
        get_weather_data("Paris")

        # Add your assertions here
        mock_image.assert_called_with(mock_icon, caption='Weather Icon', width=100)
        mock_markdown.assert_called()
        mock_requests_get.assert_called_with(mock_icon_url, stream=True)

if __name__ == '__main__':
    unittest.main()