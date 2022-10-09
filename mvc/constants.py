'''Project constant definitions.'''
from enum import Enum

MAIN_WINDOW_WIDTH = 800
MAIN_WINDOW_HEIGHT = 600

DEFAULT_MIN_POINT_ID = 0
DEFAULT_MIN_PATH_ID = 0

DEFAULT_DELIVERY_POINT_COLOR = 'red'
DEFAULT_PARKING_POINT_COLOR = 'blue'
DEFAULT_PATH_POINT_COLOR = 'green'
DEFAULT_NON_FOLLOW_POINT_COLOR = 'yellow'

DEFAULT_POINT_RADIUS = 10

class MouseMode(Enum):
    '''Map editor selected mouse mode.'''
    POINT_ADD = 0
    PATH_ADD = 1
    DELETE = 2
    SELECT = 3
