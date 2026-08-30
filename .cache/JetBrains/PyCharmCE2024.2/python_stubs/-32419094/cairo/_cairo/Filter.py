# encoding: utf-8
# module cairo._cairo calls itself cairo
# from /usr/lib/python3/dist-packages/cairo/_cairo.cpython-312-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import cairo as __cairo


class Filter(__cairo._IntEnum):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    BEST = 2
    BILINEAR = 4
    FAST = 0
    GAUSSIAN = 5
    GOOD = 1
    NEAREST = 3
    __map = {
        0: 'FAST',
        1: 'GOOD',
        2: 'BEST',
        3: 'NEAREST',
        4: 'BILINEAR',
        5: 'GAUSSIAN',
    }


