import ctypes
from ctypes import wintypes

LOCALE_NAME_INVARIANT = ''
LOCALE_NAME_SYSTEM_DEFAULT = '!sys-default-locale'
LOCALE_NAME_USER_DEFAULT = 0

LOCALE_NAME_MAX_LENGTH = 85

_kern32 = ctypes.windll['Kernel32']

def _locale_name(func) -> str:
    name = ctypes.create_string_buffer(LOCALE_NAME_MAX_LENGTH)
    ret = func(name, LOCALE_NAME_MAX_LENGTH)
    if ret:
        return name[:(ret - 1) * 2].decode('UTF-16LE')
    raise ValueError('Unable to get locale name')


def user_locale_name() -> str:
    return _locale_name(_kern32.GetUserDefaultLocaleName)


def system_locale_name() -> str:
    return _locale_name(_kern32.GetSystemDefaultLocaleName)
