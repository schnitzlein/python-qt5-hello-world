from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QVBoxLayout, QGridLayout, QHBoxLayout, QLayout
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QPushButton
from gui.gui_element import Gui_Element
from gui.gui_button_builder import GuiButtonBuilder
from gui.gui_element_builder import GuiElementsBuilder
from configreader.configreader import ConfigReader

class GuiMenuBuilder(QWidget):

    def __init__(self):
        super().__init__()
        self.foreground_color = ""
        self.button_height = 60
        self.button_width = 96
        self.config_reader = ConfigReader()

        self.gui_element_builder = GuiElementsBuilder()
        self.gui_button_builder = GuiButtonBuilder()
        self.button_counter = 0
        self.buttons = []

    def build_menu(self, config: dict, foreground_color) -> QLayout:
        self.foreground_color = foreground_color
        if type(config) == list:
            self.button_counter = len(config)

        # Menu #########################################################################################################
        self.vbox_menu = QVBoxLayout()
        self.vbox_menu.setSizeConstraint(QLayout.SetFixedSize)
        # ToDo other header for menu depending on layout option
        self.vbox_menu.addWidget(
            self.gui_element_builder.get_svg_widget(Gui_Element.TOP_LEFT_SHORT, 61, 120, self.foreground_color),
            Qt.AlignTop)
        self.gui_button_builder.set_size(self.button_height, self.button_width)
        for i in range(0, self.button_counter):
            self.gui_button_builder.set_color(config[i]["Background"])
            self.buttons.insert(i, self.gui_button_builder.create_button(config[i]["name"], Gui_Element.BUTTON_TEXT))
            self.vbox_menu.addWidget(self.buttons[i])
        # ToDo other footer for menu depending on layout option
        self.vbox_menu.addWidget(
            self.gui_element_builder.get_svg_widget(Gui_Element.BUTTON, 172, self.button_width, self.foreground_color))
        self.vbox_menu.addWidget(
            self.gui_element_builder.get_svg_widget(Gui_Element.BOTTOM_LEFT_SHORT, 41, 120, self.foreground_color),
            Qt.AlignBottom)
        # End Menu #####################################################################################################

        return self.vbox_menu

    def get_button_list(self) -> list:
        return self.buttons
