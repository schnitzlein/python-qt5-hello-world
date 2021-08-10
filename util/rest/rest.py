#import validators
import json
import requests
import logging.config
import traceback

class Rest():

    def __init__(self):
        logging.config.fileConfig('/logs/logging.ini', disable_existing_loggers=False)
        self.logger = logging.getLogger(__name__)
    
    def rest_call_get(self, path: str, headers:dict, params: dict) -> dict:
        payload = {'params': params}   
        resp = requests.get(path, params=params, headers=headers)
        if resp.status_code == 200:
            try:
                data = resp.json()    
                ret = { 'code': 200, 'data': data }
                return ret
            except Exception as e:
                self.logger.error("Something went wrong within rest_call_get: {}".format(e))
            except:
                self.logger.error("uncaught exception: %s," traceback.format_exc())    
        elif resp.status_code != 200:
            self.logger.error("Calling: '{}' went wrong with code: {}".format(self.url, resp.status_code))
            ret = { 'code': resp.status_code, 'data': self.url }
            return ret
        else:
            self.logger.error("something really bad happend.")
    
    def rest_call_post(self, path: str, headers:dict, params: dict) -> dict:
        payload = {'params': params}
        resp = requests.post(path, params=params, headers=headers)
        if resp.status_code == 200:
            try:
                data = resp.json()
                ret = { 'code': 200, 'data': data }
                return ret
            except Exception as e:
                self.logger.error("Something went wrong within rest_call_post: {}".format(e))
            except:
                self.logger.error("uncaught exception: %s," traceback.format_exc())   
        elif resp.status_code != 200:
            self.logger.error("Calling: '{}' went wrong with code: {}".format(self.url, resp.status_code))
            ret = { 'code': resp.status_code, 'data': self.url }
            return ret
        else:
            self.logger.error("something really bad happend.")
        
"""
if __name__ == "__main__":
    r = Rest()
    key = "36dcf663b6964439a18574709e1d6eef"
    data = None
    city = "Berlin"
    units = "metric"
    language = "de" # en, fr, ... , https://openweathermap.org/current#multi
    path = "http://api.openweathermap.org/data/2.5/weather?q={}&units={}&lang={}&appid={}".format(city, units, language,key)
    data = r.rest_call_get(path=path, headers={}, params={})
    if data['code'] == 200:
       print(data['data'])
    else:
       print(None)
"""