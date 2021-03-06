from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QComboBox
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QLabel ,QLineEdit
from PyQt5.QtGui import QPalette, QFont
from PyQt5.QtCore import Qt
from subscreens.weather_pkg.unitsystem import UnitSystem
from gui.gui_element import Gui_Element
from gui.gui_button_builder import GuiButtonBuilder


class SetupWidget(QWidget):
    def __init__(self, parent, foreground_color="#ffffff", font_name=""):
        super(SetupWidget, self).__init__()

        self.name = "Setup"
        self.parent = parent
        self.main_layout = QVBoxLayout()

        self.font = QFont(font_name, 60, QFont.Bold)
        self.font_small = QFont(font_name, 30, QFont.Bold)
        self.font_extra_small = QFont(font_name, 20, QFont.Bold)

        self.foreground_color = foreground_color
        self.label_style = "QLabel { color : " + self.foreground_color + "; }"

        self.app_id_label = QLabel("AppID:")
        self.app_id_value = QLineEdit()

        self.head_line = QHBoxLayout()
        self.title_label = QLabel("Stadt hinzufügen")
        self.title_label.setFont(self.font_small)
        self.title_label.setStyleSheet(self.label_style)
        self.head_line.addStretch()
        self.head_line.addWidget(self.title_label)

        self.head_line.addStretch()

        self.combobox_line = QHBoxLayout()
        self.city_combobox = QComboBox()
        self.city_combobox.setFixedSize(200, 40)
        self.city_combobox.setEditable(False)
        self.city_combobox.setFont(self.font_extra_small)
        self.city_combobox.addItems(["Berlin", "Dresden", "Leipzig"])
        self.combo_changed(self.city_combobox)
        self.combobox_line.addStretch(1)
        self.combobox_line.addWidget(self.city_combobox)

        self.gui_button_builder = GuiButtonBuilder()
        self.gui_button_builder.set_color(self.foreground_color)
        self.gui_button_builder.set_size(40, 80)
        self.add_button = self.gui_button_builder.create_button("Neu", Gui_Element.BUTTON_FULL_CIRCLE_TEXT)

        self.unit_line = QHBoxLayout()

        self.unit_combobox = QComboBox()
        self.unit_combobox.setFixedSize(200, 40)
        self.unit_combobox.setFont(self.font_extra_small)
        self.combo_changed(self.unit_combobox)

        self.unit_combobox.setAutoFillBackground(True)
        self.unit_combobox.addItems([UnitSystem.metric.name, UnitSystem.imperial.name])

        self.combobox_line.addWidget(self.unit_combobox)
        self.combobox_line.addWidget(self.add_button)
        self.combobox_line.addStretch(1)

        self.main_layout.addLayout(self.head_line)
        self.main_layout.addSpacing(40)
        self.main_layout.addLayout(self.combobox_line)

        self.main_layout.addStretch()

        self.setLayout(self.main_layout)

        self.add_button.clicked.connect(lambda: self.add_new_city())

    def add_new_city(self):
        city = self.city_combobox.currentText()
        unit_name = self.unit_combobox.currentText()
        unit = UnitSystem[unit_name]
        self.parent.create_new_city(city, unit)

    def combo_changed(self, combo_box: QComboBox):
        combo_box.setStyleSheet("color: "+ self.foreground_color + ";"
                                "background-color: black;"
                                "selection-color: " + self.foreground_color + ";")

    def get_name(self) -> str:
        return self.name

    def get_key(self) -> str:
        # ToDo create QEditline to set Key
        pass

    def get_language(self) -> str:
        # ToDo create QEditLine to set language
        pass
