# encoding: utf-8
# module _dbus_bindings
# from /usr/lib/python3/dist-packages/_dbus_bindings.cpython-312-x86_64-linux-gnu.so
# by generator 1.147
"""
Low-level Python bindings for libdbus. Don't use this module directly -
the public API is provided by the `dbus`, `dbus.service`, `dbus.mainloop`
and `dbus.mainloop.glib` modules, with a lower-level API provided by the
`dbus.lowlevel` module.
"""

# imports
import dbus.lowlevel as __dbus_lowlevel


from ._LongBase import _LongBase

class Byte(_LongBase):
    """
    dbus.Byte(integer or bytes of length 1[, variant_level])
    
    An unsigned byte: a subtype of int, with range restricted to [0, 255].
    
    A Byte `b` may be converted to a ``str`` of length 1 via
    ``str(b) == chr(b)`` (Python 2) or to a ``bytes`` of length 1
    via ``bytes([b])`` (Python 3).
    
    Most of the time you don't want to use this class - it mainly exists
    for symmetry with the other D-Bus types. See `dbus.ByteArray` for a
    better way to handle arrays of Byte.
    
    :py:attr:`variant_level` must be non-negative; the default is 0.
    
    .. py:attribute:: variant_level
    
        Indicates how many nested Variant containers this object
        is contained in: if a message's wire format has a variant containing a
        variant containing a byte, this is represented in Python by a
        Byte with variant_level==2.
    """
    def __init__(self, integer_or_bytes_of_length, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass


