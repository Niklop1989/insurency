# encoding: utf-8
# module apt_pkg
# from /usr/lib/python3/dist-packages/apt_pkg.cpython-312-x86_64-linux-gnu.so
# by generator 1.147
"""
Classes and functions wrapping the apt-pkg library.

The apt_pkg module provides several classes and functions for accessing
the functionality provided by the apt-pkg library. Typical uses might
include reading APT index files and configuration files and installing
or removing packages.
"""
# no imports

from .object import object

class Policy(object):
    """
    Policy(cache)
    
    Representation of the policy of the Cache object given by cache. This
    provides a superset of policy-related functionality compared to the
    DepCache class. The DepCache can be used for most purposes, but there
    may be some cases where a special policy class is needed.
    """
    def create_pin(self, type, pkg, data, priority): # real signature unknown; restored from __doc__
        """
        create_pin(type: str, pkg: str, data: str, priority: int)
        
        Create a pin for the policy. The parameter 'type' refers to one of the
        strings 'Version', 'Release', or 'Origin'. The argument 'pkg' is the
        name of the package. The parameter 'data' refers to the value
        (e.g. 'unstable' for type='Release') and the other possible options.
        The parameter 'priority' gives the priority of the pin.
        """
        pass

    def get_candidate_ver(self, *args, **kwargs): # real signature unknown
        """
        get_match(package: apt_pkg.Package) -> Optional[apt_pkg.Version]
        
        Get the best package for the job.
        """
        pass

    def get_priority(self, package, apt_pkg_Package=None, apt_pkg_Version=None, apt_pkg_PackageFile=None): # real signature unknown; restored from __doc__
        """
        get_priority(package: Union[apt_pkg.Package, apt_pkg.Version, apt_pkg.PackageFile]) -> int
        
        Return the priority of the package.
        """
        return 0

    def init_defaults(self): # real signature unknown; restored from __doc__
        """
        init_defaults()
        
        Initialize defaults. Needed after calling :meth:`create_pin()`
        with an empty `pkg` argument
        """
        pass

    def read_pindir(self, dirname): # real signature unknown; restored from __doc__
        """
        read_pindir(dirname: str) -> bool
        
        Read the pin files in the given dir (e.g. '/etc/apt/preferences.d')
        and add them to the policy.
        """
        return False

    def read_pinfile(self, filename): # real signature unknown; restored from __doc__
        """
        read_pinfile(filename: str) -> bool
        
        Read the pin file given by filename (e.g. '/etc/apt/preferences')
        and add it to the policy.
        """
        return False

    def set_priority(self, which, apt_pkg_Version=None, apt_pkg_PackageFile=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        set_priority(which: Union[apt_pkg.Version, apt_pkg.PackageFile], priority: int) -> None
        
        Override priority for the given package/file. Behavior is undefined ifa preferences file is read after that, or :meth:`init_defaults` is called.
        """
        pass

    def __init__(self, cache): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


