import random
import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QHBoxLayout,QVBoxLayout
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QWidget

from gui import *

windowHeight = 600
windowWidth = 800
background_color = "#111111"


def change_background(window: QMainWindow):
    c = '{:x}'.format(random.randrange(16))
    background_color = "#" + c + c + c
    window.setStyleSheet("QMainWindow {background: " + background_color + ";}")


if __name__ == '__main__':
    app = QApplication(sys.argv)

    gui_element_builder = GuiElementsBuilder()

    window = QMainWindow()
    window.setStyleSheet("QMainWindow {background: " + background_color + ";}")
    window.setFixedSize(windowWidth, windowHeight)

    buttonStyle = ("QPushButton {"
                   "border:1px;"
                   "background-color:#111111;}"
                   "QPushButton::hover {background-color: #99CCFF;}")

    button_width = 100
    button_height = int(button_width / 3)

    button = QPushButton("")
    button_layout = QHBoxLayout()
    button_layout.addWidget(
        gui_element_builder.get_svg_widget(Gui_Element.BUTTON_FULL_CIRCLE, button_height, button_width))
    button_layout.setContentsMargins(0, 0, 0, 0)
    button.setLayout(button_layout)

    button.setFixedSize(button_width, button_height)
    button.setStyleSheet(buttonStyle)

    button_left = QPushButton("")
    button_layout = QHBoxLayout()
    button_layout.addWidget(
        gui_element_builder.get_svg_widget(Gui_Element.BUTTON_SEMI_LEFT, button_height, button_width))
    button_layout.setContentsMargins(0, 0, 0, 0)
    button_left.setLayout(button_layout)

    button_left.setFixedSize(button_width, button_height)
    button_left.setStyleSheet(buttonStyle)

    button_right = QPushButton("")
    button_layout = QHBoxLayout()
    button_layout.addWidget(
        gui_element_builder.get_svg_widget(Gui_Element.BUTTON_SEMI_RIGHT, button_height, button_width))
    button_layout.setContentsMargins(0, 0, 0, 0)
    button_right.setLayout(button_layout)

    button_right.setFixedSize(button_width, button_height)
    button_right.setStyleSheet(buttonStyle)

    grid = QVBoxLayout()
    grid.addWidget(button)
    grid.addWidget(button_left)
    grid.addWidget(button_right)

    window.central_widget = QWidget()
    main_widget = QWidget()
    main_widget.setLayout(grid)

    window.setCentralWidget(main_widget)

    button_left.clicked.connect(lambda: change_background(window))
    window.show()
    app.exec_()
