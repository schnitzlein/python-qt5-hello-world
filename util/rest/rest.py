import requests
#import validators
import json

class Rest():
    url = None
    api_key = None

    def __init__(self, url: str, api_key: str):
        if isinstance(url, str):
            self.url = url
        if isinstance(api_key, str):
            self.api_key = api_key
    
    def call_server(self, subpath: str) -> dict:
        print("complete call Path: {}".format(self.url + subpath))
        resp = requests.get(self.url + subpath + "&appid={}".format(self.api_key))
        # resp = requests.get(url=url, params=params) # more generic way...
        if resp.status_code == 200:
            try:
                data = resp.json()    
                #if data == {}:
                #    logging.warning("Using old data from callServer()! Code != 200 error is: {}".format(resp.status_code))
                #    return None
                ret = { 'code': 200, 'data': data }
                return ret
            except Exception as e:
                #logging.error("Something wrong with callServer: {}".format(e))
                print("Something wrong with callServer: {}".format(e))
        elif resp.status_code != 200:
            print("Calling: '{}' went wrong with code: {}".format(self.url + subpath, resp.status_code))
            ret = { 'code': resp.status_code, 'data': None }
            return ret
        else:
            print("something different happend.")
        

if __name__ == "__main__":
    r = Rest("http://api.openweathermap.org", "36dcf663b6964439a18574709e1d6eef")
    data = None
    city = "Berlin"
    language = "de" # en, fr, ... , https://openweathermap.org/current#multi
    subpath = "/data/2.5/weather?q={}&units=metric&lang={}".format(city, language)
    data = r.call_server(subpath=subpath)
    if data['code'] == 200:
       print(data['data'])
    else:
       print(None)



  