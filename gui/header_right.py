from .render import Render


class Header_right(Render):

    # test @ https://editor.method.ac/
    #   <svg height="{100}" width="{600}">
    #       <path id="svg_1" fill="#111111" d="m0,50 q0,-50 50,-50 l-50,0 l0,50 z"/>
    #       <path id="svg_1" fill="#111111" d="m0,50 q0,50 50,50 l-50,0l0,-50 z"/>
    #       <path id="svg_1" fill="#111111" d="m0,0 l550,0 q50,0 50,50 l0,-50 l-600,0 l0,50 z"/>
    #       <path id="svg_1" fill="#111111" d="m0,100 l550,0 q50,0 50,-50 l0,50 l-600,0 l0,-50 z"/>
    #       <rect fill="#111111" x="100" y="0" width="200" height="100" id="svg_1"/>
    #   </svg>

    svg = ('<svg height="{h}" width="{w}">'
           '<path id="svg_1" fill="{backg}" d="m0,{r} q0,-{r} {r},-{r} l-{r},0 l0,{r} z"/>'
           '<path id="svg_1" fill="{backg}" d="m0,{r} q0,{r} {r},{r} l-{r},0 l0,-{r} z"/>'
           '<path id="svg_1" fill="{backg}" d="m0,0 l{rectw},0 q{r},0 {r},{r} l0,-{r} l-{w},0 l0,{r} z"/>'
           '<path id="svg_1" fill="{backg}" d="m0,{h} l{rectw},0 q{r},0 {r},-{r} l0,{r} l-{w},0 l0,-{w} z"/>'
           '<rect id="svg_1" fill="{backg}" x="{rectx}" y="0" width="{twidth}" height="{h}"/>'
           '</svg>')

    def interpolate_svg(self):
        r = self.height / 2
        rectW = self.width - r
        cx = rectW + r
        textwidth = self.width/5
        rectX = self.width - (textwidth + self.height)
        return self.svg.format(
            h=self.height,
            w=self.width,
            rectw=rectW,
            r=r,
            cx=cx,
            twidth= textwidth,
            rectx = rectX,
            backg=self.background)

    def __init__(self, width, height, background, file_name):
        super().__init__(file_name)
        self.width = width
        self.height = height
        self.background = background
        self.file_name = file_name
