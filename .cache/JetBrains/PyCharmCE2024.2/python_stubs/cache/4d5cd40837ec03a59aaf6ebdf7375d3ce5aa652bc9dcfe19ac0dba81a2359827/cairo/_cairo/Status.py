# encoding: utf-8
# module cairo._cairo calls itself cairo
# from /usr/lib/python3/dist-packages/cairo/_cairo.cpython-312-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import cairo as __cairo


class Status(__cairo._IntEnum):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    CLIP_NOT_REPRESENTABLE = 22
    DEVICE_ERROR = 35
    DEVICE_FINISHED = 37
    DEVICE_TYPE_MISMATCH = 34
    DWRITE_ERROR = 43
    FILE_NOT_FOUND = 18
    FONT_TYPE_MISMATCH = 25
    FREETYPE_ERROR = 40
    INVALID_CLUSTERS = 29
    INVALID_CONTENT = 15
    INVALID_DASH = 19
    INVALID_DSC_COMMENT = 20
    INVALID_FORMAT = 16
    INVALID_INDEX = 21
    INVALID_MATRIX = 5
    INVALID_MESH_CONSTRUCTION = 36
    INVALID_PATH_DATA = 9
    INVALID_POP_GROUP = 3
    INVALID_RESTORE = 2
    INVALID_SIZE = 32
    INVALID_SLANT = 30
    INVALID_STATUS = 6
    INVALID_STRIDE = 24
    INVALID_STRING = 8
    INVALID_VISUAL = 17
    INVALID_WEIGHT = 31
    JBIG2_GLOBAL_MISSING = 38
    LAST_STATUS = 45
    NEGATIVE_COUNT = 28
    NO_CURRENT_POINT = 4
    NO_MEMORY = 1
    NULL_POINTER = 7
    PATTERN_TYPE_MISMATCH = 14
    PNG_ERROR = 39
    READ_ERROR = 10
    SUCCESS = 0
    SURFACE_FINISHED = 12
    SURFACE_TYPE_MISMATCH = 13
    SVG_FONT_ERROR = 44
    TAG_ERROR = 42
    TEMP_FILE_ERROR = 23
    USER_FONT_ERROR = 27
    USER_FONT_IMMUTABLE = 26
    USER_FONT_NOT_IMPLEMENTED = 33
    WIN32_GDI_ERROR = 41
    WRITE_ERROR = 11
    __map = {
        0: 'SUCCESS',
        1: 'NO_MEMORY',
        2: 'INVALID_RESTORE',
        3: 'INVALID_POP_GROUP',
        4: 'NO_CURRENT_POINT',
        5: 'INVALID_MATRIX',
        6: 'INVALID_STATUS',
        7: 'NULL_POINTER',
        8: 'INVALID_STRING',
        9: 'INVALID_PATH_DATA',
        10: 'READ_ERROR',
        11: 'WRITE_ERROR',
        12: 'SURFACE_FINISHED',
        13: 'SURFACE_TYPE_MISMATCH',
        14: 'PATTERN_TYPE_MISMATCH',
        15: 'INVALID_CONTENT',
        16: 'INVALID_FORMAT',
        17: 'INVALID_VISUAL',
        18: 'FILE_NOT_FOUND',
        19: 'INVALID_DASH',
        20: 'INVALID_DSC_COMMENT',
        21: 'INVALID_INDEX',
        22: 'CLIP_NOT_REPRESENTABLE',
        23: 'TEMP_FILE_ERROR',
        24: 'INVALID_STRIDE',
        25: 'FONT_TYPE_MISMATCH',
        26: 'USER_FONT_IMMUTABLE',
        27: 'USER_FONT_ERROR',
        28: 'NEGATIVE_COUNT',
        29: 'INVALID_CLUSTERS',
        30: 'INVALID_SLANT',
        31: 'INVALID_WEIGHT',
        32: 'INVALID_SIZE',
        33: 'USER_FONT_NOT_IMPLEMENTED',
        34: 'DEVICE_TYPE_MISMATCH',
        35: 'DEVICE_ERROR',
        36: 'INVALID_MESH_CONSTRUCTION',
        37: 'DEVICE_FINISHED',
        38: 'JBIG2_GLOBAL_MISSING',
        39: 'PNG_ERROR',
        40: 'FREETYPE_ERROR',
        41: 'WIN32_GDI_ERROR',
        42: 'TAG_ERROR',
        43: 'DWRITE_ERROR',
        44: 'SVG_FONT_ERROR',
        45: 'LAST_STATUS',
    }


