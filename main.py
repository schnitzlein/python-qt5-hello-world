import sys
from PyQt5.QtWidgets import QApplication
from main_window import MainWindow
from configreader.configreader import ConfigReader

if __name__ == '__main__':

    app = QApplication(sys.argv)
    reader = ConfigReader()
    main_config_dict = reader.read_config("./configreader/main_config.json")
    screen_rect = app.desktop().screenGeometry()
    window = MainWindow(screen_rect)
    window.init_with_config(main_config_dict)
    window.show()
    app.exec()

