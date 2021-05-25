from PyQt5.QtWidgets import QLabel, QListWidget, QListWidgetItem
from gui.gui_button_builder import GuiButtonBuilder
from gui.gui_element import Gui_Element
from PyQt5.QtWidgets import QHBoxLayout, QGridLayout
from PyQt5.QtWidgets import QWidget, QStackedWidget
from PyQt5.QtCore import QTimer, QSize

from subscreens.baseclass import Base


class TimerListItem(QListWidgetItem):

    def __init__(self, parent, timer_config: dict):
        super().__init__(parent)
        self.parent = parent
        self.name = timer_config["name"]
        self.hour = int(timer_config["hour"])
        self.minutes = int(timer_config["minute"])
        self.seconds = int(timer_config["second"])

    def get_name(self) -> str:
        return self.name

    def get_start_value_as_int(self) -> int:
        value = self.hour * 60 * 60
        value = value + self.minutes * 60
        value = value + self.seconds
        value = value * 1000
        return value

    def get_start_value_as_str(self) -> str:
        value = self.format_value(self.hour) + ":" + self.format_value(self.minutes) + ":" + self.format_value(
            self.seconds)
        return value

    @staticmethod
    def format_value(value: int) -> str:
        if value < 10:
            return "0" + str(value)
        else:
            return str(value)


class TimerListWidget(QWidget):

    def __init__(self, parent, item: TimerListItem, foreground_color="#ffffff"):
        super().__init__()

        self.parent = parent
        self.item = item
        self.foreground_color = foreground_color
        self.setStyleSheet("QLabel { color : " + self.foreground_color + "; font: 30pt;}")
        self.hbox_layout = QHBoxLayout()
        self.timer_name = QLabel(self.item.get_name())
        self.timer_value = QLabel(self.item.get_start_value_as_str())
        self.start_button_state = False  # Is active
        self.check_timer = QTimer(self)
        self.check_timer.setInterval(100)  # .1 seconds
        self.check_timer.timeout.connect(lambda: self.update_count_down())
        self.count_down_timer = QTimer(self)
        self.count_down_timer.setInterval(item.get_start_value_as_int())
        self.count_down_timer.timeout.connect(lambda: self.count_down_end())
        self.gui_button_builder = GuiButtonBuilder()

        self.gui_button_builder.set_color(foreground_color)
        self.gui_button_builder.set_size(30, 60)
        self.delete_button = self.gui_button_builder.create_button("Delete", Gui_Element.BUTTON_FULL_CIRCLE_TEXT)
        self.delete_button.clicked.connect(lambda: self.remove_item())
        self.start_pause_button = self.gui_button_builder.create_button("Start", Gui_Element.BUTTON_FULL_CIRCLE_TEXT)
        self.start_pause_button.clicked.connect(lambda: self.start_button_pressed())

        self.hbox_layout.addWidget(self.timer_name)
        self.hbox_layout.addWidget(self.timer_value)
        self.hbox_layout.addWidget(self.start_pause_button)
        self.hbox_layout.addWidget(self.delete_button)

        self.setLayout(self.hbox_layout)

    def remove_item(self):
        row = self.parent.row(self.item)
        self.parent.takeItem(row)
        self.check_timer.stop()
        self.count_down_timer.stop()
        del self.item
        del self

    def start_button_pressed(self):
        if self.start_button_state:
            self.start_button_state = False
            self.start_pause_button.setText("Stop")
            self.check_timer.stop()
            self.count_down_timer.stop()
        else:
            self.start_button_state = True
            self.start_pause_button.setText("Start")
            self.check_timer.start()
            self.count_down_timer.start()

    def update_count_down(self):
        millis = self.count_down_timer.remainingTime()
        if millis < 0:
            self.timer_value.setText("00:00:00")
            return

        seconds = (millis / 1000) % 60
        seconds = int(seconds)
        minutes = (millis / (1000 * 60)) % 60
        minutes = int(minutes)
        hours = (millis / (1000 * 60 * 60)) % 24
        string = "%02d:%02d:%02d" % (hours, minutes, seconds)
        self.timer_value.setText(string)

    def count_down_end(self):
        self.count_down_timer.stop()
        # ToDo Alert Signal to main_window


class Timer(Base):

    def __init__(self, name: str, foreground_color="#ffffff", font_name=""):
        super().__init__(name, foreground_color, font_name)

        self.main_layout = QGridLayout()
        self.central_widget = QStackedWidget()
        self.timer_overview_widget = QWidget()
        self.central_widget.insertWidget(0, TimerOverview(self, "TimerOverview", "#441456"))
        self.central_widget.insertWidget(1, AddTimer(self, "AddTimer", "#ff1422"))
        self.central_widget.setCurrentIndex(0)

        self.main_layout.addWidget(self.central_widget)
        self.setLayout(self.main_layout)

    def pass_timer(self, timer_config: dict):
        self.central_widget.widget(0).add_timer(timer_config)

    def switch_central_widget(self):
        max_value = self.central_widget.count()
        index = self.central_widget.currentIndex()
        self.central_widget.setCurrentIndex((index + 1) % max_value)


class TimerOverview(Base):
    def __init__(self, parent, name: str, foreground_color="#ffffff", font_name=""):
        super().__init__(name, foreground_color, font_name)
        self.parent = parent
        self.foreground_color = foreground_color
        self.background_color = "#050505"
        self.gui_button_builder = GuiButtonBuilder()
        self.timer_name = QLabel("Name:")
        self.timer_name_value = QLabel("Timer ")
        self.main_layout = QGridLayout()
        self.timer_list = QListWidget()
        self.timer_list.setStyleSheet(
            "QListWidget{background:" + self.background_color + ";  border: 0px solid " + self.foreground_color + ";}")

        self.gui_button_builder.set_color(foreground_color)
        self.gui_button_builder.set_size(50, 100)
        self.button_add_timer = self.gui_button_builder.create_button("Create",
                                                                      Gui_Element.BUTTON_FULL_CIRCLE_TEXT)
        self.button_add_timer.clicked.connect(lambda: self.parent.switch_central_widget())

        self.main_layout.addWidget(self.timer_list, 0, 0, 3, 4)
        self.main_layout.addWidget(self.button_add_timer, 4, 5)
        self.setLayout(self.main_layout)

    def add_timer(self, timer_config: dict):
        timer_item = TimerListItem(self.timer_list, timer_config)
        timer_item.setSizeHint(QSize(100, 50))
        timer_widget_item = TimerListWidget(self.timer_list, timer_item, "#ff00ff")
        self.timer_list.addItem(timer_item)
        self.timer_list.setItemWidget(timer_item, timer_widget_item)

    def delete_timer(self, item: TimerListItem):
        self.timer_list.removeItemWidget(item)


class AddTimer(Base):

    def __init__(self, parent, name: str, foreground_color="#ffffff", font_name=""):
        super().__init__(name, foreground_color, font_name)
        self.parent = parent
        self.gui_button_builder = GuiButtonBuilder()
        self.timer_name = QLabel("Name:")
        self.timer_name_value = QLabel("Timer ")
        self.timer_counter = 0
        self.main_layout = QGridLayout()
        self.hbox_titel = QHBoxLayout()
        self.hbox_up = QHBoxLayout()
        self.hbox_value = QHBoxLayout()
        self.hbox_down = QHBoxLayout()
        self.hbox_control = QHBoxLayout()
        self.hbox_placeholder = QHBoxLayout()

        self.hour = QLabel("0")
        self.minutes = QLabel("0")
        self.seconds = QLabel("0")
        self.setStyleSheet("QLabel { color : " + self.foreground_color + "; font: 30pt;}")

        self.gui_button_builder.set_color(foreground_color)
        self.gui_button_builder.set_size(30, 100)
        self.gui_button_builder.set_style("font-size: 30pt;")
        self.button_up_h = self.gui_button_builder.create_button("h+", Gui_Element.BUTTON_FULL_CIRCLE_TEXT)
        self.button_down_h = self.gui_button_builder.create_button("h-", Gui_Element.BUTTON_FULL_CIRCLE_TEXT)
        self.button_up_min = self.gui_button_builder.create_button("min+", Gui_Element.BUTTON_FULL_CIRCLE_TEXT)
        self.button_down_min = self.gui_button_builder.create_button("min-", Gui_Element.BUTTON_FULL_CIRCLE_TEXT)
        self.button_up_sec = self.gui_button_builder.create_button("sec+", Gui_Element.BUTTON_FULL_CIRCLE_TEXT)
        self.button_down_sec = self.gui_button_builder.create_button("sec-", Gui_Element.BUTTON_FULL_CIRCLE_TEXT)

        self.button_up_h.clicked.connect(lambda state, lab=self.hour: self.plus(lab, 23))
        self.button_down_h.clicked.connect(lambda state, lab=self.hour: self.minus(lab, 23))
        self.button_up_min.clicked.connect(lambda state, lab=self.minutes: self.plus(lab, 59))
        self.button_down_min.clicked.connect(lambda state, lab=self.minutes: self.minus(lab, 59))
        self.button_up_sec.clicked.connect(lambda state, lab=self.seconds: self.plus(lab, 59))
        self.button_down_sec.clicked.connect(lambda state, lab=self.seconds: self.minus(lab, 59))

        self.button_add_timer = self.gui_button_builder.create_button("Add", Gui_Element.BUTTON_FULL_CIRCLE_TEXT)
        self.button_add_timer.clicked.connect(lambda: self.add_timer())
        self.button_close = self.gui_button_builder.create_button("OK", Gui_Element.BUTTON_FULL_CIRCLE_TEXT)
        self.button_close.clicked.connect(lambda: self.parent.switch_central_widget())

        # ToDo refactor layout
        self.hbox_titel.addStretch()
        self.hbox_titel.addWidget(self.timer_name)
        self.hbox_titel.addWidget(self.timer_name_value)
        self.hbox_titel.addStretch()

        self.hbox_up.addStretch()
        self.hbox_up.addWidget(self.button_up_h)
        self.hbox_up.addStretch()
        self.hbox_up.addWidget(self.button_up_min)
        self.hbox_up.addStretch()
        self.hbox_up.addWidget(self.button_up_sec)
        self.hbox_up.addStretch()

        self.hbox_value.addStretch()
        self.hbox_value.addWidget(self.hour)
        self.hbox_value.addStretch()
        self.hbox_value.addWidget(self.minutes)
        self.hbox_value.addStretch()
        self.hbox_value.addWidget(self.seconds)
        self.hbox_value.addStretch()

        self.hbox_down.addStretch()
        self.hbox_down.addWidget(self.button_down_h)
        self.hbox_down.addStretch()
        self.hbox_down.addWidget(self.button_down_min)
        self.hbox_down.addStretch()
        self.hbox_down.addWidget(self.button_down_sec)
        self.hbox_down.addStretch()

        self.hbox_placeholder.addStretch()
        self.hbox_placeholder.addWidget(QLabel(""))

        self.hbox_control.addStretch()
        self.hbox_control.addWidget(self.button_add_timer)
        self.hbox_control.addWidget(self.button_close)

        self.main_layout.addLayout(self.hbox_titel, 0, 0)
        self.main_layout.addLayout(self.hbox_up, 1, 0)
        self.main_layout.addLayout(self.hbox_value, 2, 0)
        self.main_layout.addLayout(self.hbox_down, 3, 0)
        self.main_layout.addLayout(self.hbox_placeholder, 4, 0)
        self.main_layout.addLayout(self.hbox_control, 5, 0)
        self.setLayout(self.main_layout)

    @staticmethod
    def plus(label: QLabel, max_value: int):
        label.setText(str((int(label.text()) + 1) % max_value))

    @staticmethod
    def minus(label: QLabel, max_value: int):
        value = int(label.text())
        value = value - 1
        if value < 0:
            label.setText(str(max_value))
        else:
            label.setText(str(value))

    def add_timer(self):
        timer_config = {"name": "Timer",
                        "hour": "0",
                        "minute": "0",
                        "second": "0"}

        self.timer_name_value.setText((self.timer_name_value.text()[:6]) + str(self.timer_counter))
        self.timer_counter = self.timer_counter + 1
        timer_config["name"] = self.timer_name_value.text()
        timer_config["hour"] = self.hour.text()
        timer_config["minute"] = self.minutes.text()
        timer_config["second"] = self.seconds.text()

        self.parent.pass_timer(timer_config)
