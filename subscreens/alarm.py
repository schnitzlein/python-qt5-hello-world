from PyQt5.QtWidgets import QWidget
from subscreens.baseclass import Base
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from gui.gui_button_builder import GuiButtonBuilder
from gui.gui_element import Gui_Element
from util.eventhandler.observer import Observer

class Alarm(Base):
    def __init__(self, observer: Observer, name, foreground_color="#ffffff", parent=None):
        super().__init__(name, observer)
        self.parent = parent
        self.name = name
        self.main_layout = QGridLayout()
        self.font = QFont("LCARSGTJ3", 80, QFont.Bold)
        self.subscreen_name = QLabel("Subscreen:")
        self.subscreen_name.setFont(self.font)
        self.info_msg_label = QLabel("Alarm Reason")
        self.info_msg_label.setFont(self.font)
        self.info_msg_label.setStyleSheet("QLabel { color : " + self.foreground_color + ";}")
        self.foreground_color = foreground_color
        self.setStyleSheet("background-color : #775500;")
        self.gui_button_builder = GuiButtonBuilder()
        self.gui_button_builder.set_color(foreground_color)
        self.gui_button_builder.set_size(50, 100)
        self.main_layout.addWidget(self.subscreen_name, 1, 0, 1, 1, Qt.AlignHCenter)
        self.main_layout.addWidget(self.info_msg_label, 2, 0, 1, 1, Qt.AlignHCenter)
        self.close_button = self.gui_button_builder.create_button("Close", Gui_Element.BUTTON_FULL_CIRCLE_TEXT)
        self.main_layout.addWidget(self.close_button, 3, 2, 1, 2, Qt.AlignLeft)

        self.setLayout(self.main_layout)
        self.close_button.clicked.connect(lambda: self.close_alarm_widget())

    def set_alarm_text(self, msg: dict):
        self.subscreen_name.setText(msg["subscreen_name"])
        self.info_msg_label.setText(msg["msg"])

    def close_alarm_widget(self):
        if self.parent is not None:
            self.parent.toggle_main_widget(0)
