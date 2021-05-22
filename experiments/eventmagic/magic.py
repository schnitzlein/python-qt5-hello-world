from PyQt5 import QtCore, QtWidgets
from globalobject import GlobalObject


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        button = QtWidgets.QPushButton(text="Press me", clicked=self.on_clicked)
        self.setCentralWidget(button)

    @QtCore.pyqtSlot()
    def on_clicked(self):
        GlobalObject().dispatchEvent("hello")


class Widget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        GlobalObject().addEventListener("hello", self.foo)
        self._label = QtWidgets.QLabel()
        lay = QtWidgets.QVBoxLayout(self)
        lay.addWidget(self._label)

    @QtCore.pyqtSlot()
    def foo(self):
        self._label.setText("foo")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    w1 = MainWindow()
    w2 = Widget()
    w1.show()
    w2.show()
    sys.exit(app.exec_())
