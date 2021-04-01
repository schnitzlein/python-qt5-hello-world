import json
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

title = ""
mywidth = 50

def readconfig():
    # read file
    with open('config.json', 'r') as myfile:
        data=myfile.read()

    # parse file
    obj = json.loads(data)

    # show values
    print("QT-Main-Title: " + str(obj['title']))
    print("QT-Amount-Sub-Screen: " + str(obj['amount_sub_screen']))
    print("Config-Param1: " + str(obj['param1']))
    print("Config-Param2: " + str(obj['param2']))

    title = str(obj['title'])
    return { 'title': title, 'width': obj['param1'] }

def window():
    print(title)
    app = QApplication(sys.argv)
    w = QWidget()
    b = QLabel(w)
    b.setText("Hello World!")
    w.setGeometry(100,100,mywidth,50)
    b.move(50,20)
    w.setWindowTitle(title)
    w.show()
    sys.exit(app.exec_())
   
if __name__ == '__main__':
    title = readconfig()['title']
    mywidth = readconfig()['width']
    window()
