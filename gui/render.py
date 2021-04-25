import os.path

from PyQt5 import QtGui, QtSvg, QtCore


class Render():
    sub_folder = "buttons"
    image_folder = "gui_elements"

    def save_img(self, svg, size):
        path = os.path.join(self.image_folder, self.sub_folder)
        filename = str(hash(self.file_name)) + ".png"  # TODO use reproducible hash for filename
        url = os.path.join(path, filename)
        if not os.path.isfile(url):
            if not os.path.isdir(path):
                os.makedirs(path)
            image = self.render_svg(svg, size)
            image.save(url, "PNG")
        return url

    def render_svg(self, svg, size):
        renderer = QtSvg.QSvgRenderer(bytes(svg, 'utf-8'))
        qim = QtGui.QImage(size, QtGui.QImage.Format_ARGB32)
        qim.fill(0)
        painter = QtGui.QPainter()
        painter.begin(qim)
        renderer.render(painter)
        painter.end()
        return qim

    def build_svg(self):
        svg = self.interpolate_svg()
        return self.save_img(svg, QtCore.QSize(self.width, self.height))

    def __init__(self, file_name):
        self.file_name = file_name