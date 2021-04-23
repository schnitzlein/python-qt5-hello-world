from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QHBoxLayout, QGridLayout, QVBoxLayout
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt
from subscreens.clock import Clock
from gui.button import Button

class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("")
        self.screens_config = []
        self.current_screen = 0
        self.button = {}

    def say_hello(self):
        print("Button clicked, Hello!")

    def change_widget(self, widget: QWidget, direction: int):
        #print("len: " + str(len(self.screens_config["sub"])))
        max_screen = len(self.screens_config["sub"])
        if direction == 0:
            self.current_screen = (self.current_screen + 1) % max_screen
        elif direction == 1:
            self.current_screen = (self.current_screen - 1) % max_screen
        else:
            print("that not a valid direction")
        #for items in self.screens_config['sub']:
        #    print(items)
        b = QColor(self.screens_config['sub'][self.current_screen]["Background"])
        #print(self.screens_config['sub'][self.current_screen]["Background"])
        p = self.central_widget.palette()
        p.setColor(self.central_widget.backgroundRole(), b)
        self.central_widget.setPalette(p)
        self.central_widget.setAutoFillBackground(True)


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
            button_width = config['main']["button-size"][0]
            button_height = config['main']["button-size"][1]
            number_of_subs = config['main']["number-of-subs"]
        else:
            title = str(config['name'])
            self.setWindowTitle(title)
            #Set Resolution
            window_width = config["resolution"][0]
            window_height = config["resolution"][1]
            button_width = config["button-size"][0]
            button_height = config["button-size"][1]
            number_of_subs = config["number-of-subs"]
        self.setFixedSize(window_width, window_height)

        layout = QGridLayout()
        vbox = QVBoxLayout()

        hbox_titel = QHBoxLayout()
        hbox_titel.addStretch()
        hbox_titel.addWidget(QLabel(title))

        layout.addLayout(hbox_titel, 0, 1)
        layout.addLayout(vbox, 1, 0)

        button_up = QPushButton("\u1403")
        button_up.setFixedSize(button_width * window_width/100, button_height * window_height/100)
        button_down = QPushButton("\u1401")
        button_down.setFixedSize(button_width * window_width / 100, button_height * window_height / 100)

        #self.central_widget = QWidget()
        vbox.addWidget(button_up)
        button_width = button_width * window_width / 100
        button_height = button_height * window_height / 100
        background_color = "#f2eeed"
        for i in range(0, number_of_subs):
            button_color = self.screens_config['sub'][i]["Background"]
            self.button[i] = QPushButton(self.screens_config["sub"][i]["name"])
            self.button[i].setFixedSize(button_width, button_height)
            path_button = Button.build_svg(
                Button(button_width, button_height, button_color, background_color, self.screens_config["sub"][i]["name"] + "_button"))
            self.button[i].setStyleSheet("background-image: url(" + path_button + ");"
                                                                             "border:1px;"
                                                                             "background-color:" + background_color + ";")
            vbox.addWidget(self.button[i])

        vbox.addWidget(button_down)

        self.central_widget = Clock()
        layout.addWidget(self.central_widget, 1, 1)

        main_widget = QWidget()
        main_widget.setLayout(layout)


        # b = QColor(self.screens_config['sub'][1]["Background"])
        # print(self.screens_config['sub'][1]["Background"])
        # p = self.central_widget.palette()
        # p.setColor(self.central_widget.backgroundRole(), b)
        # self.central_widget.setPalette(p)
        # self.central_widget.setAutoFillBackground(True)
        # self.setAutoFillBackground(True)

        self.setCentralWidget(main_widget)

        # signals
        button_up.clicked.connect(lambda: self.change_widget(self.central_widget, 0))
        #print(type(central_widget))
        button_down.clicked.connect(lambda: self.change_widget(self.central_widget, 1))

