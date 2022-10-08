# pylint: disable=W0703
'''Tkinter program entry point.'''

import traceback

from mvc.controller import MapEditor

if __name__ == '__main__':

    try:
        app = MapEditor()
        app.mainloop()
    except Exception as e:
        print(e)
        print(traceback.format_exc())
