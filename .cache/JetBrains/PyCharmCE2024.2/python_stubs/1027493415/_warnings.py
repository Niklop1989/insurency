# encoding: utf-8
# module _warnings
# from (built-in)
# by generator 1.147
"""
_warnings provides basic warning filtering support.
It is a helper module to speed up interpreter start-up.
"""
# no imports

# Variables with simple values

_defaultaction = 'default'

# functions

def warn(): # real signature unknown; restored from __doc__
    """
    Issue a warning, or maybe ignore it or raise an exception.
    
      message
        Text of the warning message.
      category
        The Warning category subclass. Defaults to UserWarning.
      stacklevel
        How far up the call stack to make this warning appear. A value of 2 for
        example attributes the warning to the caller of the code calling warn().
      source
        If supplied, the destroyed object which emitted a ResourceWarning
      skip_file_prefixes
        An optional tuple of module filename prefixes indicating frames to skip
        during stacklevel computations for stack frame attribution.
    """
    pass

def warn_explicit(*args, **kwargs): # real signature unknown
    """ Issue a warning, or maybe ignore it or raise an exception. """
    pass

def _filters_mutated(*args, **kwargs): # real signature unknown
    pass

# classes

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

filters = [
    (
        'default',
        None,
        DeprecationWarning,
        '__main__',
        0,
    ),
    (
        'ignore',
        None,
        '<value is a self-reference, replaced by this string>',
        None,
        0,
    ),
    (
        'ignore',
        None,
        PendingDeprecationWarning,
        None,
        0,
    ),
    (
        'ignore',
        None,
        ImportWarning,
        None,
        0,
    ),
    (
        'ignore',
        None,
        ResourceWarning,
        None,
        0,
    ),
]

_onceregistry = {}

__spec__ = None # (!) real value is "ModuleSpec(name='_warnings', loader=<class '_frozen_importlib.BuiltinImporter'>, origin='built-in')"

