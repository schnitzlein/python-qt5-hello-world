# TODO: add EventFilter https://doc.qt.io/qtforpython/overviews/eventsandfilters.html
# TODO: move coreitems for all subscreens qwidgets in common here

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QEvent, QPoint, Qt
from typing import List
from util.eventhandler.observer import Observer
from PyQt5.QtGui import QFont, QKeyEvent
from PyQt5.QtWidgets import (QDesktopWidget, QHBoxLayout, QLabel, QMessageBox,
                             QWidget)


class Base(QWidget):

    def __init__(self, observer: Observer, name: str, foreground_color="#ffffff", font_name=""):
        super().__init__()

        if font_name != "":
            self.font = QFont(font_name, 80, QFont.Bold)
        else:
            self.font = QFont("LCARSGTJ3", 80, QFont.Bold)
        self.foreground_color = foreground_color
        self.name = name
        self.observers: List[Observer] = []
        self.msg = {
            "subscreen_name": "",
            "msg": ""
        }
        self.attach(observer)


    def get_name(self) -> str:
        return self.name

    def attach(self, observer: Observer) -> None:
        self.observers.append(observer)
        pass

    def detach(self, observer: Observer) -> None:
        self.observers.remove(observer)
        pass

    def notify(self) -> None:
        for observer in self._observers:
            observer.update_from_subscreen(self.msg)
