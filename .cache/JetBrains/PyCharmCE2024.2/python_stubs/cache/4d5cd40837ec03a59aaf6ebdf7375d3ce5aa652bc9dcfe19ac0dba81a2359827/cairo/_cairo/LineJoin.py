# encoding: utf-8
# module cairo._cairo calls itself cairo
# from /usr/lib/python3/dist-packages/cairo/_cairo.cpython-312-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import cairo as __cairo


class LineJoin(__cairo._IntEnum):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    BEVEL = 2
    MITER = 0
    ROUND = 1
    __map = {
        0: 'MITER',
        1: 'ROUND',
        2: 'BEVEL',
    }


