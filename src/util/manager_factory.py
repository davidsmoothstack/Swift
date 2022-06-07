from enum import Enum

from managers.AptPackageManager import AptPackageManager
from managers.BasePackageManager import BasePackageManager
from managers.SnapPackageManager import SnapPackageManager
from managers.YumPackageManager import YumPackageManager
from managers.ScriptManager import ScriptPackageManager


def get_package_manager(package_config) -> BasePackageManager:
    package_manager = package_config.manager.name

    if package_manager == "apt":
        return AptPackageManager(package_config)
    if package_manager == "snap":
        return SnapPackageManager(package_config)
    if package_manager == "yum":
        return YumPackageManager(package_config)
    if package_manager == "script":
        return ScriptPackageManager(package_config)
    else:
        return None
