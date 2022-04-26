from enum import Enum

from package_managers.AptPackageManager import AptPackageManager
from package_managers.IPackageManager import IPackageManager


class PackageManagerType(Enum):
    APT = 1


def get_package_manager(type: PackageManagerType) -> IPackageManager:
    if type == PackageManagerType.APT:
        return AptPackageManager()
    else:
        return None
