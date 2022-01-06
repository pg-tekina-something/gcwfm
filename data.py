import dataclasses
from enum import IntEnum, auto

@dataclasses.dataclass
class Warning:
    class LANG(IntEnum):
        C = 0x00000001
        CPP = 0x00000002
        D = 0x00000004
        FORTRAN = 0x00000008
        GO = 0x00000010
        OBJC = 0x00000020
        OBJCPP = 0x00000040
        UNKNOWN = 0x00000000

    warning: str
    description: str
    lang: LANG = LANG.UNKNOWN
