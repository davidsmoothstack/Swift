from managers.BasePackageManager import BasePackageManager
from util.shell import shell


class SnapPackageManager(BasePackageManager):
    def update_repositores(self):
        return shell("sudo snap install core; sudo snap refresh core")

    def install_package(self, package_name: str):
        """Installs a package"""
        options = self.yaml_config.manager.installFlags
        return shell(f"sudo snap install {package_name} {options}")

    def is_installed(self, package_name: str):
        """Check if the package already exists on the system"""
        result = shell(f"sudo snap list {package_name}")
        return result.isSuccess

    def upgrade_package(self, package_name: str):
        """Upgrades the package"""
        return shell(f"sudo snap refresh {package_name}")
