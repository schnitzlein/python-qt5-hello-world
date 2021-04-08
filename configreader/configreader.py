import json
#import glob

class ConfigReader():

    def read_config(self, filename: str) -> dict:
        config_dict = { 'error': "no config file found" }
        try:
            with open(filename, "r") as json_file:
                try:
                    config_dict = json.load(json_file)
                except Exception as e:
                    print("json error")
                finally:
                    json_file.close()
        except (IOError, OSError) as e:
            print("File: {} with error: {}".format(filename,e))
        return config_dict

    def get_part_from_config(self, filename: str, part: str) -> dict:
        file = open(filename, "r")
        data=file.read()
        obj = json.loads(data)
        print("read config part: " + part)
        print(obj[part])
        return obj[part]
