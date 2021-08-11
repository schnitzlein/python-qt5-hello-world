import json
#import glob
import os
import time
import datetime
import logging
import traceback
logger = logging.getLogger(__name__)

class FileHandler():
    def __init__(self):
        pass

    def read_jsonfile(self, filename: str) -> dict:
        PATH = filename
        data_dict = { 'error': "no file found with readable data." }
        if not self.is_file_readable(filename):
            logger.error("File not found in path: {}".format(PATH))
        else:
            try:
                with open(PATH, "r") as json_file:
                    try:
                        data_dict = json.load(json_file)
                        logger.debug("File loaded: {}".format(filename))
                    except Exception as e:
                        logger.error("json error with: {}".format(e))
                    finally:
                        json_file.close()
            except (IOError, OSError) as e:
                logger.error("File: {} with error: {}".format(PATH,e))
        return data_dict

    def write_jsonfile(self, filename: str, filedata: dict) -> None:
        PATH = filename
        #if self.is_file_path(PATH):
        #    os.remove(PATH)
        try:
            with open(PATH, "w") as json_file:
                try:
                    json.dump(filedata, json_file)
                    logger.info("File: {} written.".format(PATH))
                except Exception as e:
                    logger.error("json error: {}".format(e))
                finally:
                    json_file.close()
        except (IOError, OSError) as e:
            logger.error("File: {} with error: {}".format(PATH,e))
    
    def delete_file(self, filename: str) -> None:
        PATH = filename
        if self.is_file_path(PATH):
            os.remove(PATH)

    def append_to_jsonfile(self, filename: str, filedata: dict, insert_into: str) -> None:
        """
        filename: is the path of the file with fileending
        filedata: is the data you want to append
        insert_into: is the json_subentry you want to add the filedata, take care all json key matches data are inserted!
        """
        PATH = filename
        try:
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
        except (IOError, OSError) as e:
            logger.error("File: {} with error: {}".format(PATH,e))
        except Exception as e:
                    logger.error("json error: {}".format(e))

    def is_file(self, filename: str) -> bool:
        """
        True ::= File exists and is readable/writeable/deleteable.
        False ::= File does not exist in filename/path OR access is not possible OR access permissions missing.
        """
        PATH = filename
        if self.is_file_path(PATH) and self.is_file_writeable(PATH) and self.is_file_readable(PATH):
            logger.debug("File exists and is readable/writeable/deleteable.")
            return True
        else:
            logger.warn("File does not exist in filename/path OR access is not possible OR access permissions missing!\n For File: {}".format(filename))
            return False
    
    def is_file_path(self, filename: str) -> bool:
        """
        True ::= File exists in matching filename/path.
        False ::= File does not exist in matching filename/path.
        """
        PATH = filename
        if os.path.isfile(PATH):
            logger.debug("File exists.")
            return True
        else:
            logger.warn("File: '{}' can not be found.".format(filename))
            return False

    def is_file_writeable(self, filename: str) -> bool:
        """
        True ::= File is writeable in matching filename/path.
        False ::= File is not writeable in matching filename/path.
        """
        PATH = filename
        if os.access(PATH, os.W_OK):
            logger.debug("File is writeable.")
            return True
        else:
            logger.error("File: '{}' is not writeable.".format(filename))
            return False
    
    def is_file_readable(self, filename: str) -> bool:
        """
        True ::= File is readable in matching filename/path.
        False ::= File is not readable in matching filename/path.
        """
        PATH = filename
        if os.access(PATH, os.R_OK):
            logger.debug("File is readable.")
            return True
        else:
            logger.error("File: '{}' is not readable.".format(filename))
            return False

    def getLastModificationTimeUnix(self, filename: str) -> str:
        """
        str ::= Returns a Unix timestamp in secs from last modification datetime of a given filename/path.
        """
        modification_time = os.path.getmtime(filename)
        return modification_time

    def getLastModificationTimeString(self, filename: str) -> str:
        """
        str ::= Returns a String from last modification datetime of a given filename/path.
        """
        modification_time = os.path.getmtime(filename)
        #local_time = time.gmtime(modification_time)
        local_time = time.ctime(modification_time)
        logger.debug("Last modification time(Local time): {}".format(local_time))
        return local_time
    
    def getLastModificationTime(self, filename: str) -> datetime:
        """
        datetime ::= Returns a datetime object from last modification datetime of a given filename/path.
        """
        modification_time = os.path.getmtime(filename)
        timestamp = int(modification_time)
        date_obj = datetime.datetime.fromtimestamp( timestamp )
        return date_obj

if __name__ == "__main__":
    f = FileHandler()
    f.write_jsonfile("/data/foobar.json", {"a":4, "b":17})
    f.getLastModificationTime("/data/foobar.json")