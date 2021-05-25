from .gui_element import Gui_Element
from .gui_element_builder import GuiElementsBuilder
from PyQt5.QtWidgets import QPushButton, QVBoxLayout
from PyQt5.QtCore import QSize


class GuiButtonBuilder:

    def __init__(self):
        self.height = 0
        self.width = 0
        self.color = ""
        self.style = ""
        self.gui_element_builder = GuiElementsBuilder()

    def set_size(self, height: int, width: int):
        self.height = height
        self.width = width

    def set_color(self, color: str):
        self.color = color

    def set_style(self, style: str):
        self.style = style

    def create_button(self, name: str, typ: Gui_Element) -> QPushButton:
        button = QPushButton(name)
        button.setFixedSize(QSize(self.width, self.height))

        button_layout = QVBoxLayout()
        button_layout.addWidget(
            self.gui_element_builder.get_svg_widget(
                typ,
                self.height,
                self.width,
                self.color,
                name))
        button_layout.setContentsMargins(0, 0, 0, 0)
        button.setLayout(button_layout)
        #button.setStyleSheet("border:1px;")
        button.setStyleSheet(self.style)

        return button
