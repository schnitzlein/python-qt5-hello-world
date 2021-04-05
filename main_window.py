from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QPushButton

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

        #Set Title
        title = str(config['name'])
        self.setWindowTitle(title)

        #Set Resolution
        window_width = config["resolution"][0]
        window_height = config["resolution"][1]
        self.setFixedSize(window_width, window_height)

        button_width = config["button"][0]
        button_height = config["button"][1]

        layout = QHBoxLayout()
        button_left = QPushButton("<")
        button_left.setFixedSize(button_width * window_width/100, button_height * window_height/100)
        button_right = QPushButton(">")
        button_right.setFixedSize(button_width * window_width / 100, button_height * window_height / 100)

        central_widget = QWidget()
        layout.addWidget(button_left)
        layout.addWidget(central_widget)
        layout.addWidget(button_right)
        main_widget = QWidget()
        main_widget.setLayout(layout)

        self.setCentralWidget(main_widget)



