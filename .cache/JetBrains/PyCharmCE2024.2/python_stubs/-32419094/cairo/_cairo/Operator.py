# encoding: utf-8
# module cairo._cairo calls itself cairo
# from /usr/lib/python3/dist-packages/cairo/_cairo.cpython-312-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import cairo as __cairo


class Operator(__cairo._IntEnum):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    ADD = 12
    ATOP = 5
    CLEAR = 0
    COLOR_BURN = 20
    COLOR_DODGE = 19
    DARKEN = 17
    DEST = 6
    DEST_ATOP = 10
    DEST_IN = 8
    DEST_OUT = 9
    DEST_OVER = 7
    DIFFERENCE = 23
    EXCLUSION = 24
    HARD_LIGHT = 21
    HSL_COLOR = 27
    HSL_HUE = 25
    HSL_LUMINOSITY = 28
    HSL_SATURATION = 26
    IN = 3
    LIGHTEN = 18
    MULTIPLY = 14
    OUT = 4
    OVER = 2
    OVERLAY = 16
    SATURATE = 13
    SCREEN = 15
    SOFT_LIGHT = 22
    SOURCE = 1
    XOR = 11
    __map = {
        0: 'CLEAR',
        1: 'SOURCE',
        2: 'OVER',
        3: 'IN',
        4: 'OUT',
        5: 'ATOP',
        6: 'DEST',
        7: 'DEST_OVER',
        8: 'DEST_IN',
        9: 'DEST_OUT',
        10: 'DEST_ATOP',
        11: 'XOR',
        12: 'ADD',
        13: 'SATURATE',
        14: 'MULTIPLY',
        15: 'SCREEN',
        16: 'OVERLAY',
        17: 'DARKEN',
        18: 'LIGHTEN',
        19: 'COLOR_DODGE',
        20: 'COLOR_BURN',
        21: 'HARD_LIGHT',
        22: 'SOFT_LIGHT',
        23: 'DIFFERENCE',
        24: 'EXCLUSION',
        25: 'HSL_HUE',
        26: 'HSL_SATURATION',
        27: 'HSL_COLOR',
        28: 'HSL_LUMINOSITY',
    }


