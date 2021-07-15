from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QFont

from subscreens.weather.icon_handler import get_icon_path


class SimpleTempView(QWidget):
    def __init__(self, parent, foreground_color="#ffffff", font_name=""):
        super(SimpleTempView, self).__init__()

        self.parent = parent
        self.main_layout = QVBoxLayout()
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
        self.weather_icon.setFixedSize(300, 300)
        self.weather_icon_description = QLabel()
        self.weather_icon_description.setFont(self.font_extra_small)
        self.weather_icon_description.setStyleSheet(self.label_style)

        self.current_temp_layout = QHBoxLayout()
        self.current_temp_layout.addWidget(self.temp_label)
        self.current_temp_layout.addWidget(self.temp_value)

        self.max_temp_layout = QHBoxLayout()
        self.max_temp_layout.addWidget(self.temp_max_label)
        self.max_temp_layout.addWidget(self.temp_max_value)

        self.min_temp_layout = QHBoxLayout()
        self.min_temp_layout.addWidget(self.temp_min_label)
        self.min_temp_layout.addWidget(self.temp_min_value)

        self.temp_range_layout = QVBoxLayout()
        self.temp_range_layout.addLayout(self.max_temp_layout)
        self.temp_range_layout.addLayout(self.min_temp_layout)

        self.weather_icon_layout = QVBoxLayout()
        self.weather_icon_layout.addWidget(self.weather_icon)
        self.weather_icon_layout.addWidget(self.weather_icon_description)

        self.second_line_layout = QHBoxLayout()
        self.second_line_layout.addLayout(self.temp_range_layout)
        self.second_line_layout.addLayout(self.weather_icon_layout)

        self.main_layout.addLayout(self.current_temp_layout)
        self.main_layout.addLayout(self.second_line_layout)

        self.setLayout(self.main_layout)

    def set_data(self, data: dict):
        # ToDo Einstellung behandeln bzgl. Fahrenheit
        self.temp_value.setText("{}°C".format(data['main']['temp']))
        self.temp_max_value.setText("{}°C".format(data['main']['temp_max']))
        self.temp_min_value.setText("{}°C".format(data['main']['temp_min']))

        icon_path = get_icon_path(data['weather'][0]['id'])
        print(icon_path)
        self.weather_icon.setPixmap(QPixmap(icon_path))
        self.weather_icon_description.setText(data['weather'][0]['description'])
