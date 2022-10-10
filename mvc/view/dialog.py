'''Dialog showed when a specific point is selected.'''
import tkinter as tk

from tkinter import simpledialog

class PointSelectedDialog(tk.simpledialog.Dialog):
    '''Dialog class showed when a specific point is selected.'''

    def __init__(self, parent, point_id):
        self.my_username = None
        self.my_password = None
        self._point_id = point_id
        self.dialog_return_value = None # Dialog return value.
        super().__init__(parent, 'Edit Point')

    def body(self, master):
        self._selected_point_id_label = tk.Label(master, width=25, text=self._point_id)
        self._selected_point_id_label.pack()
        self.my_username_label = tk.Label(master, width=25, text="Username")
        self.my_username_label.pack()
        self.my_username_box = tk.Entry(master, width=25)
        self.my_username_box.pack()

        self.my_password_label = tk.Label(master, width=25, text="Password")
        self.my_password_label.pack()
        self.my_password_box = tk.Entry(master, width=25)
        self.my_password_box.pack()
        self.my_password_box['show'] = '*'

        return master

    def ok_pressed(self):
        '''Event when gialog ok button pressed.'''
        #print("ok")
        self.my_username = self.my_username_box.get()
        self.my_password = self.my_password_box.get()
        self.dialog_return_value = 'return value from dialog.'
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
