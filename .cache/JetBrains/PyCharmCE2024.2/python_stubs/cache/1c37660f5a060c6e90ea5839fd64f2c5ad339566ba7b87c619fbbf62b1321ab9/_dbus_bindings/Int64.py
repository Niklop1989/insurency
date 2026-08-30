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

class Int64(_LongBase):
    """
    dbus.Int64(value: int[, variant_level: int])
    
    A signed 64-bit integer between -0x8000 0000 0000 0000 and
    +0x7FFF FFFF FFFF FFFF, represented as a
    subtype of ``long`` in Python 2 or ``int`` in Python 3.
    
    Note that this may be changed in future to be a subtype of `int` on
    64-bit platforms; applications should not rely on either behaviour.
    
    ``value`` must be within the allowed range, or `OverflowError` will be
    raised.
    
    :py:attr:`variant_level` must be non-negative; the default is 0.
    
    .. py:attribute:: variant_level
    
        Indicates how many nested Variant containers this object
        is contained in: if a message's wire format has a variant containing a
        variant containing an int64, this is represented in Python by an
        Int64 with variant_level==2.
    """
    def __init__(self, value, variant_level=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


