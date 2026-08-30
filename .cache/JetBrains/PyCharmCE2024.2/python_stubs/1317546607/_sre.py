# encoding: utf-8
# module _sre
# from (built-in)
# by generator 1.147
# no doc
# no imports

# Variables with simple values

CODESIZE = 4

copyright = ' SRE 2.2.2 Copyright (c) 1997-2002 by Secret Labs AB '

MAGIC = 20221023
MAXGROUPS = 1073741823
MAXREPEAT = 4294967295

# functions

def ascii_iscased(*args, **kwargs): # real signature unknown
    pass

def ascii_tolower(*args, **kwargs): # real signature unknown
    pass

def compile(*args, **kwargs): # real signature unknown
    pass

def getcodesize(*args, **kwargs): # real signature unknown
    pass

def template(): # real signature unknown; restored from __doc__
    """
    template
        A list containing interleaved literal strings (str or bytes) and group
        indices (int), as returned by re._parser.parse_template():
            [literal1, group1, ..., literalN, groupN]
    """
    pass

def unicode_iscased(*args, **kwargs): # real signature unknown
    pass

def unicode_tolower(*args, **kwargs): # real signature unknown
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
    __dict__ = None # (!) real value is "mappingproxy({'__module__': '_frozen_importlib', '__doc__': 'Meta path import for built-in modules.\\n\\n    All methods are either class or static methods to avoid the need to\\n    instantiate the class.\\n\\n    ', '_ORIGIN': 'built-in', 'find_spec': <classmethod(<function BuiltinImporter.find_spec at 0x7ad8fd55ef20>)>, 'create_module': <staticmethod(<function BuiltinImporter.create_module at 0x7ad8fd55efc0>)>, 'exec_module': <staticmethod(<function BuiltinImporter.exec_module at 0x7ad8fd55f060>)>, 'get_code': <classmethod(<function BuiltinImporter.get_code at 0x7ad8fd55f1a0>)>, 'get_source': <classmethod(<function BuiltinImporter.get_source at 0x7ad8fd55f2e0>)>, 'is_package': <classmethod(<function BuiltinImporter.is_package at 0x7ad8fd55f420>)>, 'load_module': <classmethod(<function _load_module_shim at 0x7ad8fd55e2a0>)>, '__dict__': <attribute '__dict__' of 'BuiltinImporter' objects>, '__weakref__': <attribute '__weakref__' of 'BuiltinImporter' objects>})"


# variables with complex values

__spec__ = None # (!) real value is "ModuleSpec(name='_sre', loader=<class '_frozen_importlib.BuiltinImporter'>, origin='built-in')"

