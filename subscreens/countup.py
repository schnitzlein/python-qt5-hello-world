from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtGui import QFont
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QWidget,QPushButton,QApplication,QListWidget,QGridLayout,QLabel,QMessageBox
from PyQt5.QtCore import QTimer,QDateTime

class Countup(QWidget):

    def __init__(self, name: str, foreground_color="#ffffff", font_name=""):
        super().__init__()

        if font_name != "":
            self.font = QFont(font_name, 80, QFont.Bold)
        else:
            self.font = QFont("LCARSGTJ3", 80, QFont.Bold)

        self.foreground_color = foreground_color
        self.name = "Countup"
        self.symbol = QLabel(self.name)
        self.symbol.setFont(self.font)
        self.symbol.setStyleSheet("QLabel { color : " + self.foreground_color + "; }, QButton { color: "+ self.foreground_color + "; }")

        self.listFile=QListWidget()
        self.label=QLabel('Label')
        self.startBtn=QPushButton('Start')
        self.endBtn=QPushButton('Stop')

        self.label.setFont(self.font)
        self.startBtn.setFont(self.font)
        self.endBtn.setFont(self.font)
        self.setStyleSheet("QLabel { color : " + self.foreground_color + "; }")

        self.time_start = None
        self.time_end = None

        layout=QGridLayout()

        self.timer=QTimer()
        self.timer.timeout.connect(self.showTime)

        layout.addWidget(self.label,0,0,1,2)
        layout.addWidget(self.startBtn,1,0)
        layout.addWidget(self.endBtn,1,1)

        self.startBtn.clicked.connect(self.startTimer)
        self.endBtn.clicked.connect(self.endTimer)

        self.setLayout(layout)

    def showTime(self):
        self.time=QDateTime.currentDateTime()
        # timeDisplay=self.time.toString('yyyy-MM-dd hh:mm:ss dddd')
        timeDisplay=self.time.toString('hh:mm:ss')
        self.label.setText(timeDisplay)

    def startTimer(self):
        self.timer.start(1000)
        self.startBtn.setEnabled(False)
        self.endBtn.setEnabled(True)
        self.time_start = QDateTime.currentDateTime()

    def endTimer(self):
        self.timer.stop()
        self.startBtn.setEnabled(True)
        self.endBtn.setEnabled(False)
        diff = self.diffTime()
        if diff:
            QMessageBox.about(self, "Timer Info", "Timer stopped, diff {}".format(diff))
        else:
            QMessageBox.about(self, "Timer Info", "Timer stopped.")
        # reset
        self.time_start = None
        self.time_end = None

    def diffTime(self) -> int:
        if self.time_start:
            self.time_end=QDateTime.currentDateTime()
            secondsDiff = self.time_start.secsTo(self.time_end) # msecsTo is millisecs
            print(secondsDiff)
            return secondsDiff

    def get_name(self) -> str:
        return self.name

    def get_TimerTime(self) -> QDateTime:
        return self.time
