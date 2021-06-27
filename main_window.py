from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QGridLayout, QVBoxLayout, QListWidget, QListWidgetItem, QLayout
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QWidget, QStackedWidget
from PyQt5.QtGui import QColor
from PyQt5.QtGui import QFont

from gui import *
from gui.gui_button_builder import GuiButtonBuilder
from gui.gui_subscreen_builder import GuiSubscreenBuilder
from PyQt5.QtCore import Qt, QRect
from util.eventhandler.alarm_observer import AlarmObserver
from subscreens.alarm import Alarm


class MainWindow(QMainWindow):
    def __init__(self, resolution: QRect, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("")
        self.screens_config = []
        self.current_screen = 0
        self.sub_screens = {}
        self.button = {}
        self.subscreen_stacked_widget = QStackedWidget()
        self.number_of_subs = 0
        self.main_stack_widget = QStackedWidget()
        self.main_widget = QWidget()
        self.main_layout = QGridLayout()
        self.gui_element_builder = GuiElementsBuilder()
        self.gui_button_builder = GuiButtonBuilder()
        self.gui_subscreen_builder = GuiSubscreenBuilder()
        self.resolution = resolution
        self.alarm_observer = AlarmObserver(self)
        self.alarm_widget = Alarm(self.alarm_observer, "Alarm_Widget", "#550055", self)

    def set_current_subscreen(self):
        source_button = self.sender()
        for i in range(0, self.number_of_subs):
            if self.subscreen_stacked_widget.widget(i).get_name() == source_button.text():
                self.subscreen_stacked_widget.setCurrentIndex(i)

    def toggle_main_widget(self, index: int):
        max_value = self.main_stack_widget.count()
        self.main_stack_widget.setCurrentIndex(index % max_value)

    def close_main_window(self):
        self.close()

    def update_from_subscreen(self, msg: dict) -> None:
        print(msg)
        self.alarm_widget.set_alarm_text(msg)
        self.toggle_main_widget(1)

    def init_with_config(self, config: dict):
        self.screens_config = config

        # Set Title
        title = str(config['main']['name'])
        self.setWindowTitle(title)
        # Set window flag
        flags = Qt.CustomizeWindowHint  # Small Frame
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

        vbox_menu.addWidget(self.gui_element_builder.get_svg_widget(Gui_Element.TOP_LEFT_SHORT, 100, 191, front_color))
        button_list_widget = QListWidget()
        vbox_menu.addWidget(button_list_widget)
        vbox_menu.addWidget(
            self.gui_element_builder.get_svg_widget(Gui_Element.BOTTOM_LEFT_SHORT, 100, 191, front_color))

        # Header #################################################################
        self.main_layout.addWidget(self.gui_element_builder.get_svg_widget(Gui_Element.BUTTON, 33, 712, front_color),
                                   0, 1, 1, 1, Qt.AlignTop)
        self.main_layout.addWidget(self.gui_element_builder.get_svg_widget(Gui_Element.BUTTON, 33, 52, front_color),
                                   0, 3, Qt.AlignTop)
        self.main_layout.addWidget(self.gui_element_builder.get_svg_widget(Gui_Element.END_RIGHT, 33, 33, front_color),
                                   0, 4, Qt.AlignTop)
        # Header - END ###########################################################

        # Menu
        self.main_layout.addLayout(vbox_menu, 0, 0, 4, 1)
        # Central Window
        self.main_layout.addWidget(self.subscreen_stacked_widget, 1, 1, 2, 4)
        # Footer #################################################################
        self.main_layout.addWidget(self.gui_element_builder.get_svg_widget(Gui_Element.BUTTON, 33, 712, front_color),
                                   3, 1, Qt.AlignBottom)
        # Add Exit Button
        exit_button = QPushButton("EXIT")
        exit_button.setFont(QFont(font, 20, QFont.Bold))
        exit_button.setFixedSize(52, 33)
        exit_button.setStyleSheet("background:#ff0000; border:1px solid " + front_color + ";")
        exit_button.clicked.connect(lambda state: self.close())

        self.main_layout.addWidget(exit_button, 3, 3, Qt.AlignBottom)
        self.main_layout.addWidget(
            self.gui_element_builder.get_svg_widget(Gui_Element.END_RIGHT, 33, 33, front_color, font),
            3, 4, Qt.AlignBottom)
        # Footer - END ###########################################################

        # button_ListWidget.setVerticalScrolllayout(QAbstractItemView.ScrollMode.ScrollPerItem)
        button_list_widget.setStyleSheet(
            "QListWidget{background:" + background_color + ";  border: 0px solid " + front_color + ";}")

        # Erstellen der linken Button-Leiste ##############
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
            self.subscreen_stacked_widget.insertWidget(i,
                                                       self.gui_subscreen_builder.init_with_config(self.screens_config['sub'][i],
                                                                                         self.alarm_observer))

            # Buttons ##################################################################################################
            self.gui_button_builder.set_color(self.screens_config['sub'][i]["Background"])
            self.gui_button_builder.set_size(button_height, button_width)
            self.button[i] = self.gui_button_builder.create_button(self.screens_config["sub"][i]["name"],
                                                                   Gui_Element.BUTTON_TEXT)

            sub_button_list_item.setSizeHint(button_size)
            button_list_widget.addItem(placeholder_list_item)
            button_list_widget.addItem(sub_button_list_item)
            button_list_widget.setItemWidget(sub_button_list_item, self.button[i])
            # signals ##################################################################################################
            self.button[i].clicked.connect(lambda widget=self.subscreen_stacked_widget.widget(i): self.set_current_subscreen())

        # button_list_widget.setMaximumWidth(1000)
        button_list_widget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        button_list_widget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        button_list_widget.setMaximumWidth(button_list_widget.sizeHintForColumn(0))

        #############################################
        self.subscreen_stacked_widget.setCurrentIndex(0)
        self.main_stack_widget.insertWidget(0, self.main_widget)
        self.main_stack_widget.insertWidget(1, self.alarm_widget)
        self.main_stack_widget.setCurrentIndex(0)
        self.setCentralWidget(self.main_stack_widget)
