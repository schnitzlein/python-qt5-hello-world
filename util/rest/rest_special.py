#import validators
#from rest import Rest
from util.rest.rest import Rest
from util.filehandler import FileHandler
from datetime import datetime
import logging
logger = logging.getLogger(__name__)

class RestSpecial():
    api_key = None
    rest_caller = None

    def __init__(self):
        self.rest_caller = Rest()
        self.f = FileHandler()
     
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
            logger.info("Weather API Call was successful.")
        else:
            logger.info("Weather API Call was not successful!")
        return data

    def call_server_weather(self, call_params: dict) -> dict:
        """
        params: call_params { "city": "", "units": "", "language": "", "key": ""}
        """
        data = None
        
        key = call_params['key']
        city = call_params['city']
        units = call_params['units']
        language = call_params['language']
        path = "http://api.openweathermap.org/data/2.5/weather?q={}&units={}&lang={}&appid={}".format(city, units, language, key)

        data = self.rest_caller.rest_call_get(path=path, headers={}, params={})
        if data['code'] == 200:
            logger.info("Weather API Call was successful.")
        else:
            logger.info("Weather API Call was not successful!")
        return data
    
    def save_data(self, data: dict, filename="./data/test.json") -> None:
        try:
            self.f.write_jsonfile(filename=filename, filedata=data)
        except Exception as e:
            logger.error("File saveing went wrong for File: {}\n With Exception: {}".format(filename, e))
        

    def load_data(self, filename="./data/test.json") -> dict:
        try:
            loaded_data = self.f.read_jsonfile(filename=filename)
            if "error" in loaded_data:
                logger.error("File loading went wrong for File: {}".format(filename))
                return {}
            else:
                return loaded_data
        except Exception as e:
            logger.error("File loading went wrong for File: {}\n With Exception: {}".format(filename, e))
    
    def get_data_age_str(self, filename: str) -> str:
        if self.f.is_file(filename):
            last_mod_time_str = self.f.getLastModificationTimeString(filename)
            return last_mod_time_str
        else:
            now = datetime.now()
            date_time = now.strftime("%d.%m.%Y, %H:%M:%S")
            return date_time

    def get_data_age(self, filename: str) -> datetime:
        if self.f.is_file(filename):
            last_mod_time = self.f.getLastModificationTime(filename)
            return last_mod_time
        else:
            return datetime.now()
    
    def dataTimeDiff(self, filename: str, timediff=3600) -> int:
        if self.f.is_file(filename):
            date_obj = self.f.getLastModificationTime(filename)
            diff = datetime.now() - date_obj
            diff_in_hours = diff.total_seconds() // timediff
            return int(diff_in_hours)
        else:
            return 0

if __name__ == "__main__":
    rastEn = RestSpecial()
    print(rastEn.call_server_weather({ "city": "berlin", "units": "metrics", "language": "de", "key": "36dcf663b6964439a18574709e1d6eef"}))