import sys
from PyQt5.QtCore import QTime, QTimer, QDate, Qt
from PyQt5 import QtWidgets
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QVBoxLayout, QGridLayout, QHBoxLayout
from PyQt5.QtWidgets import QApplication, QWidget

class Clock(QWidget):

    def __init__(self):
        super().__init__()

        self.f = QFont("LCARSGTJ3", 80, QFont.Bold)
        self.fsmall = QFont("LCARSGTJ3", 40, QFont.Bold)
        self.lblTimeTxt = QtWidgets.QLabel()
        self.lblTimeTxt.setFont(self.f)

        self.lblDateTxt = QtWidgets.QLabel()
        self.lblDateTxt.setFont(self.fsmall)
        self.Date = QDate.currentDate().toString("dd.MM.yyyy")
        self.lblDateTxt.setText(str(self.Date))

        self.checkThreadTimer = QTimer(self)
        self.checkThreadTimer.setInterval(100) #.1 seconds
        self.checkThreadTimer.timeout.connect(lambda: self.setTime())
        self.checkThreadTimer.start()

        self.symbolTxt = "\u2026"
        self.symbol = QtWidgets.QLabel(self.symbolTxt)
        self.symbol.setFont(self.f)

        self.symbol2 = QtWidgets.QLabel(self.symbolTxt)
        self.symbol2.setFont(self.f)

        layout = QGridLayout()
        # hbox = QHBoxLayout()
        # hbox.addWidget(self.symbol)
        # hbox.addStretch()
        # hbox.addWidget(self.symbol2)
        # layout.addLayout(hbox, 0, 1)
        layout.addWidget(self.lblTimeTxt, 1, 2, 2, 2)
        layout.addWidget(self.lblDateTxt, 2, 2, 2, 1)


        self.setLayout(layout)
        self.show()

    def setTime(self):
        self.lblTimeTxt.setText(self.getTime().toString())

    def getTime(self) -> QTime:
        return QTime.currentTime()