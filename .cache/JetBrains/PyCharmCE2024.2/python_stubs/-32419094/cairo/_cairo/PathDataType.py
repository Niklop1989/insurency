# encoding: utf-8
# module cairo._cairo calls itself cairo
# from /usr/lib/python3/dist-packages/cairo/_cairo.cpython-312-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import cairo as __cairo


class PathDataType(__cairo._IntEnum):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    CLOSE_PATH = 3
    CURVE_TO = 2
    LINE_TO = 1
    MOVE_TO = 0
    __map = {
        0: 'MOVE_TO',
        1: 'LINE_TO',
        2: 'CURVE_TO',
        3: 'CLOSE_PATH',
    }


