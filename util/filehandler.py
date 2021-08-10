import json
#import glob
import os
import time
import datetime
import logging.config
import traceback

class FileHandler():
    def __init__(self):
        logging.config.fileConfig('/logs/logging.ini', disable_existing_loggers=False)
        self.logger = logging.getLogger(__name__)

    def read_jsonfile(self, filename: str) -> dict:
        PATH = filename
        config_dict = { 'error': "no config file with readable data." }
        if not self.is_file_readable(filename):
            print("File not found in path: {}".format(PATH))
        try:
            with open(PATH, "r") as json_file:
                try:
                    config_dict = json.load(json_file)
                except Exception as e:
                    print("json error")
                finally:
                    json_file.close()
        except (IOError, OSError) as e:
            print("File: {} with error: {}".format(PATH,e))
        return config_dict

    def write_jsonfile(self, filename: str, filedata: dict) -> None:
        PATH = filename
        if self.is_file_path(PATH):
            os.remove(PATH)
        try:
            with open(PATH, "w") as json_file:
                try:
                    json.dump(filedata, json_file)
                    print("File: {} written.".format(PATH))
                except Exception as e:
                    print("json error")
                finally:
                    json_file.close()
        except (IOError, OSError) as e:
            print("File: {} with error: {}".format(PATH,e))
    
    def append_to_jsonfile(self, filename: str, filedata: dict, insert_into: str) -> None:
        """
        filename: is the path of the file with fileending
        filedata: is the data you want to append
        insert_into: is the json_subentry you want to add the filedata, take care all json key matches data are inserted!
        """
        PATH = filename
        if self.is_file(PATH):
            data = self.read_jsonfile(PATH)
            if insert_into == "":
                # append new json/dict entrys to end of file
                data.update(filedata)
            # append to specific json entry data
            else:
                for key, value in data:
                    if key == insert_into:
                        data.key.update(filedata)
            self.write_jsonfile(PATH, data)
        else:
            # something wrong here
            pass

    def is_file(self, filename: str) -> bool:
        PATH = filename
        if self.is_file_path(PATH) and self.is_file_writeable(PATH) and self.is_file_readable(PATH):
            print("File exists and is readable/writeable/deleteable.")
            return True
        else:
            print("File access is not possible or access permissions missing! for File: {}".format(filename))
            return False
    
    def is_file_path(self, filename: str) -> bool:
        PATH = filename
        if os.path.isfile(PATH):
            print("File exists.")
            return True
        else:
            print("File: '{}' can not be found.".format(filename))
            return False

    def is_file_writeable(self, filename: str) -> bool:
        PATH = filename
        if os.access(PATH, os.W_OK):
            print("File is writeable.")
            return True
        else:
            print("File: '{}' is not writeable.".format(filename))
            return False
    
    def is_file_readable(self, filename: str) -> bool:
        PATH = filename
        if os.access(PATH, os.R_OK):
            print("File is readable.")
            return True
        else:
            print("File: '{}' is not readable.".format(filename))
            return False

    def getLastModificationTimeString(self, filename: str) -> str:
        modification_time = os.path.getmtime(filename)
        #local_time = time.gmtime(modification_time)
        local_time = time.ctime(modification_time)
        print("Last modification time(Local time):", local_time)
        return local_time
    
    def getLastModificationTime(self, filename: str) -> datetime:
        modification_time = os.path.getmtime(filename)
        local_time = time.ctime(modification_time)
        date_obj = datetime.strptime(time.ctime(), "%a %b %d %H:%M:%S %Y")
        return date_obj

if __name__ == "__main__":
    f = FileHandler()
    f.getLastModificationTime('foobar.txt')
    f.write_jsonfile("/data/ice.json", {"a":4, "b":17})