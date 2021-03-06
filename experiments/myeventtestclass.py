from PyQt5.QtWidgets import QHBoxLayout
from PyQt5 import uic
from PyQt5.QtGui import QFont
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QSize, QPoint
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QWidget,QPushButton,QApplication,QListWidget,QGridLayout,QLabel,QMessageBox
from PyQt5.QtCore import QTimer,QDateTime

class Myeventtest(QMainWindow):

    def __init__(self, name: str, foreground_color="#ffffff", font_name=""):
        super().__init__()

        if font_name != "":
            self.font = QFont(font_name, 80, QFont.Bold)
        else:
            self.font = QFont("LCARSGTJ3", 80, QFont.Bold)
        self.foreground_color = foreground_color

        self.ui = uic.loadUi("test.ui", self)

        # Find the button with the name "printButton"
        self.button = self.findChild(QtWidgets.QPushButton, 'printButton')
        self.button.clicked.connect(self.printButtonPressed)
        # Find the InputField with the name "input"
        self.input = self.findChild(QtWidgets.QLineEdit, 'input')

        self.buttonClear = self.findChild(QtWidgets.QPushButton, 'clearButton')
        self.buttonClear.clicked.connect(self.printButtonClearPressed)

        self.pressing = False
        self.start = QPoint(0, 0)
        self.center()
        self.oldPos = self.pos()              

    def mouseReleaseEvent(self, QMouseEvent):
        self.pressing = False
        print("pressing release?: {}".format(self.pressing))

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()
        print("New Position: {}".format(self.oldPos))

    def mouseMoveEvent(self, event):
        delta = QPoint (event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    
    def printButtonPressed(self):
        # This is executed when the button is pressed
        if self.input.text() == "":
            print('Input text: ' + self.input.property("placeholderText"))
        else:
            print('Input text: ' + self.input.text())
    
    def printButtonClearPressed(self):
        # This is executed when the button is pressed
        if self.input.text() == "":
            pass
        else:
            self.input.setText("foobar")      # indirect through QLineEdit setText function
            self.ui.input.setText("barfoo")   # direct through self.ui file
            #self.input.setProperty("placeholderText", "some text 123")


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    w = Myeventtest("foobar")
    w.show()
    sys.exit(app.exec_())


