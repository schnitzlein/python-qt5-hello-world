from PyQt5.QtWidgets import QStackedWidget
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QDateTime

from subscreens.weather_pkg.setup_widget import SetupWidget
from subscreens.weather_pkg.city_widget import CityWidget
from subscreens.weather_pkg.unitsystem import UnitSystem


class StartWidget(QWidget):
    def __init__(self, parent, foreground_color="#ffffff", font_name=""):
        super(StartWidget, self).__init__()

        self.foreground_color = foreground_color
        self.font_name = font_name
        self.parent = parent

        self.key = ""
        self.language = "de"

        self.font = QFont(font_name, 40, QFont.Bold)
        self.font_small = QFont(font_name, 20, QFont.Bold)
        self.high_label_style = "QLabel { color : #ffba26; }"
        self.label_style = "QLabel { color : " + self.foreground_color + "; }"
        style = "QPushButton { background-color: " + self.foreground_color + "; border: 2px; border-radius: 20px; border-style: outset;}"
        self.line_style = "QLabel { background-color: " + self.foreground_color + "; border: 2px; border-radius: 4px;}"
        self.view_stack = QStackedWidget()
        self.view_stack.addWidget(SetupWidget(self, self.foreground_color))

        self.main_layout = QVBoxLayout()
        self.head_line = QHBoxLayout()
        self.separator_line = QHBoxLayout()
        self.main_line = QHBoxLayout()

        self.head_widget_name_backward = QLabel()
        self.set_label_style(self.head_widget_name_backward, self.font_small, self.label_style)
        self.head_widget_name_current = QLabel()
        self.set_label_style(self.head_widget_name_current, self.font, self.high_label_style)
        self.head_widget_name_foreward = QLabel()
        self.set_label_style(self.head_widget_name_foreward, self.font_small, self.label_style)

        self.line = QLabel()
        self.line.setStyleSheet(self.line_style)
        self.line.setFixedSize(640, 10)
        self.separator_line.addStretch(1)
        self.separator_line.addWidget(self.line)
        self.separator_line.addStretch(1)

        self.left_button = QPushButton("<")
        self.left_button.setFixedSize(40, 80)
        self.left_button.setStyleSheet(style)

        self.right_button = QPushButton(">")
        self.right_button.setFixedSize(40, 80)
        self.right_button.setStyleSheet(style)

        self.head_line.addWidget(self.left_button)
        self.head_line.addStretch(1)
        self.head_line.addWidget(self.head_widget_name_backward)
        self.head_line.addSpacing(30)
        self.head_line.addWidget(self.head_widget_name_current)
        self.head_line.addSpacing(30)
        self.head_line.addWidget(self.head_widget_name_foreward)
        self.head_line.addStretch(1)
        self.head_line.addWidget(self.right_button)

        self.main_line.addWidget(self.view_stack)

        self.left_button.clicked.connect(lambda state: self.toggle_main_widget(-1))
        self.right_button.clicked.connect(lambda state: self.toggle_main_widget(+1))

        self.main_layout.addLayout(self.head_line)
        self.main_layout.addLayout(self.separator_line)
        self.main_layout.addLayout(self.main_line)

        self.set_headline()
        self.setLayout(self.main_layout)

    def set_headline(self):
        max_value = self.view_stack.count()
        current = self.view_stack.currentIndex()
        if max_value == 1:
            self.head_widget_name_backward.setText("")
            self.head_widget_name_current.setText(self.view_stack.widget(current).get_name())
            self.head_widget_name_foreward.setText("")
            return
        self.head_widget_name_backward.setText(self.view_stack.widget((current - 1) % max_value).get_name())
        self.head_widget_name_current.setText(self.view_stack.widget(current).get_name())
        self.head_widget_name_foreward.setText(self.view_stack.widget((current + 1) % max_value).get_name())

    def toggle_main_widget(self, index: int):
        max_value = self.view_stack.count()
        current = self.view_stack.currentIndex()
        self.view_stack.setCurrentIndex((current + index) % max_value)
        self.set_headline()

    def create_new_city(self, city_name: str, unit: UnitSystem):
        city_widget = CityWidget(city_name, unit, self.foreground_color, self.font_name)
        call_parameter = {"city": city_name,
                          "units": unit,
                          "language": self.language,
                          "key": self.key}
        data = self.parent.get_data(call_parameter)
        city_widget.set_data(data)
        self.view_stack.addWidget(city_widget)
        current = self.view_stack.currentIndex()
        self.toggle_main_widget(current + 1)

        local = QDateTime(QDateTime.currentDateTime())
        print("UTC:", local.toTime_t())
        self.save_config()

    def set_label_style(self, label: QLabel, font: QFont, style: str):
        label.setStyleSheet(style)
        label.setFont(font)

    def update_data(self, config: dict) -> dict:
        call_parameter = {"city": config["city"],
                          "units": config["unit"],
                          "language": self.language,
                          "key": self.key}  # "key": "36dcf663b6964439a18574709e1d6eef"}
        data = self.parent.get_data(call_parameter)

    def set_key(self, key: str):
        self.key = key

    def set_language(self, language: str):
        self.language = language

    def save_city_config(self) -> list:
        if self.view_stack.count() < 2:
            return []
        cities = []

        for pos in range(1, self.view_stack.count()):
            city = {
                "name": "",
                "last_update": "",
                "unit_system": ""
            }

            widget = self.view_stack.widget(pos)
            city["unit_system"] = str(widget.get_units())
            city["name"] = widget.get_name()
            cities.append(city)

        return cities

    def save_config(self):
        config = {"language": self.language,
                  "key": self.key,
                  "cities": self.save_city_config()}
        self.parent.save_config(config)
