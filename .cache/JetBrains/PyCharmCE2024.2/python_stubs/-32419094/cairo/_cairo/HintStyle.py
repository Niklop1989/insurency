# encoding: utf-8
# module cairo._cairo calls itself cairo
# from /usr/lib/python3/dist-packages/cairo/_cairo.cpython-312-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import cairo as __cairo


class HintStyle(__cairo._IntEnum):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    DEFAULT = 0
    FULL = 4
    MEDIUM = 3
    NONE = 1
    SLIGHT = 2
    __map = {
        0: 'DEFAULT',
        1: 'NONE',
        2: 'SLIGHT',
        3: 'MEDIUM',
        4: 'FULL',
    }


