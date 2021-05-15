import sys
import PyQt5
from PyQt5.QtWidgets import QWidget,QPushButton,QApplication,QListWidget,QGridLayout,QLabel
from PyQt5.QtCore import QTimer,QDateTime,QThread,QEventLoop

class DataCaptureThread(QThread):
    def collectProcessData(self):
        print ("Collecting Process Data")

    def __init__(self, *args, **kwargs):
        QThread.__init__(self, *args, **kwargs)
        self.dataCollectionTimer = QTimer()
        self.dataCollectionTimer.moveToThread(self)
        self.dataCollectionTimer.timeout.connect(self.collectProcessData)
        # self.dataCollectionTimer.timeout.connect(lambda:self.collectProcessData)

    def run(self):
        self.dataCollectionTimer.start(1000)
        loop = QEventLoop()
        loop.exec_()


class WinForm(QWidget):
    def __init__(self,parent=None):
        super(WinForm, self).__init__(parent)
        self.setWindowTitle('QTimer Thread example')

        self.listFile=QListWidget()
        self.label=QLabel('Label')
        self.startBtn=QPushButton('Start')
        self.endBtn=QPushButton('Stop')

        layout=QGridLayout()

        self.dataCollectionThread = DataCaptureThread()
        

        self.timer=QTimer()
        self.timer.timeout.connect(self.showTime)

        layout.addWidget(self.label,0,0,1,2)
        layout.addWidget(self.startBtn,1,0)
        layout.addWidget(self.endBtn,1,1)

        self.startBtn.clicked.connect(self.startTimer)
        self.endBtn.clicked.connect(self.endTimer)

        self.setLayout(layout)

    def showTime(self):
        time=QDateTime.currentDateTime()
        timeDisplay=time.toString('yyyy-MM-dd hh:mm:ss dddd')
        self.label.setText(timeDisplay)

    def startTimer(self):
        self.dataCollectionThread.start()
        self.timer.start(1000)
        self.startBtn.setEnabled(False)
        self.endBtn.setEnabled(True)

    def endTimer(self):
        self.dataCollectionThread.terminate()
        self.timer.stop()
        self.startBtn.setEnabled(True)

def main():
     # a new app instance
     app = QApplication(sys.argv)
     form = WinForm()
     form.show()
     sys.exit(app.exec_())

if __name__ == "__main__":
     main()
