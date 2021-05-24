import sys
from PyQt5.QtCore import QTime, QTimer, QDate, Qt
from PyQt5 import QtWidgets
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QVBoxLayout, QGridLayout, QHBoxLayout, QLayout
from PyQt5.QtWidgets import QApplication, QWidget
from gui import *
from gui.gui_button_builder import GuiButtonBuilder

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

        self.setStyleSheet("QLabel { color : " + self.foreground_color + "; }")

        # Clock Hours Minutes
        self.main_layout.addWidget(self.lblTimeTxt, 0, 0, 1, 5, Qt.AlignHCenter)
        # Clock Seconds
        #self.main_layout.addWidget(self.lblTimeSecTxt, 0, 3, Qt.AlignRight | Qt.AlignBottom)

        self.main_layout.addWidget(
            self.gui_element_builder.get_svg_widget(Gui_Element.END_LEFT, 20, 10, foreground_color),
            1, 0, Qt.AlignTop)
        self.main_layout.addWidget(
            self.gui_element_builder.get_svg_widget(Gui_Element.BUTTON, 20, 590, foreground_color),
            1, 1, 1, 3, Qt.AlignLeft)
        self.main_layout.addWidget(
            self.gui_element_builder.get_svg_widget(Gui_Element.END_RIGHT, 20, 10, foreground_color),
            1, 5, Qt.AlignTop)

        # Date
        self.main_layout.addWidget(self.lblDateTxt, 2, 0, 1, 5, Qt.AlignHCenter)

        self.setLayout(self.main_layout)

    def set_time(self):
        self.lblTimeTxt.setText(self.get_time().toString("hh:mm "))
        #self.lblTimeSecTxt.setText(self.get_time().toString("ss"))

    @staticmethod
    def get_time() -> QTime:
        return QTime.currentTime()

    def get_name(self) -> str:
        return self.name
