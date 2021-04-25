from .render import Render


class Button_semi_left(Render):

    # test @ https://editor.method.ac/
    #   <svg height="{100}" width="{300}">
    #       <path id="svg_1" fill="#111111" d="m0,50 q0,-50 50,-50 l-50,0 l0,50 z"/>
    #       <path id="svg_1" fill="#111111" d="m0,50 q0,50 50,50 l-50,0l0,-50 z"/>
    #   </svg>

    svg = ('<svg height="{h}" width="{w}">'
           '<path id="svg_1" fill="{backg}" d="m0,{r} q0,-{r} {r},-{r} l-{r},0 l0,{r} z"/>'
           '<path id="svg_1" fill="{backg}" d="m0,{r} q0,{r} {r},{r} l-{r},0 l0,-{r} z"/>'
           '</svg>')

    def interpolate_svg(self):
        r = self.height / 2
        rectW = self.width - r
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
        self.file_name = file_name
