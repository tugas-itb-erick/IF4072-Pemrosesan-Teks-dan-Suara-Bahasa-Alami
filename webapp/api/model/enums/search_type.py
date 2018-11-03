from enum import Enum

class SeachType(Enum):
    USERNAME = "username"
    TAG = "tag"

    @staticmethod
    def list_values():
        return [e.value for e in SeachType]
