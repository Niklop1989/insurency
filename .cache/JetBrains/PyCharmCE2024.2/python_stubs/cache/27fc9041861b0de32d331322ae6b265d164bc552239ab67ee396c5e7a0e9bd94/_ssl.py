# encoding: utf-8
# module _ssl
# from /usr/lib/python3.12/lib-dynload/_ssl.cpython-312-x86_64-linux-gnu.so
# by generator 1.147
"""
Implementation module for SSL socket operations.  See the socket module
for documentation.
"""

# imports
import ssl as __ssl


# Variables with simple values

ALERT_DESCRIPTION_ACCESS_DENIED = 49

ALERT_DESCRIPTION_BAD_CERTIFICATE = 42

ALERT_DESCRIPTION_BAD_CERTIFICATE_HASH_VALUE = 114

ALERT_DESCRIPTION_BAD_CERTIFICATE_STATUS_RESPONSE = 113

ALERT_DESCRIPTION_BAD_RECORD_MAC = 20

ALERT_DESCRIPTION_CERTIFICATE_EXPIRED = 45
ALERT_DESCRIPTION_CERTIFICATE_REVOKED = 44
ALERT_DESCRIPTION_CERTIFICATE_UNKNOWN = 46
ALERT_DESCRIPTION_CERTIFICATE_UNOBTAINABLE = 111

ALERT_DESCRIPTION_CLOSE_NOTIFY = 0

ALERT_DESCRIPTION_DECODE_ERROR = 50

ALERT_DESCRIPTION_DECOMPRESSION_FAILURE = 30

ALERT_DESCRIPTION_DECRYPT_ERROR = 51

ALERT_DESCRIPTION_HANDSHAKE_FAILURE = 40

ALERT_DESCRIPTION_ILLEGAL_PARAMETER = 47

ALERT_DESCRIPTION_INSUFFICIENT_SECURITY = 71

ALERT_DESCRIPTION_INTERNAL_ERROR = 80

ALERT_DESCRIPTION_NO_RENEGOTIATION = 100

ALERT_DESCRIPTION_PROTOCOL_VERSION = 70

ALERT_DESCRIPTION_RECORD_OVERFLOW = 22

ALERT_DESCRIPTION_UNEXPECTED_MESSAGE = 10

ALERT_DESCRIPTION_UNKNOWN_CA = 48

ALERT_DESCRIPTION_UNKNOWN_PSK_IDENTITY = 115

ALERT_DESCRIPTION_UNRECOGNIZED_NAME = 112

ALERT_DESCRIPTION_UNSUPPORTED_CERTIFICATE = 43
ALERT_DESCRIPTION_UNSUPPORTED_EXTENSION = 110

ALERT_DESCRIPTION_USER_CANCELLED = 90

CERT_NONE = 0
CERT_OPTIONAL = 1
CERT_REQUIRED = 2

ENCODING_DER = 2
ENCODING_PEM = 1

HAS_ALPN = True
HAS_ECDH = True
HAS_NPN = False
HAS_SNI = True
HAS_SSLv2 = False
HAS_SSLv3 = False
HAS_TLSv1 = True

HAS_TLSv1_1 = True
HAS_TLSv1_2 = True
HAS_TLSv1_3 = True

HAS_TLS_UNIQUE = True

HOSTFLAG_ALWAYS_CHECK_SUBJECT = 1

HOSTFLAG_MULTI_LABEL_WILDCARDS = 8

HOSTFLAG_NEVER_CHECK_SUBJECT = 32

HOSTFLAG_NO_PARTIAL_WILDCARDS = 4

HOSTFLAG_NO_WILDCARDS = 2

HOSTFLAG_SINGLE_LABEL_SUBDOMAINS = 16

OPENSSL_VERSION = 'OpenSSL 3.0.13 30 Jan 2024'

OPENSSL_VERSION_NUMBER = 805306576

OP_ALL = 2147483728

OP_CIPHER_SERVER_PREFERENCE = 4194304

OP_ENABLE_KTLS = 8

OP_ENABLE_MIDDLEBOX_COMPAT = 1048576

OP_IGNORE_UNEXPECTED_EOF = 128

OP_LEGACY_SERVER_CONNECT = 4

OP_NO_COMPRESSION = 131072
OP_NO_RENEGOTIATION = 1073741824
OP_NO_SSLv2 = 0
OP_NO_SSLv3 = 33554432
OP_NO_TICKET = 16384
OP_NO_TLSv1 = 67108864

OP_NO_TLSv1_1 = 268435456
OP_NO_TLSv1_2 = 134217728
OP_NO_TLSv1_3 = 536870912

OP_SINGLE_DH_USE = 0

OP_SINGLE_ECDH_USE = 0

PROTOCOL_SSLv23 = 2
PROTOCOL_TLS = 2
PROTOCOL_TLSv1 = 3

PROTOCOL_TLSv1_1 = 4
PROTOCOL_TLSv1_2 = 5

PROTOCOL_TLS_CLIENT = 16
PROTOCOL_TLS_SERVER = 17

PROTO_MAXIMUM_SUPPORTED = -1

PROTO_MINIMUM_SUPPORTED = -2

PROTO_SSLv3 = 768
PROTO_TLSv1 = 769

PROTO_TLSv1_1 = 770
PROTO_TLSv1_2 = 771
PROTO_TLSv1_3 = 772

SSL_ERROR_EOF = 8

SSL_ERROR_INVALID_ERROR_CODE = 10

SSL_ERROR_SSL = 1
SSL_ERROR_SYSCALL = 5

SSL_ERROR_WANT_CONNECT = 7
SSL_ERROR_WANT_READ = 2
SSL_ERROR_WANT_WRITE = 3

SSL_ERROR_WANT_X509_LOOKUP = 4

SSL_ERROR_ZERO_RETURN = 6

VERIFY_ALLOW_PROXY_CERTS = 64

VERIFY_CRL_CHECK_CHAIN = 12
VERIFY_CRL_CHECK_LEAF = 4

VERIFY_DEFAULT = 0

VERIFY_X509_PARTIAL_CHAIN = 524288

VERIFY_X509_STRICT = 32

VERIFY_X509_TRUSTED_FIRST = 32768

_DEFAULT_CIPHERS = 'ALL:!COMPLEMENTOFDEFAULT:!eNULL'

# functions

def get_default_verify_paths(*args, **kwargs): # real signature unknown
    """
    Return search paths and environment vars that are used by SSLContext's set_default_verify_paths() to load default CAs.
    
    The values are 'cert_file_env', 'cert_file', 'cert_dir_env', 'cert_dir'.
    """
    pass

def nid2obj(*args, **kwargs): # real signature unknown
    """ Lookup NID, short name, long name and OID of an ASN1_OBJECT by NID. """
    pass

def RAND_add(*args, **kwargs): # real signature unknown
    """
    Mix string into the OpenSSL PRNG state.
    
    entropy (a float) is a lower bound on the entropy contained in
    string.  See RFC 4086.
    """
    pass

def RAND_bytes(*args, **kwargs): # real signature unknown
    """ Generate n cryptographically strong pseudo-random bytes. """
    pass

def RAND_status(*args, **kwargs): # real signature unknown
    """
    Returns True if the OpenSSL PRNG has been seeded with enough data and False if not.
    
    It is necessary to seed the PRNG with RAND_add() on some platforms before
    using the ssl() function.
    """
    pass

def txt2obj(*args, **kwargs): # real signature unknown
    """
    Lookup NID, short name, long name and OID of an ASN1_OBJECT.
    
    By default objects are looked up by OID. With name=True short and
    long name are also matched.
    """
    pass

def _test_decode_cert(*args, **kwargs): # real signature unknown
    pass

# classes

class Certificate(object):
    # no doc
    def get_info(self, *args, **kwargs): # real signature unknown
        pass

    def public_bytes(self, *args, **kwargs): # real signature unknown
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass


class MemoryBIO(object):
    # no doc
    def read(self, *args, **kwargs): # real signature unknown
        """
        Read up to size bytes from the memory BIO.
        
        If size is not specified, read the entire buffer.
        If the return value is an empty bytes instance, this means either
        EOF or that no data is available. Use the "eof" property to
        distinguish between the two.
        """
        pass

    def write(self, *args, **kwargs): # real signature unknown
        """
        Writes the bytes b into the memory BIO.
        
        Returns the number of bytes written.
        """
        pass

    def write_eof(self, *args, **kwargs): # real signature unknown
        """
        Write an EOF marker to the memory BIO.
        
        When all data has been read, the "eof" property will be True.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    eof = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether the memory BIO is at EOF."""

    pending = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The number of bytes pending in the memory BIO."""



class SSLError(OSError):
    """ An error occurred in the SSL implementation. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass


class SSLCertVerificationError(__ssl.SSLError, ValueError):
    """ A certificate could not be verified. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object"""



class SSLEOFError(__ssl.SSLError):
    """ SSL/TLS connection terminated abruptly. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object"""



class SSLSession(object):
    # no doc
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

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    has_ticket = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Does the session contain a ticket?"""

    id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Session id"""

    ticket_lifetime_hint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Ticket life time hint."""

    time = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Session creation time (seconds since epoch)."""

    timeout = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Session timeout (delta in seconds)."""


    __hash__ = None


class SSLSyscallError(__ssl.SSLError):
    """ System error when attempting SSL operation. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object"""



class SSLWantReadError(__ssl.SSLError):
    """
    Non-blocking SSL socket needs to read more data
    before the requested operation can be completed.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object"""



class SSLWantWriteError(__ssl.SSLError):
    """
    Non-blocking SSL socket needs to write more data
    before the requested operation can be completed.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object"""



class SSLZeroReturnError(__ssl.SSLError):
    """ SSL/TLS session closed cleanly. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object"""



class _SSLContext(object):
    # no doc
    def cert_store_stats(self, *args, **kwargs): # real signature unknown
        """
        Returns quantities of loaded X.509 certificates.
        
        X.509 certificates with a CA extension and certificate revocation lists
        inside the context's cert store.
        
        NOTE: Certificates in a capath directory aren't loaded unless they have
        been used at least once.
        """
        pass

    def get_ca_certs(self, *args, **kwargs): # real signature unknown
        """
        Returns a list of dicts with information of loaded CA certs.
        
        If the optional argument is True, returns a DER-encoded copy of the CA
        certificate.
        
        NOTE: Certificates in a capath directory aren't loaded unless they have
        been used at least once.
        """
        pass

    def get_ciphers(self, *args, **kwargs): # real signature unknown
        pass

    def load_cert_chain(self, *args, **kwargs): # real signature unknown
        pass

    def load_dh_params(self, *args, **kwargs): # real signature unknown
        pass

    def load_verify_locations(self, *args, **kwargs): # real signature unknown
        pass

    def session_stats(self, *args, **kwargs): # real signature unknown
        pass

    def set_ciphers(self, *args, **kwargs): # real signature unknown
        pass

    def set_default_verify_paths(self, *args, **kwargs): # real signature unknown
        pass

    def set_ecdh_curve(self, *args, **kwargs): # real signature unknown
        pass

    def _set_alpn_protocols(self, *args, **kwargs): # real signature unknown
        pass

    def _wrap_bio(self, *args, **kwargs): # real signature unknown
        pass

    def _wrap_socket(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    check_hostname = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    keylog_filename = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    maximum_version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    minimum_version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    num_tickets = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Control the number of TLSv1.3 session tickets"""

    options = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    post_handshake_auth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    protocol = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    security_level = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The current security level"""

    sni_callback = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Set a callback that will be called when a server name is provided by the SSL/TLS client in the SNI extension.

If the argument is None then the callback is disabled. The method is called
with the SSLSocket, the server name as a string, and the SSLContext object.
See RFC 6066 for details of the SNI extension."""

    verify_flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    verify_mode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _host_flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _msg_callback = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class _SSLSocket(object):
    # no doc
    def cipher(self, *args, **kwargs): # real signature unknown
        pass

    def compression(self, *args, **kwargs): # real signature unknown
        pass

    def do_handshake(self, *args, **kwargs): # real signature unknown
        pass

    def getpeercert(self, *args, **kwargs): # real signature unknown
        """
        Returns the certificate for the peer.
        
        If no certificate was provided, returns None.  If a certificate was
        provided, but not validated, returns an empty dictionary.  Otherwise
        returns a dict containing information about the peer certificate.
        
        If the optional argument is True, returns a DER-encoded copy of the
        peer certificate, or None if no certificate was provided.  This will
        return the certificate even if it wasn't validated.
        """
        pass

    def get_channel_binding(self, *args, **kwargs): # real signature unknown
        """
        Get channel binding data for current connection.
        
        Raise ValueError if the requested `cb_type` is not supported.  Return bytes
        of the data or None if the data is not available (e.g. before the handshake).
        Only 'tls-unique' channel binding data from RFC 5929 is supported.
        """
        pass

    def get_unverified_chain(self, *args, **kwargs): # real signature unknown
        pass

    def get_verified_chain(self, *args, **kwargs): # real signature unknown
        pass

    def pending(self, *args, **kwargs): # real signature unknown
        """ Returns the number of already decrypted bytes available for read, pending on the connection. """
        pass

    def read(self, size, buffer=None): # real signature unknown; restored from __doc__
        """
        read(size, [buffer])
        Read up to size bytes from the SSL socket.
        """
        pass

    def selected_alpn_protocol(self, *args, **kwargs): # real signature unknown
        pass

    def shared_ciphers(self, *args, **kwargs): # real signature unknown
        pass

    def shutdown(self, *args, **kwargs): # real signature unknown
        """ Does the SSL shutdown handshake with the remote end. """
        pass

    def verify_client_post_handshake(self, *args, **kwargs): # real signature unknown
        """ Initiate TLS 1.3 post-handshake authentication """
        pass

    def version(self, *args, **kwargs): # real signature unknown
        pass

    def write(self, *args, **kwargs): # real signature unknown
        """
        Writes the bytes-like object b into the SSL object.
        
        Returns the number of bytes written.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    context = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """_setter_context(ctx)
This changes the context associated with the SSLSocket. This is typically
used from within a callback function set by the sni_callback
on the SSLContext to change the certificate information associated with the
SSLSocket before the cryptographic exchange handshake messages
"""

    owner = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The Python-level owner of this object.Passed as "self" in servername callback."""

    server_hostname = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The currently set server hostname (for SNI)."""

    server_side = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether this is a server-side socket."""

    session = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """_setter_session(session)
Get / set SSLSession."""

    session_reused = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Was the client session reused during handshake?"""



# variables with complex values

OPENSSL_VERSION_INFO = (
    3,
    0,
    0,
    13,
    0,
)

_OPENSSL_API_VERSION = (
    3,
    0,
    0,
    13,
    0,
)

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7ad8fca6deb0>'

__spec__ = None # (!) real value is "ModuleSpec(name='_ssl', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7ad8fca6deb0>, origin='/usr/lib/python3.12/lib-dynload/_ssl.cpython-312-x86_64-linux-gnu.so')"

