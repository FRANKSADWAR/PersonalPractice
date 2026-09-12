import requests
import json

def get_historical_weather_data(latitude, longitude):
    """
    Call an API to get the current weather data from Open weather free-tier API
    """

    API_KEY = "51b5bc45ee5ad2db64bb02faf31892e6"
    base_url = "https://api.openweathermap.org/data/2.5/weather"

    headers = {
            "Content-Type": "application/json"
        }

    params = {
        "lat": latitude,
        "lon": longitude,
        "units": "metric",
        "appid":API_KEY
    }

    
    response = requests.get(url=base_url, params = params, headers= headers)
    if response.status_code == 200:
        print(response.json())
    
## store the file a json
def store_file_as_json():
    data_dir = "/home/billy/Documents/Python_fundementals/data"
    with open(data_dir + "weather_now.json", "w") as weather_file:
        json.dumps(weather_file) 


def convert_to_dataframe():
    pass


def load_data_to_db():
    pass
    

if __name__ == "__main__":
    get_historical_weather_data(-1.29, 36.29)
