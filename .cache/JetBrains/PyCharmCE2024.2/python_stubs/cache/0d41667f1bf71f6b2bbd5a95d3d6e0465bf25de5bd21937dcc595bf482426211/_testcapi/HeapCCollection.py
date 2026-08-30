# encoding: utf-8
# module _testcapi
# from /usr/lib/python3.12/lib-dynload/_testcapi.cpython-312-x86_64-linux-gnu.so
# by generator 1.147
# no doc
# no imports

from .object import object

class HeapCCollection(object):
    """ Tuple-like heap type that uses PyObject_GetItemData for items. """
    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


