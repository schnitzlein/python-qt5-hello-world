from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QWidget, QStackedWidget
from subscreens.weather_pkg.simple_temp_view_widget import SimpleTempViewWidget
from subscreens.weather_pkg.unitsystem import UnitSystem


class CityWidget(QWidget):
    def __init__(self, name: str, units: UnitSystem = UnitSystem.metric, foreground_color="#ffffff", font_name=""):
        super(CityWidget, self).__init__()

        self.main_layout = QHBoxLayout()
        self.city_name = name
        self.units = units
        self.foreground_color = foreground_color
        self.font_name = font_name
        self.weather_data = {}
        self.view_stack = QStackedWidget()
        self.temp_view = SimpleTempViewWidget(self, units, self.foreground_color, self.font_name)
        self.view_stack.addWidget(self.temp_view)
        self.main_layout.addWidget(self.view_stack)
        self.setLayout(self.main_layout)

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
