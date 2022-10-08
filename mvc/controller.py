'''Controller class.'''

import tkinter as tk

from mvc.model.map import Map, Point, PointType
from mvc.view.canvas import MapCanvas

import mvc.constants as Const

class MapEditor(tk.Tk):
    '''Controller class.'''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title('Map Editor')
        self.geometry(f'{str(Const.MAIN_WINDOW_WIDTH)}x{str(Const.MAIN_WINDOW_HEIGHT)}')
        self.resizable(width=False, height=False)

        self._map = Map()

        callbacks = {}
        callbacks['canvas_click'] = self.on_canvas_click

        self._canvas = MapCanvas(self, Const.MAIN_WINDOW_WIDTH, Const.MAIN_WINDOW_HEIGHT, callbacks)
        self._canvas.pack()

    def on_canvas_click(self, event):
        '''Canvas mouse click callback function.'''

        point = Point(self._map.generate_new_point_id(),
            event.x, event.y, PointType.PATH_POINT.value)

        self._map.add_point(point)

        self._canvas.paint(self._map)

# class Controller(tk.Tk):
#     '''Controller class.'''

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.title('Hello Tkinter')
#         self.geometry('800x600')
#         self.resizable(width=False, height=False)

#         self.name = tk.StringVar()
#         self.hello_string = tk.StringVar()
#         self.hello_string.set('Hello World')

#         variables = {}
#         variables['name'] = self.name
#         variables['hello_string'] = self.hello_string

#         callbacks = {}
#         callbacks['on_change'] = self.on_change

#         HelloFrame(self, variables, callbacks).grid(sticky=(tk.E + tk.W + tk.N + tk.S))
#         self.columnconfigure(0, weight=1)

#     def on_change(self):
#         '''On change calback function.'''

#         if self.name.get().strip():
#             self.hello_string.set('Hello ' + self.name.get())
#         else:
#             self.hello_string.set('Hello World')
