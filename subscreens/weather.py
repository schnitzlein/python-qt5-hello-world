from .weather_pkg.start_widget import StartWidget
from util.eventhandler.observer import Observer
from util.rest.rest_special import RestSpecial
from subscreens.baseclass import Base

from PyQt5.QtWidgets import QVBoxLayout

from gui.gui_element import Gui_Element
from gui.gui_button_builder import GuiButtonBuilder

_data = {'coord': {'lon': 13.4105, 'lat': 52.5244}, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'Ein paar Wolken', 'icon': '02n'}], 'base': 'stations', 'main': {'temp': 21.17, 'feels_like': 21.46, 'temp_min': 18.88, 'temp_max': 22.84, 'pressure': 1006, 'humidity': 81}, 'visibility': 10000, 'wind': {'speed': 1.34, 'deg': 340, 'gust': 3.13}, 'clouds': {'all': 20}, 'dt': 1626382653, 'sys': {'type': 2, 'id': 2011538, 'country': 'DE', 'sunrise': 1626318094, 'sunset': 1626376960}, 'timezone': 7200, 'id': 2950159, 'name': 'Berlin', 'cod': 200}


class Weather(Base):
    def __init__(self, observer: Observer, name: str, foreground_color="#ffffff", font_name=""):
        super().__init__(observer, name, foreground_color, font_name)

        self.foreground_color = foreground_color
        self.name = "Weather"
        self.font_name = font_name

        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)

        self.start_widget = StartWidget(self, self.foreground_color, self.font_name)
        self.main_layout.addWidget(self.start_widget)

        self.r = RestSpecial()
        self.data = None

    def load_start_config(self):
        # ToDo Laden von Konfigurierten Städten aus "weather_app_config.json"
        # self.start_widget.create_new_city()
        pass

    def get_data(self, config: dict) -> dict:
        # ToDo Datenabfrage entweder neu oder gespeicherte Daten
        return _data

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
        call_parameter = {"city": city, "units": "metric", "language": language, "key": "36dcf663b6964439a18574709e1d6eef"}
        self.data = self.r.call_server_weather(call_parameter)
        if self.data['code'] == 200:
            return self.data['data']
        else:
            return None

        # http://api.openweathermap.org/data/2.5/weather?q=Dresden&units=metric&lang=de&appid=36dcf663b6964439a18574709e1d6eef
