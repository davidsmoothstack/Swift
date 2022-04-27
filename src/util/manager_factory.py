from enum import Enum

from managers.AptPackageManager import AptPackageManager
from managers.BasePackageManager import BasePackageManager
from managers.SnapPackageManager import SnapPackageManager


def get_package_manager(package_config) -> BasePackageManager:
    type = package_config.manager.name

    if type == "apt":
        return AptPackageManager(package_config)
    if type == "snap":
        return SnapPackageManager(package_config)
    else:
        return None
