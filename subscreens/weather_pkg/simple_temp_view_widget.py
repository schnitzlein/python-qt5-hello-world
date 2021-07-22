from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

from subscreens.weather_pkg.icon_handler import get_icon_path
from subscreens.weather_pkg.unitsystem import UnitSystem


class SimpleTempViewWidget(QWidget):
    def __init__(self, parent, units: UnitSystem = UnitSystem.metric, foreground_color="#ffffff", font_name=""):
        super(SimpleTempViewWidget, self).__init__()

        self.name = "Temp"
        self.parent = parent
        self.units = units
        self.main_layout = QHBoxLayout()
        self.foreground_color = foreground_color
        self.label_style = "QLabel { color : " + self.foreground_color + "; }"

        self.font_name = font_name
        self.font = QFont(font_name, 80, QFont.Bold)
        self.font_small = QFont(font_name, 50, QFont.Bold)
        self.font_extra_small = QFont(font_name, 30, QFont.Bold)
        self.temp_label = QLabel("Temp:")
        self.temp_label.setFont(self.font_small)
        self.temp_label.setStyleSheet(self.label_style)
        self.temp_value = QLabel()
        self.temp_value.setFont(self.font_small)
        self.temp_value.setStyleSheet(self.label_style)
        self.temp_max_label = QLabel("Max:")
        self.temp_max_label.setFont(self.font_extra_small)
        self.temp_max_label.setStyleSheet(self.label_style)
        self.temp_max_value = QLabel()
        self.temp_max_value.setFont(self.font_extra_small)
        self.temp_max_value.setStyleSheet(self.label_style)
        self.temp_min_label = QLabel("Min:")
        self.temp_min_label.setFont(self.font_extra_small)
        self.temp_min_label.setStyleSheet(self.label_style)
        self.temp_min_value = QLabel()
        self.temp_min_value.setFont(self.font_extra_small)
        self.temp_min_value.setStyleSheet(self.label_style)

        self.weather_icon = QLabel()
        self.weather_icon.setScaledContents(True)
        self.weather_icon.setFixedSize(160, 160)
        self.weather_icon_description = QLabel()
        self.weather_icon_description.setFont(self.font_extra_small)
        self.weather_icon_description.setStyleSheet(self.label_style)

        self.temp_max_layout = QHBoxLayout()
        self.temp_max_layout.addWidget(self.temp_max_label)
        self.temp_max_layout.addSpacing(20)
        self.temp_max_layout.addWidget(self.temp_max_value)
        self.temp_max_layout.addStretch(1)

        self.temp_min_layout = QHBoxLayout()
        self.temp_min_layout.addWidget(self.temp_min_label)
        self.temp_min_layout.addSpacing(20)
        self.temp_min_layout.addWidget(self.temp_min_value)
        self.temp_min_layout.addStretch(1)

        self.temp_layout = QVBoxLayout()
        self.temp_layout.addStretch(1)
        self.temp_layout.addLayout(self.temp_max_layout)
        self.temp_layout.addWidget(self.temp_value)
        self.temp_layout.addLayout(self.temp_min_layout)
        self.temp_layout.addStretch(2)

        self.weather_icon_layout = QVBoxLayout()
        self.weather_icon_layout.addWidget(self.weather_icon)
        self.weather_icon_layout.addWidget(self.weather_icon_description)
        self.weather_icon_layout.addStretch(3)

        self.main_layout.addStretch(1)
        self.main_layout.addLayout(self.temp_layout)
        self.main_layout.addStretch(1)
        self.main_layout.addLayout(self.weather_icon_layout)
        self.main_layout.addStretch(1)

        self.setLayout(self.main_layout)

    def set_data(self, data: dict):
        unit_text = ""
        if self.units == UnitSystem.metric:
            unit_text = "{}°C"
        elif self.units == UnitSystem.imperial:
            unit_text = "{}°F"

        self.temp_value.setText(unit_text.format(data['main']['temp']))
        self.temp_max_value.setText(unit_text.format(data['main']['temp_max']))
        self.temp_min_value.setText(unit_text.format(data['main']['temp_min']))

        icon_path = get_icon_path(data['weather'][0]['id'])
        print(icon_path)
        self.weather_icon.setPixmap(QPixmap(icon_path))
        self.weather_icon_description.setText(data['weather'][0]['description'])

    def get_name(self) -> str:
        return self.name
