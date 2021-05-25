from PyQt5.QtCore import QPoint, Qt
from PyQt5.QtWidgets import QDesktopWidget, QHBoxLayout, QLabel

from subscreens.baseclass import Base


class Movesub(Base):

    def __init__(self, name: str, foreground_color="#ffffff", font_name=""):
        super().__init__(name, foreground_color, font_name)

        # Centering QWidget
        self.pressing = False
        self.start = QPoint(0, 0)
        self.center()
        self.oldPos = self.pos()

        self.symbol = QLabel(self.name)
        self.symbol.setFont(self.font)
        self.symbol.setStyleSheet(
            "QLabel { color : " + self.foreground_color + "; }, QButton { color: " + self.foreground_color + "; }")

        self.hbox = QHBoxLayout()
        self.hbox.addStretch()
        self.hbox.addWidget(self.symbol)
        self.hbox.addStretch()

        self.setLayout(self.hbox)

    def mouseReleaseEvent(self, event):
        self.pressing = False
        print("pressing released?: {}".format(self.pressing))

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()
        if event.button() == Qt.RightButton:
            print("barfoo right button")
        print("New Position: {}".format(self.oldPos))

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

    def center(self):
        qt_rectangle = self.frameGeometry()
        # print(qtRectangle)
        center_point = QDesktopWidget().availableGeometry().center()
        qt_rectangle.moveCenter(center_point)
        self.move(qt_rectangle.topLeft())
