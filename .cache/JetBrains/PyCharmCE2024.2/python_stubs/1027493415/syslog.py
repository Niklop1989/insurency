# encoding: utf-8
# module syslog
# from (built-in)
# by generator 1.147
# no doc
# no imports

# Variables with simple values

LOG_ALERT = 1
LOG_AUTH = 32
LOG_AUTHPRIV = 80
LOG_CONS = 2
LOG_CRIT = 2
LOG_CRON = 72
LOG_DAEMON = 24
LOG_DEBUG = 7
LOG_EMERG = 0
LOG_ERR = 3
LOG_INFO = 6
LOG_KERN = 0
LOG_LOCAL0 = 128
LOG_LOCAL1 = 136
LOG_LOCAL2 = 144
LOG_LOCAL3 = 152
LOG_LOCAL4 = 160
LOG_LOCAL5 = 168
LOG_LOCAL6 = 176
LOG_LOCAL7 = 184
LOG_LPR = 48
LOG_MAIL = 16
LOG_NDELAY = 8
LOG_NEWS = 56
LOG_NOTICE = 5
LOG_NOWAIT = 16
LOG_ODELAY = 4
LOG_PERROR = 32
LOG_PID = 1
LOG_SYSLOG = 40
LOG_USER = 8
LOG_UUCP = 64
LOG_WARNING = 4

# functions

def closelog(): # real signature unknown; restored from __doc__
    """ Reset the syslog module values and call the system library closelog(). """
    pass

def LOG_MASK(*args, **kwargs): # real signature unknown
    """ Calculates the mask for the individual priority pri. """
    pass

def LOG_UPTO(*args, **kwargs): # real signature unknown
    """ Calculates the mask for all priorities up to and including pri. """
    pass

def openlog(*args, **kwargs): # real signature unknown
    """ Set logging options of subsequent syslog() calls. """
    pass

def setlogmask(*args, **kwargs): # real signature unknown
    """ Set the priority mask to maskpri and return the previous mask value. """
    pass

def syslog(priority=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    syslog([priority=LOG_INFO,] message)
    Send the string message to the system logger.
    """
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

__spec__ = None # (!) real value is "ModuleSpec(name='syslog', loader=<class '_frozen_importlib.BuiltinImporter'>, origin='built-in')"

