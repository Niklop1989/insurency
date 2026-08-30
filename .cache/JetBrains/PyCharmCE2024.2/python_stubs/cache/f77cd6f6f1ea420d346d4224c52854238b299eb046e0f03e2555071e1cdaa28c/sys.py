# encoding: utf-8
# module sys
# from (built-in)
# by generator 1.147
"""
This module provides access to some objects used or maintained by the
interpreter and to functions that interact strongly with the interpreter.

Dynamic objects:

argv -- command line arguments; argv[0] is the script pathname if known
path -- module search path; path[0] is the script directory, else ''
modules -- dictionary of loaded modules

displayhook -- called to show results in an interactive session
excepthook -- called to handle any uncaught exception other than SystemExit
  To customize printing in an interactive session or to install a custom
  top-level exception handler, assign other functions to replace these.

stdin -- standard input file object; used by input()
stdout -- standard output file object; used by print()
stderr -- standard error object; used for error messages
  By assigning other file objects (or objects that behave like files)
  to these, it is possible to redirect all of the interpreter's I/O.

last_exc - the last uncaught exception
  Only available in an interactive session after a
  traceback has been printed.
last_type -- type of last uncaught exception
last_value -- value of last uncaught exception
last_traceback -- traceback of last uncaught exception
  These three are the (deprecated) legacy representation of last_exc.

Static objects:

builtin_module_names -- tuple of module names built into this interpreter
copyright -- copyright notice pertaining to this interpreter
exec_prefix -- prefix used to find the machine-specific Python library
executable -- absolute path of the executable binary of the Python interpreter
float_info -- a named tuple with information about the float implementation.
float_repr_style -- string indicating the style of repr() output for floats
hash_info -- a named tuple with information about the hash algorithm.
hexversion -- version information encoded as a single integer
implementation -- Python implementation information.
int_info -- a named tuple with information about the int implementation.
maxsize -- the largest supported length of containers.
maxunicode -- the value of the largest Unicode code point
platform -- platform identifier
prefix -- prefix used to find the Python library
thread_info -- a named tuple with information about the thread implementation.
version -- the version of this interpreter as a string
version_info -- version information as a named tuple
__stdin__ -- the original stdin; don't touch!
__stdout__ -- the original stdout; don't touch!
__stderr__ -- the original stderr; don't touch!
__displayhook__ -- the original displayhook; don't touch!
__excepthook__ -- the original excepthook; don't touch!

Functions:

displayhook() -- print an object to the screen, and save it in builtins._
excepthook() -- print an exception and its traceback to sys.stderr
exception() -- return the current thread's active exception
exc_info() -- return information about the current thread's active exception
exit() -- exit the interpreter by raising SystemExit
getdlopenflags() -- returns flags to be used for dlopen() calls
getprofile() -- get the global profiling function
getrefcount() -- return the reference count for an object (plus one :-)
getrecursionlimit() -- return the max recursion depth for the interpreter
getsizeof() -- return the size of an object in bytes
gettrace() -- get the global debug tracing function
setdlopenflags() -- set the flags to be used for dlopen() calls
setprofile() -- set the global profiling function
setrecursionlimit() -- set the max recursion depth for the interpreter
settrace() -- set the global debug tracing function
"""

# imports
import sys.monitoring as monitoring # <module 'sys.monitoring'>
from _io import __stderr__, __stdin__, __stdout__, stderr, stdin, stdout


# Variables with simple values

abiflags = ''

api_version = 1013

base_exec_prefix = '/usr'

base_prefix = '/usr'

byteorder = 'little'

copyright = 'Copyright (c) 2001-2023 Python Software Foundation.\nAll Rights Reserved.\n\nCopyright (c) 2000 BeOpen.com.\nAll Rights Reserved.\n\nCopyright (c) 1995-2001 Corporation for National Research Initiatives.\nAll Rights Reserved.\n\nCopyright (c) 1991-1995 Stichting Mathematisch Centrum, Amsterdam.\nAll Rights Reserved.'

dont_write_bytecode = True

executable = '/home/nikita/PycharmProjects/python_advanced/.venv/bin/python'

exec_prefix = '/home/nikita/PycharmProjects/python_advanced/.venv'

float_repr_style = 'short'

hexversion = 51119088

maxsize = 9223372036854775807
maxunicode = 1114111

platform = 'linux'
platlibdir = 'lib'

prefix = '/home/nikita/PycharmProjects/python_advanced/.venv'

pycache_prefix = None

version = '3.12.3 (main, Nov  6 2024, 18:32:19) [GCC 13.2.0]'

_base_executable = '/usr/bin/python3.12'

_framework = ''

_home = '/usr/bin'

_stdlib_dir = '/usr/lib/python3.12'

# functions

def activate_stack_trampoline(*args, **kwargs): # real signature unknown
    """ Activate stack profiler trampoline *backend*. """
    pass

def addaudithook(*args, **kwargs): # real signature unknown
    """ Adds a new audit hook callback. """
    pass

def audit(event, *args): # real signature unknown; restored from __doc__
    """
    audit(event, *args)
    
    Passes the event to any audit hooks that are attached.
    """
    pass

def breakpointhook(*args, **kws): # real signature unknown; restored from __doc__
    """
    breakpointhook(*args, **kws)
    
    This hook function is called by built-in breakpoint().
    """
    pass

def call_tracing(*args, **kwargs): # real signature unknown
    """
    Call func(*args), while tracing is enabled.
    
    The tracing state is saved, and restored afterwards.  This is intended
    to be called from a debugger from a checkpoint, to recursively debug
    some other code.
    """
    pass

def deactivate_stack_trampoline(*args, **kwargs): # real signature unknown
    """
    Deactivate the current stack profiler trampoline backend.
    
    If no stack profiler is activated, this function has no effect.
    """
    pass

def displayhook(*args, **kwargs): # real signature unknown
    """ Print an object to sys.stdout and also save it in builtins._ """
    pass

def excepthook(*args, **kwargs): # real signature unknown
    """ Handle an exception by displaying it with a traceback on sys.stderr. """
    pass

def exception(*args, **kwargs): # real signature unknown
    """
    Return the current exception.
    
    Return the most recent exception caught by an except clause
    in the current stack frame or in an older stack frame, or None
    if no such exception exists.
    """
    pass

def exc_info(*args, **kwargs): # real signature unknown
    """
    Return current exception information: (type, value, traceback).
    
    Return information about the most recent exception caught by an except
    clause in the current stack frame or in an older stack frame.
    """
    pass

def exit(*args, **kwargs): # real signature unknown
    """
    Exit the interpreter by raising SystemExit(status).
    
    If the status is omitted or None, it defaults to zero (i.e., success).
    If the status is an integer, it will be used as the system exit status.
    If it is another kind of object, it will be printed and the system
    exit status will be one (i.e., failure).
    """
    pass

def getallocatedblocks(*args, **kwargs): # real signature unknown
    """ Return the number of memory blocks currently allocated. """
    pass

def getdefaultencoding(*args, **kwargs): # real signature unknown
    """ Return the current default encoding used by the Unicode implementation. """
    pass

def getdlopenflags(*args, **kwargs): # real signature unknown
    """
    Return the current value of the flags that are used for dlopen calls.
    
    The flag constants are defined in the os module.
    """
    pass

def getfilesystemencodeerrors(*args, **kwargs): # real signature unknown
    """ Return the error mode used Unicode to OS filename conversion. """
    pass

def getfilesystemencoding(*args, **kwargs): # real signature unknown
    """ Return the encoding used to convert Unicode filenames to OS filenames. """
    pass

def getprofile(*args, **kwargs): # real signature unknown
    """
    Return the profiling function set with sys.setprofile.
    
    See the profiler chapter in the library manual.
    """
    pass

def getrecursionlimit(*args, **kwargs): # real signature unknown
    """
    Return the current value of the recursion limit.
    
    The recursion limit is the maximum depth of the Python interpreter
    stack.  This limit prevents infinite recursion from causing an overflow
    of the C stack and crashing Python.
    """
    pass

def getrefcount(): # real signature unknown; restored from __doc__
    """
    Return the reference count of object.
    
    The count returned is generally one higher than you might expect,
    because it includes the (temporary) reference as an argument to
    getrefcount().
    """
    pass

def getsizeof(p_object, default=None): # real signature unknown; restored from __doc__
    """
    getsizeof(object [, default]) -> int
    
    Return the size of object in bytes.
    """
    return 0

def getswitchinterval(*args, **kwargs): # real signature unknown
    """ Return the current thread switch interval; see sys.setswitchinterval(). """
    pass

def gettrace(*args, **kwargs): # real signature unknown
    """
    Return the global debug tracing function set with sys.settrace.
    
    See the debugger chapter in the library manual.
    """
    pass

def getunicodeinternedsize(*args, **kwargs): # real signature unknown
    """ Return the number of elements of the unicode interned dictionary """
    pass

def get_asyncgen_hooks(*args, **kwargs): # real signature unknown
    """
    Return the installed asynchronous generators hooks.
    
    This returns a namedtuple of the form (firstiter, finalizer).
    """
    pass

def get_coroutine_origin_tracking_depth(*args, **kwargs): # real signature unknown
    """ Check status of origin tracking for coroutine objects in this thread. """
    pass

def get_int_max_str_digits(*args, **kwargs): # real signature unknown
    """ Return the maximum string digits limit for non-binary int<->str conversions. """
    pass

def intern(*args, **kwargs): # real signature unknown
    """
    ``Intern'' the given string.
    
    This enters the string in the (global) table of interned strings whose
    purpose is to speed up dictionary lookups. Return the string itself or
    the previously interned string object with the same value.
    """
    pass

def is_finalizing(*args, **kwargs): # real signature unknown
    """ Return True if Python is exiting. """
    pass

def is_stack_trampoline_active(*args, **kwargs): # real signature unknown
    """ Return *True* if a stack profiler trampoline is active. """
    pass

def setdlopenflags(*args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    Set the flags used by the interpreter for dlopen calls.
    
    This is used, for example, when the interpreter loads extension
    modules. Among other things, this will enable a lazy resolving of
    symbols when importing a module, if called as sys.setdlopenflags(0).
    To share symbols across extension modules, call as
    sys.setdlopenflags(os.RTLD_GLOBAL).  Symbolic names for the flag
    modules can be found in the os module (RTLD_xxx constants, e.g.
    os.RTLD_LAZY).
    """
    pass

def setprofile(function): # real signature unknown; restored from __doc__
    """
    setprofile(function)
    
    Set the profiling function.  It will be called on each function call
    and return.  See the profiler chapter in the library manual.
    """
    pass

def setrecursionlimit(*args, **kwargs): # real signature unknown
    """
    Set the maximum depth of the Python interpreter stack to n.
    
    This limit prevents infinite recursion from causing an overflow of the C
    stack and crashing Python.  The highest possible limit is platform-
    dependent.
    """
    pass

def setswitchinterval(*args, **kwargs): # real signature unknown
    """
    Set the ideal thread switching delay inside the Python interpreter.
    
    The actual frequency of switching threads can be lower if the
    interpreter executes long sequences of uninterruptible code
    (this is implementation-specific and workload-dependent).
    
    The parameter must represent the desired switching delay in seconds
    A typical value is 0.005 (5 milliseconds).
    """
    pass

def settrace(function): # real signature unknown; restored from __doc__
    """
    settrace(function)
    
    Set the global debug tracing function.  It will be called on each
    function call.  See the debugger chapter in the library manual.
    """
    pass

def set_asyncgen_hooks(firstiter=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    set_asyncgen_hooks([firstiter] [, finalizer])
    
    Set a finalizer for async generators objects.
    """
    pass

def set_coroutine_origin_tracking_depth(*args, **kwargs): # real signature unknown
    """
    Enable or disable origin tracking for coroutine objects in this thread.
    
    Coroutine objects will track 'depth' frames of traceback information
    about where they came from, available in their cr_origin attribute.
    
    Set a depth of 0 to disable.
    """
    pass

def set_int_max_str_digits(*args, **kwargs): # real signature unknown
    """ Set the maximum string digits limit for non-binary int<->str conversions. """
    pass

def unraisablehook(*args, **kwargs): # real signature unknown
    """
    Handle an unraisable exception.
    
    The unraisable argument has the following attributes:
    
    * exc_type: Exception type.
    * exc_value: Exception value, can be None.
    * exc_traceback: Exception traceback, can be None.
    * err_msg: Error message, can be None.
    * object: Object causing the exception, can be None.
    """
    pass

def _clear_type_cache(*args, **kwargs): # real signature unknown
    """ Clear the internal type lookup cache. """
    pass

def _current_exceptions(*args, **kwargs): # real signature unknown
    """
    Return a dict mapping each thread's identifier to its current raised exception.
    
    This function should be used for specialized purposes only.
    """
    pass

def _current_frames(*args, **kwargs): # real signature unknown
    """
    Return a dict mapping each thread's thread id to its current stack frame.
    
    This function should be used for specialized purposes only.
    """
    pass

def _debugmallocstats(*args, **kwargs): # real signature unknown
    """
    Print summary info to stderr about the state of pymalloc's structures.
    
    In Py_DEBUG mode, also perform some expensive internal consistency
    checks.
    """
    pass

def _getframe(*args, **kwargs): # real signature unknown
    """
    Return a frame object from the call stack.
    
    If optional integer depth is given, return the frame object that many
    calls below the top of the stack.  If that is deeper than the call
    stack, ValueError is raised.  The default for depth is zero, returning
    the frame at the top of the call stack.
    
    This function should be used for internal and specialized purposes
    only.
    """
    pass

def _getframemodulename(*args, **kwargs): # real signature unknown
    """
    Return the name of the module for a calling frame.
    
    The default depth returns the module containing the call to this API.
    A more typical use in a library will pass a depth of 1 to get the user's
    module rather than the library module.
    
    If no frame, module, or name can be found, returns None.
    """
    pass

def _setprofileallthreads(*args, **kwargs): # real signature unknown
    """
    Set the profiling function in all running threads belonging to the current interpreter.
    
    It will be called on each function call and return.  See the profiler chapter
    in the library manual.
    """
    pass

def _settraceallthreads(*args, **kwargs): # real signature unknown
    """
    Set the global debug tracing function in all running threads belonging to the current interpreter.
    
    It will be called on each function call. See the debugger chapter
    in the library manual.
    """
    pass

def __breakpointhook__(*args, **kwargs): # real signature unknown
    """
    breakpointhook(*args, **kws)
    
    This hook function is called by built-in breakpoint().
    """
    pass

def __displayhook__(*args, **kwargs): # real signature unknown
    """ Print an object to sys.stdout and also save it in builtins._ """
    pass

def __excepthook__(*args, **kwargs): # real signature unknown
    """ Handle an exception by displaying it with a traceback on sys.stderr. """
    pass

def __interactivehook__(): # reliably restored by inspect
    # no doc
    pass

def __unraisablehook__(*args, **kwargs): # real signature unknown
    """
    Handle an unraisable exception.
    
    The unraisable argument has the following attributes:
    
    * exc_type: Exception type.
    * exc_value: Exception value, can be None.
    * exc_traceback: Exception traceback, can be None.
    * err_msg: Error message, can be None.
    * object: Object causing the exception, can be None.
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

argv = [] # real value of type <class 'list'> skipped

builtin_module_names = () # real value of type <class 'tuple'> skipped

flags = (
    0,
    0,
    0,
    0,
    1,
    0,
    0,
    0,
    0,
    0,
    0,
    1,
    0,
    False,
    0,
    0,
    False,
    4300,
)

float_info = (
    1.7976931348623157e+308,
    1024,
    308,
    2.2250738585072014e-308,
    -1021,
    -307,
    15,
    53,
    2.220446049250313e-16,
    2,
    1,
)

hash_info = (
    64,
    2305843009213693951,
    314159,
    0,
    1000003,
    'siphash13',
    64,
    128,
    0,
)

implementation = None # (!) real value is "namespace(name='cpython', cache_tag='cpython-312', version=sys.version_info(major=3, minor=12, micro=3, releaselevel='final', serial=0), hexversion=51119088, _multiarch='x86_64-linux-gnu')"

int_info = (
    30,
    4,
    4300,
    640,
)

meta_path = [
    None, # (!) real value is '<_virtualenv._Finder object at 0x79faa8902750>'
    __loader__,
    None, # (!) real value is "<class '_frozen_importlib.FrozenImporter'>"
    None, # (!) real value is "<class '_frozen_importlib_external.PathFinder'>"
    None, # (!) real value is '<six._SixMetaPathImporter object at 0x79faa7f6e150>'
]

modules = {} # real value of type <class 'dict'> skipped

orig_argv = [
    '/home/nikita/PycharmProjects/python_advanced/.venv/bin/python',
    '/snap/pycharm-community/436/plugins/python-ce/helpers/generator3/__main__.py',
    '-d',
    '/home/nikita/.cache/JetBrains/PyCharmCE2024.2/python_stubs/1027493415',
    '-s',
    '/usr/lib/python3.12:/usr/lib/python3.12/lib-dynload:/home/nikita/PycharmProjects/python_advanced/.venv/lib/python3.12/site-packages',
]

path = [
    '/snap/pycharm-community/436/plugins/python-ce/helpers',
    '/snap/pycharm-community/436/plugins/python-ce/helpers/generator3',
    '/snap/pycharm-community/436/plugins/python-ce/helpers',
    '/usr/lib/python312.zip',
    '/usr/lib/python3.12',
    '/usr/lib/python3.12/lib-dynload',
    '/home/nikita/PycharmProjects/python_advanced/.venv/lib/python3.12/site-packages',
]

path_hooks = [
    None, # (!) real value is "<class 'zipimport.zipimporter'>"
    None, # (!) real value is '<function FileFinder.path_hook.<locals>.path_hook_for_FileFinder at 0x79faa935c5e0>'
]

path_importer_cache = {} # real value of type <class 'dict'> skipped

stdlib_module_names = None # (!) real value is "frozenset({'venv', 'nt', 'warnings', '_contextvars', '_functools', '_sitebuiltins', 'codeop', 'copy', 'antigravity', 're', 'struct', 'traceback', 'fcntl', 'compileall', 'base64', 'telnetlib', '_pydatetime', '_zoneinfo', 'xdrlib', 'tty', 'audioop', 'dis', 'nturl2path', '_pyio', '_sqlite3', 'mailbox', '_codecs', 'netrc', '_json', 'email', 'time', 'types', '_statistics', 'abc', 'gettext', 'copyreg', 'os', '_signal', 'collections', 'tabnanny', 'pty', '_lsprof', 'pprint', 'bz2', '_codecs_hk', 'unicodedata', '_msi', '_typing', '_weakref', 'encodings', 'binascii', 'ensurepip', 'cProfile', 'pydoc_data', 'xml', 'glob', '_tkinter', 'uuid', 'rlcompleter', '_markupbase', 'gzip', '_scproxy', 'cmd', 'shelve', '_abc', 'configparser', 'genericpath', 'sre_constants', '_pydecimal', '_pickle', '_aix_support', 'uu', '_sha2', '_lzma', 'fnmatch', '_compression', 'http', 'html', 'doctest', '_queue', 'nis', 'modulefinder', 'dataclasses', 'ntpath', '_weakrefset', '_gdbm', 'filecmp', 'math', 'statistics', 'string', 'turtledemo', '_codecs_iso2022', 'decimal', 'reprlib', 'queue', 'tarfile', 'pdb', '_frozen_importlib_external', 'locale', 'resource', 'sysconfig', 'gc', '_frozen_importlib', 'token', 'wsgiref', '_ssl', 'pydoc', 'pyclbr', '_elementtree', 'opcode', 'tkinter', 'imghdr', 'runpy', 'ssl', 'weakref', 'webbrowser', 'datetime', 'spwd', '_io', 'sqlite3', '_imp', 'numbers', 'readline', 'graphlib', 'sndhdr', 'ctypes', 'zipimport', 'multiprocessing', 'this', '_collections', '_ast', 'select', 'mmap', 'textwrap', '_winapi', 'turtle', 'ast', 'winsound', 'codecs', 'posixpath', 'shlex', '_compat_pickle', 'stat', '_string', 'zipapp', 'sre_parse', 'py_compile', '_multiprocessing', 'termios', 'mailcap', 'zlib', '_collections_abc', 'socket', 'poplib', '_heapq', '_random', 'importlib', '_pylong', 'signal', 'sys', 'tracemalloc', 'hmac', 'fractions', 'contextvars', 'ossaudiodev', '_threading_local', '_uuid', '_bz2', 'grp', 'cgitb', 'atexit', 'selectors', 'pickle', 'winreg', 'linecache', '_overlapped', 'contextlib', '_tokenize', 'urllib', '_blake2', 'zoneinfo', 'lib2to3', 'cmath', 'pwd', 'argparse', 'getpass', '_stat', 'aifc', '_osx_support', 'smtplib', 'posix', 'functools', '_posixsubprocess', 'pyexpat', '_locale', 'socketserver', '_warnings', 'msilib', 'dbm', 'chunk', 'crypt', 'subprocess', '_operator', 'bdb', '_py_abc', '_csv', '_struct', 'sched', '_md5', '_ctypes', '_strptime', 'io', '_bisect', '_posixshmem', '_thread', 'heapq', 'pkgutil', 'array', 'faulthandler', 'platform', 'sre_compile', 'threading', 'unittest', 'itertools', '_asyncio', 'csv', '_datetime', 'pickletools', 'pipes', 'keyword', 'ipaddress', 'enum', 'symtable', 'builtins', 'bisect', '_hashlib', 'errno', 'idlelib', 'profile', 'curses', 'quopri', 'fileinput', 'site', '_tracemalloc', 'logging', 'json', 'timeit', '_codecs_jp', 'tomllib', 'plistlib', '_codecs_tw', 'hashlib', '_sha1', 'pstats', 'shutil', 'sunau', 'syslog', 'trace', 'operator', '_socket', 'ftplib', 'wave', 'nntplib', 'asyncio', '_sre', '_decimal', 'optparse', 'inspect', 'marshal', '__future__', 'colorsys', '_dbm', 'code', '_codecs_cn', '_sha3', 'concurrent', 'msvcrt', 'pathlib', 'calendar', 'mimetypes', 'zipfile', 'random', 'getopt', '_multibytecodec', '_opcode', 'difflib', '_symtable', 'xmlrpc', '_crypt', 'secrets', '_curses_panel', '_codecs_kr', 'imaplib', 'tempfile', 'tokenize', 'lzma', 'typing', 'stringprep', 'cgi', '_curses'})"

thread_info = (
    'pthread',
    'semaphore',
    'NPTL 2.39',
)

version_info = (
    3,
    12,
    3,
    'final',
    0,
)

warnoptions = []

_git = (
    'CPython',
    '',
    '',
)

_xoptions = {}

__spec__ = None # (!) real value is "ModuleSpec(name='sys', loader=<class '_frozen_importlib.BuiltinImporter'>, origin='built-in')"

# intermittent names
exc_value = Exception()
exc_traceback=None
