'''View classes.'''

import tkinter as tk

from tkinter import ttk

import mvc.constants as Const

class EditorPanel(tk.Frame):
    '''Map editor mouse mode selection panel.'''

    def __init__(self, parent, variables, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self._variables = variables

        save_btn = ttk.Button(self, text='Save')
        load_btn = ttk.Button(self, text='Load')
        save_btn = ttk.Button(self, text='Redo')
        load_btn = ttk.Button(self, text='Undo')
        add_point_btn = ttk.Button(self, text='Add Point',
            command=lambda mode=Const.MouseMode.POINT_ADD.value: self._on_mode_change(mode))
        add_path_btn = ttk.Button(self, text='Add Path',
            command=lambda mode=Const.MouseMode.PATH_ADD.value: self._on_mode_change(mode))
        delete_btn = ttk.Button(self, text='Delete',
            command=lambda mode=Const.MouseMode.DELETE.value: self._on_mode_change(mode))
        select_btn = ttk.Button(self, text='Select',
            command=lambda mode=Const.MouseMode.SELECT.value: self._on_mode_change(mode))

        save_btn.grid(row=0, column=0)
        load_btn.grid(row=0, column=1)
        add_point_btn.grid(row=0, column=2)
        add_path_btn.grid(row=0, column=3)
        delete_btn.grid(row=0, column=4)
        select_btn.grid(row=0, column=5)

    def _on_mode_change(self, mode):
        '''Change current mouse mode.'''
        self._variables['current_mouse_mode'] = mode
