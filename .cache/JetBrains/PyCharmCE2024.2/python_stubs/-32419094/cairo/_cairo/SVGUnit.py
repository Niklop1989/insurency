# encoding: utf-8
# module cairo._cairo calls itself cairo
# from /usr/lib/python3/dist-packages/cairo/_cairo.cpython-312-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import cairo as __cairo


class SVGUnit(__cairo._IntEnum):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    CM = 5
    EM = 1
    EX = 2
    IN = 4
    MM = 6
    PC = 8
    PERCENT = 9
    PT = 7
    PX = 3
    USER = 0
    __map = {
        0: 'USER',
        1: 'EM',
        2: 'EX',
        3: 'PX',
        4: 'IN',
        5: 'CM',
        6: 'MM',
        7: 'PT',
        8: 'PC',
        9: 'PERCENT',
    }


