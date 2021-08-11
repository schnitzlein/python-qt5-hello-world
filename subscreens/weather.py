from .weather_pkg.start_widget import StartWidget
from util.eventhandler.observer import Observer
from util.rest.rest_special import RestSpecial
from subscreens.baseclass import Base

from PyQt5.QtWidgets import QVBoxLayout

from gui.gui_element import Gui_Element
from gui.gui_button_builder import GuiButtonBuilder

from util.filehandler import FileHandler
import logging
log = logging.getLogger(__name__)

#_data = {'coord': {'lon': 13.4105, 'lat': 52.5244}, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'Ein paar Wolken', 'icon': '02n'}], 'base': 'stations', 'main': {'temp': 21.17, 'feels_like': 21.46, 'temp_min': 18.88, 'temp_max': 22.84, 'pressure': 1006, 'humidity': 81}, 'visibility': 10000, 'wind': {'speed': 1.34, 'deg': 340, 'gust': 3.13}, 'clouds': {'all': 20}, 'dt': 1626382653, 'sys': {'type': 2, 'id': 2011538, 'country': 'DE', 'sunrise': 1626318094, 'sunset': 1626376960}, 'timezone': 7200, 'id': 2950159, 'name': 'Berlin', 'cod': 200}


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
        self.f = FileHandler()

    def load_start_config(self):
        # TODO: Laden von Konfigurierten Städten aus "weather_app_config.json"
        # self.start_widget.create_new_city()
        pass

    def get_data(self, config: dict) -> dict:
        # TODO: read from config dictionary call param data
        city = "Berlin"
        filepath_str = "./data/weather_{}.json".format(city)

        # check time age
        log.debug( "Last time file was modified: {}".format(self.r.get_data_age_str(filepath_str)) )
        log.debug( "Diff in hours: {}h".format(self.r.dataTimeDiff(filepath_str)))
        if self.r.dataTimeDiff(filepath_str) >= 1 or not self.f.is_file(filepath_str):
            log.info("call server")
            self.call_server(city=city, language="de")
            self.save_data(filepath=filepath_str)
        # keep old Data
        # TODO: create a toggle/switch/config param for this threshold calling server for new data or not
        elif self.r.dataTimeDiff(filepath_str) < 1:
            self.load_data(filepath=filepath_str)
        return self.data
    
    def save_data(self, filepath: str):
        self.r.save_data(data=self.data, filename=filepath)

    def load_data(self, filepath: str):
        self.data = self.r.load_data(filename=filepath)

    def showData(self):
        if self.data is not None:
            self.label.setText("{}°C".format(self.data['main']['temp']))
        else:
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
        
        call_parameter = {"city": city, "units": "metric", "language": language, "key": "36dcf663b6964439a18574709e1d6eef"}
        new_data = self.r.call_server_weather(call_parameter)
        if new_data['code'] == 200:
            self.data = new_data['data']
        else:
            # check if self.data contains old data, if not set to empty dictionary, 
            # it will raise in exception in higher order class, for empty dictionary entrys
            if not self.data:
                self.data = {}
        return self.data

        # http://api.openweathermap.org/data/2.5/weather?q=Dresden&units=metric&lang=de&appid=36dcf663b6964439a18574709e1d6eef
