#import validators
#from rest import Rest
from util.rest.rest import Rest

class RestSpecial():
    api_key = None
    rest_caller = None

    def __init__(self):
        self.rest_caller = Rest()
     
    # https://openweathermap.org/api/air-pollution
    def call_server_pollution(self, call_params: dict) -> dict:
        """
        params: call_params { "lat": "", "lon": "", "units": "", "language": "", "key": ""}
        """
        data = None
        lat = call_params['lat']
        lon = call_params['lon']
        units = call_params['units']
        language = call_params['language']
        key = call_params['key']
        path = "http://api.openweathermap.org/data/2.5/air_pollution?lat={}&lon={}&units={}&lang={}&appid={}".format(lat, lon, units, language, key)
        data = self.rest_caller.rest_call_get(path=path, headers={}, params={})
        if data['code'] == 200:
            print("Weather API Call was successful.")
        else:
            print("Weather API Call was not successful!")
        return data

    def call_server_weather(self, call_params: dict) -> dict:
        """
        params: call_params { "city": "", "units": "", "language": "", "key": ""}
        """
        data = None

        # TODO: if data file exists and is older than ... 1h, 
        # than do not call for new data, else call for data
        
        key = call_params['key']
        city = call_params['city']
        units = call_params['units']
        language = call_params['language']
        path = "http://api.openweathermap.org/data/2.5/weather?q={}&units={}&lang={}&appid={}".format(city, units, language, key)

        data = self.rest_caller.rest_call_get(path=path, headers={}, params={})
        if data['code'] == 200:
            print("Weather API Call was successful.")
        else:
            print("Weather API Call was not successful!")
        return data
        

if __name__ == "__main__":
    rastEn = RestSpecial()
    print(rastEn.call_server_weather({ "city": "berlin", "units": "metrics", "language": "de", "key": "36dcf663b6964439a18574709e1d6eef"}))