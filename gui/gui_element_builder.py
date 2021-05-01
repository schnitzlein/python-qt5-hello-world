import os
import sys

from PyQt5.QtCore import QSize
from PyQt5.QtSvg import QSvgWidget

from .gui_element import Gui_Element

strWinDirectory = "\\gui\\svg\\"
strLinuxDirectory = "/gui/svg/"


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

    case = {Gui_Element.NONE: file_none(),
            Gui_Element.END_LEFT: file_end_left(),
            Gui_Element.END_RIGHT: file_end_right(),
            Gui_Element.TOP_LEFT: file_top_left(),
            Gui_Element.BOTTOM_LEFT: file_bottom_left(),
            Gui_Element.BUTTON: file_button(),
            Gui_Element.BUTTON_FULL_CIRCLE: file_button_full_circle(),
            Gui_Element.BUTTON_SEMI_LEFT: file_button_semi_left(),
            Gui_Element.BUTTON_SEMI_RIGHT: file_button_semi_right(),
            Gui_Element.BUTTON_NOTIFICATION_FULL_CIRCLE: file_button_notification_full_circle(),
            Gui_Element.BUTTON_FULL_CIRCLE_TEXT: file_button_full_circle_text()
            }

    def get_full_file_path(self, element: Gui_Element) -> str:
        filename = self.case[element]
        cwd = os.getcwd()

        if sys.platform == 'win32':
            directory = strWinDirectory
        else:
            directory = strLinuxDirectory

        return cwd + directory + filename

    def read_svg_from_file(self, element: Gui_Element) -> str:

        file_full_path = self.get_full_file_path(element)
        file = open(file_full_path, "r")
        data = file.read()
        file.close()

        return data

    def interpolate_svg(self, svg: str, fill: str, text: str) -> str:
        fill = "{fill:" + fill + ";}"
        return svg.format(background=fill,
                          filltext=text)

    def get_svg_widget(self, element: Gui_Element, height: int, width: int, fill="#FF9933", text="00") -> QSvgWidget:

        svg = self.read_svg_from_file(element)
        svg = self.interpolate_svg(svg, fill, text)

        svg_bytes = bytearray(svg, encoding='utf-8')
        svg_widget = QSvgWidget()
        svg_widget.renderer().load(svg_bytes)
        if height > 0 and width > 0:
            size = QSize(width, height)
            svg_widget.setFixedSize(size)
        else:
            svg_widget.setFixedSize(svg_widget.renderer().defaultSize())

        return svg_widget
