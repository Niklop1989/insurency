# encoding: utf-8
# module cairo._cairo calls itself cairo
# from /usr/lib/python3/dist-packages/cairo/_cairo.cpython-312-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import cairo as __cairo


class Format(__cairo._IntEnum):
    # no doc
    def stride_for_width(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    A1 = 3
    A8 = 2
    ARGB32 = 0
    INVALID = -1
    RGB16_565 = 4
    RGB24 = 1
    RGB30 = 5
    RGB96F = 6
    RGBA128F = 7
    __map = {
        -1: 'INVALID',
        0: 'ARGB32',
        1: 'RGB24',
        2: 'A8',
        3: 'A1',
        4: 'RGB16_565',
        5: 'RGB30',
        6: 'RGB96F',
        7: 'RGBA128F',
    }


