# pylint: disable=C0103
'''Controller class.'''

import tkinter as tk

from mvc.model.map import Map, Point, PointType
from mvc.view.panel import EditorPanel
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

        # Initialize selected start and end point ID for drawing path.
        self._add_path_start_point_id = None
        self._add_path_end_point_id = None

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
            self._add_point(event.x, event.y)
        elif self._panel_variables['current_mouse_mode'] == Const.MouseMode.PATH_ADD.value:
            selected_object = self._canvas.get_selected_tags()
            print(selected_object)
            if selected_object:
                try:
                    target_point_id, _ = selected_object
                    self._add_path(target_point_id)
                except ValueError:
                    # Ignore duplicate selection on the same point twice.
                    self._add_path_start_point_id = None
                    self._add_path_end_point_id = None
        elif self._panel_variables['current_mouse_mode'] == Const.MouseMode.SELECT.value:
            selected_tag_name = self._canvas.get_selected_tags()
            print(f'Selected point tag name: {selected_tag_name}')
        elif self._panel_variables['current_mouse_mode'] == Const.MouseMode.DELETE.value:
            selected_object = self._canvas.get_selected_tags()
            print(selected_object)
            if selected_object:
                try:
                    target_point_id, _ = selected_object
                    self._delete_point(target_point_id)
                except ValueError:
                    # Ignore duplicate selection on the same point twice.
                    pass
        else:
            print('Mode: default')

    def _delete_point(self, target_point_id):
        '''Delete point from canvas.'''
        self._map.remove_point(int(target_point_id))
        self._canvas.paint(self._map)

    def _add_point(self, x, y):
        '''Add point to canvas.'''
        point = Point(self._map.generate_new_point_id(),
            x, y, PointType.PATH_POINT.value)
        self._map.add_point(point)
        self._canvas.paint(self._map)

    def _add_path(self, target_point_id):
        '''Add path to canvas.'''
        if self._add_path_start_point_id is None:
            self._add_path_start_point_id = target_point_id
        else:
            self._add_path_end_point_id = target_point_id

            if not self._add_path_start_point_id == self._add_path_end_point_id:
                self._map.add_path(int(self._add_path_start_point_id),
                    int(self._add_path_end_point_id))

                self._canvas.paint(self._map)

            self._add_path_start_point_id = None
            self._add_path_end_point_id = None
