import json
#import glob
import os
import time

class FileWriter():

    def write_jsonfile(self, filename: str, filedata: dict) -> None:
        if self.is_file(filename):
            os.remove(filename)
        try:
            with open(filename, "w") as json_file:
                try:
                    json.dump(filedata, json_file)
                    print("File: {} written.".format(filename))
                except Exception as e:
                    print("json error")
                finally:
                    json_file.close()
        except (IOError, OSError) as e:
            print("File: {} with error: {}".format(filename,e))
    
    def is_file(self, filename: str) -> bool:
        PATH = filename
        if os.path.isfile(PATH) and os.access(PATH, os.R_OK) and os.access(PATH, os.W_OK):
            print("File exists and is readable/writeable/deleteable.")
            return True
        else:
            return False

    def getLastModificationTime(self, filename: str) -> None:
        modification_time = os.path.getmtime(filename)
        #local_time = time.gmtime(modification_time)
        local_time = time.ctime(modification_time)
        print("Last modification time(Local time):", local_time)
        return local_time

if __name__ == "__main__":
    f = FileWriter()
    f.getLastModificationTime('foobar.txt')
    f.write_jsonfile("ice.json", {"a":4, "b":17})