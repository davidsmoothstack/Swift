from enum import Enum

from managers.AptPackageManager import AptPackageManager
from managers.IPackageManager import IPackageManager


class PackageManagerType(Enum):
    APT = 1


def get_package_manager(type: PackageManagerType) -> IPackageManager:
    if type == PackageManagerType.APT:
        return AptPackageManager()
    else:
        return None
