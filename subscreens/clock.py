import sys
from PyQt5.QtCore import QTime, QTimer, QDate, Qt
from PyQt5 import QtWidgets
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QVBoxLayout, QGridLayout, QHBoxLayout
from PyQt5.QtWidgets import QApplication, QWidget


class Clock(QWidget):

    def __init__(self, foreground_color="#ffffff"):
        super().__init__()

        self.name = "Clock"
        self.foreground_color = foreground_color
        self.font = QFont("LCARSGTJ3", 80, QFont.Bold)
        self.font_small = QFont("LCARSGTJ3", 40, QFont.Bold)
        self.lblTimeTxt = QtWidgets.QLabel()
        self.lblTimeTxt.setFont(self.font)

        self.lblDateTxt = QtWidgets.QLabel()
        self.lblDateTxt.setFont(self.font_small)
        self.Date = QDate.currentDate().toString("dd.MM.yyyy")
        self.lblDateTxt.setText(str(self.Date))

        self.checkThreadTimer = QTimer(self)
        self.checkThreadTimer.setInterval(100) #.1 seconds
        self.checkThreadTimer.timeout.connect(lambda: self.set_time())
        self.checkThreadTimer.start()

        self.symbolTxt = "\u2026"
        self.symbol = QtWidgets.QLabel(self.symbolTxt)
        self.symbol.setFont(self.font)

        self.symbol2 = QtWidgets.QLabel(self.symbolTxt)
        self.symbol2.setFont(self.font)
        self.setStyleSheet("QLabel { color : " + self.foreground_color + "; }")

        layout = QGridLayout()
        hbox = QHBoxLayout()
        hbox.addStretch()
        hbox.addWidget(self.symbol)
        hbox.addStretch()
        layout.addLayout(hbox, 0, 1)
        layout.addWidget(self.lblTimeTxt, 1, 1)
        layout.addWidget(self.lblDateTxt, 2, 1)

        self.setLayout(layout)

    def set_time(self):
        self.lblTimeTxt.setText(self.get_time().toString())

    @staticmethod
    def get_time() -> QTime:
        return QTime.currentTime()

    def get_name(self) -> str:
        return self.name