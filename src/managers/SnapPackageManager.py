from managers.BasePackageManager import BasePackageManager
from util.shell import shell


class SnapPackageManager(BasePackageManager):
    def install_package(self, package_name: str):
        """Installs a package"""
        return shell(f"sudo snap install {package_name}")

    def post_install(self, package_name: str):
        """Runs a check after package is installed"""
        pass

    def is_installed(self, package_name: str):
        """Check if the package already exists on the system"""
        return shell(f"snap info {package_name}")

    def upgrade_package(self, package_name: str):
        """Upgrades the package"""
        return shell(f"sudo snap refresh {package_name}")
