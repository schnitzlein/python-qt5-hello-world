from PyQt5.QtWidgets import QPushButton

from PyQt5.QtWidgets import QStackedWidget
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout
from util.eventhandler.observer import Observer
from util.rest.rest_special import RestSpecial
from subscreens.baseclass import Base

from subscreens.weather.setup_widget import SetupWidget
from subscreens.weather.city_widget import CityWidget
from subscreens.weather.unitsystem import UnitSystem

from gui.gui_element import Gui_Element
from gui.gui_button_builder import GuiButtonBuilder

_data = {'coord': {'lon': 13.4105, 'lat': 52.5244}, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'Ein paar Wolken', 'icon': '02n'}], 'base': 'stations', 'main': {'temp': 21.17, 'feels_like': 21.46, 'temp_min': 18.88, 'temp_max': 22.84, 'pressure': 1006, 'humidity': 81}, 'visibility': 10000, 'wind': {'speed': 1.34, 'deg': 340, 'gust': 3.13}, 'clouds': {'all': 20}, 'dt': 1626382653, 'sys': {'type': 2, 'id': 2011538, 'country': 'DE', 'sunrise': 1626318094, 'sunset': 1626376960}, 'timezone': 7200, 'id': 2950159, 'name': 'Berlin', 'cod': 200}


class Weather(Base):
    def __init__(self, observer: Observer, name: str, foreground_color="#ffffff", font_name=""):
        super().__init__(observer, name, foreground_color, font_name)

        self.foreground_color = foreground_color
        self.name = "Weather"
        self.font_name = font_name
        #self.symbol = QLabel(self.name)
        #self.symbol.setFont(self.font)
        #self.symbol.setStyleSheet("QLabel { color : " + self.foreground_color + "; }, QButton { color: "+ self.foreground_color + "; }")

        #self.listFile = QListWidget()
        #self.label = QLabel('Stadt:')
        #self.data_button = QPushButton('Start')

        self.view_stack = QStackedWidget()
        self.view_stack.addWidget(SetupWidget(self, self.foreground_color))

        #self.label.setFont(self.font)
        #self.data_button.setFont(self.font)
        #self.setStyleSheet("QLabel { color : " + self.foreground_color + "; }")

        self.main_layout = QVBoxLayout()
        self.head_line = QHBoxLayout()
        self.main_line = QHBoxLayout()
        self.main_layout.addLayout(self.head_line)
        self.main_layout.addLayout(self.main_line)

        #self.gui_button_builder = GuiButtonBuilder()
        #self.gui_button_builder.set_color(self.foreground_color)
        #self.gui_button_builder.set_size(400, 40)
        style = "QPushButton { background-color: " + self.foreground_color + "; border: 2px; border-radius: 20px; border-style: outset;}"
        self.left_button = QPushButton("<")
        self.left_button.setFixedSize(40, 400)
        self.left_button.setStyleSheet(style)

        self.main_line.addWidget(self.left_button)
        self.main_line.addWidget(self.view_stack)
        self.right_button = QPushButton(">")
        self.right_button.setFixedSize(40, 400)
        self.right_button.setStyleSheet(style)
        self.main_line.addWidget(self.right_button)
        #self.data_button.clicked.connect(self.startTimer)

        self.setLayout(self.main_layout)

        self.r = RestSpecial()
        self.data = None

        self.left_button.clicked.connect(
            lambda state: self.toggle_main_widget(-1))
        self.right_button.clicked.connect(
            lambda state: self.toggle_main_widget(+1))
        #self.data_button.clicked.connect(self.showData)

    def create_new_city(self, city_name: str, unit: UnitSystem):
        city_widget = CityWidget(city_name, unit, self.foreground_color, self.font_name)
        #data = _data
        data = self.call_server(city=city_name, language="de") # ToDo Rest anbinden
        #f = open("demofile.txt", "w")
        #f.write(str(self.call_server(city=city_name, language="de")))
        #f.close()
        city_widget.set_data(data)
        self.view_stack.addWidget(city_widget)
        current = self.view_stack.currentIndex()
        self.toggle_main_widget(current + 1)


    def showData(self):
        if self.data is not None:
            self.label.setText("{}°C".format(self.data['main']['temp']))
        else:
            self.call_server(city="Dresden", language="de")
            self.label.setText("{}°C".format(self.data["data"]['main']['temp']))

    def call_server( self, city: str, language: str ) -> dict:
        """
        returns dictionary with response from Rest
        if response HTTP Status != 200 returns None
        """
        if not city:
            city = "Berlin"
        if not language:
            language = "de" # en, fr, ... , https://openweathermap.org/current#multi
        
        #TODO: write to file / read from file etc... and store calls and check if...
        call_parameter = { "city": city, "units": "metric", "language": language, "key": "36dcf663b6964439a18574709e1d6eef"}
        self.data = self.r.call_server_weather(call_parameter)
        if self.data['code'] == 200:
            return self.data['data']
        else:
            return None

        #http://api.openweathermap.org/data/2.5/weather?q=Dresden&units=metric&lang=de&appid=36dcf663b6964439a18574709e1d6eef

    def toggle_main_widget(self, index: int):
        max_value = self.view_stack.count()
        current = self.view_stack.currentIndex()
        self.view_stack.setCurrentIndex((current + index) % max_value)
