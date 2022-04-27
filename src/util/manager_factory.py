from enum import Enum

from managers.AptPackageManager import AptPackageManager
from managers.BasePackageManager import BasePackageManager
from managers.SnapPackageManager import SnapPackageManager


class PackageManagerType(Enum):
    APT = 1
    SNAP = 2


def get_package_manager(type: PackageManagerType) -> BasePackageManager:
    if type == PackageManagerType.APT:
        return AptPackageManager()
    if type == PackageManagerType.SNAP:
        return SnapPackageManager()
    else:
        return None
