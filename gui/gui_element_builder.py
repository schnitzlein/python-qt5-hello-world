import os
import sys

from PyQt5.QtCore import QSize
from PyQt5.QtSvg import QSvgWidget

from .gui_element import Gui_Element

strWinDirectory = "gui\\svg\\"
strLinuxDirectory = "gui/svg/"


class GuiElementsBuilder:

    def __init__(self):
        self.font_name = "sans-serif"

    def file_none() -> str:
        return ""  # ToDo add svg-symbol for no file

    def file_button() -> str:
        return "button_1.svg"

    def file_end_left() -> str:
        return "endcap_left.svg"

    def file_end_right() -> str:
        return "endcap_right.svg"

    def file_top_right_short() -> str:
        return "elbow_right_top_shortened.svg"

    def file_top_right() -> str:
        return "elbow_right_top.svg"

    def file_bottom_right_short() -> str:
        return "elbow_right_bottom_shortened.svg"

    def file_bottom_right() -> str:
        return "elbow_right_bottom.svg"

    def file_top_left_short() -> str:
        return "elbow_left_top_shortened.svg"

    def file_top_left() -> str:
        return "elbow_left_top.svg"

    def file_bottom_left_short() -> str:
        return "elbow_left_bottom_shortened.svg"

    def file_bottom_left() -> str:
        return "elbow_left_bottom.svg"

    def file_button_full_circle() -> str:
        return "button_full_circle.svg"

    def file_button_semi_left() -> str:
        return "button_semi_left.svg"

    def file_button_semi_right() -> str:
        return "button_semi_right.svg"

    def file_button_notification_full_circle() -> str:
        return "button_notification_full_circle.svg"

    def file_button_full_circle_text() -> str:
        return "button_full_circle_text.svg"

    def file_button_text() -> str:
        return "button_text.svg"

    case = {Gui_Element.NONE: file_none(),
            Gui_Element.END_LEFT: file_end_left(),
            Gui_Element.END_RIGHT: file_end_right(),
            Gui_Element.TOP_LEFT: file_top_left(),
            Gui_Element.TOP_LEFT_SHORT: file_top_left_short(),
            Gui_Element.BOTTOM_LEFT: file_bottom_left(),
            Gui_Element.BOTTOM_LEFT_SHORT: file_bottom_left_short(),
            Gui_Element.BUTTON: file_button(),
            Gui_Element.BUTTON_FULL_CIRCLE: file_button_full_circle(),
            Gui_Element.BUTTON_SEMI_LEFT: file_button_semi_left(),
            Gui_Element.BUTTON_SEMI_RIGHT: file_button_semi_right(),
            Gui_Element.BUTTON_NOTIFICATION_FULL_CIRCLE: file_button_notification_full_circle(),
            Gui_Element.BUTTON_FULL_CIRCLE_TEXT: file_button_full_circle_text(),
            Gui_Element.TOP_RIGHT: file_top_right(),
            Gui_Element.TOP_RIGHT_SHORT: file_top_right_short(),
            Gui_Element.BOTTOM_RIGHT: file_bottom_right(),
            Gui_Element.BOTTOM_RIGHT_SHORT: file_bottom_right_short(),
            Gui_Element.BUTTON_TEXT: file_button_text()
            }

    def get_full_file_path(self, element: Gui_Element) -> str:
        filename = self.case[element]

        if sys.platform == 'win32':
            directory = strWinDirectory
        else:
            directory = strLinuxDirectory

        return directory + filename

    def read_svg_from_file(self, element: Gui_Element) -> str:

        file_full_path = self.get_full_file_path(element)
        file = open(file_full_path, "r")
        data = file.read()
        file.close()

        return data

    def interpolate_svg(self, svg: str, fill: str, text: str) -> str:
        fill = "{fill:" + fill + ";}"
        return svg.format(background=fill, # ToDo
                          filltext=text, font=self.font_name)

    def get_svg_widget(self, element: Gui_Element, height: int, width: int, fill: str = "#FF9933",
                       text: str = "00") -> QSvgWidget:

        svg = self.read_svg_from_file(element)
        svg = self.interpolate_svg(svg, fill, text)

        svg_bytes = bytearray(svg, encoding='utf-8')
        svg_widget = QSvgWidget()
        svg_widget.load(svg_bytes)
        #svg_widget.renderer().load(svg_bytes)
        if height > 0 and width > 0:
            size = QSize(width, height)
            svg_widget.setFixedSize(size)
        #else:
        #    svg_widget.setFixedSize(svg_widget.renderer().defaultSize())
        #    svg_widget.setFixedSize(svg_w)

        return svg_widget

    def set_font(self, font: str):
        self.font_name = font
