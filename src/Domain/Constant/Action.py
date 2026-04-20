from enum import Enum

class Action(Enum):
    ALLOW = "allow"
    DELETE = "delete"
    MUTE = "mute"
    MUTE_AND_DELETE = "mute_and_delete"
    BAN = "ban"