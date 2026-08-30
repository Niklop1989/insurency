# encoding: utf-8
# module cairo._cairo calls itself cairo
# from /usr/lib/python3/dist-packages/cairo/_cairo.cpython-312-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import cairo as __cairo


class SurfaceObserverMode(__cairo._IntEnum):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    NORMAL = 0
    RECORD_OPERATIONS = 1
    __map = {
        0: 'NORMAL',
        1: 'RECORD_OPERATIONS',
    }


