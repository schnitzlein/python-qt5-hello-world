from subscreens.baseclass import Base
from subscreens.countup import Countup
from subscreens.placeholder import Placeholder
from subscreens.clock import Clock
from subscreens.timer import Timer
from subscreens.moveablesub import Movesub
from experiments.myevent import MyCustomEventTest
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QWidget, QStackedWidget
from gui.gui_menu_builder import GuiMenuBuilder
from gui.gui_element import Gui_Element
from .gui_element_builder import GuiElementsBuilder


class GuiSubscreenBuilder:

    def __init__(self):
        self.widget = QWidget()
        self.main_layout = QGridLayout()
        self.gui_menu_builder = GuiMenuBuilder()
        self.gui_element_builder = GuiElementsBuilder()
        self.foreground_color = ""
        self.central_widget = QStackedWidget()
        self.buttons = []

    def inti_with_config(self, config: dict) -> QWidget:
        self.widget = Base(config["name"], config["Background"])
        self.foreground_color = config["Background"]
        if config["layout"] == 1:
            # Header
            self.main_layout.addWidget(
                self.gui_element_builder.get_svg_widget(Gui_Element.BUTTON, 20, 640, self.foreground_color),
                0, 1, 1, 3, Qt.AlignTop)
            self.main_layout.addWidget(
                self.gui_element_builder.get_svg_widget(Gui_Element.END_RIGHT, 20, 20, self.foreground_color),
                0, 5, Qt.AlignTop)

            self.main_layout.addWidget(self.central_widget, 1, 1, 2, 4)
            # self.central_widget.setStyleSheet("background-color:" + "#ffffff")  # Show size of Central_Widget
            # Footer
            self.main_layout.addWidget(
                self.gui_element_builder.get_svg_widget(Gui_Element.BUTTON, 13, 640, self.foreground_color),
                4, 1, 1, 2, Qt.AlignBottom)
            self.main_layout.addWidget(
                self.gui_element_builder.get_svg_widget(Gui_Element.END_RIGHT, 13, 10, self.foreground_color),
                4, 5, Qt.AlignLeft | Qt.AlignBottom)

            if "subapp" in config:
                self.main_layout.addLayout(
                    self.gui_menu_builder.build_menu(config.get("subapp"), self.foreground_color), 0, 0, 5, 1)
                self.buttons = self.gui_menu_builder.get_button_list()

                for i in range(0, len(config.get("subapp"))):
                    widget = self.create_subapp(config.get("subapp")[i])
                    button = self.buttons[i]
                    self.central_widget.insertWidget(i, widget)
                    button.clicked.connect(lambda state, wid=widget: self.central_widget.setCurrentWidget(wid))

            self.widget.setLayout(self.main_layout)
            return self.widget
        else:
            return self.create_subapp(config)

    @staticmethod
    def create_subapp(config: dict) -> QWidget:
        name = config["name"]
        # ToDo besseren Weg zum Erstellen der Subapps suchen
        # ToDo Laden der Subscreens aus Verzeichniss je nach Nennung in Config
        if name == "Clock":
            return Clock(config["Background"])
        elif name == "Timer":
            return Timer(name, config["Background"])
        elif name == "Countup":
            return Countup(name, config["Background"])
        elif name == "Movesub":
            return Movesub(name, config["Background"])
        elif name == "MyCustomEventTest":
            return MyCustomEventTest(name, config["Background"])
        else:
            return Placeholder(name, config["Background"])
