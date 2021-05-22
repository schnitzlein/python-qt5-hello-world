from PyQt5.QtCore import QPoint, Qt
from PyQt5.QtWidgets import QAction, QDesktopWidget, QHBoxLayout, QLabel, QMenu

from subscreens.baseclass import Base


class Movesub(Base):

    def __init__(self, name: str, foreground_color="#ffffff", font_name=""):
        super().__init__(name, foreground_color, font_name)

        # Centering QWidget
        self.pressing = False
        self.start = QPoint(0, 0)
        self.center()
        self.oldPos = self.pos()  

        # TODO: child class
        self.symbol = QLabel(self.name)
        self.symbol.setFont(self.font)
        self.symbol.setStyleSheet("QLabel { color : " + self.foreground_color + "; }, QButton { color: "+ self.foreground_color + "; }")

        self.hbox = QHBoxLayout()
        self.hbox.addStretch()
        self.hbox.addWidget(self.symbol)
        self.hbox.addStretch()

        self.setLayout(self.hbox)
    
    def mouseReleaseEvent(self, QMouseEvent):
        self.pressing = False
        print("pressing released?: {}".format(self.pressing))

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()
        if event.button() == Qt.RightButton:
            print("barfoo right button")
        print("New Position: {}".format(self.oldPos))

    def mouseMoveEvent(self, event):
        delta = QPoint (event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

    def center(self):
        qtRectangle = self.frameGeometry()
        #print(qtRectangle)
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())
