# encoding: utf-8
# module spwd
# from (built-in)
# by generator 1.147
"""
This module provides access to the Unix shadow password database.
It is available on various Unix versions.

Shadow password database entries are reported as 9-tuples of type struct_spwd,
containing the following items from the password database (see `<shadow.h>'):
sp_namp, sp_pwdp, sp_lstchg, sp_min, sp_max, sp_warn, sp_inact, sp_expire, sp_flag.
The sp_namp and sp_pwdp are strings, the rest are integers.
An exception is raised if the entry asked for cannot be found.
You have to be root to be able to use this module.
"""
# no imports

# functions

def getspall(*args, **kwargs): # real signature unknown
    """
    Return a list of all available shadow password database entries, in arbitrary order.
    
    See `help(spwd)` for more on shadow password database entries.
    """
    pass

def getspnam(*args, **kwargs): # real signature unknown
    """
    Return the shadow password database entry for the given user name.
    
    See `help(spwd)` for more on shadow password database entries.
    """
    pass

# classes

class struct_spwd(tuple):
    """
    spwd.struct_spwd: Results from getsp*() routines.
    
    This object may be accessed either as a 9-tuple of
      (sp_namp,sp_pwdp,sp_lstchg,sp_min,sp_max,sp_warn,sp_inact,sp_expire,sp_flag)
    or via the object attributes as named in the above tuple.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    sp_expire = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """#days since 1970-01-01 when account expires"""

    sp_flag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """reserved"""

    sp_inact = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """#days after pw expires until account is disabled"""

    sp_lstchg = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """date of last change"""

    sp_max = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """max #days between changes"""

    sp_min = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """min #days between changes"""

    sp_nam = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """login name; deprecated"""

    sp_namp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """login name"""

    sp_pwd = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """encrypted password; deprecated"""

    sp_pwdp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """encrypted password"""

    sp_warn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """#days before pw expires to warn user about it"""


    n_fields = 11
    n_sequence_fields = 9
    n_unnamed_fields = 0
    __match_args__ = (
        'sp_namp',
        'sp_pwdp',
        'sp_lstchg',
        'sp_min',
        'sp_max',
        'sp_warn',
        'sp_inact',
        'sp_expire',
        'sp_flag',
    )


class __loader__(object):
    """
    Meta path import for built-in modules.
    
        All methods are either class or static methods to avoid the need to
        instantiate the class.
    """
    def create_module(spec): # reliably restored by inspect
        """ Create a built-in module """
        pass

    def exec_module(module): # reliably restored by inspect
        """ Exec a built-in module """
        pass

    @classmethod
    def find_spec(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def get_code(cls, *args, **kwargs): # real signature unknown
        """ Return None as built-in modules do not have code objects. """
        pass

    @classmethod
    def get_source(cls, *args, **kwargs): # real signature unknown
        """ Return None as built-in modules do not have source code. """
        pass

    @classmethod
    def is_package(cls, *args, **kwargs): # real signature unknown
        """ Return False as built-in modules are never packages. """
        pass

    @classmethod
    def load_module(cls, *args, **kwargs): # real signature unknown
        """
        Load the specified module into sys.modules and return it.
        
            This method is deprecated.  Use loader.exec_module() instead.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object"""


    _ORIGIN = 'built-in'
    __dict__ = None # (!) real value is "mappingproxy({'__module__': '_frozen_importlib', '__doc__': 'Meta path import for built-in modules.\\n\\n    All methods are either class or static methods to avoid the need to\\n    instantiate the class.\\n\\n    ', '_ORIGIN': 'built-in', 'find_spec': <classmethod(<function BuiltinImporter.find_spec at 0x79faa9316f20>)>, 'create_module': <staticmethod(<function BuiltinImporter.create_module at 0x79faa9316fc0>)>, 'exec_module': <staticmethod(<function BuiltinImporter.exec_module at 0x79faa9317060>)>, 'get_code': <classmethod(<function BuiltinImporter.get_code at 0x79faa93171a0>)>, 'get_source': <classmethod(<function BuiltinImporter.get_source at 0x79faa93172e0>)>, 'is_package': <classmethod(<function BuiltinImporter.is_package at 0x79faa9317420>)>, 'load_module': <classmethod(<function _load_module_shim at 0x79faa93162a0>)>, '__dict__': <attribute '__dict__' of 'BuiltinImporter' objects>, '__weakref__': <attribute '__weakref__' of 'BuiltinImporter' objects>})"


# variables with complex values

__spec__ = None # (!) real value is "ModuleSpec(name='spwd', loader=<class '_frozen_importlib.BuiltinImporter'>, origin='built-in')"

