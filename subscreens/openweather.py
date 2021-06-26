from PyQt5.QtWidgets import QPushButton, QWidget
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QListWidget,QGridLayout,QLabel

from util.rest.rest import Rest
from subscreens.baseclass import Base

class Rest(Base):
    def __init__(self, name: str, foreground_color="#ffffff", font_name=""):
        super().__init__(name, foreground_color, font_name)

        self.foreground_color = foreground_color
        self.name = "Rest"
        self.symbol = QLabel(self.name)
        self.symbol.setFont(self.font)
        self.symbol.setStyleSheet("QLabel { color : " + self.foreground_color + "; }, QButton { color: "+ self.foreground_color + "; }")

        self.listFile=QListWidget()
        self.label=QLabel('Label')
        self.data_button=QPushButton('Start')

        self.label.setFont(self.font)
        self.data_button.setFont(self.font)
        self.setStyleSheet("QLabel { color : " + self.foreground_color + "; }")

        layout=QGridLayout()
        layout.addWidget(self.label, 0, 0, 1, 2)
        layout.addWidget(self.data_button, 1, 0)

        self.data_button.clicked.connect(self.startTimer)

        self.setLayout(layout)

        self.r = Rest("http://api.openweathermap.org", "36dcf663b6964439a18574709e1d6eef")
        self.data = None

        self.data_button.clicked.connect(self.showData)
    
    def showData(self):
        if self.data is not None:
            self.label.setText("{}°C".format(self.data['main']['temp']))
        else:
            self.call_server(city="Dresden", language="de")
            self.label.setText("{}°C".format(self.data['main']['temp']))

    def call_server( self, city: str, language: str ) -> dict:
        """
        returns dictionary with response from Rest
        if response HTTP Status != 200 returns None
        """
        if not city:
            city = "Berlin"
        if not language:
            language = "de" # en, fr, ... , https://openweathermap.org/current#multi
        
        subpath = "/data/2.5/weather?q={}&units=metric&lang={}".format(city, language)
        self.data = self.r.call_server(subpath=subpath)
        if self.data['code'] == 200:
            return self.data['data']
        else:
            return None


        #http://api.openweathermap.org/data/2.5/weather?q=Dresden&units=metric&lang=de&appid=36dcf663b6964439a18574709e1d6eef