# pylint: disable=R0903, C0103
'''Map model module.'''

from enum import Enum

import mvc.constants as Const

class Map():
    '''Map model class.'''

    def __init__(self):
        self.points = []
        self.path = []
        self._max_point_id = Const.DEFAULT_MIN_POINT_ID
        self._max_path_id = Const.DEFAULT_MIN_PATH_ID

    def generate_new_point_id(self):
        '''Generate new ID for point.'''
        self._max_point_id = self._max_point_id + 1
        return self._max_point_id

    def generate_new_path_id(self):
        '''Generate new ID for path.'''
        self._max_path_id = self._max_path_id + 1
        return self._max_path_id

    def load_map(self):
        '''Load map from json file.'''

    def save_map(self):
        '''Save map from json file.'''

    def add_point(self, point):
        '''Add new point into map.'''

        self.points.append(point)

    def remove_point(self, target_point_id):
        '''Remove point from map.'''
        for i, point in enumerate(self.points):
            if target_point_id == point.point_id:
                del self.points[i]
                break

class PointType(Enum):
    '''Point type enumeration definition.'''
    DELIVERY_POINT = 0
    PARKING_POINT = 1
    PATH_POINT = 2
    NON_FOLLOW_POINT = 3

class PathType(Enum):
    '''Path type enumberation definition.'''
    DIRECT = 0
    TURN_LEFT_90 = 1
    TURN_RIGHT_90 = 2
    TURN_LEFT_180 = 3
    TURN_RIGHT_180 = 4

class Point():
    '''Point data class.'''

    def __init__(self, point_id, x, y, point_type):
        self.point_id = point_id
        self.x = x
        self.y = y
        self.point_type = point_type

class Path():
    '''Path data class.'''

    def __init__(self, path_id, start_point, end_point, path_type):
        self.path_id = path_id
        self.start_point = start_point
        self.end_point = end_point
        self.path_type = path_type
