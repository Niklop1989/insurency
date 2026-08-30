# encoding: utf-8
# module cairo._cairo calls itself cairo
# from /usr/lib/python3/dist-packages/cairo/_cairo.cpython-312-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import cairo as __cairo


class PDFMetadata(__cairo._IntEnum):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    AUTHOR = 1
    CREATE_DATE = 5
    CREATOR = 4
    KEYWORDS = 3
    MOD_DATE = 6
    SUBJECT = 2
    TITLE = 0
    __map = {
        0: 'TITLE',
        1: 'AUTHOR',
        2: 'SUBJECT',
        3: 'KEYWORDS',
        4: 'CREATOR',
        5: 'CREATE_DATE',
        6: 'MOD_DATE',
    }


