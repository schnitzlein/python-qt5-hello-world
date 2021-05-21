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
        self.gui_button_builder = GuiButtonBuilder()
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

        # Menu #########################################################################################################
        button_height = 60
        button_width = 96
        self.vbox_menu = QVBoxLayout()
        self.vbox_menu.setSizeConstraint(QLayout.SetFixedSize)
        self.vbox_menu.addWidget(self.gui_element_builder.get_svg_widget(Gui_Element.TOP_LEFT_SHORT, 61, 120, foreground_color), Qt.AlignTop)
        self.gui_button_builder.set_color(self.foreground_color)
        self.gui_button_builder.set_size(button_height, button_width)
        button = self.gui_button_builder.create_button("Clock", Gui_Element.BUTTON_TEXT)
        self.vbox_menu.addWidget(button)
        button2 = self.gui_button_builder.create_button("Timer", Gui_Element.BUTTON_TEXT)
        self.vbox_menu.addWidget(button2)
        #placeholder = self.gui_element_builder.get_svg_widget(Gui_Element.BUTTON, 170, button_width, foreground_color)
        self.vbox_menu.addWidget(self.gui_element_builder.get_svg_widget(Gui_Element.BUTTON, 172, button_width, foreground_color))
        #self.vbox_menu.addWidget(
        #    self.gui_element_builder.get_svg_widget(Gui_Element.BOTTOM_LEFT_SHORT, 41, 120, foreground_color),
        #    Qt.AlignBottom)
        #self.vbox_menu.addWidget(
        #    self.gui_element_builder.get_svg_widget(Gui_Element.TOP_LEFT_SHORT, 61, 120, foreground_color), Qt.AlignTop)
        self.vbox_menu.addWidget(self.gui_element_builder.get_svg_widget(Gui_Element.BOTTOM_LEFT_SHORT, 41, 120, foreground_color), Qt.AlignBottom)

        self.main_layout.addLayout(self.vbox_menu, 0, 0, 5, 1)
        # End Menu #####################################################################################################

        # Header
        self.main_layout.addWidget(self.gui_element_builder.get_svg_widget(Gui_Element.BUTTON, 20, 640, foreground_color),
                                   0, 1, 1, 3, Qt.AlignTop)
        self.main_layout.addWidget(self.gui_element_builder.get_svg_widget(Gui_Element.END_RIGHT, 20, 20, foreground_color),
                                   0, 5, Qt.AlignTop)

        #self.main_layout.addWidget(self.symbol, 0, 1)
        # Clock Hours Minutes
        self.main_layout.addWidget(self.lblTimeTxt, 1, 0, 1, 3, Qt.AlignRight)
        # self.main_layout.itemAtPosition(1, 0).widget().setStyleSheet("background-color:" + "#ff00ff")
        # Clock Seconds
        self.main_layout.addWidget(self.lblTimeSecTxt, 1, 3, Qt.AlignLeft | Qt.AlignBottom)

        self.main_layout.addWidget(
            self.gui_element_builder.get_svg_widget(Gui_Element.BUTTON, 10, 640, foreground_color),
            2, 1, 1, 3, Qt.AlignLeft)
        self.main_layout.addWidget(
            self.gui_element_builder.get_svg_widget(Gui_Element.END_RIGHT, 10, 10, foreground_color),
            2, 5, Qt.AlignTop)
        #self.main_layout.itemAtPosition(1, 3).widget().setStyleSheet("background-color:" + "#ff00ff")
        # Date
        self.main_layout.addWidget(self.lblDateTxt, 3, 0, 1, 5, Qt.AlignHCenter)

        self.main_layout.addWidget(
            self.gui_element_builder.get_svg_widget(Gui_Element.BUTTON, 13, 640, foreground_color),
            4, 1, 1, 2, Qt.AlignBottom)
        self.main_layout.addWidget(
            self.gui_element_builder.get_svg_widget(Gui_Element.END_RIGHT, 13, 10, foreground_color),
            4, 5, Qt.AlignLeft | Qt.AlignBottom)

        self.setLayout(self.main_layout)

    def set_time(self):
        self.lblTimeTxt.setText(self.get_time().toString("hh:mm "))
        self.lblTimeSecTxt.setText(self.get_time().toString("ss"))

    @staticmethod
    def get_time() -> QTime:
        return QTime.currentTime()

    def get_name(self) -> str:
        return self.name
