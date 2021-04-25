from .render import Render

class Button_old(Render):
    svg = ('<svg height="{h}" width="{w}">'
           '<circle id="svg_1" fill="{f}" r="{r}" cy="{r}" cx="{r}"/>'
           '<rect height="{h}" width="{rectw}" x="{r}" y="0" fill="{f}" id="svg_1"/>'
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

    def __init__(self, width, height, fill, background, file_name):
        super().__init__(file_name)
        self.width = width
        self.height = height
        self.fill = fill
        self.background = background
