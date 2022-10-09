# pylint: disable=C0103
'''Controller class.'''

import tkinter as tk

from mvc.model.map import Map, Point, PointType
from mvc.view.panel import EditorPanel
from mvc.view.canvas import MapCanvas

import mvc.constants as Const
from mvc.view.panel import EditorPanel

class MapEditor(tk.Tk):
    '''Controller class.'''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title('Map Editor')
        self.geometry(f'{str(Const.MAIN_WINDOW_WIDTH)}x{str(Const.MAIN_WINDOW_HEIGHT)}')
        self.resizable(width=False, height=False)

        self._map = Map()

        self._panel_variables = {}
        self._panel_variables['current_mouse_mode'] = Const.MouseMode.POINT_ADD

        self._panel = EditorPanel(self, self._panel_variables)

        canvas_callbacks = {}
        canvas_callbacks['canvas_click'] = self.on_canvas_click

        self._canvas = MapCanvas(self, Const.MAIN_WINDOW_WIDTH, Const.MAIN_WINDOW_HEIGHT,
            canvas_callbacks)

        self._panel.grid(row=0, column=0, sticky=(tk.E + tk.W))
        self._canvas.grid(row=1, column=0, sticky=(tk.E + tk.W + tk.N + tk.S))

    def on_canvas_click(self, event):
        '''Canvas mouse click callback function.'''

        if self._panel_variables['current_mouse_mode'] == Const.MouseMode.POINT_ADD.value:
            self._point_add(event.x, event.y)
        elif self._panel_variables['current_mouse_mode'] == Const.MouseMode.PATH_ADD.value:
            print('Mode: path add.')
        elif self._panel_variables['current_mouse_mode'] == Const.MouseMode.SELECT.value:
            print('Mode: select.')
        elif self._panel_variables['current_mouse_mode'] == Const.MouseMode.DELETE.value:
            print('Mode: delete.')
        else:
            print('Mode: default')

    def _point_add(self, x, y):
        '''Add point to canvas.'''

        point = Point(self._map.generate_new_point_id(),
            x, y, PointType.PATH_POINT.value)

        self._map.add_point(point)

        self._canvas.paint(self._map)
