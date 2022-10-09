'''View classes.'''

import tkinter as tk

import mvc.constants as Const

class MapCanvas(tk.Frame):
    '''Map canvas view class.'''

    def __init__(self, parent, width, height, callbacks, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self._canvas = tk.Canvas(self, width=width, height=height, bg='black')
        self._canvas.bind("<Button-1>", callbacks['canvas_click'])
        self._canvas.pack()

    def get_selected_tags(self):
        '''Get the current selected tag name.'''
        return self._canvas.gettags("current")

    def paint(self, map_data):
        '''Update canvas content.'''

        self._canvas.delete("all")

        for point in map_data.points:
            x_1, y_1 = (point.x - Const.DEFAULT_POINT_RADIUS), \
                (point.y - Const.DEFAULT_POINT_RADIUS)
            x_2, y_2 = (point.x + Const.DEFAULT_POINT_RADIUS), \
                (point.y + Const.DEFAULT_POINT_RADIUS)

            self._canvas.create_oval(x_1, y_1, x_2, y_2,
                fill=Const.DEFAULT_DELIVERY_POINT_COLOR, tags=point.point_id)
