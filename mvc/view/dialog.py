'''Dialog showed when a specific point is selected.'''
import tkinter as tk

from tkinter import simpledialog

class PointSelectedDialog(tk.simpledialog.Dialog):
    '''Dialog class showed when a specific point is selected.'''

    def __init__(self, parent, point):
        self._point = point
        self.updated_point = None # Dialog return value.
        super().__init__(parent, 'Edit Point')

    def body(self, master):
        point_id_label = tk.Label(master, text='Point ID:')
        point_id_label.grid(row=0, column=0)
        self._point_id_entry = tk.Entry(master)
        self._point_id_entry.insert(0, str(self._point.point_id))
        self._point_id_entry.grid(row=0, column=1)

        point_type_label = tk.Label(master, text="Point Type:")
        point_type_label.grid(row=1, column=0)
        self._point_type_entry = tk.Entry(master)
        self._point_type_entry.insert(0, str(self._point.point_type))
        self._point_type_entry.grid(row=1, column=1)

        return master

    def ok_pressed(self):
        '''Event when gialog ok button pressed.'''
        #print("ok")
        self._point.point_id = self._point_id_entry.get()
        self._point.point_type = self._point_type_entry.get()
        self.updated_point = self._point  # Dialog return value.
        self.destroy()

    def cancel_pressed(self):
        '''Event when gialog cancel button pressed.'''
        #print("cancel")
        self.destroy()

    def buttonbox(self):
        self.ok_button = tk.Button(self, text='OK', width=5, command=self.ok_pressed)
        self.ok_button.pack(side="left")
        cancel_button = tk.Button(self, text='Cancel', width=5, command=self.cancel_pressed)
        cancel_button.pack(side="right")
        self.bind("<Return>", lambda event: self.ok_pressed())
        self.bind("<Escape>", lambda event: self.cancel_pressed())
