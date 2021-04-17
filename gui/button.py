from PyQt5 import QtCore, QtGui, QtSvg
import os.path


class Button():
    sub_folder = "buttons"
    image_folder = "gui_elements"
    svg = ('<svg height="{h}" width="{w}">'
           '<circle id="svg_1" fill="{f}" r="{r}" cy="{r}" cx="{r}"/>'
           '<rect height="{h}" width="{rectw}" x="{r}" y="0" fill="{f}" id="svg_2"/>'
           '<circle id="svg_1" fill="{f}" r="{r}" cy="{r}" cx="{cx}"/>'
           '</svg>')

    def interpolate_svg(self):
        r = self.height / 2
        rectW = self.width - r * 2
        cx = rectW + r
        return self.svg.format(
            h=self.height,
            w=self.width,
            rectw=rectW,
            r=r,
            f=self.fill,
            cx=cx,
            backg=self.background)

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

    def build_svg(self):
        svg = self.interpolate_svg()
        return self.save_img(svg, QtCore.QSize(self.width, self.height))

    def render_svg(self, svg, size):
        renderer = QtSvg.QSvgRenderer(bytes(svg, 'utf-8'))
        qim = QtGui.QImage(size, QtGui.QImage.Format_ARGB32)
        qim.fill(0)
        painter = QtGui.QPainter()
        painter.begin(qim)
        renderer.render(painter)
        painter.end()
        return qim

    def __init__(self, width, height, fill, background, file_name):
        self.width = width
        self.height = height
        self.fill = fill
        self.background = background
        self.file_name = file_name
