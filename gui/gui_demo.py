import random
import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QHBoxLayout
from gui import Button

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

    yellow_button_width = 300
    yellow_button_height = int(yellow_button_width / 3)
    path_yellow = Button.build_svg(
        Button(yellow_button_width, yellow_button_height, "#FFFF99", background_color, "yellow_button"))
    button_yellow = QPushButton("#FFFF99")
    button_yellow.setStyleSheet("background-image : url(" + path_yellow + ");"
                                                                          "border:1px;"
                                                                          "background-color:" + background_color + ";")

    button_yellow.setFixedSize(yellow_button_width, yellow_button_height)

    blue_button_width = 210
    blue_button_height = int(blue_button_width / 3)
    path_blue = Button.build_svg(
        Button(blue_button_width, blue_button_height, "#99CCFF", background_color, "blue_button"))
    button_blue = QPushButton("#99CCFF")
    button_blue.setStyleSheet("background-image : url(" + path_blue + ");"
                                                                      "border:1px;"
                                                                      "background-color:" + background_color + ";")
    button_blue.setFixedSize(blue_button_width, blue_button_height)

    layout = QHBoxLayout()
    layout.addWidget(button_yellow)
    layout.addWidget(button_blue)

    window.central_widget = QWidget()
    main_widget = QWidget()
    main_widget.setLayout(layout)

    window.setCentralWidget(main_widget)

    button_yellow.clicked.connect(lambda: change_background(window))
    button_blue.clicked.connect(lambda: change_background(window))

    window.show()
    app.exec_()
