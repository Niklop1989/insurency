# encoding: utf-8
# module cairo._cairo calls itself cairo
# from /usr/lib/python3/dist-packages/cairo/_cairo.cpython-312-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import cairo as __cairo


class Content(__cairo._IntEnum):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    ALPHA = 8192
    COLOR = 4096
    COLOR_ALPHA = 12288
    __map = {
        4096: 'COLOR',
        8192: 'ALPHA',
        12288: 'COLOR_ALPHA',
    }


