# encoding: utf-8
# module _testcapi
# from /usr/lib/python3.12/lib-dynload/_testcapi.cpython-312-x86_64-linux-gnu.so
# by generator 1.147
# no doc
# no imports

from .object import object

class HeapCTypeWithBuffer(object):
    """
    Heap type with buffer support.
    
    The buffer is set to [b'1', b'2', b'3', b'4']
    """
    def __buffer__(self, *args, **kwargs): # real signature unknown
        """ Return a buffer object that exposes the underlying memory of the object. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __release_buffer__(self, *args, **kwargs): # real signature unknown
        """ Release the buffer object that exposes the underlying memory of the object. """
        pass


