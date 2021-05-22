from PyQt5.QtCore import QCoreApplication, QEvent
from PyQt5.QtWidgets import QGridLayout, QLabel, QPushButton
from subscreens.baseclass import Base


class MyEvent(QEvent):
    idType = 65535
    name = "MyEventName"
    data = None

    def __init__(self, event_id=1000, name="", data=None):
        '''after id 1000 starts custom_user_event'''
        self.idType = QEvent.registerEventType(event_id)
        self.name = name
        self.data = data
        QEvent.__init__(self, self.idType)
        print("Created CustomEvent with id: ", self.idType)
    
    def set_data(self, data=None):
        self.data = data

    def get_data(self):
        return self.data
    
    def get_name(self) -> str:
        return self.name
    
    # TODO: override spontaneous()


class MyCustomEventTest(Base):

    def __init__(self, name: str, foreground_color="#ffffff", font_name=""):
        super().__init__(name, foreground_color, font_name)

        # create Custom Events + fill with data
        self.event1 = MyEvent(event_id=512, name="Arnold Reacting", data={'mydata': 'foobar', 'value': 512})
        self.event2 = MyEvent(event_id=1337, name="Johny Knocksville", data={'mydata': 'barfoo', 'value': 1337})

        # GUI Stuff
        self.resize(400, 200)

        self.event1_button = QPushButton("Event1", self)
        self.event2_button = QPushButton("Event2", self)
        self.label = QLabel("Custom Event Experiment", self)
        
        self.event1_button.clicked.connect(self.call_back_event1_button)
        self.event2_button.clicked.connect(self.call_back_event2_button)

        self.label.setFont(self.font)
        self.label.setStyleSheet("QLabel { color : " + self.foreground_color + "; }")
        self.event1_button.setFont(self.font)
        self.event1_button.setStyleSheet("QButton { color: "+ self.foreground_color + "; }")
        self.event2_button.setFont(self.font)
        self.event2_button.setStyleSheet("QButton { color: "+ self.foreground_color + "; }")

        layout = QGridLayout()
        layout.addWidget(self.event1_button)
        layout.addWidget(self.event2_button)
        layout.addWidget(self.label)
        self.setLayout(layout)

        

    def call_back_event1_button(self):
        QCoreApplication.sendEvent(self, self.event1)

    def call_back_event2_button(self):
        QCoreApplication.sendEvent(self, self.event2)

    def customEvent(self, e):
        print("customEvent:", e.type())
        if e.type() == self.event1.idType:
            print("Received Event1: {}".format(e.get_data()))
            print("Event Name: {}".format(e.get_name()))
            self.label.setText("Event1")
            #print(e.isAccepted())
        elif e.type() == self.event2.idType:
            print("Received Event2: {}".format(e.get_data()))
            print("Event Name: {}".format(e.get_name()))
            self.label.setText("Event2")
        else:
            self.label.setText("Unknown Event")
    
    # TODO: use event filters to override and do custom action, see: https://doc.qt.io/qtforpython/overviews/eventsandfilters.html#event-types

