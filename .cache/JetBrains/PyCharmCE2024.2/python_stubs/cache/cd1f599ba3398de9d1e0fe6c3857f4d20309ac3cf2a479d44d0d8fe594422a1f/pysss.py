# encoding: utf-8
# module pysss
# from /usr/lib/python3/dist-packages/pysss.cpython-312-x86_64-linux-gnu.so
# by generator 1.147
# no doc
# no imports

# functions

def getgrouplist(*args, **kwargs): # real signature unknown
    """
    Get list of groups user belongs to.
    
    NOTE: The interface uses the system NSS calls and is not limited to users served by the SSSD!
    :param username: name of user to get list for
    """
    pass

# classes

class password(object):
    """ SSS password obfuscation """
    def encrypt(self, *args, **kwargs): # real signature unknown
        """
        Obfuscate a password
        
        :param password: The password to obfuscate
        
        :param method: The obfuscation method
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    AES_256 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x73dd9a19ab10>'

__spec__ = None # (!) real value is "ModuleSpec(name='pysss', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x73dd9a19ab10>, origin='/usr/lib/python3/dist-packages/pysss.cpython-312-x86_64-linux-gnu.so')"

