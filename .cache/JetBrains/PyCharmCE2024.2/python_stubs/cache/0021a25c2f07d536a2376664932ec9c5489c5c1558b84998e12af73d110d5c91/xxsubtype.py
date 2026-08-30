# encoding: utf-8
# module xxsubtype
# from /usr/lib/python3.12/lib-dynload/xxsubtype.cpython-312-x86_64-linux-gnu.so
# by generator 1.147
"""
xxsubtype is an example module showing how to subtype builtin types from C.
test_descr.py in the standard test suite requires it in order to complete.
If you don't care about the examples, and don't intend to run the Python
test suite, you can recompile Python without Modules/xxsubtype.c.
"""
# no imports

# functions

def bench(*args, **kwargs): # real signature unknown
    pass

# classes

class spamdict(dict):
    # no doc
    def getstate(self): # real signature unknown; restored from __doc__
        """ getstate() -> state """
        pass

    def setstate(self, state): # real signature unknown; restored from __doc__
        """ setstate(state) """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    state = property(lambda self: 0)
    """an int variable for demonstration purposes

    :type: int
    """



class spamlist(list):
    # no doc
    @classmethod
    def classmeth(cls, *args, **kw): # real signature unknown; restored from __doc__
        """ classmeth(*args, **kw) """
        pass

    def getstate(self): # real signature unknown; restored from __doc__
        """ getstate() -> state """
        pass

    def setstate(self, state): # real signature unknown; restored from __doc__
        """ setstate(state) """
        pass

    def staticmeth(self, *args, **kw): # real signature unknown; restored from __doc__
        """ staticmeth(*args, **kw) """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    state = property(lambda self: 0)
    """an int variable for demonstration purposes

    :type: int
    """



# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7ad8fca18140>'

__spec__ = None # (!) real value is "ModuleSpec(name='xxsubtype', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7ad8fca18140>, origin='/usr/lib/python3.12/lib-dynload/xxsubtype.cpython-312-x86_64-linux-gnu.so')"

