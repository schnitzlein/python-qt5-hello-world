from PyQt5.QtWidgets import QWidget, QLabel, QHBoxLayout
from PyQt5.QtGui import QFont

class Placeholder(QWidget):

    def __init__(self, name: str, foreground_color="#ffffff", font_name=""):
        super().__init__()

        self.f = QFont(font_name, 80, QFont.Bold)
        self.foreground_color = foreground_color
        self.name = name
        self.symbol = QLabel(self.name)
        self.symbol.setFont(self.f)
        self.symbol.setStyleSheet("QLabel { color : " + self.foreground_color + "; }")

        self.hbox = QHBoxLayout()
        self.hbox.addStretch()
        self.hbox.addWidget(self.symbol)
        self.hbox.addStretch()

        self.setLayout(self.hbox)

    def get_name(self) -> str:
        return self.name