# encoding: utf-8
# module cairo._cairo calls itself cairo
# from /usr/lib/python3/dist-packages/cairo/_cairo.cpython-312-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import cairo as __cairo


class Antialias(__cairo._IntEnum):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    BEST = 6
    DEFAULT = 0
    FAST = 4
    GOOD = 5
    GRAY = 2
    NONE = 1
    SUBPIXEL = 3
    __map = {
        0: 'DEFAULT',
        1: 'NONE',
        2: 'GRAY',
        3: 'SUBPIXEL',
        4: 'FAST',
        5: 'GOOD',
        6: 'BEST',
    }


