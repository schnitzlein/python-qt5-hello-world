from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout
from PyQt5.QtWidgets import QWidget, QStackedWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QTimer

from subscreens.weather_pkg.simple_temp_view_widget import SimpleTempViewWidget
from subscreens.weather_pkg.simple_wind_view_widget import SimpleWindViewWidget
from subscreens.weather_pkg.unitsystem import UnitSystem


class CityWidget(QWidget):
    def __init__(self, name: str, units: UnitSystem = UnitSystem.metric, foreground_color="#ffffff", font_name=""):
        super(CityWidget, self).__init__()

        self.city_name = name
        self.units = units
        self.foreground_color = foreground_color
        self.font_name = font_name

        self.label_style = "QLabel { color : " + self.foreground_color + "; }"
        self.high_label_style = "QLabel { color : #ffba26; }"
        self.button_style = "QPushButton { background-color: " + self.foreground_color + "; border: 2px; " \
                                                                                         "border-radius: 20px; " \
                                                                                         "border-style: outset;}"
        self.line_style = "QLabel { background-color: " + self.foreground_color + "; border: 2px; border-radius: 4px;}"

        self.font = QFont(font_name, 30, QFont.Bold)
        self.font_small = QFont(font_name, 20, QFont.Bold)

        self.weather_data = {}
        self.main_layout = QVBoxLayout()
        self.view_stack = QStackedWidget()
        self.main_layout.addWidget(self.view_stack)

        self.temp_view = SimpleTempViewWidget(self, units, self.foreground_color, self.font_name)
        self.view_stack.addWidget(self.temp_view)
        self.wind_view = SimpleWindViewWidget(self, units, self.foreground_color, self.font_name)
        self.view_stack.addWidget(self.wind_view)

        self.separator_line = QHBoxLayout()
        self.main_layout.addLayout(self.separator_line)

        self.line = QLabel()
        self.line.setStyleSheet(self.line_style)
        self.line.setFixedSize(640, 10)
        self.separator_line.addStretch(1)
        self.separator_line.addWidget(self.line)
        self.separator_line.addStretch(1)

        self.bottom_line = QHBoxLayout()
        self.main_layout.addLayout(self.bottom_line)

        self.left_button = QPushButton("<")
        self.left_button.setFixedSize(40, 80)
        self.left_button.setStyleSheet(self.button_style)

        self.bottom_widget_name_backward = QLabel()
        self.set_label_style(self.bottom_widget_name_backward, self.font_small, self.label_style)
        self.bottom_widget_name_current = QLabel()
        self.set_label_style(self.bottom_widget_name_current, self.font, self.high_label_style)
        self.bottom_widget_name_foreward = QLabel()
        self.set_label_style(self.bottom_widget_name_foreward, self.font_small, self.label_style)

        self.right_button = QPushButton(">")
        self.right_button.setFixedSize(40, 80)
        self.right_button.setStyleSheet(self.button_style)

        self.bottom_line.addWidget(self.left_button)
        self.bottom_line.addStretch(1)
        self.bottom_line.addWidget(self.bottom_widget_name_backward)
        self.bottom_line.addSpacing(30)
        self.bottom_line.addWidget(self.bottom_widget_name_current)
        self.bottom_line.addSpacing(30)
        self.bottom_line.addWidget(self.bottom_widget_name_foreward)
        self.bottom_line.addStretch(1)
        self.bottom_line.addWidget(self.right_button)

        self.setLayout(self.main_layout)
        self.set_bottom_line()

        # Timer
        self.switch_timer = QTimer(self)
        self.switch_timer.setInterval(10000)  # 10 seconds
        self.switch_timer.timeout.connect(lambda: self.toggle_main_widget(+1))
        self.switch_timer.start()

        self.left_button.clicked.connect(lambda state: self.toggle_main_widget(-1))
        self.right_button.clicked.connect(lambda state: self.toggle_main_widget(+1))

    def set_units(self, units: UnitSystem):
        self.units = units

    def units(self) -> UnitSystem:
        return self.units

    def switch_view(self, index: int = 0):
        max_value = self.self.view_stack.count()
        self.self.view_stack.setCurrentIndex(index % max_value)

    def set_data(self, data: dict):
        for i in range(0, self.view_stack.count()):
            self.view_stack.widget(i).set_data(data)

    def get_name(self) -> str:
        return self.city_name

    def set_label_style(self, label: QLabel, font: QFont, style: str):
        label.setStyleSheet(style)
        label.setFont(font)

    def set_bottom_line(self):
        max_value = self.view_stack.count()
        current = self.view_stack.currentIndex()
        if max_value == 1:
            self.bottom_widget_name_backward.setText("")
            self.bottom_widget_name_current.setText(self.view_stack.widget(current).get_name())
            self.bottom_widget_name_foreward.setText("")
            return
        self.bottom_widget_name_backward.setText(self.view_stack.widget((current - 1) % max_value).get_name())
        self.bottom_widget_name_current.setText(self.view_stack.widget(current).get_name())
        self.bottom_widget_name_foreward.setText(self.view_stack.widget((current + 1) % max_value).get_name())

    def toggle_main_widget(self, index: int):
        max_value = self.view_stack.count()
        current = self.view_stack.currentIndex()
        self.view_stack.setCurrentIndex((current + index) % max_value)
        self.set_bottom_line()