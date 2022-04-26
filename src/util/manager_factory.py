from enum import Enum

from managers.AptPackageManager import AptPackageManager
from managers.BasePackageManager import BasePackageManager


class PackageManagerType(Enum):
    APT = 1


def get_package_manager(type: PackageManagerType) -> BasePackageManager:
    if type == PackageManagerType.APT:
        return AptPackageManager()
    else:
        return None
