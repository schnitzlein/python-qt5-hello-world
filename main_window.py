from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("")

        # label = QLabel("This is a PyQt5 window!")
        #
        # # The `Qt` namespace has a lot of attributes to customise
        # # widgets. See: http://doc.qt.io/qt-5/qt.html
        # label.setAlignment(Qt.AlignCenter)
        #
        # # Set the central widget of the Window. Widget will expand
        # # to take up all the space in the window by default.
        # self.setCentralWidget(label)

    def init_with_config(self, config: dict):

        title = str(config['name'])
        self.setWindowTitle(title)

        nWidth = config["resolution"][0]
        nHight = config["resolution"][1]
        self.setFixedSize(nWidth, nHight)

