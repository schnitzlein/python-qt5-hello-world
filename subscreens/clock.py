import sys
from PyQt5.QtCore import QTime, QTimer
from PyQt5 import QtWidgets
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QApplication, QWidget

class Clock(QWidget):

    def __init__(self):
        super().__init__()

        self.f = QFont("Times", 30, QFont.Bold)
        self.lblTimeTxt = QtWidgets.QLabel()
        self.lblTimeTxt.setFont(self.f)

        self.checkThreadTimer = QTimer(self)
        self.checkThreadTimer.setInterval(100) #.1 seconds
        self.checkThreadTimer.timeout.connect(lambda: self.setTime())
        self.checkThreadTimer.start()

        layout = QHBoxLayout()
        layout.addStretch(1)
        layout.addWidget(self.lblTimeTxt)
        layout.addStretch(1)
        self.setLayout(layout)
        self.show()

    def setTime(self):
        self.lblTimeTxt.setText(self.getTime().toString())

    def getTime(self) -> QTime:
        return QTime.currentTime()