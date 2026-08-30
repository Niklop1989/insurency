# encoding: utf-8
# module grp
# from (built-in)
# by generator 1.147
"""
Access to the Unix group database.

Group entries are reported as 4-tuples containing the following fields
from the group database, in order:

  gr_name   - name of the group
  gr_passwd - group password (encrypted); often empty
  gr_gid    - numeric ID of the group
  gr_mem    - list of members

The gid is an integer, name and password are strings.  (Note that most
users are not explicitly listed as members of the groups they are in
according to the password database.  Check both databases to get
complete membership information.)
"""
# no imports

# functions

def getgrall(*args, **kwargs): # real signature unknown
    """
    Return a list of all available group entries, in arbitrary order.
    
    An entry whose name starts with '+' or '-' represents an instruction
    to use YP/NIS and may not be accessible via getgrnam or getgrgid.
    """
    pass

def getgrgid(*args, **kwargs): # real signature unknown
    """
    Return the group database entry for the given numeric group ID.
    
    If id is not valid, raise KeyError.
    """
    pass

def getgrnam(*args, **kwargs): # real signature unknown
    """
    Return the group database entry for the given group name.
    
    If name is not valid, raise KeyError.
    """
    pass

# classes

class struct_group(tuple):
    """
    grp.struct_group: Results from getgr*() routines.
    
    This object may be accessed either as a tuple of
      (gr_name,gr_passwd,gr_gid,gr_mem)
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

    gr_gid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """group id"""

    gr_mem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """group members"""

    gr_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """group name"""

    gr_passwd = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """password"""


    n_fields = 4
    n_sequence_fields = 4
    n_unnamed_fields = 0
    __match_args__ = (
        'gr_name',
        'gr_passwd',
        'gr_gid',
        'gr_mem',
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

__spec__ = None # (!) real value is "ModuleSpec(name='grp', loader=<class '_frozen_importlib.BuiltinImporter'>, origin='built-in')"

