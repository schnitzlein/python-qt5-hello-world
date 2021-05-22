# TODO: add EventFilter https://doc.qt.io/qtforpython/overviews/eventsandfilters.html
# TODO: move coreitems for all subscreens qwidgets in common here

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QEvent, QPoint, Qt
from PyQt5.QtGui import QFont, QKeyEvent
from PyQt5.QtWidgets import (QDesktopWidget, QHBoxLayout, QLabel, QMessageBox,
                             QWidget)


class Base(QWidget):

    def __init__(self, name: str, foreground_color="#ffffff", font_name=""):
        super().__init__()

        if font_name != "":
            self.font = QFont(font_name, 80, QFont.Bold)
        else:
            self.font = QFont("LCARSGTJ3", 80, QFont.Bold)
        self.foreground_color = foreground_color
        self.name = name

    def get_name(self) -> str:
        return self.name
    
        
    