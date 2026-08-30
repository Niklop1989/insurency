# encoding: utf-8
# module cairo._cairo calls itself cairo
# from /usr/lib/python3/dist-packages/cairo/_cairo.cpython-312-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import cairo as __cairo


class Dither(__cairo._IntEnum):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    BEST = 4
    DEFAULT = 1
    FAST = 2
    GOOD = 3
    NONE = 0
    __map = {
        0: 'NONE',
        1: 'DEFAULT',
        2: 'FAST',
        3: 'GOOD',
        4: 'BEST',
    }


