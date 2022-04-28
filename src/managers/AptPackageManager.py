import logging
from managers.BasePackageManager import BasePackageManager
from util.shell import shell


class AptPackageManager(BasePackageManager):
    def install_package(self, package_name: str):
        """Installs a package"""
        return shell(f"sudo apt install -y {package_name}")

    def is_installed(self, package_name: str):
        """Check if the package already exists on the system"""
        result = shell(f"sudo apt -qq list {package_name} | grep installed")
        return result.isSuccess

    def upgrade_package(self, package_name: str):
        """Upgrades the package"""
        return shell(f"sudo apt install --only-upgrade {package_name}")
