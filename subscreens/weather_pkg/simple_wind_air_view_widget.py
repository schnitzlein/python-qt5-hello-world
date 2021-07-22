from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QTransform
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLabel

from subscreens.weather_pkg.icon_handler import get_part_of_file_path


class SimpleWindAirViewWidget(QWidget):
    def __init__(self, parent, foreground_color="#ffffff", font_name=""):
        super(SimpleWindAirViewWidget, self).__init__()

        self.name = "Wind/Luft"
        self.parent = parent
        self.foreground_color = foreground_color
        self.font_name = font_name

        self.main_layout = QHBoxLayout()
        self.setLayout(self.main_layout)

        self.windrose_image = get_part_of_file_path() + "/windrose.png"


        self.windrose_label = QLabel()
        self.windrose_label.setScaledContents(True)
        self.windrose_label.setFixedSize(50, 50)
        self.main_layout.addWidget(self.windrose_label)


    def set_windrose_direction(self, deg: int):
        pixmap = QPixmap(self.windrose_image)
        transform = QTransform()
        transform.rotate(deg)
        rotated_pixmap = pixmap.transformed(transform)
        self.windrose_label.setPixmap(rotated_pixmap)

    def get_name(self) -> str:
        return self.name

    def set_data(self, data: dict):
        self.set_windrose_direction(data['wind']['deg'])
        #data["wind"]["speed"]