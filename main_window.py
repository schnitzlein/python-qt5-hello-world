from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QGridLayout, QHBoxLayout, QVBoxLayout, QListWidget, QListWidgetItem, QLayout
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QWidget, QStackedWidget, QAbstractItemView
from PyQt5.QtGui import QColor
from PyQt5.QtGui import QFont

from gui import *
from subscreens.clock import Clock
from subscreens.countup import Countup
from subscreens.placeholder import Placeholder
from PyQt5.QtCore import Qt, QRect


class MainWindow(QMainWindow):

    def __init__(self, resolution: QRect, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("")
        self.screens_config = []
        self.current_screen = 0
        self.sub_screens = {}
        self.button = {}
        self.central_widget = QStackedWidget()
        self.number_of_subs = 0
        self.main_widget = QWidget()
        self.main_layout = QGridLayout()
        self.gui_element_builder = GuiElementsBuilder()
        self.resolution = resolution

    def set_central_widget2(self, widget: QWidget):
        source_button = self.sender()
        print("set_central_widget2 WidgetName:  " + widget.getName())
        index = self.central_widget.widget(widget)
        self.central_widget.setCurrentIndex(index)

    def set_central_widget(self):
        source_button = self.sender()
        for i in range(0, self.number_of_subs):
            if self.central_widget.widget(i).get_name() == source_button.text():
                self.central_widget.setCurrentIndex(i)

    def close_main_window(self):
        self.close()

    def init_with_config(self, config: dict):
        self.screens_config = config

        # TODO: put in delegation or inheritance
        # Set Title
        title = str(config['main']['name'])
        self.setWindowTitle(title)
        # Set window flag
        flags = Qt.CustomizeWindowHint # Small Frame
        # flags = Qt.FramelessWindowHint # No Frame
        self.setWindowFlags(flags)
        # Set Resolution ######################################################
        # via config
        window_width = config['main']["resolution"][0]
        window_height = config['main']["resolution"][1]
        # via given screen geometry
        # window_width = self.resolution.width()
        # window_height = self.resolution.height()
        # Set Resolution End ##################################################

        button_width = config['main']["button-size"][0]
        button_height = config['main']["button-size"][1]

        front_color = config['main']["front_color"]
        background_color = config['main']["background_color"]
        font = config['main']["font"]

        self.number_of_subs = len(config['sub'])
        self.gui_element_builder.set_font(font)

        self.setFixedSize(window_width, window_height)

        self.main_widget.setLayout(self.main_layout)
        self.main_widget.setStyleSheet("background-color:" + background_color)
        vbox_menu = QVBoxLayout()
        vbox_menu.setSizeConstraint(QLayout.SetFixedSize)

        # Header
        self.main_layout.addWidget(self.gui_element_builder.get_svg_widget(Gui_Element.TOP_LEFT, 0, 0, front_color),
                                   0, 0, 1, 1)
        self.main_layout.addWidget(self.gui_element_builder.get_svg_widget(Gui_Element.BUTTON, 30, 590, front_color),
                                   0, 1, Qt.AlignTop)
        self.main_layout.addWidget(self.gui_element_builder.get_svg_widget(Gui_Element.BUTTON, 30, 53, front_color),
                                   0, 3, Qt.AlignTop)
        self.main_layout.addWidget(self.gui_element_builder.get_svg_widget(Gui_Element.END_RIGHT, 0, 0, front_color),
                                   0, 4, Qt.AlignTop)

        # Menu
        self.main_layout.addLayout(vbox_menu, 2, 0, 1, 1)
        # Central Window
        self.main_layout.addWidget(self.central_widget, 1, 1, 2, -1)
        # Footer
        self.main_layout.addWidget(self.gui_element_builder.get_svg_widget(Gui_Element.BOTTOM_LEFT, 0, 0, front_color),
                                   3, 0)
        self.main_layout.addWidget(self.gui_element_builder.get_svg_widget(Gui_Element.BUTTON, 30, 590, front_color),
                                   3, 1, Qt.AlignBottom)
        # Add Exit Button
        exit_button = QPushButton("EXIT")
        exit_button.setFont(QFont(font, 20, QFont.Bold))
        exit_button.setFixedSize(52, 30)
        exit_button.setStyleSheet("background:#ff0000; border:1px solid " + front_color + ";")
        exit_button.clicked.connect(lambda: self.close())

        self.main_layout.addWidget(exit_button,
                                   3, 3, Qt.AlignBottom)
        self.main_layout.addWidget(
            self.gui_element_builder.get_svg_widget(Gui_Element.END_RIGHT, 0, 0, front_color, font),
            3, 4, Qt.AlignBottom)

        button_list_widget = QListWidget()
        # button_ListWidget.setVerticalScrollMode(QAbstractItemView.ScrollMode.ScrollPerItem)
        button_list_widget.setStyleSheet(
            "QListWidget{background:" + background_color + ";  border: 0px solid " + front_color + ";}")

        # Erstellen der rechten Button-Leiste ##############
        button_width = button_width * window_width / 100
        button_height = button_height * window_height / 100
        button_size = QSize(button_width, button_height)
        for i in range(0, self.number_of_subs):
            sub_button_list_item = QListWidgetItem(button_list_widget)
            placeholder_list_item = QListWidgetItem(button_list_widget)
            placeholder_list_item.setSizeHint(QSize(button_width, 4))
            placeholder_list_item.setBackground(QColor(background_color))

            flag = placeholder_list_item.flags() & Qt.ItemIsUserCheckable
            placeholder_list_item.setFlags(flag)
            # Widgets ##################################################################################################
            if i == 0:
                self.central_widget.insertWidget(i, Clock(self.screens_config['sub'][i]["Background"]))
                #self.central_widget.setStyleSheet("background-color:" + "#ffffff") # Show size of Central_Widget
            elif i == 1:
                self.central_widget.insertWidget(i, Countup(self.screens_config['sub'][i]["Background"]))
            else:
                self.central_widget.insertWidget(i, Placeholder(self.screens_config["sub"][i]["name"], self.screens_config['sub'][i]["Background"]))

            # Buttons ##################################################################################################
            button_color = self.screens_config['sub'][i]["Background"]
            self.button[i] = QPushButton(self.screens_config["sub"][i]["name"], self)
            self.button[i].setFixedSize(button_size)

            button_layout = QVBoxLayout()
            button_layout.addWidget(
                self.gui_element_builder.get_svg_widget(
                    Gui_Element.BUTTON_FULL_CIRCLE_TEXT,
                    button_height,
                    button_width,
                    button_color, self.screens_config["sub"][i]["name"]))
            button_layout.setContentsMargins(0, 0, 0, 0)
            self.button[i].setLayout(button_layout)
            self.button[i].setStyleSheet("border:1px;")

            sub_button_list_item.setSizeHint(button_size)
            button_list_widget.addItem(placeholder_list_item)
            button_list_widget.addItem(sub_button_list_item)
            button_list_widget.setItemWidget(sub_button_list_item, self.button[i])
            # signals ##################################################################################################
            self.button[i].clicked.connect(lambda widget=self.central_widget.widget(i): self.set_central_widget())

        vbox_menu.addWidget(button_list_widget)
        button_list_widget.setMaximumWidth(1000)
        button_list_widget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        button_list_widget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        button_list_widget.setMaximumWidth(button_list_widget.sizeHintForColumn(0))

        #############################################
        self.central_widget.setCurrentIndex(2)
        self.setCentralWidget(self.main_widget)
