# encoding: utf-8
# module _xxsubinterpreters
# from /usr/lib/python3.12/lib-dynload/_xxsubinterpreters.cpython-312-x86_64-linux-gnu.so
# by generator 1.147
"""
This module provides primitive operations to manage Python interpreters.
The 'interpreters' module provides a more convenient interface.
"""
# no imports

# functions

def create(): # real signature unknown; restored from __doc__
    """
    create() -> ID
    
    Create a new interpreter and return a unique generated ID.
    """
    pass

def destroy(id): # real signature unknown; restored from __doc__
    """
    destroy(id)
    
    Destroy the identified interpreter.
    
    Attempting to destroy the current interpreter results in a RuntimeError.
    So does an unrecognized ID.
    """
    pass

def get_current(): # real signature unknown; restored from __doc__
    """
    get_current() -> ID
    
    Return the ID of current interpreter.
    """
    pass

def get_main(): # real signature unknown; restored from __doc__
    """
    get_main() -> ID
    
    Return the ID of main interpreter.
    """
    pass

def is_running(id): # real signature unknown; restored from __doc__
    """
    is_running(id) -> bool
    
    Return whether or not the identified interpreter is running.
    """
    return False

def is_shareable(obj): # real signature unknown; restored from __doc__
    """
    is_shareable(obj) -> bool
    
    Return True if the object's data may be shared between interpreters and
    False otherwise.
    """
    return False

def list_all(): # real signature unknown; restored from __doc__
    """
    list_all() -> [ID]
    
    Return a list containing the ID of every existing interpreter.
    """
    pass

def run_string(id, script, shared): # real signature unknown; restored from __doc__
    """
    run_string(id, script, shared)
    
    Execute the provided string in the identified interpreter.
    
    See PyRun_SimpleStrings.
    """
    pass

# classes

class InterpreterID(object):
    """ A interpreter ID identifies a interpreter and may be used as an int. """
    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __index__(self, *args, **kwargs): # real signature unknown
        """ Return self converted to an integer, if self is suitable for use as an index into a list. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __int__(self, *args, **kwargs): # real signature unknown
        """ int(self) """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass


class RunFailedError(RuntimeError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object"""



# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7ad8fca6df10>'

__spec__ = None # (!) real value is "ModuleSpec(name='_xxsubinterpreters', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7ad8fca6df10>, origin='/usr/lib/python3.12/lib-dynload/_xxsubinterpreters.cpython-312-x86_64-linux-gnu.so')"

