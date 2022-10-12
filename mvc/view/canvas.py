'''View classes.'''

import tkinter as tk

from PIL import Image, ImageTk

import mvc.constants as Const

class MapCanvas(tk.Frame):
    '''Map canvas view class.'''

    def __init__(self, parent, width, height, callbacks, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self._canvas = tk.Canvas(self, width=width, height=height, bg='black')
        # scrollbar: https://stackoverflow.com/questions/20645532/move-a-tkinter-canvas-with-mouse
        self._xsb = tk.Scrollbar(self, orient="horizontal", command=self._canvas.xview)
        self._ysb = tk.Scrollbar(self, orient="vertical", command=self._canvas.yview)
        self._canvas.configure(yscrollcommand=self._ysb.set, xscrollcommand=self._xsb.set)
        self._canvas.configure(scrollregion=(0,0,1000,1000))
        self._canvas.bind("<Button-1>", callbacks['canvas_click'], add='+')
        self._canvas.bind("<Button-1>", self._scroll_start, add='+')
        self._canvas.bind("<B1-Motion>", self._scroll_move)
        # Mouse wheel: https://www.daniweb.com/programming/software-development/code/217059/using-the-mouse-wheel-with-tkinter-python
        self._canvas.bind("<MouseWheel>", self._on_mousewheel) # For Windows OS
        self._canvas.bind("<Button-4>", self._on_mousewheel) # For Linux OS
        self._canvas.bind("<Button-5>", self._on_mousewheel) # For Linux OS
        self._canvas.pack()

        self._img = ImageTk.PhotoImage(Image.open("test.png"))

    def _scroll_start(self, event):
        '''Mouse click and drag event for moving the canvas.'''
        self._canvas.scan_mark(event.x, event.y)

    def _scroll_move(self, event):
        '''Mouse click and drag event for moving the canvas.'''
        self._canvas.scan_dragto(event.x, event.y, gain=1)

    def _on_mousewheel(self, event):
        print('event.')

    def get_selected_tags(self):
        '''Get the current selected tag name.'''
        return self._canvas.gettags("current")

    def paint(self, map_data):
        '''Update canvas content.'''

        self._canvas.delete("all")

        self._canvas.create_image(0, 0, image=self._img)

        for path in map_data.paths:
            x_1 = path.start_point.x
            y_1 = path.start_point.y
            x_2 = path.end_point.x
            y_2 = path.end_point.y

            self._canvas.create_line(x_1, y_1, x_2, y_2, fill=Const.DEFAULT_PATH_COLOR,
                width=Const.DEFAULT_PATH_WIDTH)

        for point in map_data.points:
            x_1, y_1 = (point.x - Const.DEFAULT_POINT_RADIUS), \
                (point.y - Const.DEFAULT_POINT_RADIUS)
            x_2, y_2 = (point.x + Const.DEFAULT_POINT_RADIUS), \
                (point.y + Const.DEFAULT_POINT_RADIUS)

            self._canvas.create_oval(x_1, y_1, x_2, y_2,
                fill=Const.DEFAULT_DELIVERY_POINT_COLOR, tags=point.point_id)
