from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QTransform
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QFont

from subscreens.weather_pkg.icon_handler import get_part_of_file_path
from subscreens.weather_pkg.unitsystem import UnitSystem


class SimpleWindViewWidget(QWidget):
    def __init__(self, parent, units: UnitSystem = UnitSystem.metric, foreground_color="#ffffff", font_name=""):
        super(SimpleWindViewWidget, self).__init__()

        self.name = "Wind"
        self.parent = parent
        self.units = units
        self.foreground_color = foreground_color
        self.label_style = "QLabel { color : " + self.foreground_color + "; }"
        self.font_name = font_name
        self.font = QFont(font_name, 50, QFont.Bold)

        self.main_layout = QHBoxLayout()
        self.setLayout(self.main_layout)

        self.windrose_image = get_part_of_file_path() + "/windrose.png"
        self.speed_image = get_part_of_file_path() + "/speed.png"
        self.gust_image = get_part_of_file_path() + "/gust.png"

        self.windrose_label = QLabel()
        self.windrose_label.setScaledContents(True)
        self.windrose_label.setFixedSize(50, 50)

        self.wind_direction_label = QLabel()
        self.wind_direction_label.setStyleSheet(self.label_style)
        self.wind_direction_label.setFont(self.font)


        self.speed_label = QLabel()
        self.speed_label.setFont(self.font)
        self.speed_label.setStyleSheet(self.label_style)

        self.speed_icon_label = QLabel()
        self.speed_icon_label.setScaledContents(True)
        self.speed_icon_label.setFixedSize(50, 50)
        self.set_speed_image()

        self.gust_label = QLabel()
        self.gust_label.setFont(self.font)
        self.gust_label.setStyleSheet(self.label_style)

        self.gust_icon_label = QLabel()
        self.gust_icon_label.setScaledContents(True)
        self.gust_icon_label.setFixedSize(50, 50)
        self.set_gust_image()

        self.main_layout.addStretch(1)
        self.main_layout.addWidget(self.windrose_label)
        self.main_layout.addWidget(self.wind_direction_label)
        self.main_layout.addSpacing(20)
        self.main_layout.addWidget(self.speed_icon_label)
        self.main_layout.addWidget(self.speed_label)
        self.main_layout.addSpacing(20)
        self.main_layout.addWidget(self.gust_icon_label)
        self.main_layout.addSpacing(6)
        self.main_layout.addWidget(self.gust_label)
        self.main_layout.addStretch(2)

    def set_gust_image(self):
        pixmap = QPixmap(self.gust_image)
        transform = QTransform()
        transform.rotate(0)
        rotated_pixmap = pixmap.transformed(transform)
        self.gust_icon_label.setPixmap(rotated_pixmap)

    def set_speed_image(self):
        pixmap = QPixmap(self.speed_image)
        transform = QTransform()
        transform.rotate(0)
        rotated_pixmap = pixmap.transformed(transform)
        self.speed_icon_label.setPixmap(rotated_pixmap)

    def set_windrose_direction(self, deg: int):
        pixmap = QPixmap(self.windrose_image)
        transform = QTransform()
        transform.rotate(deg)
        rotated_pixmap = pixmap.transformed(transform)
        self.windrose_label.setPixmap(rotated_pixmap)

    def get_name(self) -> str:
        return self.name

    def set_data(self, data: dict):
        unit_text_dec = "{}°"
        speed_label = "{}"
        if self.units == UnitSystem.metric:
            speed_label = "{}m/s"
        elif self.units == UnitSystem.imperial:
            speed_label = "{}mph"

        self.set_windrose_direction(data['wind']['deg'])
        self.wind_direction_label.setText(unit_text_dec.format(data['wind']['deg']))
        self.speed_label.setText(speed_label.format(data['wind']['speed']))
        self.gust_label.setText(speed_label.format(data['wind']['gust']))
