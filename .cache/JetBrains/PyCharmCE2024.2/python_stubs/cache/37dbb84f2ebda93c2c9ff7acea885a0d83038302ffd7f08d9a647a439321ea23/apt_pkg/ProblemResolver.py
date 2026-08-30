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

class ProblemResolver(object):
    """
    ProblemResolver(depcache: apt_pkg.DepCache)
    
    ProblemResolver objects take care of resolving problems
    with dependencies. They mark packages for installation/
    removal and try to satisfy all dependencies.
    """
    def clear(self, pkg): # real signature unknown; restored from __doc__
        """
        clear(pkg: apt_pkg.Package)
        
        Revert the actions done by protect()/remove() on the package.
        """
        pass

    def keep_phased_updates(self): # real signature unknown; restored from __doc__
        """
        keep_phased_updates() -> bool
        
        Hold back upgrades to phased versions of already installed
        packages, unless they are security updates.
        """
        return False

    def protect(self, pkg): # real signature unknown; restored from __doc__
        """
        protect(pkg: apt_pkg.Package)
        
        Mark the package as protected in the resolver, meaning that its
        state will not be changed.
        """
        pass

    def remove(self, pkg): # real signature unknown; restored from __doc__
        """
        remove(pkg: apt_pkg.Package)
        
        Mark the package for removal in the resolver.
        """
        pass

    def resolve(self, fix_broken=True): # real signature unknown; restored from __doc__
        """
        resolve([fix_broken: bool = True]) -> bool
        
        Try to intelligently resolve problems by installing and removing
        packages. If 'fix_broken' is True, apt will try to repair broken
        dependencies of installed packages.
        """
        return False

    def resolve_by_keep(self): # real signature unknown; restored from __doc__
        """
        resolve_by_keep() -> bool
        
        Try to resolve problems only by using keep.
        """
        return False

    def __init__(self, depcache): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


