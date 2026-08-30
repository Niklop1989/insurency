# encoding: utf-8
# module systemd.id128
# from /usr/lib/python3/dist-packages/systemd/id128.cpython-312-x86_64-linux-gnu.so
# by generator 1.147
"""
Python interface to the libsystemd-id128 library.

Provides SD_MESSAGE_* constants and functions to query and generate
128-bit unique identifiers.
"""
# no imports

# Variables with simple values

__version__ = '235'

# functions

def get_boot(): # real signature unknown; restored from __doc__
    """
    get_boot() -> UUID
    
    Return a 128-bit unique identifier for this boot.
    Wraps sd_id128_get_boot(3).
    """
    pass

def get_machine(): # real signature unknown; restored from __doc__
    """
    get_machine() -> UUID
    
    Return a 128-bit unique identifier for this machine.
    Wraps sd_id128_get_machine(3).
    """
    pass

def get_machine_app_specific(UUID): # real signature unknown; restored from __doc__
    """
    get_machine_app_specific(UUID) -> UUID
    
    Return a 128-bit unique identifier for this application and machine.
    Wraps sd_id128_get_machine_app_specific(3).
    """
    pass

def randomize(): # real signature unknown; restored from __doc__
    """
    randomize() -> UUID
    
    Return a new random 128-bit unique identifier.
    Wraps sd_id128_randomize(3).
    """
    pass

# no classes
# variables with complex values

SD_MESSAGE_BACKTRACE = None # (!) real value is "UUID('1f4e0a44-a886-4993-9aae-a34fc6da8c95')"

SD_MESSAGE_BOOTCHART = None # (!) real value is "UUID('9f26aa56-2cf4-40c2-b16c-773d0479b518')"

SD_MESSAGE_CONFIG_ERROR = None # (!) real value is "UUID('c772d24e-9a88-4cbe-b9ea-12625c306c01')"

SD_MESSAGE_COREDUMP = None # (!) real value is "UUID('fc2e22bc-6ee6-47b6-b907-29ab34a250b1')"

SD_MESSAGE_DEVICE_PATH_NOT_SUITABLE = None # (!) real value is "UUID('01019013-8f49-4e29-a0ef-6669749531aa')"

SD_MESSAGE_DNSSEC_DOWNGRADE = None # (!) real value is "UUID('36db2dfa-5a90-45e1-bd4a-f5f93e1cf057')"

SD_MESSAGE_DNSSEC_FAILURE = None # (!) real value is "UUID('1675d7f1-7217-4098-b110-8bf8c7dc8f5d')"

SD_MESSAGE_DNSSEC_TRUST_ANCHOR_REVOKED = None # (!) real value is "UUID('4d4408cf-d0d1-4485-9184-d1e65d7c8a65')"

SD_MESSAGE_FACTORY_RESET = None # (!) real value is "UUID('c14aaf76-ec28-4a5f-a1f1-05f88dfb061c')"

SD_MESSAGE_FORWARD_SYSLOG_MISSED = None # (!) real value is "UUID('0027229c-a064-4181-a76c-4e92458afa2e')"

SD_MESSAGE_HIBERNATE_KEY = None # (!) real value is "UUID('b72ea4a2-8815-45a0-b50e-200e55b9b073')"

SD_MESSAGE_HIBERNATE_KEY_LONG_PRESS = None # (!) real value is "UUID('167836df-6f7f-428e-9814-7227b2dc8945')"

SD_MESSAGE_INVALID_CONFIGURATION = None # (!) real value is "UUID('c772d24e-9a88-4cbe-b9ea-12625c306c01')"

SD_MESSAGE_JOURNAL_DROPPED = None # (!) real value is "UUID('a596d6fe-7bfa-4994-828e-72309e95d61e')"

SD_MESSAGE_JOURNAL_MISSED = None # (!) real value is "UUID('e9bf28e6-e834-481b-b6f4-8f548ad13606')"

SD_MESSAGE_JOURNAL_START = None # (!) real value is "UUID('f77379a8-490b-408b-be5f-6940505a777b')"

SD_MESSAGE_JOURNAL_STOP = None # (!) real value is "UUID('d93fb3c9-c24d-451a-97ce-a615ce59c00b')"

SD_MESSAGE_JOURNAL_USAGE = None # (!) real value is "UUID('ec387f57-7b84-4b8f-a948-f33cad9a75e6')"

SD_MESSAGE_LID_CLOSED = None # (!) real value is "UUID('b72ea4a2-8815-45a0-b50e-200e55b9b070')"

SD_MESSAGE_LID_OPENED = None # (!) real value is "UUID('b72ea4a2-8815-45a0-b50e-200e55b9b06f')"

SD_MESSAGE_MACHINE_START = None # (!) real value is "UUID('24d8d445-2573-4024-9606-8381a6312df2')"

SD_MESSAGE_MACHINE_STOP = None # (!) real value is "UUID('58432bd3-bace-477c-b514-b56381b8a758')"

SD_MESSAGE_MOUNT_POINT_PATH_NOT_SUITABLE = None # (!) real value is "UUID('1b3bb940-37f0-4bbf-8102-8e135a12d293')"

SD_MESSAGE_NOBODY_USER_UNSUITABLE = None # (!) real value is "UUID('b480325f-9c39-4a7b-802c-231e51a2752c')"

SD_MESSAGE_OVERMOUNTING = None # (!) real value is "UUID('1dee0369-c7fc-4736-b709-9b38ecb46ee7')"

SD_MESSAGE_POWER_KEY = None # (!) real value is "UUID('b72ea4a2-8815-45a0-b50e-200e55b9b071')"

SD_MESSAGE_POWER_KEY_LONG_PRESS = None # (!) real value is "UUID('3e011710-1eb2-43c1-b9a5-0db3494ab10b')"

SD_MESSAGE_REBOOT_KEY = None # (!) real value is "UUID('9fa9d2c0-1213-4ec3-8545-1ffe316f97d0')"

SD_MESSAGE_REBOOT_KEY_LONG_PRESS = None # (!) real value is "UUID('f1c59a58-c9d9-4366-8965-c337caec5975')"

SD_MESSAGE_SEAT_START = None # (!) real value is "UUID('fcbefc5d-a23d-4280-93f9-7c82a9290f7b')"

SD_MESSAGE_SEAT_STOP = None # (!) real value is "UUID('e7852bfe-4678-4ed0-accd-e04bc864c2d5')"

SD_MESSAGE_SESSION_START = None # (!) real value is "UUID('8d45620c-1a43-48db-b174-10da57c60c66')"

SD_MESSAGE_SESSION_STOP = None # (!) real value is "UUID('33549394-24b4-456d-9802-ca8333ed424a')"

SD_MESSAGE_SHUTDOWN = None # (!) real value is "UUID('98268866-d1d5-4a49-9c4e-98921d93bc40')"

SD_MESSAGE_SLEEP_START = None # (!) real value is "UUID('6bbd95ee-9779-41e4-97c4-8be27c254128')"

SD_MESSAGE_SLEEP_STOP = None # (!) real value is "UUID('8811e6df-2a8e-40f5-8a94-cea26f8ebf14')"

SD_MESSAGE_SPAWN_FAILED = None # (!) real value is "UUID('64125765-1c1b-4ec9-a862-4d7a40a9e1e7')"

SD_MESSAGE_STARTUP_FINISHED = None # (!) real value is "UUID('b07a249c-d024-414a-82dd-00cd181378ff')"

SD_MESSAGE_SUSPEND_KEY = None # (!) real value is "UUID('b72ea4a2-8815-45a0-b50e-200e55b9b072')"

SD_MESSAGE_SUSPEND_KEY_LONG_PRESS = None # (!) real value is "UUID('bfdaf6d3-12ab-4007-bc1f-e40a15df78e8')"

SD_MESSAGE_SYSTEMD_UDEV_SETTLE_DEPRECATED = None # (!) real value is "UUID('1c0454c1-bd22-41e0-ac6f-efb4bc631433')"

SD_MESSAGE_SYSTEM_DOCKED = None # (!) real value is "UUID('f5f416b8-6207-4b28-927a-48c3ba7d51ff')"

SD_MESSAGE_SYSTEM_UNDOCKED = None # (!) real value is "UUID('51e171bd-5852-4856-8110-144c517cca53')"

SD_MESSAGE_TAINTED = None # (!) real value is "UUID('50876a9d-b00f-4c40-bde1-a2ad381c3a1b')"

SD_MESSAGE_TIMEZONE_CHANGE = None # (!) real value is "UUID('45f82f4a-ef7a-4bbf-942c-e861d1f20990')"

SD_MESSAGE_TIME_CHANGE = None # (!) real value is "UUID('c7a78707-9b35-4eaa-a9e7-7b371893cd27')"

SD_MESSAGE_TIME_SYNC = None # (!) real value is "UUID('7c8a41f3-7b76-4941-a0e1-780b1be2f037')"

SD_MESSAGE_TRUNCATED_CORE = None # (!) real value is "UUID('5aadd8e9-54dc-4b1a-8c95-4d63fd9e1137')"

SD_MESSAGE_UNIT_FAILED = None # (!) real value is "UUID('be02cf68-55d2-428b-a40d-f7e9d022f03d')"

SD_MESSAGE_UNIT_FAILURE_RESULT = None # (!) real value is "UUID('d9b373ed-55a6-4feb-8242-e02dbe79a49c')"

SD_MESSAGE_UNIT_OOMD_KILL = None # (!) real value is "UUID('d989611b-15e4-4c9d-bf31-e3c81256e4ed')"

SD_MESSAGE_UNIT_OUT_OF_MEMORY = None # (!) real value is "UUID('fe6faa94-e777-4663-a0da-52717891d8ef')"

SD_MESSAGE_UNIT_PROCESS_EXIT = None # (!) real value is "UUID('98e32220-3f7a-4ed2-90d0-9fe03c09fe15')"

SD_MESSAGE_UNIT_RELOADED = None # (!) real value is "UUID('7b05ebc6-6838-4222-baa8-881179cfda54')"

SD_MESSAGE_UNIT_RELOADING = None # (!) real value is "UUID('d34d037f-ff18-47e6-ae66-9a370e694725')"

SD_MESSAGE_UNIT_RESOURCES = None # (!) real value is "UUID('ae8f7b86-6b03-47b9-af31-fe1c80b127c0')"

SD_MESSAGE_UNIT_RESTART_SCHEDULED = None # (!) real value is "UUID('5eb03494-b658-4870-a536-b337290809b3')"

SD_MESSAGE_UNIT_SKIPPED = None # (!) real value is "UUID('0e4284a0-caca-4bfc-81c0-bb6786972673')"

SD_MESSAGE_UNIT_STARTED = None # (!) real value is "UUID('39f53479-d3a0-45ac-8e11-786248231fbf')"

SD_MESSAGE_UNIT_STARTING = None # (!) real value is "UUID('7d4958e8-42da-4a75-8f6c-1cdc7b36dcc5')"

SD_MESSAGE_UNIT_STOPPED = None # (!) real value is "UUID('9d1aaa27-d601-40bd-9636-5438aad20286')"

SD_MESSAGE_UNIT_STOPPING = None # (!) real value is "UUID('de5b426a-63be-47a7-b6ac-3eaac82e2f6f')"

SD_MESSAGE_UNIT_SUCCESS = None # (!) real value is "UUID('7ad2d189-f7e9-4e70-a38c-781354912448')"

SD_MESSAGE_UNSAFE_USER_NAME = None # (!) real value is "UUID('b61fdac6-12e9-4b91-8228-5b998843061f')"

SD_MESSAGE_USER_STARTUP_FINISHED = None # (!) real value is "UUID('eed00a68-ffd8-4e31-8821-05fd973abdd1')"

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x73dd9a19b9b0>'

__spec__ = None # (!) real value is "ModuleSpec(name='systemd.id128', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x73dd9a19b9b0>, origin='/usr/lib/python3/dist-packages/systemd/id128.cpython-312-x86_64-linux-gnu.so')"

