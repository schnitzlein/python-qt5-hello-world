from .render import Render


class Button_semi_right(Render):
    
    # test @ https://editor.method.ac/
    #   <svg height="{100}" width="{300}">
    #       <path id="svg_1" fill="#111111" d="m0,0 l250,0 q50,0 50,50 l0,-50 l-300,0 l0,50 z"/>
    #       <path id="svg_1" fill="#111111" d="m0,100 l250,0 q50,0 50,-50 l0,50 l-300,0 l0,-50 z"/>
    #   </svg>

    svg = ('<svg height="{h}" width="{w}">'
           '<path id="svg_1" fill="{backg}" d="m0,0 l{rectw},0 q{r},0 {r},{r} l0,-{r} l-{w},0 l0,{r} z"/>'
           '<path id="svg_1" fill="{backg}" d="m0,{h} l{rectw},0 q{r},0 {r},-{r} l0,{r} l-{w},0 l0,-{r} z"/>'
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
            cx=cx,
            backg=self.background)

    def __init__(self, width, height, background, file_name):
        super().__init__(file_name)
        self.width = width
        self.height = height
        self.background = background
        self.file_name = file_name
