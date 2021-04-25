import random
import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QVBoxLayout
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

    window = QMainWindow()
    window.setStyleSheet("QMainWindow {background: " + background_color + ";}")
    window.setFixedSize(windowWidth, windowHeight)

    button_full_width = 100
    button_full_height = int(button_full_width / 3)
    button_full_path = Render.build_svg(
        Button_full(button_full_width, button_full_height, "#111111", "button_full"))
    button_full = QPushButton("#FFFF99")
    button_full.setStyleSheet("QPushButton {"
                                  "font-size: 10pt;"
                                  "font-family: Oswald;"
                                  "background-image : url(" + button_full_path + ");"
                                                                                     "border:1px;"
                                                                                     "background-color:#CCDDFF;}"
                                                                                     "QPushButton::hover {background-color: #99CCFF;}")
    button_full.setFixedSize(button_full_width, button_full_height)

    button_left_width = 100
    button_left_height = int(button_left_width / 3)
    button_left_path = Render.build_svg(
        Button_semi_left(button_left_width, button_left_height, "#111111", "button_left"))
    button_left = QPushButton("#FFFF99")
    button_left.setStyleSheet("QPushButton {"
                              "font-size: 10pt;"
                              "font-family: Oswald;"
                              "background-image : url(" + button_left_path + ");"
                                                                             "border:1px;"
                                                                             "background-color:#CCDDFF;}"
                                                                             "QPushButton::hover {background-color: #99CCFF;}")
    button_left.setFixedSize(button_left_width, button_left_height)

    button_right_width = 100
    button_right_height = int(button_right_width / 3)
    button_right_path = Render.build_svg(
        Button_semi_right(button_right_width, button_right_height, "#111111", "button_right"))
    button_right = QPushButton("#FFFF99")
    button_right.setStyleSheet("QPushButton {"
                              "font-size: 10pt;"
                              "font-family: Oswald;"
                              "background-image : url(" + button_right_path + ");"
                                                                             "border:1px;"
                                                                             "background-color:#CCDDFF;}"
                                                                             "QPushButton::hover {background-color: #99CCFF;}")
    button_right.setFixedSize(button_right_width, button_right_height)

    header_left_width = 600
    header_left_heigth = 30
    header_left_path = Render.build_svg(
        Header_left(header_left_width, header_left_heigth, "#111111", "header_left"))
    header_left = QPushButton("")
    header_left.setStyleSheet("QPushButton {"
                               "font-size: 10pt;"
                               "font-family: Oswald;"
                               "background-image : url(" + header_left_path + ");"
                                                                               "border:1px;"
                                                                               "background-color:#CCDDFF;}"
                                                                               "QPushButton::hover {background-color: #99CCFF;}")
    header_left.setFixedSize(header_left_width, header_left_heigth)

    header_right_width = 600
    header_right_heigth = 30
    header_right_path = Render.build_svg(
        Header_right(header_right_width, header_right_heigth, "#111111", "header_right"))
    header_right = QPushButton("")
    header_right.setStyleSheet("QPushButton {"
                              "font-size: 10pt;"
                              "font-family: Oswald;"
                              "background-image : url(" + header_right_path + ");"
                                                                             "border:1px;"
                                                                             "background-color:#CCDDFF;}"
                                                                             "QPushButton::hover {background-color: #99CCFF;}")
    header_right.setFixedSize(header_right_width, header_right_heigth)

    grid = QVBoxLayout()
    grid.addWidget(button_full)
    grid.addWidget(button_left)
    grid.addWidget(button_right)
    grid.addWidget(header_left)
    grid.addWidget(header_right)

    window.central_widget = QWidget()
    main_widget = QWidget()
    main_widget.setLayout(grid)

    window.setCentralWidget(main_widget)

    button_full.clicked.connect(lambda: change_background(window))

    window.show()
    app.exec_()
