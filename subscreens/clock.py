import sys
from PyQt5.QtCore import QTime, QTimer, QDate, Qt
from PyQt5 import QtWidgets
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QVBoxLayout, QGridLayout, QHBoxLayout
from PyQt5.QtWidgets import QApplication, QWidget
from gui import *

class Clock(QWidget):

    def __init__(self, foreground_color="#ffffff"):
        super().__init__()

        self.name = "Clock"
        self.gui_element_builder = GuiElementsBuilder()
        self.main_layout = QGridLayout()
        self.foreground_color = foreground_color
        self.font = QFont("LCARSGTJ3", 180, QFont.Bold)
        self.font_small = QFont("LCARSGTJ3", 60, QFont.Bold)
        self.lblTimeTxt = QtWidgets.QLabel()
        self.lblTimeTxt.setFont(self.font)
        self.lblTimeSecTxt = QtWidgets.QLabel()
        self.lblTimeSecTxt.setFont(self.font_small)

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

        self.setStyleSheet("QLabel { color : " + self.foreground_color + "; }")

        # Header
        self.main_layout.addWidget(self.gui_element_builder.get_svg_widget(Gui_Element.END_LEFT, 20, 20, foreground_color),
                                   0, 0, Qt.AlignTop)
        self.main_layout.addWidget(self.gui_element_builder.get_svg_widget(Gui_Element.BUTTON, 20, 630, foreground_color),
                                   0, 1, 1, 3, Qt.AlignHCenter)
        self.main_layout.addWidget(self.gui_element_builder.get_svg_widget(Gui_Element.END_RIGHT, 20, 20, foreground_color),
                                   0, 5, Qt.AlignTop)

        #self.main_layout.addWidget(self.symbol, 0, 1)
        self.main_layout.addWidget(self.lblTimeTxt, 1, 0, 1, 3, Qt.AlignRight)
        # self.main_layout.itemAtPosition(1, 0).widget().setStyleSheet("background-color:" + "#ff00ff")
        self.main_layout.addWidget(self.lblTimeSecTxt, 1, 3, Qt.AlignLeft | Qt.AlignBottom)
        #self.main_layout.itemAtPosition(1, 3).widget().setStyleSheet("background-color:" + "#ff00ff")
        self.main_layout.addWidget(self.lblDateTxt, 3, 0, 1, 5, Qt.AlignHCenter)

        self.main_layout.addWidget(
            self.gui_element_builder.get_svg_widget(Gui_Element.END_LEFT, 10, 10, foreground_color),
            2, 0, Qt.AlignRight)
        self.main_layout.addWidget(
            self.gui_element_builder.get_svg_widget(Gui_Element.BUTTON, 10, 630, foreground_color),
            2, 1, 1, 2, Qt.AlignHCenter)
        self.main_layout.addWidget(
            self.gui_element_builder.get_svg_widget(Gui_Element.END_RIGHT, 10, 10, foreground_color),
            2, 5, Qt.AlignTop)

        self.setLayout(self.main_layout)

    def set_time(self):
        self.lblTimeTxt.setText(self.get_time().toString("hh:mm "))
        self.lblTimeSecTxt.setText(self.get_time().toString("ss"))

    @staticmethod
    def get_time() -> QTime:
        return QTime.currentTime()

    def get_name(self) -> str:
        return self.name
