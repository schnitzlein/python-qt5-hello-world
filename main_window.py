from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QGridLayout, QVBoxLayout, QListWidget, QListWidgetItem, QLayout
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QWidget, QStackedWidget

from gui import *
from subscreens.clock import Clock
from subscreens.placeholder import Placeholder


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("")
        self.screens_config = []
        self.current_screen = 0
        self.sub_screens = {}
        self.button = {}
        self.central_widget = QStackedWidget()
        self.number_of_subs = 0
        self.main_layout = QGridLayout()
        self.gui_element_builder = GuiElementsBuilder()

    def say_hello(self):
        print("Button clicked, Hello!")

    def set_central_widget2(self, widget: QWidget):
        source_button = self.sender()
        print("set_central_widget2 WidgetName:  " + widget.getName())
        index = self.central_widget.widget(widget)
        self.central_widget.setCurrentIndex(index)

    def set_central_widget(self):
        source_button = self.sender()
        for i in range(0, self.number_of_subs):
            if self.central_widget.widget(i).getName() == source_button.text():
                self.central_widget.setCurrentIndex(i)

    def change_widget(self, widget: QWidget, direction: int):
        # print("len: " + str(len(self.screens_config["sub"])))
        max_screen = len(self.screens_config["sub"])
        if direction == 0:
            self.central_widget.setCurrentIndex((self.central_widget.currentIndex() - 1) % max_screen)
            # self.current_screen = (self.current_screen + 1) % max_screen
        elif direction == 1:
            self.central_widget.setCurrentIndex((self.central_widget.currentIndex() + 1) % max_screen)
            # self.current_screen = (self.current_screen - 1) % max_screen
        else:
            print("that not a valid direction")

        # Farbe sollte im Widget selbst geetzt werden bzw. schon bei Erstellung
        # for items in self.screens_config['sub']:
        # b = QColor(self.screens_config['sub'][self.current_screen]["Background"])
        # b = QColor(self.screens_config['sub'][self.central_widget.currentIndex()]["Background"])
        # p = self.central_widget.palette()
        # p.setColor(self.central_widget.backgroundRole(), b)
        # self.central_widget.setPalette(p)
        # self.central_widget.setAutoFillBackground(True)

    def init_with_config(self, config: dict):
        self.screens_config = config

        # TODO: put in delegation or inheritance
        # Set Title
        if 'name' not in config:
            title = str(config['main']['name'])
            self.setWindowTitle(title)
            # Set Resolution
            window_width = config['main']["resolution"][0]
            window_height = config['main']["resolution"][1]
            button_width = config['main']["button-size"][0]
            button_height = config['main']["button-size"][1]
            self.number_of_subs = len(config['sub'])
        else:
            title = str(config['name'])
            self.setWindowTitle(title)
            # Set Resolution
            window_width = config["resolution"][0]
            window_height = config["resolution"][1]
            button_width = config["button-size"][0]
            button_height = config["button-size"][1]
            self.number_of_subs = len(self.screens_config["sub"])
        self.setFixedSize(window_width, window_height)

        main_widget = QWidget()
        main_widget.setLayout(self.main_layout)
        vbox_menu = QVBoxLayout()
        vbox_menu.setSizeConstraint(QLayout.SetFixedSize)

        system_color = "#ffd966"

        # Header
        self.main_layout.addWidget(self.gui_element_builder.get_svg_widget(Gui_Element.TOP_LEFT, 0, 0), 0, 0)
        self.main_layout.addWidget(self.gui_element_builder.get_svg_widget(Gui_Element.BUTTON, 30, 650), 0, 1,
                                   Qt.AlignTop)
        self.main_layout.addWidget(self.gui_element_builder.get_svg_widget(Gui_Element.END_RIGHT, 0, 0), 0, 3,
                                   Qt.AlignTop)

        # Menu
        self.main_layout.addLayout(vbox_menu, 1, 0)

        # Footer
        self.main_layout.addWidget(self.gui_element_builder.get_svg_widget(Gui_Element.BOTTOM_LEFT, 0, 0), 2, 0)
        self.main_layout.addWidget(self.gui_element_builder.get_svg_widget(Gui_Element.BUTTON, 30, 650), 2, 1,
                                   Qt.AlignBottom)
        self.main_layout.addWidget(self.gui_element_builder.get_svg_widget(Gui_Element.END_RIGHT, 0, 0), 2, 3,
                                   Qt.AlignBottom)

        # button_stylesheet = "background-color:" + system_color +"; border-width: 2px; border-radius: 36px; bordericolor: black; font: bold 14px; min-width: 10em; padding: 6px;"
        # button_up = QPushButton("\u1403")
        # button_up.setFixedSize(button_width * window_width/100, button_height * window_height/100)
        # button_up.setStyleSheet(button_stylesheet)
        #
        # button_down = QPushButton("\u1401")
        # button_down.setFixedSize(button_width * window_width / 100, button_height * window_height / 100)
        # button_down.setStyleSheet(button_stylesheet)

        button_ListWidget = QListWidget()
        button_ListWidget.setStyleSheet("""QListWidget{background: #f2eeed;  border: 0px solid #f2eeed;}""")
        # Erstellen der rechten Button-Leiste ##############
        # vbox_menu.addWidget(button_up)
        button_width = button_width * window_width / 100
        button_height = button_height * window_height / 100
        background_color = "#f2eeed"
        button_size = QSize(button_width, button_height)
        for i in range(0, self.number_of_subs):
            subbutton_list_item = QListWidgetItem(button_ListWidget)
            placeholder_listItem = QListWidgetItem(button_ListWidget)
            placeholder_listItem.setSizeHint(QSize(button_width, 4))

            flag = placeholder_listItem.flags() & Qt.ItemIsUserCheckable
            placeholder_listItem.setFlags(flag)
            # subbutton_listItem.setBackground(QColor("#f2eeed"))
            # Widgets ##################################################################################################
            if i == 0:
                self.central_widget.insertWidget(i, Clock())
            else:
                self.central_widget.insertWidget(i, Placeholder(self.screens_config["sub"][i]["name"]))
            # Buttons ##################################################################################################
            button_color = self.screens_config['sub'][i]["Background"]
            self.button[i] = QPushButton(self.screens_config["sub"][i]["name"], self)
            self.button[i].setFixedSize(button_size)

            # Button with stylsheet
            # self.button[i].setStyleSheet("background-color:" +button_color +"; border-width: 2px; border-radius: 10px; bordericolor: black; font: bold 14px; min-width: 10em; padding: 6px;")

            button_layout = QVBoxLayout()
            button_layout.addWidget(
                self.gui_element_builder.get_svg_widget(
                    Gui_Element.BUTTON_FULL_CIRCLE,
                    button_height,
                    button_width,
                    button_color))
            button_layout.setContentsMargins(0, 0, 0, 0)
            self.button[i].setLayout(button_layout)
            self.button[i].setStyleSheet("border:1px;")

            # print("Button: " + self.button[i].text() + "Screen: " + self.central_widget.widget(i).getName())
            # signals ##################################################################################################
            # self.button[i].clicked.connect(lambda widget=self.central_widget.widget(i): self.set_central_widget2(self, widget))
            self.button[i].clicked.connect(lambda widget=self.central_widget.widget(i): self.set_central_widget())
            subbutton_list_item.setSizeHint(button_size)
            # print(self.button[i].size())
            #
            button_ListWidget.addItem(placeholder_listItem)
            button_ListWidget.addItem(subbutton_list_item)
            button_ListWidget.setItemWidget(subbutton_list_item, self.button[i])
            button_ListWidget.setMaximumWidth(1000)
            # vbox_menu.addWidget(self.button[i])

        vbox_menu.addWidget(button_ListWidget)
        # vbox_menu.addWidget(button_down)
        # downbutton_listItem = QListWidgetItem(button_ListWidget)
        # downbutton_listItem.setSizeHint(button_down.size())
        # button_ListWidget.addItem(downbutton_listItem)
        # button_ListWidget.setItemWidget(downbutton_listItem, button_down)
        button_ListWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        button_ListWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        button_ListWidget.setMaximumWidth(button_ListWidget.sizeHintForColumn(0))

        #############################################
        self.central_widget.setCurrentIndex(1)
        self.main_layout.addWidget(self.central_widget, 1, 1)

        self.setCentralWidget(main_widget)

        # signals
        # button_up.clicked.connect(lambda: self.change_widget(self.central_widget, 0))
        # button_down.clicked.connect(lambda: self.change_widget(self.central_widget, 1))
