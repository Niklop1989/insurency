# encoding: utf-8
# module _typing
# from (built-in)
# by generator 1.147
""" Accelerators for the typing module. """
# no imports

# functions

def _idfunc(*args, **kwargs): # real signature unknown
    pass

# classes

class Generic(object):
    """
    Abstract base class for generic types.
    
    On Python 3.12 and newer, generic classes implicitly inherit from
    Generic when they declare a parameter list after the class's name::
    
        class Mapping[KT, VT]:
            def __getitem__(self, key: KT) -> VT:
                ...
            # Etc.
    
    On older versions of Python, however, generic classes have to
    explicitly inherit from Generic.
    
    After a class has been declared to be generic, it can then be used as
    follows::
    
        def lookup_name[KT, VT](mapping: Mapping[KT, VT], key: KT, default: VT) -> VT:
            try:
                return mapping[key]
            except KeyError:
                return default
    """
    @classmethod
    def __class_getitem__(cls, *args, **kwargs): # real signature unknown
        """
        Parameterizes a generic class.
        
        At least, parameterizing a generic class is the *main* thing this
        method does. For example, for some generic class `Foo`, this is called
        when we do `Foo[int]` - there, with `cls=Foo` and `params=int`.
        
        However, note that this method is also called when defining generic
        classes in the first place with `class Foo[T]: ...`.
        """
        pass

    @classmethod
    def __init_subclass__(cls, *args, **kwargs): # real signature unknown
        """ Function to initialize subclasses. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class ParamSpec(object):
    """
    Parameter specification variable.
    
    The preferred way to construct a parameter specification is via the
    dedicated syntax for generic functions, classes, and type aliases,
    where the use of '**' creates a parameter specification::
    
        type IntFunc[**P] = Callable[P, int]
    
    For compatibility with Python 3.11 and earlier, ParamSpec objects
    can also be created as follows::
    
        P = ParamSpec('P')
    
    Parameter specification variables exist primarily for the benefit of
    static type checkers.  They are used to forward the parameter types of
    one callable to another callable, a pattern commonly found in
    higher-order functions and decorators.  They are only valid when used
    in ``Concatenate``, or as the first argument to ``Callable``, or as
    parameters for user-defined Generics. See class Generic for more
    information on generic types.
    
    An example for annotating a decorator::
    
        def add_logging[**P, T](f: Callable[P, T]) -> Callable[P, T]:
            '''A type-safe decorator to add logging to a function.'''
            def inner(*args: P.args, **kwargs: P.kwargs) -> T:
                logging.info(f'{f.__name__} was called')
                return f(*args, **kwargs)
            return inner
    
        @add_logging
        def add_two(x: float, y: float) -> float:
            '''Add two numbers together.'''
            return x + y
    
    Parameter specification variables can be introspected. e.g.::
    
        >>> P = ParamSpec("P")
        >>> P.__name__
        'P'
    
    Note that only parameter specification variables defined in the global
    scope can be pickled.
    """
    def __init__(self, P): # real signature unknown; restored from __doc__
        pass

    def __mro_entries__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __or__(self, *args, **kwargs): # real signature unknown
        """ Return self|value. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __ror__(self, *args, **kwargs): # real signature unknown
        """ Return value|self. """
        pass

    def __typing_prepare_subst__(self, *args, **kwargs): # real signature unknown
        pass

    def __typing_subst__(self, *args, **kwargs): # real signature unknown
        pass

    args = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Represents positional arguments."""

    kwargs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Represents keyword arguments."""

    __bound__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __contravariant__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __covariant__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __infer_variance__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __name__ = 'ParamSpec'


class ParamSpecArgs(object):
    """
    The args for a ParamSpec object.
    
    Given a ParamSpec object P, P.args is an instance of ParamSpecArgs.
    
    ParamSpecArgs objects have a reference back to their ParamSpec::
    
        >>> P = ParamSpec("P")
        >>> P.args.__origin__ is P
        True
    
    This type is meant for runtime introspection and has no special meaning
    to static type checkers.
    """
    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __mro_entries__(self, *args, **kwargs): # real signature unknown
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

    __origin__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __hash__ = None


class ParamSpecKwargs(object):
    """
    The kwargs for a ParamSpec object.
    
    Given a ParamSpec object P, P.kwargs is an instance of ParamSpecKwargs.
    
    ParamSpecKwargs objects have a reference back to their ParamSpec::
    
        >>> P = ParamSpec("P")
        >>> P.kwargs.__origin__ is P
        True
    
    This type is meant for runtime introspection and has no special meaning
    to static type checkers.
    """
    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __mro_entries__(self, *args, **kwargs): # real signature unknown
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

    __origin__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __hash__ = None


class TypeAliasType(object):
    """
    Type alias.
    
    Type aliases are created through the type statement::
    
        type Alias = int
    
    In this example, Alias and int will be treated equivalently by static
    type checkers.
    
    At runtime, Alias is an instance of TypeAliasType. The __name__
    attribute holds the name of the type alias. The value of the type alias
    is stored in the __value__ attribute. It is evaluated lazily, so the
    value is computed only if the attribute is accessed.
    
    Type aliases can also be generic::
    
        type ListOrSet[T] = list[T] | set[T]
    
    In this case, the type parameters of the alias are stored in the
    __type_params__ attribute.
    
    See PEP 695 for more information.
    """
    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __or__(self, *args, **kwargs): # real signature unknown
        """ Return self|value. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __ror__(self, *args, **kwargs): # real signature unknown
        """ Return value|self. """
        pass

    __parameters__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __type_params__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __value__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __name__ = 'TypeAliasType'


class TypeVar(object):
    """
    Type variable.
    
    The preferred way to construct a type variable is via the dedicated
    syntax for generic functions, classes, and type aliases::
    
        class Sequence[T]:  # T is a TypeVar
            ...
    
    This syntax can also be used to create bound and constrained type
    variables::
    
        # S is a TypeVar bound to str
        class StrSequence[S: str]:
            ...
    
        # A is a TypeVar constrained to str or bytes
        class StrOrBytesSequence[A: (str, bytes)]:
            ...
    
    However, if desired, reusable type variables can also be constructed
    manually, like so::
    
       T = TypeVar('T')  # Can be anything
       S = TypeVar('S', bound=str)  # Can be any subtype of str
       A = TypeVar('A', str, bytes)  # Must be exactly str or bytes
    
    Type variables exist primarily for the benefit of static type
    checkers.  They serve as the parameters for generic types as well
    as for generic function and type alias definitions.
    
    The variance of type variables is inferred by type checkers when they
    are created through the type parameter syntax and when
    ``infer_variance=True`` is passed. Manually created type variables may
    be explicitly marked covariant or contravariant by passing
    ``covariant=True`` or ``contravariant=True``. By default, manually
    created type variables are invariant. See PEP 484 and PEP 695 for more
    details.
    """
    def __init__(self, T): # real signature unknown; restored from __doc__
        pass

    def __mro_entries__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __or__(self, *args, **kwargs): # real signature unknown
        """ Return self|value. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __ror__(self, *args, **kwargs): # real signature unknown
        """ Return value|self. """
        pass

    def __typing_subst__(self, *args, **kwargs): # real signature unknown
        pass

    __bound__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __constraints__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __contravariant__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __covariant__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __infer_variance__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __name__ = 'TypeVar'


class TypeVarTuple(object):
    """
    Type variable tuple. A specialized form of type variable that enables
    variadic generics.
    
    The preferred way to construct a type variable tuple is via the
    dedicated syntax for generic functions, classes, and type aliases,
    where a single '*' indicates a type variable tuple::
    
        def move_first_element_to_last[T, *Ts](tup: tuple[T, *Ts]) -> tuple[*Ts, T]:
            return (*tup[1:], tup[0])
    
    For compatibility with Python 3.11 and earlier, TypeVarTuple objects
    can also be created as follows::
    
        Ts = TypeVarTuple('Ts')  # Can be given any name
    
    Just as a TypeVar (type variable) is a placeholder for a single type,
    a TypeVarTuple is a placeholder for an *arbitrary* number of types. For
    example, if we define a generic class using a TypeVarTuple::
    
        class C[*Ts]: ...
    
    Then we can parameterize that class with an arbitrary number of type
    arguments::
    
        C[int]       # Fine
        C[int, str]  # Also fine
        C[()]        # Even this is fine
    
    For more details, see PEP 646.
    
    Note that only TypeVarTuples defined in the global scope can be
    pickled.
    """
    def __init__(self, Ts): # real signature unknown; restored from __doc__
        pass

    def __iter__(self, *args, **kwargs): # real signature unknown
        """ Implement iter(self). """
        pass

    def __mro_entries__(self, *args, **kwargs): # real signature unknown
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

    def __typing_prepare_subst__(self, *args, **kwargs): # real signature unknown
        pass

    def __typing_subst__(self, *args, **kwargs): # real signature unknown
        pass

    __name__ = 'TypeVarTuple'


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

__spec__ = None # (!) real value is "ModuleSpec(name='_typing', loader=<class '_frozen_importlib.BuiltinImporter'>, origin='built-in')"

