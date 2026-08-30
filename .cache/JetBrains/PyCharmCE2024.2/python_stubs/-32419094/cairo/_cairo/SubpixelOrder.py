# encoding: utf-8
# module cairo._cairo calls itself cairo
# from /usr/lib/python3/dist-packages/cairo/_cairo.cpython-312-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import cairo as __cairo


class SubpixelOrder(__cairo._IntEnum):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    BGR = 2
    DEFAULT = 0
    RGB = 1
    VBGR = 4
    VRGB = 3
    __map = {
        0: 'DEFAULT',
        1: 'RGB',
        2: 'BGR',
        3: 'VRGB',
        4: 'VBGR',
    }


