from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("")
        self.screens_config = []
        self.current_screen = 0
        

    def say_hello(self):                                                                                     
        print("Button clicked, Hello!")

    def change_widget(self, widget: QWidget, direction: str):
        max_screen = len( self.screens_config )
        if direction == ">":
            self.current_screen = (self.current_screen + 1) % max_screen
        elif direction == "<":
            self.current_screen = (self.current_screen - 1) % max_screen
        else:
            print("that not a valid direction")
        #for items in self.screens_config['sub']:
        #    print(items)
        b = self.screens_config['sub'][self.current_screen]["Background"]
        p = widget.palette()
        p.setColor(widget.backgroundRole(), Qt.red)
        widget.setPalette(p)

    def init_with_config(self, config: dict):
        self.screens_config = config

        # TODO: put in delegation or inheritance
        #Set Title
        if 'name' not in config:
            title = str(config['main']['name'])
            self.setWindowTitle(title)
            #Set Resolution
            window_width = config['main']["resolution"][0]
            window_height = config['main']["resolution"][1]
            button_width = config['main']["button"][0]
            button_height = config['main']["button"][1]
        else:
            title = str(config['name'])
            self.setWindowTitle(title)
            #Set Resolution
            window_width = config["resolution"][0]
            window_height = config["resolution"][1]
            button_width = config["button"][0]
            button_height = config["button"][1]
        self.setFixedSize(window_width, window_height)

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

        self.setAutoFillBackground(True)
        self.setCentralWidget(main_widget)

        # signals
        button_left.clicked.connect(self.say_hello)
        button_right.clicked.connect(self.change_widget(central_widget, ">"))
