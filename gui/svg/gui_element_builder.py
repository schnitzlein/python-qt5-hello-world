from PyQt5.QtSvg import QSvgWidget
from enum import Enum
from PyQt5.QtCore import QSize
import os

strDirectory = "\\gui\\svg\\"


class Gui_Element(Enum):
    NONE = 0
    END_LEFT = 1
    END_RIGHT = 2
    TOP_LEFT = 3
    BOTTOM_LEFT = 5
    BUTTON = 6


class GuiElementsBuilder:

    def file_none() -> str:
        return ""  # ToDo add svg-symbol for no file

    def file_button() -> str:
        return "button_1.svg"

    def file_end_left() -> str:
        return "endcap_left.svg"

    def file_end_right() -> str:
        return "endcap_right.svg"

    def file_top_left() -> str:
        return "elbow_left_top.svg"

    def file_bottom_left() -> str:
        return "elbow_left_bottom.svg"

    case = {0: file_none(),
            1: file_end_left(),
            2: file_end_right(),
            3: file_top_left(),
            5: file_bottom_left(),
            6: file_button()
            }

    def get_svg_widget(self, element: Gui_Element, height: int, width: int) -> QSvgWidget:

        filename = self.case[element.value]
        cwd = os.getcwd()
        file_all = cwd + strDirectory + filename
        # print("filename: " + cwd + strDirectory + filename)
        file = open(file_all, "r")
        data = file.read()
        file.close()

        svg_bytes = bytearray(data, encoding='utf-8')
        svg_widget = QSvgWidget()
        svg_widget.renderer().load(svg_bytes)
        if height > 0 and width > 0:
            size = QSize(width, height)
            svg_widget.setFixedSize(size)
        else:
            print ("else")
            svg_widget.setFixedSize(svg_widget.renderer().defaultSize())

        return svg_widget
