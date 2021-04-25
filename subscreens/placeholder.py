from PyQt5.QtWidgets import QWidget, QLabel, QHBoxLayout
from PyQt5.QtGui import QFont

class Placeholder(QWidget):

    def __init__(self, name: str):
        super().__init__()

        self.f = QFont("LCARSGTJ3", 80, QFont.Bold)

        self.name = name
        self.symbol = QLabel(self.name)
        self.symbol.setFont(self.f)

        self.hbox = QHBoxLayout()
        self.hbox.addStretch()
        self.hbox.addWidget(self.symbol)
        self.hbox.addStretch()

        self.setLayout(self.hbox)
        #self.show()

    def getName(self) -> str:
        return self.name