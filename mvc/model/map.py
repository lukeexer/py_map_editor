# pylint: disable=R0903, C0103
'''Map model module.'''

from enum import Enum

from mvc.exception import PointNotFound

import mvc.constants as Const

class Map():
    '''Map model class.'''

    def __init__(self):
        self.points = []
        self.paths = []
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

    def update_point(self, old_point_id, point):
        '''Update point info. by old point ID.'''

        self.remove_point(old_point_id)
        self.add_point(point)

    def get_point(self, point_id):
        '''Get point by point ID.'''

        ret = None

        for point in self.points:
            if point_id == point.point_id:
                ret = point
                break

        if ret is None:
            raise PointNotFound(f'Can not find point with ID: {point_id}')

        return ret

    def add_path(self, start_point_id, end_point_id):
        '''Add new path to map.'''
        start_point = None
        end_point = None

        for point in self.points:
            if start_point_id == point.point_id:
                start_point = point
                break

        for point in self.points:
            if end_point_id == point.point_id:
                end_point = point
                break

        new_path_id = self.generate_new_path_id()
        new_path = Path(new_path_id, start_point, end_point, PathType.DIRECT.value)
        self.paths.append(new_path)

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
