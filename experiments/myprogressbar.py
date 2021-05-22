import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import QObject, QThread, pyqtSignal
from time import sleep

class Worker_InitData(QObject):
    finished = pyqtSignal()
    progress = pyqtSignal(int)

    def run(self):
        """Long-running task."""
        for i in range(30):
            sleep(1)
            self.progress.emit(i)
        self.finished.emit()

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("My MainWindow")
        self.qProgressBar = QtWidgets.QProgressBar(self)
        self.qProgressBar.setGeometry(100, 100, 200, 30)

        self.label = QtWidgets.QLabel("Hello", self)
        self.label.setGeometry(50, 50, 200, 20)

        self.initData()

    def reportProgress(self, i):
        self.qProgressBar.setValue(int((i+1)/30*100))
    
    def initData(self):
        # Step 2: Create a QThread object
        self.thread = QThread()
        # Step 3: Create a worker object
        self.worker = Worker_InitData()
        # Step 4: Move worker to the thread
        self.worker.moveToThread(self.thread)
        # Step 5: Connect signals and slots
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.worker.progress.connect(self.reportProgress)
        # Step 6: Start the thread
        self.thread.start()
   
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    w = MainWindow()
    screen = QtWidgets.QDesktopWidget().screenGeometry()
    w.setGeometry(screen.width()//2-200, screen.height()//2-200, 400, 400) # x, y, Width, Height
    w.show()
    
    sys.exit(app.exec_())
